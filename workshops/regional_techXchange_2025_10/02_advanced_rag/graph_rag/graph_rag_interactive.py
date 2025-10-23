#%% [markdown]
# # Graph RAG System - Interactive Notebook
# 
# This notebook processes markdown documents and creates a graph-based RAG system.
# Each cell is designed to be run independently for easy debugging and experimentation.


#%%
# =============================================================================
# 1. IMPORTS AND CONFIGURATION
# =============================================================================
from langchain_astradb.vectorstores import AstraDBVectorStore
import os
import re
import pandas as pd
from pathlib import Path
from typing import List, Dict, Any
from bs4 import BeautifulSoup
from datetime import datetime
from dotenv import load_dotenv



# Change to script's directory
script_dir = Path(__file__).parent
os.chdir(script_dir)

# Load environment variables
load_dotenv()

# Configuration
DATA_DIRECTORY = "97_raw_markdown_files copy"
COLLECTION_NAME = "galax_docs"
CHUNK_SIZE = 3000
CHUNK_OVERLAP = 500

print("✅ Imports loaded successfully")
print(f"📁 Data directory: {DATA_DIRECTORY}")
print(f"🗄️  Collection name: {COLLECTION_NAME}")


#%% [markdown]
# # Graph RAG System - Interactive Notebook
# 
# This notebook processes markdown documents and creates a graph-based RAG system.
# Each cell is designed to be run independently for easy debugging and experimentation.
#%%
# =============================================================================
# 2. UTILITY FUNCTIONS
# =============================================================================

def get_relative_path_from_root(absolute_path: str, root_dir: str = "97_raw_markdown_files") -> str:
    """Convert absolute path to relative path from the root directory."""
    abs_path = Path(absolute_path).resolve()
    root_path = Path(root_dir).resolve()
    
    try:
        rel_path = abs_path.relative_to(root_path)
        return str(rel_path)
    except ValueError:
        return str(abs_path)

def print_summary(title: str, data: Any, max_items: int = 5):
    """Print a nice summary of data."""
    print(f"\n{'='*50}")
    print(f"📊 {title}")
    print(f"{'='*50}")
    
    if isinstance(data, list):
        print(f"Total items: {len(data)}")
        if data and max_items > 0:
            print(f"\nFirst {min(max_items, len(data))} items:")
            for i, item in enumerate(data[:max_items]):
                if isinstance(item, dict):
                    print(f"  {i+1}. {item.get('title', item.get('doc_id', str(item)))}")
                else:
                    print(f"  {i+1}. {item}")
    elif isinstance(data, dict):
        for key, value in data.items():
            print(f"{key}: {value}")
    else:
        print(str(data))

