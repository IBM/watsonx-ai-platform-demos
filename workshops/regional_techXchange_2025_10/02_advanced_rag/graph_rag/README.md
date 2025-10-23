# Advanced RAG Workshop - Graph RAG with Langflow

This workshop demonstrates advanced Retrieval-Augmented Generation (RAG) techniques using Graph RAG and Langflow integration. The system processes markdown documents about Galaxium Travels (a fictional space tourism company) and creates a graph-based RAG system for intelligent document retrieval and question answering.

## Overview

The workshop includes:
- **Graph RAG System**: Interactive Python notebook for processing markdown documents and creating graph-based relationships
- **Langflow Integration**: Pre-configured Langflow workflow for visual RAG pipeline management
- **Document Processing**: Automated extraction of document metadata, links, and relationships
- **Vector Storage**: Integration with AstraDB for scalable vector storage
- **Interactive Chat**: Complete RAG pipeline with IBM watsonx.ai and OpenAI integration

## Files Structure

```
02_advanced_rag/
├── 97_raw_markdown_files/          # Sample markdown documents (Galaxium Travels dataset)
├── graph_rag_interactive.py        # Main interactive notebook for data processing
├── graph_rag_langflow_export.json  # Pre-configured Langflow workflow
├── patch_langflow_limits.sh        # Script to patch Langflow text limits
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## Prerequisites

### Required Services
- **AstraDB Account**: For vector storage
  - Create database and obtain API token
  - Set up environment variables (see below)
- **OpenAI API Key**: For embeddings (optional - fallback available)
- **IBM watsonx.ai**: For language model (configured in Langflow)

### Environment Variables
Create a `.env` file with:
```bash
ASTRA_DB_APPLICATION_TOKEN=your_astra_token
ASTRA_DB_API_ENDPOINT=your_astra_endpoint
ASTRA_DB_KEYSPACE=default_keyspace
OPENAI_API_KEY=your_openai_key  # Optional
```

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Patch Langflow Limits (REQUIRED)
**⚠️ Important: Run this BEFORE starting Langflow**
```bash
chmod +x patch_langflow_limits.sh
./patch_langflow_limits.sh
```

This script patches Langflow's text length limits to handle large document contexts properly.

### 3. Process Documents
Run the interactive Python script to process markdown files and populate AstraDB:
```bash
python graph_rag_interactive.py
```

The script will:
- Process all markdown files in `97_raw_markdown_files/`
- Extract document metadata and inter-document links
- Create a network visualization of document relationships
- Generate embeddings and store in AstraDB
- Create a timestamped collection for use in Langflow

### 4. Import Langflow Workflow
1. Start Langflow: `langflow run`
2. Import the workflow: `graph_rag_langflow_export.json`
3. Configure the AstraDB collection name (use the timestamped collection from step 3)
4. Test the chat interface

## How It Works

### Document Processing Pipeline
1. **Markdown Parsing**: Extracts titles, content, and inter-document links
2. **Graph Creation**: Builds a network graph of document relationships
3. **Chunking**: Splits documents into manageable chunks (3000 chars, 500 overlap)
4. **Embedding**: Generates vector embeddings (OpenAI or fallback)
5. **Storage**: Stores in AstraDB with metadata preservation

### Graph RAG Retrieval
The system uses graph-based retrieval strategies:
- **Edge Definition**: `linked_docs,doc_id` - follows document links
- **Traversal Strategy**: Configurable (Eager, MMR, NodeTracker, Scored)
- **Context Enhancement**: Retrieves related documents through graph traversal

### Langflow Workflow Components
- **OpenAI Embeddings**: Vector embedding generation
- **AstraDB**: Vector storage and retrieval
- **Graph RAG**: Advanced graph-based document retrieval
- **Parser**: Formats retrieved documents for context
- **Prompt**: RAG prompt template
- **IBM watsonx.ai**: Language model for response generation
- **Chat I/O**: Interactive chat interface

## Sample Dataset

The `97_raw_markdown_files/` directory contains a comprehensive dataset about Galaxium Travels, including:
- **Corporate**: Company overview, sustainability initiatives
- **Customer Service**: FAQs, policies, procedures
- **HR**: Training programs, safety certifications
- **Marketing**: Travel packages, partnerships, spacecraft specifications
- **Legal**: Terms of service, privacy policies
- **Technical**: Research documents, specifications
- **Finance**: Pricing, payment options
- **IT**: System documentation

Documents are interconnected with markdown links, creating a rich graph structure for advanced retrieval.

## Key Features

### Graph-Based Retrieval
- Follows document relationships for enhanced context
- Multiple traversal strategies for different use cases
- Configurable depth and breadth parameters

### Interactive Processing
- Step-by-step document processing
- Network visualization of document relationships
- Real-time feedback and statistics

### Production-Ready Integration
- AstraDB vector storage with proper configuration
- Langflow visual pipeline management
- IBM watsonx.ai integration for enterprise use

## Troubleshooting

### Common Issues
1. **Langflow Text Limits**: Ensure `patch_langflow_limits.sh` was run before starting Langflow
2. **AstraDB Connection**: Verify environment variables and network connectivity
3. **Collection Not Found**: Ensure the interactive script completed successfully and note the collection name
4. **Memory Issues**: Reduce chunk size or batch size in the processing script

### Performance Optimization
- Adjust chunk size and overlap based on document characteristics
- Configure Graph RAG strategy parameters for optimal retrieval
- Use appropriate embedding models for your use case

## Next Steps

After completing this workshop, consider:
- Experimenting with different Graph RAG strategies
- Adding custom document types and processing logic
- Integrating with other vector stores or embedding models
- Building custom Langflow components for specific use cases
- Scaling to larger document collections

## Support

For questions or issues:
- Review the interactive notebook comments and documentation
- Check Langflow logs for detailed error messages
- Verify all environment variables are properly set
- Ensure all dependencies are installed correctly