def extract_metadata_from_markdown(file_path: str) -> Dict[str, Any]:
    """Extract metadata and content from a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title (first # heading)
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE) # regex to extract the title from the markdown file
    title = title_match.group(1) if title_match else Path(file_path).stem
    
    # Extract links to other documents
    links = []
    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)' # regex to extract the links from the markdown file
    for match in re.finditer(link_pattern, content):
        link_path = match.group(2)
        
        # Strip anchor fragments (everything after #) from the path
        if '#' in link_path:
            link_path = link_path.split('#')[0]
        
        # Only process markdown files (skip external links, images, etc.)
        if not link_path.endswith('.md'):
            continue
            
        # Convert paths to relative paths from root
        if link_path.startswith('../'):
            base_path = Path(file_path).parent
            full_path = base_path / link_path
            relative_path = get_relative_path_from_root(str(full_path.resolve()))
            links.append(relative_path)
        elif link_path.startswith('./'):
            base_path = Path(file_path).parent
            full_path = base_path / link_path[2:]
            relative_path = get_relative_path_from_root(str(full_path.resolve()))
            links.append( relative_path)
        else:
            if os.path.isabs(link_path):
                relative_path = get_relative_path_from_root(link_path)
            else:
                relative_path = link_path
            links.append(relative_path)
    
    # Extract document category from path
    path_parts = Path(file_path).parts
    category = path_parts[-2] if len(path_parts) > 1 else 'root'
    
    return {
        'doc_id': get_relative_path_from_root(file_path),
        'title': title,
        'content': content,
        'category': category,
        'file_path': file_path,
        'links': links,
        'metadata': {
            'file_size': len(content),
            'word_count': len(content.split()),
            'link_count': len(links)
        }
    }

def process_all_markdown_files(data_dir: str) -> List[Dict[str, Any]]:
    """Process all markdown files in the directory and extract metadata."""
    documents = []
    data_path = Path(data_dir)
    
    print(f"🔍 Scanning for markdown files in: {data_path}")
    
    for md_file in data_path.rglob('*.md'):
        try:
            doc_metadata = extract_metadata_from_markdown(str(md_file))
            documents.append(doc_metadata)
            print(f"  ✅ {md_file.name}")
        except Exception as e:
            print(f"  ❌ Error processing {md_file}: {e}")
    
    return documents

print("✅ Utility functions defined")



#%%
# =============================================================================
# 3. EMBEDDING CLASSES
# =============================================================================

from langchain_core.embeddings import Embeddings
import numpy as np

class SimpleEmbeddings(Embeddings):
    """Simple embeddings class for testing without actual API calls."""
    
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Create simple random embeddings for testing."""
        embeddings = []
        for text in texts:
            hash_val = hash(text) % (2**32)
            np.random.seed(hash_val)
            embedding = np.random.rand(384).tolist()
            embeddings.append(embedding)
        return embeddings
    
    def embed_query(self, text: str) -> List[float]:
        """Create a simple random embedding for a query."""
        hash_val = hash(text) % (2**32)
        np.random.seed(hash_val)
        return np.random.rand(384).tolist()

def get_embedding_model():
    """Get the appropriate embedding model based on available API keys."""
    if os.getenv("OPENAI_API_KEY"):
        print("🔑 Using OpenAI embeddings...")
        from langchain_openai import OpenAIEmbeddings
        return OpenAIEmbeddings()
    else:
        print("🧪 Using simple test embeddings...")
        return SimpleEmbeddings()

print("✅ Embedding classes defined")

#%%
# =============================================================================
# 5. PROCESS MARKDOWN FILES
# =============================================================================

# Execute markdown processing
print("🚀 Processing markdown files...")
documents = process_all_markdown_files(DATA_DIRECTORY)

print_summary("Markdown Processing Results", documents)
print(f"Total links found: {sum(len(doc['links']) for doc in documents)}")


#%%
# =============================================================================
# 4. DOCUMENT LINK VISUALIZATION
# =============================================================================

import networkx as nx
import matplotlib.pyplot as plt

def visualize_document_links(documents: List[Dict[str, Any]]):
    """Create a network graph visualization of document links."""
    G = nx.DiGraph()
    
    # Add nodes (documents)
    for doc in documents:
        G.add_node(doc['doc_id'], title=doc['title'], category=doc['category'])
    
    # Add edges (links between documents)
    for doc in documents:
        for link in doc['links']:
            if any(d['doc_id'] == link for d in documents):  # Only link to existing documents
                G.add_edge(doc['doc_id'], link)
    
    # Create visualization
    plt.figure(figsize=(15, 10))
    pos = nx.circular_layout(G, scale=2)
    
    # Color nodes by category
    categories = list(set(doc['category'] for doc in documents))
    colors = plt.cm.Set3(range(len(categories)))
    category_colors = {cat: colors[i] for i, cat in enumerate(categories)}
    
    node_colors = [category_colors[G.nodes[node]['category']] for node in G.nodes()]
    
    # Draw the graph
    nx.draw(G, pos, 
            node_color=node_colors,
            node_size=500,
            font_size=8,
            font_weight='bold',
            arrows=True,
            arrowsize=20,
            edge_color='gray',
            alpha=0.7)
    
    # Add labels
    labels = {node: node.split('/')[-1].replace('.md', '') for node in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels, font_size=6)
    
    # Create legend
    legend_elements = [plt.Line2D([0], [0], marker='o', color='w', 
                                 markerfacecolor=category_colors[cat], 
                                 markersize=10, label=cat) for cat in categories]
    plt.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1, 1))
    
    plt.title("Document Link Network", fontsize=16, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    plt.show()
    
    # Print statistics
    print(f"\n📊 Network Statistics:")
    print(f"   Nodes (documents): {G.number_of_nodes()}")
    print(f"   Edges (links): {G.number_of_edges()}")
    print(f"   Average degree: {sum(dict(G.degree()).values()) / G.number_of_nodes():.2f}")

# Execute visualization
print("🎨 Creating document link visualization...")
visualize_document_links(documents)

#%%
# =============================================================================
# 6. CREATE LANGCHAIN DOCUMENTS
# =============================================================================

from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

def create_langchain_documents(metadata_list: List[Dict[str, Any]]) -> List[Document]:
    """Convert extracted metadata to LangChain Document objects."""
    documents = []
    
    for metadata in metadata_list:
        doc = Document(
            page_content=metadata['content'],
            metadata={
                'doc_id': metadata['doc_id'],
                'title': metadata['title'],
                'category': metadata['category'],
                'file_path': metadata['file_path'],
                'linked_docs': metadata['links']
            }
        )
        documents.append(doc)
    
    return documents

def split_documents(documents: List[Document], chunk_size: int = 1000, chunk_overlap: int = 200) -> List[Document]:
    """Split documents into smaller chunks for better embedding."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )
    return text_splitter.split_documents(documents)

# Execute document creation
print("🔄 Creating LangChain documents...")
langchain_docs = create_langchain_documents(documents)

print("🔄 Splitting documents into chunks...")
split_docs = split_documents(langchain_docs, CHUNK_SIZE, CHUNK_OVERLAP)

print_summary("Document Processing Results", split_docs)

#%%



#%%
# =============================================================================
# 9. ASTRA DB STORAGE
# =============================================================================

from langchain_astradb import AstraDBVectorStore
from astrapy.api_options import APIOptions, SerdesOptions

def store_documents_in_astradb(documents: List[Document], collection_name: str = "galaxium_travels") -> AstraDBVectorStore:
    """Store documents in AstraDB with vector embeddings using FLOAT ARRAYS."""
    
    embedding_model = get_embedding_model()
    
    try:
        # Configure AstraPy to use plain float arrays instead of binary encoding
        api_options = APIOptions(
            serdes_options=SerdesOptions(
                binary_encode_vectors=False,  # Key flag for Langflow compatibility
                custom_datatypes_in_reading=False
            )
        )
        
        print("🔧 Configuring AstraDB with float array vector support...")
        
        # Initialize AstraDB vector store
        vector_store = AstraDBVectorStore(
            embedding=embedding_model,
            collection_name=collection_name,
            token=os.getenv("ASTRA_DB_APPLICATION_TOKEN"),
            api_endpoint=os.getenv("ASTRA_DB_API_ENDPOINT"),
            namespace=os.getenv("ASTRA_DB_KEYSPACE", "default_keyspace"),
            api_options=api_options
        )
        
        print(f"✅ Connected to AstraDB collection: {collection_name}")
        
        # Add documents in batches
        print(f"Adding {len(documents)} documents to AstraDB...")
        batch_size = 50
        for i in range(0, len(documents), batch_size):
            batch = documents[i:i + batch_size]
            vector_store.add_documents(batch)
            print(f"  📦 Added batch {i//batch_size + 1}/{(len(documents)-1)//batch_size + 1}")
        
        print(f"✅ Successfully stored {len(documents)} documents in AstraDB")
        return vector_store
        
    except Exception as e:
        print(f"❌ Error connecting to AstraDB: {e}")
        print("This is expected if AstraDB credentials are not configured.")
        return None

# Execute AstraDB storage
print("🚀 Starting AstraDB storage...")
timestamp: str = datetime.now().strftime(format="%m%d_%H%M")
collection_name = f"{COLLECTION_NAME}_{timestamp}"
print(f"📅 Using collection name: {collection_name}")

vector_store: AstraDBVectorStore = store_documents_in_astradb(split_docs, collection_name)

#%%

