## Text Search Guide

<!-- image -->

## Text Search Guide

<!-- image -->

## Notice regarding this document

This document in PDF form is provided as a courtesy to customers who have requested documentation in this format: It is provided As-Is without warranty or maintenance commitment:

## Contents

Notice regarding this document

Figures

Tables

Chapter 1. Dbz Text Search

## Chapter 2. Dbz Text Search features and concepts key

Text search index creation,

Db2 Text Search server deployment scenarios updates

alterations and property

Db2 Text Search in environment

partitioned database

Incremental

Linguistic processing for Db2 Text Search vii

ix

3

9

11

updates for Db2 Text Search indexes

Scenario: Indexing and searching

13

14

Rich text and proprietary format

17

support

## Chapter 3. Text search solution planning

Db2 Text Search XML namespaces

| Chapter 3. Text search solution planning                                                                          | 19                                                                                                                |
|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Document characteristics 19                                                                                       | Document characteristics 19                                                                                       |
| Document formats supported for Db2 Text Search 19                                                                 | Document formats supported for Db2 Text Search 19                                                                 |
| Supported data types 19                                                                                           | Supported data types 19                                                                                           |
| Conversion of unsupported formats and data                                                                        | Conversion of unsupported formats and data                                                                        |
| types 19                                                                                                          | types 19                                                                                                          |
| Supported languages and code pages. 20                                                                            | Supported languages and code pages. 20                                                                            |
| Document size considerations 20                                                                                   | Document size considerations 20                                                                                   |
| Db2 Text Search security overview. 21                                                                             | Db2 Text Search security overview. 21                                                                             |
| User roles 22 Access policies and communication security 24 Db2 Text Search capacity planning and optimization 24 | User roles 22 Access policies and communication security 24 Db2 Text Search capacity planning and optimization 24 |
| Db2 Text Search server configuration                                                                              | 25                                                                                                                |
| Db2 Text Search index planning and optimization 29 Db2 Text Search system tuning                                  | 34 35                                                                                                             |
| Db2 Text Search query planning                                                                                    |                                                                                                                   |
| Db2 Text Search arguments                                                                                         | 35                                                                                                                |
| Db2 Text Search multiple predicates 36                                                                            | Db2 Text Search multiple predicates 36                                                                            |
| 36                                                                                                                | 36                                                                                                                |
| Db2 Text Search locale and language 37 37                                                                         | Db2 Text Search locale and language 37 37                                                                         |
| Db2 Text Search SCORE function Db2 Text Search RESULTLIMIT function _                                             | Db2 Text Search SCORE function Db2 Text Search RESULTLIMIT function _                                             |
| Parser                                                                                                            | Parser                                                                                                            |
| 38                                                                                                                | 38                                                                                                                |
| Db2 Text Search XML namespaces                                                                                    | Db2 Text Search XML namespaces                                                                                    |
| 39                                                                                                                | 39                                                                                                                |
| configuration for Db2 Text Search                                                                                 | configuration for Db2 Text Search                                                                                 |

## Chapter 4 Installing and configuring Db2 Text Search:

41

Search requirements for Db2 Text

Installing DB2 Text Search with default

configuration the Db2 Setup Wizard

Installing and configuring Db2 Text Search with

43

44

44

## 19

Installing and configuring Db2 Text Search with a

| response file                                                        |   45 |
|----------------------------------------------------------------------|------|
| Installing Db2 Text Search using db2_install (Linux and UNIX)        |   46 |
| Installing DB2 Text Search without initial configuration             |   46 |
| Installing Db2 database servers the Db2 wizard (Windows) using Setup |   46 |
| Installing Db2 servers the Db2 Setup wizard (Linux and UNIX) using   |   49 |
| Response file installation of Db2 overview (Windows).                |   52 |
| Response file installation of Db2 overview (Linux and UNIX)          |   53 |
| Installing and configuring stand-alone Text search server            |   53 |
| Installation space requirements for the stand-alone server           |   53 |
| Installing stand-alone Db2 Text Search server                        |   54 |
| Installing and configuring stand-alone server as Windows service     |   55 |
| Uninstalling stand-alone Db2 Text Search server                      |   55 |

## Chapter 5. Configuring Db2 Text

| Search                                                     | 57   |
|------------------------------------------------------------|------|
| Initial configuration of an integrated Db2 Text            |      |
| Search server                                              | 59   |
| Updating Db2 Text Search server information                | 60   |
| Configuring stand-alone Db2 Text Search server             | 61   |
| communications                                             | 63   |
| Installing Db2 Accessories Suite for Db2 Text Search       | 63   |
| Uninstalling the Db2 Accessories Suite for Db2 Text Search | 65   |

## Chapter 6. Upgrading DBZ Text Search 67

| Upgrading Db2 Text Search for administrator or root installation     | 67   |
|----------------------------------------------------------------------|------|
| Upgrading Db2 Text Search for non-root installation (Linux and UNIX) | 70   |
| Upgrading multi-partition instance without Db2                       | 71   |
| Text Search                                                          | 72   |
| Upgrading stand-alone Db2 Text Search Server                         |      |

## Chapter 7 . Configuring and administering text search indexes 75

Stopping the Db2 Text Search instance service

| Command-line tools for Db2 Text Search                   | 76   |
|----------------------------------------------------------|------|
| Issuing text search commands                             |      |
| Rich text and proprietary format support                 |      |
| Enabling Db2 Text Search for rich text document support. | 76   |
| Disabling support for rich text and proprietary formats  |      |
| the Db2 Text Search instance service Starting            |      |
|                                                          | 7    |

| Enabling database for Db2 Text Search.        | 78                                         | Enabling database for Db2 Text Search.        |                                               |                                               |                                              |                                            |
|-----------------------------------------------|--------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|----------------------------------------------|--------------------------------------------|
| Disabling a database for Db2 Text Search      | Disabling a database for Db2 Text Search   | Disabling a database for Db2 Text Search      |                                               |                                               |                                              |                                            |
| Deleting orphaned DB2 Text Search collections | 80                                         | Deleting orphaned DB2 Text Search collections | Deleting orphaned DB2 Text Search collections | Deleting orphaned DB2 Text Search collections |                                              |                                            |
| Synonym dictionaries for Db2 Text Search      | 82                                         | Synonym dictionaries for Db2 Text Search      | Synonym dictionaries for Db2 Text Search      |                                               |                                              |                                            |
| Adding synonym dictionary for Db2 Text        | Adding synonym dictionary for Db2 Text     | Adding synonym dictionary for Db2 Text        | Adding synonym dictionary for Db2 Text        | Adding synonym dictionary for Db2 Text        | Adding synonym dictionary for Db2 Text       |                                            |
| Search                                        | 82                                         |                                               |                                               |                                               |                                              |                                            |
| Removing a synonym dictionary for Db2 Text    | Removing a synonym dictionary for Db2 Text | Removing a synonym dictionary for Db2 Text    | Removing a synonym dictionary for Db2 Text    | Removing a synonym dictionary for Db2 Text    | Removing a synonym dictionary for Db2 Text   | Removing a synonym dictionary for Db2 Text |
| Search                                        | 83                                         |                                               |                                               |                                               |                                              |                                            |
| Text search index creation                    | 83                                         |                                               |                                               |                                               |                                              |                                            |
| Creating a text search index                  | 84                                         |                                               |                                               |                                               |                                              |                                            |
| Text search index maintenance                 | 91                                         |                                               |                                               |                                               |                                              |                                            |
| Updating a text search index                  | 93                                         |                                               |                                               |                                               |                                              |                                            |
| Clearing text search index events             | 96                                         |                                               |                                               |                                               |                                              |                                            |
| Altering a text search index                  | 97                                         |                                               |                                               |                                               |                                              |                                            |
| Viewing text search index status              | 98                                         |                                               |                                               |                                               |                                              |                                            |
| Changing the location of Db2 Text Search      | Changing the location of Db2 Text Search   | Changing the location of Db2 Text Search      | Changing the location of Db2 Text Search      | Changing the location of Db2 Text Search      | Changing the location of Db2 Text Search     |                                            |
| collection                                    | 98                                         |                                               |                                               |                                               |                                              |                                            |
| Backing up and restoring text search indexes  | 99                                         | Backing up and restoring text search indexes  | Backing up and restoring text search indexes  | Backing up and restoring text search indexes  | Backing up and restoring text search indexes |                                            |
| Dropping a text search index                  | 99                                         |                                               |                                               |                                               |                                              |                                            |
| Sample: Scheduling Db2 Text Search index      | Sample: Scheduling Db2 Text Search index   | Sample: Scheduling Db2 Text Search index      | Sample: Scheduling Db2 Text Search index      | Sample: Scheduling Db2 Text Search index      | Sample: Scheduling Db2 Text Search index     | Sample: Scheduling Db2 Text Search index   |
| update                                        | 101                                        |                                               |                                               |                                               |                                              |                                            |

## Chapter 8. Searching with text search

| indexes                                      | 103                             |                                              |                                              |                                              |
|----------------------------------------------|---------------------------------|----------------------------------------------|----------------------------------------------|----------------------------------------------|
| Search functions for Db2 Text Search         | 103                             | Search functions for Db2 Text Search         | Search functions for Db2 Text Search         | Search functions for Db2 Text Search         |
| Full-text search methods.                    | 104                             | Full-text search methods.                    | Full-text search methods.                    | Full-text search methods.                    |
| Basic search                                 | 105                             |                                              |                                              |                                              |
| Fuzzy search                                 | 105                             |                                              |                                              |                                              |
| Proximity search                             | 107                             | Proximity search                             | Proximity search                             | Proximity search                             |
| Searching for characters special             | 107                             | Searching for characters special             | Searching for characters special             | Searching for characters special             |
| Structural full-text search in XML documents | 110                             | Structural full-text search in XML documents | Structural full-text search in XML documents | Structural full-text search in XML documents |
| Searching text search indexes using SCORE    | 112                             | Searching text search indexes using SCORE    | Searching text search indexes using SCORE    | Searching text search indexes using SCORE    |
| Db2 Text Search argument syntax.             | 113                             | Db2 Text Search argument syntax.             | Db2 Text Search argument syntax.             | Db2 Text Search argument syntax.             |
| Search syntax for XML documents              | 117                             | Search syntax for XML documents              | Search syntax for XML documents              | Search syntax for XML documents              |
| Enhancing performance for full-text queries  | 121                             | Enhancing performance for full-text queries  | Enhancing performance for full-text queries  | Enhancing performance for full-text queries  |
| Chapter 9. SQL and XML built-in              | Chapter 9. SQL and XML built-in | Chapter 9. SQL and XML built-in              | Chapter 9. SQL and XML built-in              | Chapter 9. SQL and XML built-in              |
|                                              | 123                             |                                              |                                              |                                              |
| search functions                             | search functions                | search functions                             | search functions                             | search functions                             |
| CONTAINS function                            | 123                             | CONTAINS function                            | CONTAINS function                            | CONTAINS function                            |

| SCORE function                                    | 125                                               |                                                   |                                                   |                                                   |
|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|
| xmlcolumn-contains function                       | 128                                               |                                                   |                                                   |                                                   |
| Chapter 10. Administration commands               | Chapter 10. Administration commands               | Chapter 10. Administration commands               | Chapter 10. Administration commands               | Chapter 10. Administration commands               |
| for Db2 Text Search                               | 133                                               |                                                   |                                                   |                                                   |
| DB2 Text Search commands                          | 134                                               |                                                   |                                                   |                                                   |
| db2ts ALTER INDEX                                 | 134                                               |                                                   |                                                   |                                                   |
| db2ts CLEANUP FOR TEXT                            | 139                                               |                                                   |                                                   |                                                   |
| db2ts CLEAR COMMAND LOCKS                         | 140                                               |                                                   |                                                   |                                                   |
| db2ts CLEAR EVENTS FOR TEXT                       | 141                                               |                                                   |                                                   |                                                   |
| db2ts CREATE INDEX                                | 143                                               |                                                   |                                                   |                                                   |
| db2ts DISABLE DATABASE FOR TEXT                   | 152                                               |                                                   |                                                   |                                                   |
| db2ts DROP INDEX                                  | 154                                               |                                                   |                                                   |                                                   |
| db2ts ENABLE DATABASE FOR TEXT .                  | 156                                               |                                                   |                                                   |                                                   |
| db2ts HELP                                        | 158                                               |                                                   |                                                   |                                                   |
| db2ts RESET PENDING command                       | 159                                               |                                                   |                                                   |                                                   |
| db2ts SET COMMAND LOCK command                    | 160                                               |                                                   |                                                   |                                                   |
| db2ts START FOR TEXT .                            | 161                                               |                                                   |                                                   |                                                   |
| db2ts STOP FOR TEXT                               | 162                                               |                                                   |                                                   |                                                   |
| db2ts UPDATE INDEX                                | 163                                               |                                                   |                                                   |                                                   |
| Chapter 11. Db2 Text Search stored procedures 169 | Chapter 11. Db2 Text Search stored procedures 169 | Chapter 11. Db2 Text Search stored procedures 169 | Chapter 11. Db2 Text Search stored procedures 169 | Chapter 11. Db2 Text Search stored procedures 169 |
| Chapter 12. Text search administrative            | Chapter 12. Text search administrative            | Chapter 12. Text search administrative            | Chapter 12. Text search administrative            | Chapter 12. Text search administrative            |
| views                                             | 171                                               |                                                   |                                                   |                                                   |
| Text Search Administrative Views                  | 171                                               |                                                   |                                                   |                                                   |
| SYSIBMTS.TSDEFAULTS view.                         | 171                                               |                                                   |                                                   |                                                   |
| SYSIBMTS.TSLOCKS view                             | 172                                               |                                                   |                                                   |                                                   |
| SYSIBMTS.TSSERVERS view                           | 173                                               |                                                   |                                                   |                                                   |
| SYSIBMTS.TSINDEXES view                           | 173                                               |                                                   |                                                   |                                                   |
| SYSIBMTS.TSCONFIGURATION view                     | 175                                               | SYSIBMTS.TSCONFIGURATION view                     | SYSIBMTS.TSCONFIGURATION view                     | SYSIBMTS.TSCONFIGURATION view                     |
| SYSIBMTS.TSCOLLECTIONNAMES view                   | 176                                               | SYSIBMTS.TSCOLLECTIONNAMES view                   | SYSIBMTS.TSCOLLECTIONNAMES view                   | SYSIBMTS.TSCOLLECTIONNAMES view                   |
| SYSIBMTS.TSEVENT view                             | 176                                               |                                                   |                                                   |                                                   |
| SYSIBMTS.TSSTAGING view                           | 177                                               |                                                   |                                                   |                                                   |
| Index 179                                         | Index 179                                         | Index 179                                         | Index 179                                         | Index 179                                         |

## Figures

| 1   | Deployment diagram for an integrated Db2 Text Search server                                                       |
|-----|-------------------------------------------------------------------------------------------------------------------|
| 2   | Creating a text search index 3                                                                                    |
| 3_  | Integrated Db2 Text Search server setup 5                                                                         |
| 4   | Stand-alone Db2 Text Search server setup 5                                                                        |
| 5_  | Stand-alone Db2 Text Search server setup in a partitioned environment: 5                                          |
| 6_  | Creating a text search index and then performing initial and incremental updates                                  |
| 7_  | Incremental update with triggers .                                                                                |
| 8_  | Incremental with triggers and integrity processing update                                                         |
| 9   | A Db2 Text Search server setup in a partitioned environment 10                                                    |
| 10. | Setting up text search indexes for searching in non-partitioned instance with an integrated Text Search server 15 |

| 11_   | Installation and configuration on Windows platforms 41                                         |
|-------|------------------------------------------------------------------------------------------------|
| 12    | Installation and configuration on Linux and UNIX platforms 42                                  |
| 13.   | Configuration of a stand-alone Db2 Text Search server 43 Content of the Books_zh_TWIlob object |
| 14.   | 88                                                                                             |
| 15.   | Query results for meaningful Chinese words 88                                                  |
| 16.   | Query results for meaningless Chinese words 89                                                 |
| 17 .  | Sample segment of content in Simplified Chinese 90                                             |
| 18.   | Query results for linguistically meaningful Chinese words 91                                   |
| 19.   | Query results for meaningless Chinese words 91                                                 |

## Tables

| 1                                      | Role privileges 22 Hardware requirements for Db2 Text Search   |
|----------------------------------------|----------------------------------------------------------------|
| 2_                                     | 44                                                             |
| 3 searched                             | Special characters that must be escaped to be 108              |
| 4 Examples of require escaping special | characters that do not 109                                     |
| 5_ Valid XML search queries            | 111                                                            |
| 6_                                     | Boolean operators 115                                          |
| 7. Occurrence modifiers                | 116                                                            |
| 8_ Other modifiers                     | 116                                                            |
| 9 Specifications for option-value      | 136                                                            |

| 10.                               |   Status changes without invalid index: 139 |
|-----------------------------------|---------------------------------------------|
| 11. Option-value pairs            |                                         147 |
| 12 SYSIBMTS.TSDEFAULTS view       |                                         171 |
| 13. SYSIBMTS.TSLOCKS view         |                                         172 |
| 14 SYSIBMTS.TSSERVERS view        |                                         173 |
| 15. SYSIBMTS.TSINDEXES view       |                                         174 |
| 16. SYSIBMTS.TSCONFIGURATION view |                                         175 |
| SYSIBMTS.TSCOLLECTIONNAMES view   |                                         176 |
| 18. Event view                    |                                         176 |
| 19. SYSIBMTS.TSSTAGING view       |                                         178 |

## Chapter 1. Db2 Text Search

After you started the Db2e Text Search instance and a text search index is created for a text column, you can search the text data by issuing SQL and XQUERY statements.

Db2 Text Search provides extensive capabilities for searching data in text columns that are stored in a database table: The search system provides fast query response times and a consolidated, ranked result set that quickly and easily locates the information that you require. By incorporating the functions of Db2 Text Search in your SQL and XQuery statements, you can create powerful and versatile text-retrieval programs. Furthermore, the search engine uses linguistic analysis to ensure that it returns only relevant search query results. By enabling text search support, you can use the CONTAINS, SCORE, and xmlcolumn-contains functions, which are built into the database engine, to search text search indexes that are based on the search arguments that you specify:

Db2 Text Search achieves high performance and scalability by data streaming to avoid high resource consumption search using during

You can install the Db2 Text Search server and the database servers on the same system for an integrated text search server You can also install Db2 Text Search server and the database server on different systems for stand-alone TM The Db2 Text Search server runs in its own Java Virtual Machine (JVM): You explicitly start and the Db2 Text Search services after the database instance is started. Use the stand-alone text search server release that corresponds with the database server release setup: setup: stop

Figure 1. Deployment diagram for an integrated Dbz Text Search server

<!-- image -->

Db2 Text Search does not have a graphical user interface. Instead, command-line tools are available for tasks such as configuring and administering the Db2 Text Search server; creating a synonym dictionary for a collection, and diagnosing problems. In addition, you can use stored-procedure interface for various common administrative tasks:

You can migrate from Net Search Extender to Db2 Text Search by creating and updating Db2 Text Search indexes and then toggling the index status when the indexes are ready for use. For details, see the topic about migration from Net Search Extender to Db2 Text Search:

You cannot search or modify Db2 Text Search indexes or collections that are created or modified by using V10.5 Text search by an earlier release of the Db2 Text Searchh server: using

Note: Db2 Text Search does not support clustering:

Db2 Text Search includes the following key features:

## Tight integration with Db2

- A stored procedure interface for administration commands
- Installation and configuration that is performed by the database installer
- Invisible authentication
- SQL codes for error handling

## Document indexing

- pureXML support
- Fast indexing of large amounts of data
- Multiple document format support
- Incremental and asynchronous index updating

## Advanced search technology

- SQL, SQL /XML, and XQuery support
- The CONTAINS and SCORE SQL functions
- Built-in SQL functions that are combined with the database Optimizer
- The xmlcolumn-contains XML function
- XML filtering
- Linguistic processing in all supported languages
- Weight, wildcard, and optional term support
- Synonym dictionary support

## Chapter 2. Db2 Text Search key features and concepts

Db2 Text Search offers you a fast and versatile method for searching text documents that are stored in table column in Db2 databases. You can search the documents by using SQL queries or XQuery for searches on XML documents.

The text documents must be uniquely identifiable: Db2 Text Search uses the primary key of the table for this purpose

Rather than searching text documents sequentially, Db2 Text Search searches using a text search index, which is a more efficient approach: A text search index consists of significant terms that are extracted from the text documents.

Figure 2. Creating a text search index

<!-- image -->

Creating a text search index defines the properties of the index, such as the update frequency The text search index does not contain any data immediately after you create it: Updating the index adds data about the terms and the text documents to the text search index: The initial index update adds all text documents from a text column to the index Subsequent updates are known as incremental and synchronize the data in the table and the data in the text search index Db2 Text Search provides two methods for synchronizing a text search index with its table: updates

- The basic synchronization method uses triggers that automatically store information about new, changed, and deleted documents in a staging table:
- The extended synchronization method uses a trigger to store information about changed documents in staging table but captures information about new and deleted documents through integrity processing and stores that information in an auxiliary staging table:

See the text search index creation, updates, and property alterations topic for details.

Db2 Text Search works by collecting data from diverse sources and indexing it for subsequent fast retrieval. Db2 Text Search uses linguistic analysis to improve search results and supports the following document formats:

- Unstructured plain text
- Structured text such as that in HTML or XML documents
- Proprietary document formats such as PDF or Microsoft Office document formats\_

For proprietary formats, you need filtering software that might require an additional download and setup step:

Db2 Text Search supports full-text search in a partitioned database environment You can also create a text search index for range-partitioned tables or tables that use the multidimensional clustering feature in a single-partition Or partitioned database environment\_ Text search indexes are supported for any partitioning feature combination: In partitioned database environment, the text search index is partitioned according to the partitioning of the table across multiple database partitions. Other partitioning features, such as table partitioning O multidimensional clustering, do not affect the partitioning of the text search index

Db2 Text Search supports both stand-alone and integrated setups. For partitioned environments, a stand-alone setup is preferred to avoid resource contention with the database server: For Db2 pureScale environments, only stand-alone servers are supported. For more detail on Db2 text search set up for pureScale environments please see this recipe:

In all environments, Db2 text search is not supported on column-organized tables.

## Db2 Text Search server deployment scenarios

Db2 Text Search supports an integrated installation of the text search server as well as well as stand-alone one separate from the Db2 database product: The stand-alone server deployment is the preferred for Db2 Text Search: option using

A stand-alone text search server; also known as Enterprise Content Management (ECM) Text Search server; can be installed and administered on supported host platforms. Db2 Text Search is not supported with the High availability disaster recovery (HADR) feature:

The Db2 database instance uses TCP /IP to communicate with the stand-alone Db2 Text Search server: SSL or GSKit support are not available. However; encryption channels can be used through the stunnel program or SSH tunneling: Restrict access to your document repository and text search index files depending on your security requirements. The stand-alone text search server must be installed on computers with a secure network connection behind a firewall to prevent unauthorized access to the text search indexes. Setting up TCP /IP access restriction

to the stand-alone text search server ensures that it can only be accessed by the host on which the database server is installed:

The following are high-level illustrations of Db2 Text Search server deployments, including integrated and stand-alone setups: You can set up and configure an integrated Db2 Text Search server and switch to a stand-alone server later: However, there is no automated support to move text search indexes to a different text search server Depending on the it might therefore be necessary to drop existing text indexes before assigning a new text search server to the database instance: setup

<!-- image -->

Figure 4. Stand-alone Db2 Text Search server setup

<!-- image -->

Figure 5. Stand-alone Db2 Text Search server setup in a partitioned environment

<!-- image -->

Note: The Db2 Text Search installation directory depends on the type of deployment:

- For an integrated server:
- &lt;TS\_HOME&gt; represents the on Windows, Linux or UNIX operating systems. path
- For a stand-alone &lt;ECMTS\_HOME&gt; represents the install location of the text search server: setup,

- By default, &lt;ECMTS\_HOME&gt; represents the /opt/ibm/ ECMTextSearch path on Linux or UNIX systems.
- By default, &lt;ECMTS\_HOME&gt; represents the C: | Program Files ECMTextSearch on Windows systems. path

Deployment of a stand-alone text search server should be considered for:

- security management: the stand-alone Text Search server allows to define a text server process owner other than the database instance owner:
- workload management: the stand-alone Text Search server separates the resource-intensive text search processing from database server tasks.

Each database instance is associated with a single Text Search server: In partitioned database environments involving multiple partition servers, a stand-alone setup avoids concentration of resource-intensive processing on single partition server:

The stand-alone and the integrated Text Search server only differ in the initial configuration, most notably, the stand-alone Text Search server is already configured for processing of rich text/proprietary format documents

## Text search index creation, updates and property alterations

Text search index creation is the process of defining the properties of a text index After you create a text search index, you must it by adding data from the table that it is associated with: You can also alter some properties of the text search index later; such as the UPDATE FREQUENCY or UPDATE MINIMUM parameters\_ update

You can use a text search index to search through the data in a text column using text search functions: A text search index consists of significant terms that are extracted from text documents. The primary of the table row is used in the index to identify the source of the terms. key

Immediately after its creation, a text search index contains no data. You add data to a text search index by the dbzts UPDATE INDEX command or the SYSTS\_UPDATE administrative SQL routine: The first index update, also known as initial update, adds all text documents in a text column to the text search index Subsequent updates, also known as incremental updates, synchronize the data in the base table with the text search index using

In the following example, a user creates a text search index called MYSCHEMA.PRODUCTINDEX on the PRODUCT table in the SAMPLE database. Creating a text search index and then performing initial and incremental updates shows that the index is empty until the user performs an initial update and that as the user adds data to the table, an incremental must be run to add the new data to the text search index: update

## Create index for text

<!-- image -->

## Update index for text (initial update)

<!-- image -->

## Update index for text (incremental update)

Figure 6. Creating a text search index and then performing initial and incremental updates

<!-- image -->

DB2 Text Search provides two methods for synchronizing a text index with its table:

- The basic synchronization method uses triggers that automatically store information about new, changed, and deleted documents in staging table: There is one staging table for each text index:

Figure 7. Incremental update with triggers

<!-- image -->

Because the basic method uses only triggers, updates that are not recognized by triggers are ignored, for example, loading data with the LOAD command and attaching or detaching the ranges of a range-partitioned table.

- The extended synchronization method uses trigger to store information about changed documents in staging table but captures information about new and deleted documents through integrity processing and stores that information in a

text-maintained auxiliary staging table: If you attach a partition or load data, must then issue the SET INTEGRITY command on the base table to make data available in the auxiliary staging table: As for the case when a partition is detached, the staging table then requires another SET INTEGRITY command to make the data accessible for processing: Alternatively, a RESET PENDING command on the base table can be used to make the data accessible in all its auxiliary staging tables. The base table is fully accessible for read and write operations while the command is executing: If you detach partition, you must issue the RESET PENDING command on the base table or the SET INTEGRITY command on each of the staging tables. you

Figure 8 Incremental update with triggers and integrity processing

<!-- image -->

Some database operations implicitly or explicitly invalidate the text search index

An explicit invalidation will set the status of the text search index INDSTATUS='INVALID' in the SYSIBMTS TSINDEXES administrative view, for example, the command ALTER DATABASE PARTITION GROUP An implicit invalidation occurs when content changes bypass the staging mechanism, for example, if a LOAD INSERT is used without the extended staging infrastructure: An implicit invalidation will not mark the text search index as invalid.

You can the text index by using a manual or automatic The automatic uses an schedule with specified days and times. You can manually the text search index by issuing the UPDATE INDEX FOR TEXT command or the SYSPROC. SYSTS\_UPDATE procedure. The text search index is updated asynchronously, that is, outside the transaction that inserts, updates, Or deletes data in the database: Asynchronous text search index processing improves throughput and concurrency because multiple updates can be batched and applied to copy of the affected text index segments. The text search index is then only locked for read access for a short period of time while the index segments are in place of the original: update option. update option update update updated put

Text search indexes are reorganized automatically as needed; in addition, you can explicitly trigger reorganization with the adminTool or re-create an index with the ALLROWS when you it. option update

## Dbz Text Search in a partitioned database environment

Db2 Text Search supports full-text search in a partitioned database environment: Text search indexes are distributed in pattern that matches the base tables on which are created. For each database partition, a text index partition, also called collection, is created. This pattern facilitates text search maintenance by allowing text search index with parallel execution on all index partitions they updates

The staging tables used for multi-collection text search index updates are per index rather than per collection and are distributed in a manner similar to the base table: Staging tables use the DBPARTITIONNUM scalar function to find relevant changes that need to be to each index partition per index refresh. Data from each database partition server is in the corresponding text index partition the text search index to enable a parallelization of the operation. applied updated during update update

Every text search index may result in multiple collection updates and text search server capacity planning is required. For workload distribution, a stand-alone remote text search server is recommended in partitioned database environments. update setup

A Db2 Text Search server setup that is installed and configured separately from the Db2 instance is referred to as stand-alone setup. A remote stand-alone setup, that a on separate host from the database server, can be used for non-partitioned, Single-partition and multi-partitioned Db2 instances to remove the resource-intensive text search server workload from the database server host: iS, setup

The configuration of the integrated Text Search server during the default instance creation of a partitioned database instance to the lowest numbered database partition server: It is not required to configure during installation, the administration and configuration of the Text Search server in an existing partitioned database environment can be managed by Text Search server tools\_ applies

The following diagram depicts a Db2 instance with four database partitions are located on two dedicated hosts, Machinel and Machine2 with two logical partitions per host: All database partition servers are served by a single text search server They

Figure 9. A Dbz Text Search server setup in a partitioned environment

<!-- image -->

Stand-alone setups are suggested to help achieve a balanced workload and avoid sharing resources by the text search server with a single database partition server:

In a partitioned database environment, the dbzts START FOR TEXT command with the STATUS and VERIFY parameters can be issued on any one of the partition server hosts. To start the instance services, you must run the dbzts START FOR TEXT command on the integrated text search server host machine. The integrated text search server host machine is the host of the lowest-numbered database partition server: If custom collection directories are used, ensure that no lower numbered partitions are created later: This restriction is especially relevant for Linux and UNIX platforms. If you configure Db2 Text Search when creating an instance, the configuration initially determines the integrated text search server host: That configuration must always remain the host of the lowest-numbered database partition server:

Database partitions in partitioned instance can be added and deleted: This is generally followed by data redistribution, using the REDISTRIBUTE DATABASE PARTITION GROUP command to move and rebalance data in the tables. If a text search index is hosted by one of the affected tables, such data redistribution requires reshuffling of the text index partition content to align the text index partitions with the new set of relevant database partitions. Incremental updates of text search indexes are usually inadequate for this purpose, instead, the text search

index must be updated with the FOR DATA REDISTRIBUTION option: Note that this can result in significant downtimes for large workloads similar to initial updates.

When enabling and administering Db2 Text Search in a partitioned database environment; consider the following:

- Ensure that the Db2 setup is complete as described in the Db2 documentation The NFS mount must be configured with root access and setuid.
- If startup fails, you need to check if Db2 Text Search has been configured correctly and then issue the dbzts START command second time
- On Windows platforms, while Db2 Text Search in a partitioned database environment; the dbznodes.cfg file should not use IP addresses as well as host names for the same host: using
- Before inserting or deleting partition numbers from the dbznodes.cfg file, the Db2 Text Search instance services This applies to any command that might result in changes to the dbznodes.cfg configuration file stop

You should be aware of the following considerations when conducting searches in partitioned database environment:

- The RESULT LIMIT is evaluated on every partition search: This means that if you specify a RESULT LIMIT of 3 and use 4 partitions, you will get up to 12 results. during
- The SCORE value reflects the document's relevance when compared to the SCORE value of all documents from a single partition even if the query accesses multiple partitions.

## Incremental updates for Db2 Text Search indexes

Data synchronization in Db2 Text Search is based on processing the content of a staging table that contains information about new, changed, or deleted documents. By default, triggers are created to capture changes in the text table and the staging table: There is one staging table for each text index: Applying the information in the staging table to the corresponding text index is referred to as performing an incremental update update.

You can perform incremental by the following options: updates using

## LOGTYPE CUSTOM or BASIC

LOGTYPE BASIC is the default and creates primary staging table with triggers on the text table to recognize changes.

LOGTYPE CUSTOM creates a primary staging table but does not automatically add any mechanism to recognize changes. Populate the staging table with a replication setup, or by comparing timestamps in the text table, or any other applicable method to identify changed records.

Depending on the data source, the type might be set automatically and is not customizable: Use the LOGTYPE index configuration option of the CREATE INDEX operation for text search indexes to specify the log log

## AUXLOG ON or OFF

The AUXLOG index configuration option of the Db2 Text Search CREATE INDEX operation controls whether a text-maintained staging table is used for a text search index. This option can be combined with either LOGTYPE basic or BASIC options If the AUXLOG is set to ON, with Logtype BASIC, information about new and deleted documents is captured through integrity processing in option along

an auxiliary staging table that is maintained by Db2 Text Search, and information about changed documents is captured through triggers and stored in the staging table. With LOGTYPE CUSTOM, if the AUXLOG option is set to ON, then information about new, changed, and deleted documents is captured in the auxiliary staging table: By default, this configuration option is set to ON for range-partitioned tables and OFF for nonpartitioned tables.

Capturing changes for an incremental of the text index through integrity processing might require you to perform more administrative tasks. For example, you might need to issue a RESET PENDING command before text search index updates can be processed: The effect of the text-maintained staging infrastructure is similar to the effect of a materialized query table (MQT) with deferred refresh, and similar limitations and restrictions apply for the creation of an auxiliary staging table as for the creation of an MQT: If you tables by using only commands that affect all rows in the tables, for example, by the LOAD REPLACE command, adding the extended staging infrastructure does not provide a benefit: Instead, it is suggested YOu re-create the text search index after table is update update using updated.

To create a text index with a LOGTYPE BASIC and AUXLOG ON, see the following example for an initial and incremental update.

- 1.
- Create a table and add data to it: db2 "create table test.simple (pk integer not null primary comment varchar(48) ) " dbz insert into test.simple values (1, blue and red' ) " key,
- 2. Create a text search index

dbzts "create index test simpleix for text on test\_ imple(comment) index configuration(auxlog on) connect to mydb"

- 3. Update the index and load data:

dbzts "update index test.simpleix for text connect to mydb" dbz Ioad from Ioaddata4.sq] of del insert into test.simple"

- 4. After the load operation, the base table is locked. For example, a select for reason code "1" on table "TEST.SIMPLE" SQLSTATE=57016. The staging table is accessible, but it does not contain the information about the new data: yet
- 5. Enable integrity processing:

dbz "set integrity for test.simple immediate checked"

- The following message is returned:

SQL3601W The statement caused one or more tables to automatically be placed in the Set Integrity Pending state.SQLSTATE-01586

- 6\_ At this point, the staging table is locked, and modifying operations for the base table are rejected. For example, the following statement fails:

"insert into test.simple values (15, green' )

The following message is returned: DBZ1034E The command was processed as an SQL statement because it was not valid command Tine processor command \_ During SQL processing it returned: SQLO668N Operation not for reason code "1" on table "SYSIBMTS" SYSTSAUXLOG\_IX114555" SQLSTATE-57016

- 7 . Reset the tables:

dbzts "reset pending for table test.simple for text connect to mydb"

- After successfully issuing the RESET PENDING command, the staging table is unlocked and modifications on the base table are possible. Unlock the staging table either by issuing RESET PENDING command on the base table to unlock all dependent text-maintained staging tables, or with a SET INTEGRITY command on the specific staging table: again
- 8\_ The text-maintained staging table now contains the changes that must be to the text search index: Issue an command for the index dbzts "update index test.simpleix for text connect to mydb" applied update

## Linguistic processing for Db2 Text Search

Db2 Text Search provides dictionary packs to support the linguistic processing of documents and queries. In addition, n-gram segmentation is supported for languages such as Chinese, Japanese, and Korean: As an alternative to dictionary-based word segmentation, the search engine provides an to select n-gram segmentation for languages such as Chinese, Japanese, and Korean: option

If a text document is in one of the supported languages, linguistic processing is carried out the tokenization stage, that is when then text is broken up into individual words\_ For unsupported languages, the document is parsed white space Or n-gram segmentation: Lemmatization (like stemming, this means to find the normalized form of a word, but it also analyzes the word's part of speech) is not performed on unsupported languages. during using

When you search a text search index, match is indicated if the indexed document contains the query terms or linguistic variations of the query terms. The variations of a word depend on the language of the query

## Linguistic processing for Chinese; Japanese; and Korean documents

For a search engine, getting search results depends in part on the techniques that are used to process text: After the text is extracted from the document, the first step in text processing is to identify the individual words in the text: Identifying the individual words in the text is referred to as segmentation. For many languages, white space (blanks, the end of a line, and certain punctuation) can be used to recognize word boundaries. However; Chinese, Japanese, and Korean do not use white space between characters to separate words, so other techniques must be used. good large

Db2 Text Search provides processing options for Chinese, Japanese, and Korean: morphological segmentation option, also called dictionary-based word segmentation, and an n-gram segmentation (the default setting): two option

Morphological segmentation uses language-specific dictionary to identify words in the sequence of characters in the document: This technique provides search results, because the dictionaries are used to identify word boundaries. precise

N-gram segmentation avoids the problem of identifying word boundaries, and instead indexes overlapping of characters\_ Because two characters are used, this technique is also called bi-gram segmentation: N-gram segmentation always returns all matching documents that contain the search terms However; this technique can return documents that do not match the query: pairs

## Example

To show how both types of linguistic processing work, examine the following text in document: election for governor of Kanagawa prefecture: In Japanese, this text contains eight characters. For this example, the eight characters are represented as A B C D E F G H. A sample query that users might enter could be election for governor; which is four characters and are represented as E F G H. (The document text and the sample query share similar characters.)

- After the document is indexed using morphological segmentation, the search engine segments the text election for governor of Kanagawa prefecture into the following sets of characters: ABC DEF GH.
- The sample query election for governor is segmented into the following sets of characters EF GH. The characters EF do not appear in the tokens of the document text: Even though the document does not have EF, it does have DEF.

Since the document text contains DEF, but the query contains only EF, the document is less likely to be found by using the sample query:

- When you enable morphological segmentation, you will likely see more precise results, but possibly fewer results.
- After the document is indexed using n-gram segmentation the search engine segments the text election for governor of Kanagawa prefecture into the following

The sample query election for governor is segmented into the following sets of characters: DE EF FG GH: If you search with the sample query election for governor, the document will be found by the query because the tokens for both the document text and the query appear in the same order:

When you enable n-gram segmentation, you will likely see more results but possibly less precise results. For example, in Japanese, if you search with the query Kyoto and document in your index contains the text City of Tokyo, the query Kyoto will return the document with the text City of Tokyo. The reason is that City of Tokyo and Kyoto share two of the same Japanese characters

## Scenario: Indexing and searching

After you have installed and configured Db2 Text Search, there are four steps that you must take before performing searches.

- 1. Start the Db2 Text Search instance services.
- 2
- use the Search: The configure procedure is necessary in the following cases:
- Prepare the database for use by Db2 Text Search: Enable the database and configure procedure to complete the Text Search server association. You must enable the database only once for Db2 Text
- enablement was incomplete
- for partitioned databases
- for stand-alone Text Search server setups

Note that you cannot enable Net Search Extender for a database once it has

- 3\_ Create a text search index on column that contains, or will contain, text that you want to search:
- 4 Populate the text search index This adds data to the empty, newly created text search index:

To set up automatic for text search indexes according to specified frequencies, see the topic about scheduling Db2 Text Search index updates update update.

After a text search index contains data, you can search the index an SQL statement and can search with XQuery if the index contains XML data using

As Figure 10 shows, you should update existing text search indexes, either manually or automatically, to reflect changes to the text column that the index is associated with:

Figure 10. Setting up text search indexes for searching in a non-partitioned instance with an integrated Text Search server

<!-- image -->

## Basic scenario

Suppose that you want to make the products in the PRODUCT table in the SAMPLE database searchable by Db2 Text Search: Assuming that you already created the sample database (by running the dbzsamp] command) and that you set the DBZDBDFT environment variable to SAMPLE, you could issue the following commands:

```
dbzts START FOR TEXT dbzts ENABLE DATABASE FOR TEXT dbzts CREATE INDEX myschema. productindex FOR TEXT ON product (name) dbzts UPDATE INDEX myschema. productindex FOR TEXT
```

The product names and descriptions contained in the NAME column of PRODUCT are now indexed and searchable: If you want to find the product IDs of all the snow shovels, you can issue the following search query:

dbz "SELECT pid FROM product WHERE CONTAINS (name, snow shovel ' ) 1"

## Coexistence scenario for Db2 Text Search and Net Search Extender

If a database is already enabled for Net Search Extender; and you want to use Text Search in that database, you can use the index coexistence feature to query the database:

Start the database for text search: dbzts start for text command

The SQL completed successfully\_

Enable Text Search for a database where Net Search Extender indexes are already present:

dbzts enable database for text completed successfully

Create and Db2 Text Search index on a column which has an existing Net Search Extender index update dbzts CREATE INDEX db2ts.title\_idx FOR TEXT ON books (title) completed successfully\_

dbzts "UPDATE INDEX dbzts.title idx FOR TEXT CIEOOOO1 Operation completed successfully.

Activate the new Db2 Text Search index to switch query processing from the NSE index to the new index dbzts CIEOOOO1 Operation completed success fully-

Issue query to use the Db2 Text Search index dbz "select isbn, title from books where contains(title, 'top' )=1"

ISBN

TITLE

123-014014014

Mountain Tops

111-223334444

of the Mountain: Mountain Lore Top

2 record(s) selected.

Queries that attempt to use both types of text indexes are not supported. For example, here the title column has an active Db2 Text Search index, while the bookinfo column has an active Net Search Extender index The search will return an error because all text indexes in one query must be of the same index type:

db2 "select isbn, title from books where contains(title, 'top' )=1 and contains (bookinfo, MOUNTAin )=l"

ISBN

TITLE

BOOKINFO" in table BOOKS" was fied as an argument to text search function, but text search index does not exist for the column \_ SQLSTATE-38H12 speci-

To avoid this error; create Db2 Text Search index on the bookinfo column and activate it.

dbzts CREATE INDEX dbzts.bookinfo\_idx FOR TEXT ON books bookinfo ) CIEOOO01 Operation completed successfuly.

dbzts ALTER INDEX dbzts.bookinfo\_idx FOR TEXT set active completed successfully \_

## Rich text and proprietary format support

Db2 Text Search supports indexing and searching of documents in rich text format and proprietary formats within a properly configured Db2 Text Search instance:

Db2 Text Search supports TEXT, XML, and HTML text index formats to prepare indexes full-text search on text data: In addition, the INSO format enables indexing and searching in documents with rich text Or proprietary formatting: for

- Proprietary formats encompass a variety of common office products, such as, ppt, ods. pdf, doc,
- Rich text documents are documents that contain text as well as formatting instructions such as bold, italics, font types, font sizes, spacing, and more

For information about the enablement and configuration of the INSO format feature, see the topic about setting up Db2 Text Search for rich text and proprietary formats.

## Chapter 3. Text search solution planning

Understanding certain concepts, such as supported document types and languages and user roles, will help you leverage the benefits of Db2 Text Search: key

## Document characteristics

## Document formats supported for Dbz Text Search

You must specify the format (or type) of text documents that you intend to search using Db2 Text Search: This information is necessary for indexing text documents.

The text column data can be plain text, HTML documents, XML documents, or documents with rich text or proprietary formatting: Documents are parsed to extract relevant for indexing, thus making them searchable: Some elements, for example,, and metadata in an HTML document; are not indexed and thus not searchable: parts tags

## Supported data types

The data types in the text columns that you want to index and search can be either binary or character:

Db2 Text Search supports the following data types:

- CHAR
- VARCHAR
- LONG VARCHAR
- CLOB
- DBCLOB
- BLOB
- GRAPHIC
- VARGRAPHIC
- LONG VARGRAPHIC
- XML

## Conversion of unsupported formats and data types

You can use your own function to convert an unsupported format Or data type into a supported format or data type:

By creating the text index using a user-defined function (UDF), you can convert an unsupported format to supported format that can be processed indexing by filtering the unsupported characters. during

You can also use this approach for indexing documents that are stored in external unsupported data stores. In this case, where a column contains document references, you can use a UDF to return the content of documents that have the relevant document reference

## Supported languages and code pages

You can specify that the text documents be parsed using a particular language when you first create a text search index: You can also specify that the query terms be interpreted in a particular language while searching: In addition, You can specify a code page when you create a text search index on binary data type column:

## Language specification

A locale is a combination of language and territory (region or country) information and is represented by a five-character locale code. You define the message locale for a text search administration procedure by passing the procedure the locale code: Refinements of these locale codes are possible depending on the locales installed on the Db2 server:

There is an important difference between specifying language when you create text search index and specifying a language when you issue a search query:

- The locale that you specify in a search query is used to perform linguistic processing on the query and to help identify the base forms of the query term After the locale of the base form has been identified, the locale does not play any part in the search process itself Thus, You could use the English language for a query and obtain German documents in the search result if the search term in its base form is present in the documents.
- The locale that you specify in your dbzts CREATE INDEX command determines the language used to tokenize or analyze documents for indexing: If you know that all documents in the column to be indexed use specific language, specify the applicable locale when you create the text search index: If you do not specify locale, the database territory will be used to determine the default for LANGUAGE. To have your documents automatically scanned to determine the locale, in the SYSIBMTS TSDEFAULTS view, set the LANGUAGE attribute to AUTO. The SYSIBMTS.TSDEFAULTS view describes database defaults for text search attribute-value setting using pairs.

The list of supported locales can be found here

## Code page specification

You can index documents if use one of the supported Db2 code pages. Although specifying the code page when creating a text search index is optional, doing SO helps to identify the character encoding of binary columns If you do not specify code page for binary columns, the code page from the column property is they used\_

## Document size considerations

Db2 Text Search has limits on the size of a document that can be indexed and on the number of characters within that document:

The maximum size of documents that can be processed successfully is controlled through the MAXDOCUMENTSIZEINMB parameter in SYSIBMTS TSDEFAULTS administrative view. The default value of this parameter is 100 MB. If a document exceeds the size limit, that document is rejected and an entry is created in the event table with that information, including the primary to identify it Processing continues for other documents that are a part of that operation. key update

Db2 Text Search limits the number of Unicode characters that you can index for each text document: Sometimes, this character limit results in the truncation of text documents in the text search index large

The default value for the number of Unicode characters allowed for each text document depends on the text document format:

- Text files that are larger than the value of max text.size (in characters) are truncated to this size before are indexed: The default value is 60 000 000 characters: they
- XML files that are larger than the value of max xml.text size (in bytes) are not indexed. The default value is 60 000 000 bytes. The count includes names, attribute names, and attribute values, but not XML directives and comments\_ tag
- Binary files that are larger than the value of max: text.size (in bytes) are not indexed: The default value is 60 000 000 bytes. This limit is applied after the document is transformed to text\_ binary t

When the size of a text file exceeds the maximum text file size (60 million characters by default), the text file is truncated to the size limit before it is indexed: If a text document is truncated the parsing stage, you receive a warning that some text was not processed correctly or completely: during

When the size of a document in binary or XML format exceeds the maximum file size (60 million bytes by default), the document is not indexed and an error is generated.

Search results are incomplete if text is incorrectly or incompletely processed: If possible adjust the size limits or alternatively prune the document for processing: Details about the warning are written to the event table that was created for the text search index:

If you want to increase the file size limits, you must increase the heap size accordingly You can use the configuration tool to adjust the maximum heap size by specifying the startupHeapSize parameter:

## Db2 Text Search security overview

Db2 Text Search executes administrative operations based on the authorization ID of the user executing the operation. Different to previous releases, there is no prerequisite for database privileges for the instance owner anymore, and it is not necessary for the fenced user to be in the same primary group as the instance owner

Executing operations with the authorization ID of the user improves auditability and improves control of text search management: To simplify access control, three new system roles are available:

- Text Search Administrator (SYSTS\_ADM) executes operations on database level
- Text Search User (SYSTS\_USR) has access to text search catalog data
- Text Search Manager (SYSTS\_MGR) executes operations on index level

The security administrator can grant or revoke these roles like user-defined roles, however; roles with prefix SYSTS are managed otherwise and cannot be dropped or created. system

When a database is created, the roles are automatically assigned to the database creator; and in non-restricted databases, the SYSTS\_USR role is assigned to PUBLIC. All other role assignments must be done explicitly by the security

In restricted database setup, the security administrator must grant execute privileges for scheduler procedures to SYSTS\_MGR role and user privileges for the SYSTS\_USR role:

Table privileges to manage or access content in the SYSIBMTS catalog tables are automatically granted to the roles during database enablement for Db2 Text Search: Similarly, table privileges to manage or access content in the SYSIBMTS administration tables for a specific text search index are automatically granted to the roles during text index creation. For example, to create a text index you will need privileges on the base table corresponding to the privileges that are needed to create other types of indexes, and also the SYSTS\_MGR role which provides access privileges to the SYSIBMTS tables.

Certain index-level commands require a connection to the text search server: The relevant connection information is retrieved from the SYSIBMTS.TSSERVERS administrative view and includes an authentication token: The token is generated when the text search server is configured and used as an identification mechanism by callers to ensure that the right text search server is addressed. If the token is used, the index management or search request is rejected: wrong

The following table provides a summary of required role privileges. The security administrator must have granted the appropriate role to the user for successful execution of an operation.

Table 1\_ Role privileges

|                           | Role      | Operation                                                                                 |
|---------------------------|-----------|-------------------------------------------------------------------------------------------|
| Text Search Administrator | SYSTS_ADM | Enable, Disable, Clear command locks (all), Configure                                     |
| Text Search Manager       | SYSTS_MGR | Create, Update, Alter; Clear Events, Clear command locks (per index), Reset Pending Drop, |
| Text Search User          | SYSTS_USR | Limited access to the text search SYSIBMTS catalog                                        |

## User roles

There are different user roles and authorizations for users of Db2 Text Search: System roles control execution privileges for administrative operations and the authorization ID of the user thus needs the adequate text search role in addition to database or table access privileges to execute a text search operation.

Typical users are:

- Text Search Server Administrator
- Text Search Administrator
- Text Search Index Manager
- Users performing text search queries

## Db2 Text Search Server Administrator

The Text Search Server Administrator configures Db2 Text Search server options, starts and stops the text search instance services for integrated and stand-alone text server deployments and monitors text search server operation.

For integrated text search server setups this role is tied to the database instance owner:

The instance owner is determined differently on UNIX and Windows operating systems:

- On UNIX operating systems, the instance owner user is the name and user ID of the instance specified for the dbzicrt command.
- On Windows operating systems, the instance owner is the user ID running the Db2 instance service.

Contrary to Db2 Version 9.7, the instance owner does not need to hold database privileges. stand-alone text search server setups, the server administrator must have appropriate access to text search server executable, configuration and index files. For

## Text Search Administrator

The Text Search Administrator enables and disables databases for use with Db2 Text Search: Another main task that the Text Search Administrator performs is clearing command locks.

The text search administrator requires the SYSTS ADM role in addition to DBADM authorization, which allows the manipulation of all database objects, including text search indexes.

## Text Search Index Manager

The Text Search Index Manager defines and maintains text search indexes.

Typical tasks are:

- Creating text search indexes and defining their characteristics
- Updating text search indexes
- Changing the characteristics of text search indexes update
- Dropping text search indexes
- Clearing the event table periodically

Text Search Index Managers have the SYSTS\_MGR role and usually have CONTROL privilege for the table on which a text search index is created:

## User performing text search queries

Users who perform search queries can use the Db2 Text Search CONTAINS and SCORE functions in an SQL query user table: can also use the xmlcolumn-contains function in an XQuery that references a table with a text search index against They

There is no Db2 Text Search search authorization. Depending on the access rights that the users are granted on the table that the text search index is created on, the query is permitted or rejected. If users can issue a SELECT statement on a given table, can also perform a text search on that table: specific they

Users performing the search queries can for example include the following functionality in their queries:

- Limit the text search to a particular document (using SQL or XQuery)
- Return a score indicating how a document compares with other matching documents for a given search argument (using SQL) well

## Access policies and communication security

## File access considerations for the Text Search server

The process owner of the text server process requires read and write access to configuration data and all collection data, including collections located in custom collection directories\_

For the integrated text server the process owner is the instance owner; for stand-alone text servers it is the user who starts the text server with the startup command.

Collections may include confidential data that can be partially readable when opening a file directly To prevent unauthorized access, check and update the access permissions to configuration and collection directories to ensure that only the process owners of the text server may access the files.

## Staging table access policies

To identify changes that need to be applied to a text index, the primary of modified rows (inserted, updated, deleted) is inserted into the staging table key

The primary may be based on data columns of the base table that contain confidential data. By default, users with role SYSTS ADM and SYSTS\_MGR, and with some restrictions, SYSTS\_USR, have at least read access to the content of staging tables. Access and audit policies for the base table are not inherited for the staging table: If further restrictions for access to a particular staging table are needed, the security administrator will need to revoke read privileges on the specific table for the roles and them to a user or a custom role who will manage the text index key grant specific

## Stand-alone setup

The Db2 database instance uses TCP /IP to communicate with the stand-alone Db2 Text Search server: SSL or GSKit support are not available, however; encryption channels can be used through the stunnel program or SSH tunneling: Restrict access to your document repository and text search index files depending on your security requirements. The stand-alone text search server must be installed on computers with a secure network connection, behind firewall to prevent unauthorized access to the text search indexes. Setting up TCP / IP access restriction to the stand-alone text search server ensures that it can only be accessed by the host on which the database server is installed:

## Db2 Text Search capacity planning and optimization

number of factors influence performance and resource use in Db2 Text Search: When planning system capacity for Db2 Text Search, consider the query workload, the number of parallel index updates, the expected size and growth rates of text indexes, and the processing time for the documents you are indexing: your

database, including support for XML documents and a rich-text o proprietary format feature: Full-text search is supported through a text search server instance that is integrated with the database instance or in a stand-alone setup associated with the database instance. Communication between the database and text search server instance is through TCP\_ IP Full-text indexing and search performance depend on the text search server configuration, available system resources, and text index specific settings.

## Text search server deployment and configuration

single text search server is configured for the database instance. The text search server has a recommended minimum memory requirement of 4 GB of memory for production use, which increases according to the number of parallel index updates:

Updating the text search index is resource-intensive, both in terms of disk I/O and CPU or memory requirements. Multiple configuration parameters are available to control the Text Search server resource usage: workload distribution, for example, in partitioned database environment, a stand-alone setup is recommended: For

## Size of text search indexes

On average, a text search index is about 50-150% of the original data.

There is no absolute size limit for text search indexes, however; the combination of throughput factors with completion time dependencies results in practical limits on the total text search index size. For example, when a considerable amount of data is added to or removed from a text search index, the text search index structure is merged to improve query performance, and the time for completion of the merge depends on the size of the index:

## Factors affecting throughput

Absolute text index throughput depends on the data type and the index format: For perceived query performance, the biggest impact is due to the number of matching results, not the size of the text search index For example, a query with a single predicate using a single-term search term on 100 GB text search index performs similar to search on an 800 GB text search index if the number of results is the same update

Optimal processing for text index updates occurs when there is approximately 10-100 KB of text per document Throughput degrades above 1 MB and below 1 KB of text:

## Dbz Text Search server configuration

You can tune Db2 Text Search configuration by adjusting the queue Sizes, heap size, number of indexing threads, and other factors. Balance adjustments to these different parameters for performance of your your your optimal system.

For the Db2 Text Search server configuration the number of indexer threads should not exceed the number of CPUs, and the number of parallel should not exceed the number of indexer threads. Note that to determine the number of parallel updates in partitioned database the number of indexes is multiplied with the number of collections for a text index updates

Stop the Db2 Text Search instance services the dbzts STOP FOR TEXT command before making any configuration changes. using

## Start the configUtility:

- an For
- For an stand-alone text search server it is located in the &lt;ECMTSHOME&gt;/bin directory:

For example, to change the number of indexing threads: 3

For your changes to take effect, restart the Db2 Text Search processes.

## Maximum heap size configuration

When document is received by the document ingestion thread, its content is placed in the document queue. Documents placed on the document queue remain there until an active indexing thread indexes it: In typical operation, the of placing documents on the document queue is faster than the time required to parse and index the document: Therefore, at some in time, the document queue reaches its capacity, and the document ingestion thread is blocked until another slot is freed from the document queue: speed point

As the document queue fills with unprocessed documents, it consumes memory: Further memory is consumed for document processing like parsing and indexing: The combined memory consumption must be less than the maximum size of the process. By default, the size is configured to be 1500 MB. heap heap heap heap

Also, consider the ratio between the input and output queue memory size and the memory The queue size is determined by the memory consumption of the documents in the queue: If you intend to process documents, like 20 MB each, and decide to increase the queue memory size, consider increasing the size: heap long heap

The startupHeapSize variable sets the maximum allowed heap size for the integrated or the stand-alone Db2 Text Search server: The default startup size is 1.5 GB. This value must be a number between 1.5 GB and the maximum amount of memory allowed by operating system and JVM version. Consider the following examples: heap your

- If you have an AIX@ system with 64-bit JVM, then the maximum size is limited only by the amount of virtual memory configured on the system If many documents with an average size of 20 MB must be processed continuously, then increase the startupHeapSize parameter to approximately 4 GB. heap large
- If you have a Windows system with a 32-bit JVM, then a process can have a maximum size of 2 GB. Therefore, your startupHeapSize parameter must be set to less than 2 GB. For example, 1.8 GB heap

You can set the maximum size when you install or upgrade the stand-alone response file. When you set the maximum size to a value greater than 2 GB during the installation or upgrade of the stand-alone text search server on 64-bit operating system, file size limits for text, XML, and binary documents are increased for new collections. File size limits are specified per collection in the parser\_config.xm] file: The default file size limits new collections are specified in the &lt;ECMTS\_HOME Iconfigl heap heap for

memory over 2 GBs, the values of the file size limits (60 MB by default) are increased by 1 MB (up to 400 MB). heap

Attention: When you modify the maximum size by using the configuration tool after installation, you must manually adjust the file size limits in the parser\_config.xm] file. File size limits are automatically adjusted only during installation and upgrade when you specify the IA\_STARTUP\_HEAP\_SIZE parameter in the response file: heap

To change the maximum issue the following command: heap, configToo] configureParams ~configPath &lt;full-path-to-configuration-folder&gt; ~startupHeapSize &lt;value&gt;

where, &lt;value&gt; is the size and &lt;full-path-to-configuration-folder&gt; is the full to the config.xm] file for Db2 Text Search server: heap path

On a 32-bit operating system, the typical configuration is:

- Maximum heap
- Queue sizes: 90 MB each
- File size limits: 60 MB

On a 64-bit operating system, the typical configuration is:

- Maximum size: 3 GB heap
- Queue sizes: 150 MB each
- File size limits: 200 MB

## Dbz Text Search indexing threads

Multiple indexing threads work in parallel to parse and index documents. This usually reduces the total elapsed time for text search index updates.

Indexer threads pick documents from the queue and manage the indexing process. make use of index preprocessing threads to prepare the document content for indexing and write the result to the text index collection: They

Index preprocessing threads extract text; identify the language, tokenize and analyze the document:

Usually the number of indexer threads and index preprocessing threads is configured to be the same. However; in some scenarios, for example, when documents are processed, increasing the number of preprocessing threads might provide performance benefit: large

## Indexing thread usage

If multiple indexer threads work on the same collection, the effect is reduced by the coordination required to synchronize the processing among the threads. Also, indexing threads that are single threaded perform better while parsing, but there can be a performance hit while merging or writing to disk For example, four indexing threads working on four different text indexes show better throughput than four indexing threads working on single text index

## Number of indexing threads

You should have at least two indexing threads and ensure that the number of indexing threads does not exceed the number of available CPUs The maximum number of parallel index updates should not exceed the number of indexing threads to avoid thread sharing: With too many indexing threads or too many parallel index updates, the overall system performance suffers due to memory usage for process context switches.

For example, if 40 text indexes are frequently updated, and the system contains 8 CPUs, do not use more than eight indexing threads. Also, use staggered schedule for the text indexes to minimize contention for index threads.

The default setting for the number of indexer threads is 4, the same default applies to index preprocessing threads.

To configure the number of indexing threads, issue the following command: configTool configureParams ~configPath &lt;full-path-to-configuration-folderz ~numberOfIndexerThreads &lt;value&gt;

where &lt;value&gt; is the number of threads and &lt;full-path-to-configuration-folder&gt; is the full to the config.xm] file for the Db2 Text Search server: path

To configure the number of preprocessing threads, issue the following command: configToo] configureParams ~configPath &lt;full-path-to-configuration-folder&gt;

~numberofPreprocessingThreads &lt;value&gt;

where &lt;value&gt; is the number of threads and &lt;full-path-to-configuration-folder&gt; is the full to the config.xm] file for the Db2 Text Search server: path

## Db2 Text Search queue memory size

The queue memory size for Db2 Text Search must be set properly for optimal index processing: Queue memory assignment can be controlled both for the database and for the text server update

The database queue memory determines the number of documents that can be sent to the text server for processing at any time: To control the size of the database queue memory, the SYSIBMTS TSDEFAULTS administration view and set the value for the DocumentResultQueueSize parameter: The default value is 10,000. This value is used to limit much database memory is reserved per operation for a collection. Note that on multi-partition setup, a single text index that is configured for parallel execution will reserve memory space for each collection that needs an update update how update update update:

The second mechanism for queue memory control applies to the text server: Two configuration values determine the use of queue memory

- inputQueueMemorySize: Specifies the memory size of the input queue on the indexing server: The input queue contains documents that are waiting for preprocessing: A larger memory size will be faster; but will consume more resources\_ The default size is 15 MB.
- outputQueueMemorySize:

Specifies the memory size of the output queue on the indexing server: The output queue contains documents that are waiting to be indexed after preprocessing: A larger memory size will be faster; but will consume more resources. The default size is 15 MB.

Consider the ratio between the input and output queue's memory size and the memory The queue Size is determined by the memory consumption of the documents in the queue. If you intend to process documents, for example 20 MB each, consider increasing the queue memory size and increasing the size heap long heap

To change, for example, the inputQueueMemory size, issue the following command: configToo] configureParams -configPath &lt;full-path-to-configuration-folder&gt; -inputQueueMemorySize &lt;value&gt;

where &lt;value&gt; is the memory size and &lt;full-path-to-configuration-folder&gt; is the full to the config xml file for Db2 Text Search: path

## Dbz Text Search index planning and optimization

Data source characteristics have major impact on performance

The time required to complete a text index depends mainly on the following factors: update

- the number of documents to be indexed
- the document size
- the index type
- index update parallelism
- text search server configuration

The processing time for each document is the sum of an approximate fixed time and variable time: The fixed time is influenced by the document type, such as plain text, XML or INSO. The fixed time is approximate because there can be minor variations in time for memory usage Or reuse: The variable time is determined mainly by the document size and linguistic processing variations.

For indexes of INSO documents, handling different MIME types can also affect the processing time.

The number of documents that can be processed in a given timeframe increases for smaller document sizes. However; the total throughput is less for smaller documents than for larger documents due to the fixed cost per document:

## Db2 Text Search index source characteristics

To enhance performance during indexing or search, use the following techniques:

- For primary columns, use numeric data types, such as INTEGER, instead of VARCHAR type: Avoid primary keys that are a compound of multiple VARCHAR columns to minimize traffic for query results. key
- Ensure that your system has enough real memory available for the index update operation: Index require memory that is in addition to that required for any database buffer If there is insufficient memory, the operating uses paging space instead which decreases search performance considerably updates pools. system
- If large numbers of small documents must be processed in text search server index updates, consider reducing the number of parallel index updates and instead increase the queue Sizes to increase the maximum flow of documents to the text server: See the capacity planning topics for details:
- Ensure that the content to be indexed is accessible and of proper format, as the performance might decrease an index update if many error and warning messages are written to the event table: during

## Asynchronous index updates

To improve performance, a text search index is not synchronized with its associated user table within the scope of a DB2 transaction that updates, deletes text documents from, or inserts text documents into that table Instead, text search indexes are updated asynchronously:

To facilitate the asynchronous of a text search index, create a staging table, which is also known as a table, for each text search index With the default logtype BASIC option enabled, triggers are created on the text table to capture any changes to a text column that the text search is associated with: The triggers then write these changes to the staging table. In cases where the use of triggers is not possible or not required, you can use the logtype CUSTOM to create logtable without adding triggers to the text table: With the logtype CUSTOM option, there is no automatic detection of changes for incremental updates. Instead, you must manually populate the logtable parameter: update log

You can use auxiliary staging table to capture changes that are recognized through integrity processing: The updates to the text search index are applied at a later stage, either a manual or an automatic The is made to a copy of a small part of the index During the update, can still do searches on the index, but you cannot access the text search index until the synchronization is complete an during update update. update you updated

Text index update processing provides a feature to specify the commit size by the updateautocommit argument: To provide further control, more settings are now available to determine whether the commit size must be treated as rows or hours and to help determine how many batches to process: For example, with the committype hours setting, You can control how much time is acceptable for potential reprocessing in case of failure, such as, 2 hours or 4 hours. using

If you set the commitcycle parameter; an initial processes data in index order and saves the last committed This is then used to continue the process when the is restarted. For an incremental update, the entries are deleted after a is completed, and there is no need for a committed to restart processing: However; new changes on previously processed keys are processed before the incremental update continues with the remaining update key key: key log \_ update cycle key again keys:

Consider that each commit requires significant processor usage if using the updateautocommit or commitcyc]e options, which increases the total time for completing an index You should set these options for updates that have a large total elapsed time, such as initial updates or updates that involve all o most of the rows. By using these settings you can avoid completed work due to rollback that is caused by a system or server failure: cycle update. losing

## Optimizing a Dbz Text Search index

Db2 Text Search index optimization compacts the text search index and speeds up indexing and searching: Optimization removes deleted documents from the text search index and merges the index segment files on the disk

Optimization and indexing of the same index cannot be performed in parallel: Take this into account when scheduling optimization and indexing sessions. However; optimization and search can be performed in parallel. Disk space consumption during index optimization can be high, especially if the same index is searched in parallel.

You can optimize the index after you completely index your document set or after incremental index Index optimization can take a long time, depending on the index size. If your incremental updates add documents frequently, perform optimization less frequently to minimize the extra processor usage for the optimization process. updates.

To optimize the index:

- 1\_ From the ECMTS\_HOME/bin directory, start the administration tool with the optimizeIndex command: For example:
- adminTool.bat optimizeIndex -configPath "C:|Program
- 2\_ You can check the status of the last executed optimization process by running the administration tool with the optimizeIndexStatus command.

## Disk consumption

## Text index size

The amount of disk space a text search index uses depends highly on the nature of the text in each document: However; there is an approximately linear relationship between the disk space required for the text search index and the disk space required for the original data. Typically, the size of the index on the disk is 50 150% of the original text size: example, on a table with an integer primary the text search index for 100,000 20 KB documents is expected to require about 1100 MB of disk space (100,000 x 20 KB x 55%). The size of the text search index relative to the source documents depends on the following factors: For key

- the average size of the document
- the size of the document (the primary columns) key key
- the number of sortable fields
- the number and distribution of unique terms

During the index update, additional work space is needed. The intermediate space requirements are about a factor 2-3 times the final text search index size, provided the maximum segment size is not reached. The free space required is 2-3 times the maximum segment size. Disk space is reserved even after a segment merge if the old segments have been used in a search.

## Log files

In addition to the db2diag. og file, Db2 Text Search generates trace and Configuration tool files with messages from the Db2 Text Search server: log

For an integrated Text Search sever; the default file location is db2tss/Iog directory If you want Db2 database and text search in the same location, set &lt;instanceProfilePath&gt;|&lt;instance\_name&gt;|dbztss ts]og on Windows platforms log logs

For the stand-alone the default location for the Db2 Text Search server is &lt;ECMTS\_HOME&gt;/Iog: You can change the default location during installation by setting the IA\_ LOG\_PATH parameter in the response file: logs setup,

In either case, ensure that the target location has sufficient free disk space for the files: A minimum of 100 MB of free disk space is required. Without sufficient log

space for the files, the text search service stops logging and throws a disk full error log

## Administrative tables

If you do not specify a table space for the administrative tables for the text search index when you run the CREATE INDEX FOR TEXT command, the administrative tables are created in the table space that contains the base table: To determine the appropriate location, consider the following information:

- Staging table for the text index

The staging table holds the reference to rows that have been in the base table for an incremental update of the text index: This table is automatically cleaned up with each updated update:

Size number of rows for index updates (Tength of primary key of base table 18)

- Event table for the text index

The event table contains status information about text index processing, including errors and warnings during an index In the worst case, if each document is rejected due to a nonfatal error; the number of events is the number of documents plus a few begin and end messages for the process: The event table is not cleaned automatically, and increases in Size until a CLEAR EVENTS FOR INDEX operation is update. update completed.

Event table size

number of events

(Tength of primary key of base table 1050)

## Db2 Text Search index location

It is important to note that the default index location has changed in this release:

an integrated Text Search sever; configuration and collection metadata is stored in instanceHome/sq]lib/dbztss/config on UNIX Or instanceProfilePath" instance\_ name ldbztss |config on Windows: For

The configuration and collection metadata for each text search index require little space. However; unless a custom is specified, the location for text search indexes is in a subdirectory of dbztss/config: This location is often restricted in size, it is therefore strongly recommended to configure the defaultDataDirectory parameter for the Text Search server to a custom location with sufficient disk space if you plan to create multiple or large indexes with an integrated Text Search server: path

The location of collection data is determined when you create a collection and is location of configuration files for collections is determined by the defaultDataDirectory parameter: By default, the collection configuration directory text collection configuration directory

In any case, if you plan to create multiple large indexes, consider storing them on separate or striped disk devices, in particular if concurrent index updates are scheduled:

## Index specific parameters for Db2 Text Search index updates

You can configure the following collection-specific parameters to improve performance:

- MaxMergeDocs
- MaxMergeMB
- MergeFactor
- BufferSize

You can modify indexing parameters for a particular collection by editing the the default settings for future collections that are created, set the values of these

- The MaxMergeDocs parameter defines the largest segment (measured by the number of documents) that can be merged with other segments in the index There is trade-off between overall indexing throughput and segment merge time.
- If you specify a low value for the MaxMergeDocs parameter (for example, 100,000 documents) , segments will be limited in size. In this case, segment merges are quicker and indexing flows more smoothly without time-outs. However; if your content is very large, there will be numerous segments and a degradation in indexing throughput over time: your

If you specify a high value for the MaxMergeDocs parameter (for example, 100,000,000 or 500,000,000 documents) , you fewer segments (until the index becomes very large) and the overall indexing throughput is better: However; segment merges take more time and you might encounter time-outs during indexing: get

Typically the value of MaxMergeDocs should be higher for collections of small documents and lower for collections of larger documents.

- The MaxMergeMB parameter defines the largest segment, measured by the physical size of the file, that can be merged with other segments in the index:
- There is trade-off between overall indexing throughput and segment merge time. If you specify low value for the MaxMergeMB parameter; for example 500 MB, your segments will be limited in size. In this case, segment merges are quicker and indexing flows more smoothly: However; if your content is very there will be numerous segments and a degradation in indexing throughput over time, as well as degradation in search performance: large,
- If you specify a high value for the MaxMergeMB parameter; for example 50,000 MB or 100,000 MB, you get fewer segments (until the index becomes very large) and the overall indexing throughput is better: However; segment merges take more time and you might encounter time-outs during indexing:
- The BufferSize parameter specifies the amount of RAM that can be for buffering added documents before the documents are flushed as a new segment: There is trade-off between frequent, small flushes to disk and less frequent, large flushes to disk In some cases you can improve performance by increasing the value of the BufferSize parameter: For example, when you index a single used
- The MergeFactor parameter defines the number of segments that are merged at a time and also controls the total number of segments that can accumulate in the index: There is a trade-off between frequent; small merges (for example, two at a time) and less frequent; large merges (for example, 10 at a time) You can specify merge factor does not typically impact performance

collection of small documents, increasing the buffer size will improve performance, especially for the first 100,000 documents in the index

## Db2 Text Search system tuning

Text index processing and text search query performance are influenced by various system characteristics. update

Take the following into consideration:

- TCP /IP port considerations for Windows
- File descriptors

## TCPIP port considerations for Db2 Text Search and Windows

On 32-bit Windows operating systems, your ability to handle high query loads is affected by the number of TCP /IP ports and the wait time to reuse a port:

## Port assignments on Windows (32-bit)

The integrated Db2 Text Search runs as a separate process on the same host as the database server: The database server and text server communicate through a TCP /IP connection.

The number of available ports for TCP /IP connections is influenced by the number of ports and the wait time to reuse port after a connection is closed: The default configuration values for these parameters might not be sufficient to provide enough available ports to serve high query load. If you have too few TCP /IP ports, you might get an CIEO0756 Connection failed error:

If a CIEO0756 Connection fai ]ed error occurs, run the following commands to view port usage on the server:

netstat ~n netstat ~n number&gt;

If the output shows many TCP \_ IP connections and local addresses 127.0.0.1:port\_number in TIME\_WAIT state, the server is likely running out of TCP /IP ports.

You can determine the Db2 Text Search port numbers by issuing the following command:

configToo] printAdminHTTPPort -configPath where, INSTPROF is set to the value of the DBZINSTPROF registry variable applicable to integrated Db2 Text Search server setups.

## Port settings

Port settings are controlled by the following registry entries that are found in

- TcpTimedWaitDelay

A DWORD value, in the range 30 300, that determines the time in seconds that elapses before TCP /TP can release a closed connection and reuse its resources Set the TcpTimedWaitDelay value to a low value to reduce the amount of time that sockets stay in TIME\_WAIT state

- MaxUserPort

A DWORD value that determines the highest port number that TCP /IP can assign when an application requests an available user port: Set MaxUserPort to a high value to increase the total number of sockets that can be connected to the port:

system making many connection requests might perform better if TcpTimedWaitDelay is set to 30 seconds, and MaxUserPort is set to 32678.

After or changing the registry entries, reboot the Windows machine to reflect the changes. adding

## Db2 Text Search file descriptors

For Db2 Text Search index updates and queries, system resources such as file descriptors are consumed to handle multiple index and search requests. update

In typical system, the number of open file descriptors per process may be limited to relatively small number like 1024, which can result in the text search server running out of file descriptors. If this occurs, the search and requests will fail. update

To resolve this error

- Check the server logs for an exception with the message string similar to too many open files.
- On UNIX systems, check the limits with ulimit ~a\_ system

To increase file descriptors, follow these steps:

- 1. Shut down the text search server:
- 2. Increase the number of file descriptors per process by following your operating manual. This increase in file descriptors must be sufficient to accommodate all requests across login sessions. system
- 3 Restart the text search server:

## Dbz Text Search query planning

There are several aspects to consider when planning your text search query

## Dbz Text Search arguments

Wildcard characters and their expansion limit, the case sensitivity of arguments, and argument options are different types of text search arguments that can all affect query performance

## Wildcard characters

a wildcard character at the beginning of a search term slows query processing: Where possible, avoid performing searches such as *search\_ term or ?search term\_ Using

## Wildcard expansion limit

When a query term includes a wildcard, the query term is expanded matching documents are retrieved. A text index collection might include more distinct matching terms than the wildcard expansion limit allows. In that case, only the subset of documents that match the already expanded terms is returned. This limitation applies to the asterisk wildcard character: (*)

By default, 1024 terms can be returned. To change this limit, specify the queryExpansionLimit parameter and a value for the parameter in the ECMTS\_HOMEIconfig lconfiguration.xm] file: For example, to set the limit to 4096, add the following line to the file:

&lt;queryExpansionLimit 4096&lt;/queryExpansionLimit&gt;

## Case sensitivity

Text search arguments are not case sensitive, even if you specify an exact term or phrase by double quotation marks. For example, a search for the term Ham]et can return both the Shakespearean play Ham] et and hamlet, the term for a small using village.

## Search argument options

Search argument options are properties of the search argument: For example; in the following search query for the word bank, the options of the QUERYLANGUAGE search argument are different:

CONTAINS (co]umn bank QUERYLANGUAGE-en\_US ' ) and

CONTAINS (column\_ bank QUERYLANGUAGE-de\_DE' )

## Db2 Text Search multiple predicates

If a query contains multiple predicates, consider the following limitations depending on how the predicates are organized.

## UNION versus OR operators

Query performance might improve by using UNION instead of OR to combine multiple predicates.

## Using a JOIN

Text search functions can be a predicate in an outer join, with limitations for LEFT OUTER JOIN and FULL OUTER JOIN. For these cases a text search predicate can only be if the search on this text index can be joined back with the primary of its base table: For example, the following type of query is supported: applied key select place.placenum, Iocation.description from place LEFT OUTER JOIN ocation on (Iocation.mgrid place.ownerid) where (Tocation.description is null and contains (place.description, Paris' )=l )

The CONTAINS and SCORE functions are not supported as predicate in LEFT OUTER JOIN or FULL OUTER JOIN.

## Dbz Text Search locale and language

Locale specification can also impact the performance of a text search query:

## Locale specification

When you perform a search on a text search index in multi-lingual environment, it is suggested that always use the QUERYLANGUAGE with search query to specify which locale (a combination of language and territory information) to use to interpret a search term. For example, if you have a search term such as bald, YOu can specify to treat it as an English word by setting the QUERYLANGUAGE-en\_US in the search query Similarly, if you want it to be treated as option you your

German word, QUERYLANGUAGE can be set to de\_DE. However; it should be noted that the results returned are highly dependent on the LANGUAGE used for indexing, regardless of the QUERYLANGUAGE specified in a query

If the QUERYLANGUAGE is not specified in the search query, then the following logic is used:

- The search term is interpreted to be of the locale that was set for the underlying text index index creation. during
- If the locale set for the index during index creation is AUTO, then this defaults to English (en\_US), and the search term will be treated as an English word.

## Restrictions:

- If the locale specified in the search queries is invalid (for example, QUERYLANGUAGE-Mongol ian), then the query will be considered invalid and an exception will be thrown:
- Setting QUERYLANGUAGE-AUTO in the search query is an unsupported and the results of the query are undefined. option

Note that the locale specified by QUERYLANGUAGE has no effect on the locale of error messages resulting from search queries The error-message locale that is used depends on whether you started the text search instance services. If you did not start them, messages are written en\_US; if you did start them, messages are written in the same locale of the environment in which you issued the START FOR TEXT command using

## Db2 Text Search SCORE function

The score of a document is dynamic and calculated independently for each query

Updates to a document as well as or removing documents from a text index can cause a change of the score of a document for a query term. adding

Assume there is a set of documents discussing transportation and pollution: If you want to locate documents containing references to both terms, but only if the term po] Tution scores higher than the term transportation, you can use the following command:

```
SELECT document id FROM document library WHERE SCORE (document content po] lution' ) SCORE (document_content , transportation and CONTAINS (document content transportation pollution' ) 1
```

To enhance performance, You can format your query to use the boost modifier so that the search function is run only once, as follows:

```
SELECT document id FROM document library WHERE SCORE (document content po] ution^10 transportation' ) ORDER BY SCORE (document content po] Iution^10 transportation
```

DESC

query gives higher importance to Iution but still returns documents if

Multiple instances of RESULTLIMIT within query require the same search argument to produce predictable results

## Description

If you use multiple text searches that specify RESULTLIMIT in the same query, use the same search argument different text search arguments might not return the expected results. Using

For example, in the following query, it is unpredictable whether the 10 documents specified by RESULTLIMIT will be returned:

```
SELECT EMPNO FROM EMP RESUME WHERE RESUME  FORMAT ascii AND   CONTAINS RESUME , ruby on rails" RESULTLIMIT-l0' ) 1 AND   CONTAINS RESUME , "java script' RESULTLIMIT-10 ' )
```

Instead, use RESULTLIMIT as follows:

SELECT EMPNO FROM EMP RESUME WHERE RESUME\_FORMAT ascii AND   CONTAINS (RESUME, java script" "ruby on rails

Note that this method works only when both CONTAINS functions are operating on the same table column: If are not operating on the same column, try using FETCH FIRST n ROWS to improve query performance: they

## Parser configuration for Db2 Text Search

You can configure some of the settings that are used for XML search:

All parser configuration parameters are located in the parser\_config.xm] in the XML element defining the parser; com.ibm esnuvo-parser xml XMLParser: Each parameter is specified by a Parameter element of this form: file,

&lt;Parameter Name= parameter"zsetting&lt;/ Parameter&gt;

## ParserName: text

## Parserclass: com. ibm.es.nuvo.parser.text.TextParser

The class that is invoked when the content type is textual:

## required.text.confidence

Not in use\_

The parser that is activated when the text parser fails, the content type is specified as unknown, and content detection identifies the content as Binary:

## fa]1.back.encoding

The encoding that is used when the encoding is specified as unknown or null:

## detection.encoding.buffer.size

The buffer size (in bytes) that is passed to the content detection mechanism to determine the encoding: The default is 2000 bytes

ParserName:

xm]

## titleTagNameList

A comma separated list of tags that are handled as title fields.

## maxTextUnicodeChars

Not in use

Not in use\_

## handleSkippedEntities

Not in use

## Db2 Text Search XML namespaces

Searching on XML namespaces requires a workaround.

You can index XML documents that contain namespace bindings without generating errors, but the namespace information is removed from each tag: As a result, text searches on XML documents with namespace bindings can lead to undesired results.

However; there is a workaround to this limitation for queries that use Db2 XQuery The Db2 Text Search engine is not namespace aware, but you can use the Db2 XQuery support for namespaces to do namespace filtering for the unwanted documents returned from a text search:

Consider the following example in which the default database environment variable is set to SAMPLE and a text search index called desc\_idx is created on the PRODUCT table: prod dbzts ENABLE DATABASE FOR TEXT"

dbzts "CREATE INDEX prod\_desc\_idx FOR TEXT ON product(description)

Now; a new row with the namespace http: , 'posample.org / wheelshovel is added to the PRODUCT table, which already has two XML documents with the namespace http: / / posample.org:

INSERT INTO PRODUCT VALUES ( 100-104-01 Wheeled Snow Shovel 99.99 \_ NULL, NULL, NULL, XMLPARSE ( DOCUMENT &lt;product xm]ns= "http: / /posamp]e.org/whee] shovel pid="100-104-01"&gt; &lt;descriptionz&lt;name Wheeled Snow Shovel&lt;/namez&lt;details&gt; Wheeled Snow Shovel assisted ergonomic foam grips, gravel wheel clears away snow 3 times faster&lt;/details&gt;

The text search index is then updated, as follows: dbzts   "UPDATE INDEX prod\_desc\_idx FOR TEXT"

The following XQuery expression, which specifies the default element as 'posample.org, returns all documents that have the matching XPath 1 'product/ description / details that contains the word ergonomic:

xquery declare default element namespace dbz-fn:xm]column-contains ( ' PRODUCT. DESCRIPTION @xmIxp Iproduct/description/details contains ("ergonomic" ) ]

Three documents are returned, two of which are expected because have the namespace http: \_ 'posample org and one of which is unexpected because it has the namespace http: \_ 'posample org wheelshovel: they

The following XQuery expression uses the path expression / product/ . to use the Db2 XQuery support for XML search and namespaces to filter the documents returned by Db2 Text Search engine so that only documents with the namespace http: / / posample.org are returned:

xquery declare default element namespace http: / /posample.org' db2-fn:xm]column-contains ( ' PRODUCT . DESCRIPTION" @xmIxp Iproduct/description/details [. contains ("ergonomic" )] ) /productl \_

Note: SQL queries can use Db2 XQuery to force namespace filtering: Given the previous example, the corresponding expression an SQL query is as follows: using xquery declare default element namespace "http://posample.org" dbz-fn:sqlquery ( "select description from product where contains(description, @xmIxp: Iproduct/description/details contains ergonomic"")]' ') 1")

## The workaround is as follows:

xquery declare default element namespace "http:/ /posamp]e.org' from product where contains(description, @xmIxp: Iproduct/description/details [ contains (""ergonomic"")]

Similarly, to access specific element in the document (as opposed to just having the matching document returned, as in the previous query), the following query can be used:

xquery declare default element namespace "http: / /posamp]e.org" dbz-fn xm]column-contains ( ' PRODUCT. DESCRIPTION' @xmIxp Iproduct/description/details contains ("ergonomic")] ) Iproduct/description[price 20] /name

Note: This workaround is limited and might not work as expected if, for example, multiple product elements exist within a document:

## Chapter 4. Installing and configuring Db2 Text Search

Db2 Text Search is an optionally installable component whose installation and configuration are integrated with the installation of all Db2 database server products. The stand-alone server deployment is the preferred option for using Db2 Text Search: fully

You can have the Db2 installer automatically install and configure Db2 Text Search: The steps that you must take are platform dependent: Figure 11 describes the installation and configuration process Windows operating systems, and Figure 12 on page 42 describes the process on Linux and UNIX operating systems on

Figure 11. Installation and configuration on Windows platforms

<!-- image -->

On Windows, choose the installation type, decide whether to configure, and choose the configuration method.

Figure 12. Installation and configuration on Linux and UNIX platforms

<!-- image -->

On Linux and UNIX, choose the installation method and type, decide whether to configure, and choose the configuration method. If you run db2setup as a non-root user; have system administrator (who has SYSADM authority) run the DBZRFE command afterwards to reserve the port number that you want in the services file: your

Figure 13. Configuration of a stand-alone Db2 Text Search server

<!-- image -->

For a stand-alone Db2 Text Search server; the integrated text search server configuration. Then the server connection data and run the CONFIGURE procedure: update update

Db2 Text Search has the following restrictions:

- Only stand-alone text servers are supported in a Db2 pureScale environment:
- You need to be on the coordinating member or instance owning partition when creating database partitioned instance the Db2 Wizard: Setup using
- Db2 Text Search is not supported on column-organized tables

## Hardware and software requirements for Db2 Text Search

## Software platforms

Except for little-endian Linux on Power systems which is not a supported platform, Db2 Text Search is supported on all the Db2 server V1L.1 supported platforms listed here: System requirements for IBM DB2 for Linux, UNIX, and Windows

Important: The Tibstdct+.so.5 shared library must be installed on Linux operating systems.

The stand-alone Db2 Text Search server is available for all platforms supported by Db2 Text Search: Cross-platform usage is supported. A these platforms can be configured to use a stand-alone Db2 Text Search server on a supported platform.

## Hardware requirements

The minimum hardware requirements for Db2 Text Search are as follows:

Table 2. Hardware requirements for Db2 Text Search

| Db2 Text Search Server                                                               | Processor            | RAM Memory   | Disk                                                                                                                                                                                                                                          |
|--------------------------------------------------------------------------------------|----------------------|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Integrated setup (In addition to Db2 database server requirements) Stand-alone setup | 2 dual-core 2.66 GHz | 4 GB         | Including temporary working space, each text search index requires about four times the size of all documents that you want to index_ example, a text index on column with million rows of 1 KB text size needs about 4 GB of disk space: For |

Actual disk space, memory, and processor consumption depends on various factors such as the number of collections, the number of documents per collection, the number of concurrently indexed collections, the required indexing throughput, and the query load. For more information, see the Db2 Text Search capacity planning topics.

For recommended operating user process resource limits on Linux and UNIX operating systems, see the topic about operating system user limit requirements. These general resource limit requirements apply to both the integrated and stand-alone setups of the Db2 Text Search server: system

## Installing DB2 Text Search with a default configuration

## Installing and configuring Db2 Text Search with the Dbz Setup Wizard

You can install Db2 Text Search with the Db2 Wizard as part of a custom installation of your Db2 database product: Setup

## About this task

Perform a custom installation of your Db2 database product and select Db2 Text Search from the feature tree: You can have Db2 Text Search automatically configured, Or YOu can manually configure it later: You need to be on the coordinating member or instance owning partition if you are creating a partitioned instance using the Db2 Wizard: Setup

## Procedure

To perform custom installation of Db2 Text Search setup or dbzsetup: using

- "Installing Db2 servers using the Db2 Setup wizard (Windows)' in Installing Db2 Servers
- 1. Install the Db2 server using the instructions for your platform:
- "Installing Db2 servers using the Db2 Setup wizard (Linux and UNIX)" in Installing Db2 Servers

- You can select the Db2 Text Search component from the feature tree\_ During the installation, you have the to configure Db2 Text Search for the default instance. If you do not want to configure Db2 Text Search, skip step 2 option
- 2\_ To configure Db2 Text Search yourself, provide a valid service name and port number if these fields do not already have values. You do not have to configure Db2 Text Search immediately after installing it; you can configure it later: For instructions on how to perform the configuration later; see Chapter 5, "Configuring Db2 Text Search;' on page 57 .

## Installing and configuring Db2 Text Search with a response file

You can install and configure Db2 Text Search as a part of custom silent installation of your Db2 database product: This type of installations uses the setup or dbzsetup command with response file:

## About this task

Perform a custom installation of your Db2 database product to install Db2 Text Search. You must add number of keywords to your response file to have Dbz Text Search installed and configured:

## Procedure

To perform a custom installation:

- 1 Add the following line to the response file that are to install your Db2 database product: using you
- COMP TEXT\_SEARCH
- 2 To configure Db2 Text Search during the installation, add the following lines to the response file:
- For root installations only: dbzinst name TEXT\_SEARCH\_HTTP\_SERVICE\_NAME db2j\_dbzinst\_
- name
- where db2inst\_name is the name of the Db2 instance and db2j\_db2inst\_name is the service name
- For root installations and non-root installations: dbzinst\_name TEXT\_SEARCH\_HTTP\_PORT\_NUMBER port-number If you provide a value for the TEXT SEARCH\_HTTP\_SERVICE NAME keyword for a

You can specify any valid service name and port number that are not in use. If you do not provide any values, default values are used for configuration if the response file keyword db2inst\_name.CONFIGURE\_TEXT SEARCH is set to YES.

- "Installing Db2 product using a response file (Windows)" in Installing Db2 Servers
- 3\_ Install the Db2 database product the instructions for your platform: using
- "Installing a Db2 product using response file (Linux and UNIX) in Installing Db2 Servers

## What to do next

You do not have to configure Db2 Text Search immediately after installing it; you can configure it later: For instructions o how to perform the configuration later, see Chapter 5, "Configuring Db2 Text Search;' on page 57.

## Installing Dbz Text Search using db2\_install (Linux and UNIX)

When you issue the db2\_instal] command, you also install Db2 Text Search.

## About this task

Important: The command db2\_instal1 is deprecated and might be removed in a future release. Use the dbzsetup command with a response file instead.

To install Db2 Text Search, follow the steps outlined in "Install a Db2 product db2 install' in Installing Db2 Servers Db2 Text Search will automatically be installed as a part of the installation of your Db2 database product using

If this is a non-root installation, a Db2 instance is created and Db2 Text Search will be installed. If this a installation, you must create Db2 instance and configure Db2 Text Search using one of the available methods. root

You do not have to configure Db2 Text Search immediately after you install it: For instructions on how to perform the configuration, see Chapter 5, "Configuring Db2 Text Search; on page 57.

## Installing DB2 Text Search without initial configuration

## Installing Db2 database servers using the Dbz2 Setup wizard (Windows)

This task describes how to start the Db2 wizard on Windows. Use the Db2 wizard to define your installation and install your Db2 database product on your Setup Setup system.

## Before you begin

Before you start the Db2 wizard: Setup

- Ensure that your system meets installation, memory, and disk requirements.
- If you are planning on setting up a partitioned database environment, refer to up partitioned database environment". "Setting
- If you are planning to use LDAP to register the Db2 server in Windows operating Active Directory, extend the directory schema before you install. Otherwise, you must manually register the node and the databases. For more information, see 'Extending the Active Directory Schema for LDAP directory services (Windows). systems catalog
- You must have a local Administrator user account with the recommended user rights to perform the installation: In Db2 database servers where LocalSystem can be used as the DAS and Db2 instance user and you are not the database partitioning feature, a non-administrator user with elevated privileges can perform the installation: using
- Although not mandatory; it is recommended that you close all programs so that the installation program can any files on the computer without requiring reboot update
- Installing Db2 products from a virtual drive or an unmapped network drive (such as Vhostname | sharename in Windows Explorer) is not supported. Before you attempt to install Db2 products, you must map the network drive to a Windows drive letter (for example, Z:).

## Restrictions

- You cannot have more than one instance of the Db2 Setup wizard that is running in any user account
- The Db2 copy name and the instance name cannot start with a numeric value.The Db2 copy name is limited to 64 English characters that consists of the characters A-Z, a-z and 0-9.
- The Db2 copy name and the instance name must be unique among all Db2 copies.
- The use of XML features is restricted to a database that has only one database partition.
- If you installed one of the following products, then no other Db2 database product can be installed in the same path:
- IBM Data Server Runtime Client
- IBM Data Server Driver Package
- Db2 Information Center
- The Db2 Setup wizard fields do not accept non-English characters.
- If you enable extended security on Windows or higher; the users must to the DBZADMNS or DBZUSERS group to run local Db2 commands and applications. This setup is required because of an extra security feature (User Access Control) that limits the privileges that local administrators have by default: If users do not to one of these groups, will not have read access to local Db2 configuration or application data. belong belong they

## Procedure

To start the Db2 wizard: Setup

- 1\_ on to the system with the local Administrator account that you defined for the Db2 installation: Log
- 2 If you have the Db2 database product DVD, insert it into the drive. If enabled, the auto-run feature automatically starts the Db2 Setup Launchpad: If the autorun does not work, use Windows Explorer to browse the Db2 database product DVD and double-click the setup icon to start the Db2 Launchpad. Setup
- 3\_ If you downloaded the Db2 database product from Passport Advantage" run the executable file to extract the Db2 database product installation files Use setup icon to start the Db2 Launchpad. On Windows 2008 and Windows Vista or later versions of Windows operating system, you must right-click on setup.exe and select Run as administrator or start setup.exe from command prompt from "Command Window: Administrator' Setup

Attention: You must never start the installation package(" msi' present in the Db2 installation media directly: Installation must always be started by setup.exe with full administrative privileges. file)

- 4\_ From the Db2 launchpad, you can view installation prerequisites and the release notes, or you can proceed directly to the installation. You might want to review the instaliation prerequisites and release notes for late-breaking information. On Windows 2008 and Windows Vista or later versions of Windows operating system, you must right-click on setup.exe and select Run as administrator Or start setup.exe from command prompt from "Command Window: Administrator' Setup

- 5\_ Click Install a Product and the Install a Product window displays the products available for installation:
- If you did not install any Db2 database products on your computer; launch the installation by clicking Install New. Proceed through the installation by following the Db2 wizard prompts. Setup

If you installed at least one Db2 database product on your computer; you can:

- Click Install New to create a new Db2 copy:
- 6\_ The Db2 wizard determines the system language, and launch the program for that language. Online help is available to guide you through the remaining steps. To invoke the online help, click Help or press F1  You can click Cancel at any time to end the installation: Setup setup
- Click Work with Existing to an existing Db2 copy, add function to an existing cOPY, upgrade an existing Version 9.7, Version 9.8, or Version 10.1 copy, or to install an add-on product: update
- a\_ When you're at the Select the installation type when you click View Features\_\_ some features are unchecked: step,
- 1) The Connect support feature option does not affect your system's ability If you select this option, two extra trace utilities are installed: These utilities are ddcstrcn and ddcspkgn. The DDCSTRCN utility implements detailed DRDA traces and usually IBM support might request that you use this utility when need more diagnostic data to resolve a problem. For more information about the ddcspkgn tool, see Binding applications and utilities (Db2 Connect server). they
- 7 . Sample panels when you are using the Db2 setup wizard lead you to the installation process. See the related links.

## Results

Your Db2 database product is installed, by default, in the Program\_Files IBM' sq]ib directory where Program\_Files represents the location of the Program Files directory

If you are installing on a system where this directory is already used, the Db2 database product installation has \_xx added to it: The xx are digits, starting at 01 and increasing, depending on how Db2 copies you installed. being path many

You can also specify your own Db2 database product installation path:

## What to do next

- Verify your installation.
- Perform the necessary post-installation tasks.

For information about errors that are encountered installation, review the installation file that is located in the My Documents | DBZLOG| directory: The file uses the following format: DB2-ProductAbrrev-DateTime for example, DB2-ESE-Tue Apr 04 17\_04\_45 2012. during log log

If this is new Db2 product installation on Windows 64-bit, and you use a 32-bit OLE DB provider; you must manually register the IBMDADB2 DLL. To register this DLL, run the following command:

c:lwindows |SysWOW64 |regsvr32 Is C: |Program\_Files| IBM| SQLLIBIbin| ibmdadbz.d]1

where Program\_Files represents the location of the Program FiTes directory

If you want your Db2 database product to have access to Db2 documentation either on your local computer or on another computer on your network, then you must install the Db2 Information Center. The Information Center contains documentation for the database system and related products By default, Db2 information is accessed from the web if the Information Center is not locally installed:

IBM Data Studio can be installed by running the Db2 Setup wizard

## Db2 Workgroup Server Edition memory limits

If you are installing Db2 Workgroup Server Edition, the maximum allowed memory for the instance is 64 GB

The amount of memory that is allocated to the instance is determined by the INSTANCE\_MEMORY database manager configuration parameter

## Important notes when you upgrade from V9.7, V9.8, or V1o.l:

- The self memory manager does not increase your overall instance memory limit beyond the license limits. tuning

## Installing Db2 servers using the Db2 Setup wizard (Linux and UNIX)

This task describes how to start the Db2 wizard on Linux and UNIX operating systems. The Db2 Setup wizard is used to define your installation preferences and to install your Db2 database product on your system. Setup

## Before you begin

Before you start the Db2 Setup wizard:

- Ensure that your meets installation, memory, and disk requirements system
- If you are planning on up a partitioned database environment, refer to up a partitioned database environment" in Installing Db2 Servers. setting "Setting
- Ensure that you installed a supported browser:
- The Db2 database product image must be available  You can obtain a Dbz installation image either by purchasing physical Db2 database product DVD, or by downloading an installation image from Passport Advantage:
- You can install a Db2 database server by either root or non-root authority: For more information about non-root installation, see "Non-root installation overview (Linux and UNIX)" in Installing Db2 Servers. using
- If you are installing non-English version of a Db2 database product, you must have the appropriate National Language Packages
- The Db2 Setup wizard is graphical installer: To install a Db2 product by the Db2 wizard, you require an X Window System (X1L) to display the graphical user interface (GUI). To display the GUI on local workstation, the X Window System software must be installed and running: You must also set the DISPLAY variable to the IP address of the workstation you use to install the Db2 product: using Setup your

export DISPLAY-&lt;ip-addressz:0.0

For example, export DISPLAY-192.168.1.2:0.0

For more information, see this developerWorks article:

- If you are using the security software in your environment, you must manually create Db2 users before you start the Db2 wizard. required Setup

## Restrictions

- You cannot have more than one instance of the Db2 wizard running in any user account: Setup
- The use of XML features is restricted to a database that is defined with the code set UTF-8 and has only one database partition:
- The Db2 wizard fields do not accept non-English characters. Setup

## Procedure

To start the Db2 Setup wizard:

- 1. If you have a physical Db2 database product DVD, change to the directory where the Db2 database product DVD is mounted by entering the following command:

cd /dvdrom where /dvdrom represents the mount of the Db2 database product DVD. point

- a\_ Extract the product file:
- 2 If you downloaded the Db2 database product image, you must extract and untar the product file:

gzip ~d product.tar.gz where product is the name of the product that you downloaded.

- b Untar the product file:

On Linux operating systems

tar ~Xvf product.tar

On AIX operating systems

gnutar ~Xvf product.tar

where product is the name of the product that you downloaded:

- C\_ Change directory:

cd Iproduct where product is the name of the product that you downloaded.

Note: If you downloaded National Language Package, untar it into the same directory: This creates the subdirectories (for example InIpack) in the same directory, and allows the installer to automatically find the installation images without prompting: step

- 4 The Db2 wizard opens. Launch the installation by clicking New Install: Proceed through the installation by following the Db2 Setup wizard's prompts. Setup
- 3\_ Enter the Idb2setup command from the directory where the database product image resides to start the Db2 Setup wizard.

## Results

For non-root installations, Db2 database products are always installed in the SHOME/sq]ib directory, where SHOME represents the non-root user's home directory

For root installations, Db2 database products are installed, by default; in one of the following directories:

AIX

lopt/IBM/dbz/V1l.1

Linux

If you are installing on a system where this directory is already used, the Db2 database product installation has \_xx added to it: The are digits, starting at 01 and increasing, depending on how many Db2 copies you have installed: being path

You can also specify your own Db2 database product installation path:

Db2 installation paths have the following rules:

- Can include lowercase letters (a-z) , uppercase letters (A-Z), and the underscore character ( \_ )
- Cannot exceed 128 characters
- Cannot contain spaces
- Cannot contain characters that are other than English characters
- The name cannot be a subdirectory of an existing Db2 installation. path
- The installation paths cannot be symbolic links:

The installation files are: log

- The Db2 setup file. This file captures all Db2 installation information, including errors\_ log
- For root installations, the Db2 setup file name is db2setup. log
- For non-root installations, the Db2 setup file name is dbzsetup\_username \_ where username is the non-root user ID under which the installation was performed. log 1og,
- The Db2 error file. This file captures any error output that is returned by Java (for example, exceptions and trap information): log
- For root installations, the Db2 error file name is db2setup.err. log
- For non-root installations, the Db2 error log file name is dbzsetup\_username err, where username is the non-root user ID under which the installation was performed.

By default, these files are located in the tmp directory You can specify the location of the log files. log

There is no longer a db2setup.his file: Instead, the Db2 installer saves copy of the Db2 setup dbzinstal].history.XXXX, where xxxx is 0000-9999, depending on the number of installations you have on that machine log

Each installation copy has a separate list of history files. If an installation copy is removed, the history files under this install path are removed as well  This copying action is done near the end of the installation and if the program is stopped or aborted before completion, then the history file will not be created:

## What to do next

- Verify your installation.
- Perform the necessary post-installation tasks.

National Language Packs can also be installed by running the Idbzsetup command from the directory, where the National Language Pack resides, after you install the Db2 database product:

On Linux x86, if you want your Db2 database product to have access to Db2 documentation either on your local computer or on another computer on your network then you must install the Db2 Information Center. The Db2 Information Center contains documentation for the Db2 database system and Db2 related products.

## Db2 Workgroup Server Edition memory limits

If you are installing Db2 Workgroup Server Edition, the maximum allowed memory for the instance is 64 GB.

The amount of memory that is allocated to the instance is determined by the INSTANCE\_MEMORY database manager configuration parameter:

## Important notes when you upgrade from V9.7, V1O.1, or V1O.5:

- When you upgrade from V9.7, V1O.1, or V1O.5 Db2 database product if the memory configuration exceeds the allowed limit, the database product might not start after you upgrade to the current version:
- The self memory manager will not increase your overall instance memory limit beyond the license limits. tuning

## Response file installation of Db2 overview (Windows)

On Windows, you can perform a response file installation of a Db2 product on single machine or on multiple machines: A response file installation might also be referred to as silent installation or an unattended installation.

## Before you begin

Before you begin the installation, ensure that:

- You have all of the required user accounts to perform the installation.
- Your meets all of the memory, hardware, and software requirements to install your Db2 product: system
- Ensure all Db2 processes are stopped:

## Procedure

- To perform response file installation of a Db2 product on single machine:
- Modifying sample response file. Sample response files are located in (db2 | Windows | samples).
- 1. Create and customize a response file by one of the following methods:
- Using the Db2 wizard to generate a response file: Setup
- Using the response file generator:
- 2. Run the setup -u command specifying your customized response file: For example, response file created during an installation:
- setup
- To perform response file installation of a Db2 product on multiple machines:

- Set up shared access to directory:
- 2. Create a response file using the sample response file:
- 3. Install a Db2 product response file: using

## Response file installation of Db2 overview (Linux and UNIX)

This task describes how to perform response file installations on Linux or UNIX: You can use the response file to install additional components or products after an initial installation: A response file installation might also be referred to as a silent installation or an unattended installation.

## Before you begin

Before you begin the installation, ensure that:

- All Db2 processes are stopped. If you are installing Db2 database product of an existing Db2 installation on the computer; you must all Db2 applications, the Db2 database manager, and Db2 processes for ali Db2 instances and Db2 DAS related to the existing Db2 installation. on top stop
- Your system meets all of the memory, hardware, and software requirements to install your Db2 database product:

## Restrictions

Be aware of the following limitations when the response files method to install Db2 on Linux or UNIX operating systems: using

- Ensure that you have sufficient disk space before installing: Otherwise, if the installation fails, manual cleanup is required:
- If you set any instance or global profile registry keywords to BLANK (the word "BLANK") that keyword is, in effect, deleted from the list of currently set keywords.
- If you are performing multiple installations or are installing Db2 database products from multiple DVDs, it is recommended that you install from a network file system rather than a DVD drive Installing from network file system significantly decreases the amount of time it takes to perform the installation:
- If you are planning on installing multiple clients, set up mounted file on code server to improve performance: system

## Procedure

To perform a response file installation:

- 1 Mount your Db2 database product DVD or access the file system where the installation image is stored.
- 2 Create response file by using the sample response file: Response files have a file type of rsp: For example, ese rsp:
- 3\_ Install Db2 the response file: using

## Installing and configuring a stand-alone Text search server

## Installation space requirements for the stand-alone server

The stand-alone text search server installation requires at least 1 GB of disk space:

small amount of disk space is needed in addition for configuration data for each collection, however; significant space is needed for the index data. For details, see the topic about disk consumption for Db2 Text Search:

The location of index data files can be configured using the default data directory or specified as collection directory parameter when creating a text search index

## Installing a stand-alone Db2 Text Search server

You can install stand-alone Db2 Text Search server silently The silent installation takes input values from response file: You can install one or more servers for a stand-alone The stand-alone text search server is also known as FCM Text Search server: option setup.

## Procedure

To install a stand-alone text search server:

- 1. Create an empty installation directory:
- example, on Linux or UNIX systems, create the following directory: lopt/ibm/ ECMTextSearch For
- For example, on Windows systems, create the following directory: C:|Program Files| IBMI ECMTextSearch

This directory is known as &lt;ECMTS\_HOME&gt;.

- 3. in as user with the required authorities Or permissions Log
- 2 Download the Db2 Accessories Suite for your platform from the IBM DB2 Accessories Suite for Linux, UNIX, and Windows website: Extract it to temporary directory
- On Linux and UNIX systems, you need read, write, and execute permission for the installation directory:
- On Windows systems, you need administrator authority
- 4\_ Review the license and edit the ecmts\_response.txt file to customize settings. your
- Search server: Start the installation by issuing the following command: &lt;ecmts\_setup\_file\_name&gt; silent -f ecmts response.txt
- 5. Use the setup file ecmts21\_install\_&lt;platform&gt;.exe to install the stand-alone Text
- For example, on Windows systems, issue the following command: ecmts21 instal] win32.exe silent -f ecmts response.txt
- 6\_
- Verify that the installation was successful: Check the installation file and the folders that were created in the &lt;ECMTS\_ HOME&gt; directory: You should see at least bin, Tib, config and resource folders. log
- 7. Start the server by running the startup script from the &lt;ECMTS\_HOME&gt; directory:
- On Linux and UNIX platforms: bin/startup.sh
- On Windows platforms: binlstartup
- Configure and customize the Text Search server properties. For details, see the topic about configuring a stand-alone Db2 Text Search server:

## Installing and configuring stand-alone server as a Windows service

You can install and configure stand-alone text search server processes as Microsoft Windows service

## About this task

The stand-alone server service runs under the local system account and the startup type is set to automatic You can specify a name for the service and specify whether the service starts automatically after installation.

## Procedure

To install and run stand-alone server as a Windows service:

- 1 Open the ecmts\_response.txt response file and set the following parameters:
- IA INSTALL\_AS\_WINDOWS\_SERVICE Set the value of this parameter to YES.
- IA\_ WINDOWS\_SERVICE\_NAME This is an optional parameter:
- When the value of this parameter is not specified or set to AUTO, a default name ECM Text Search Server is assigned to the Windows service. If the service already exists and its name was not specified, a numeric suffix is added to the name, for example ECM Text Search Serverl. If you specify a name for the service and a service with the same name already exists, an error is returned
- IA START\_SERVER
- 2 Install the stand-alone text search server: From the directory that contains the setup and response files, run the appropriate file for your operating system: setup
- To automatically start the Db2 Text Search Windows service after installation, ensure that the IA\_START\_SERVER parameter is set to YES. This is an parameter: The default setting is YES. optional
- 3\_ You can start and stop the Text Search Windows service by the Microsoft Services window. To access the Services window, open the Windows Control Services\_ using

## Uninstalling a stand-alone Db2 Text Search server

You can uninstall a stand-alone Db2 Text Search by using the UninstalI\_ECMTextSearch command.

## Before you begin

any Db2 Text Search services and shutdown the stand-alone Db2 Text Search server before starting the uninstallation process. Stop

## Procedure

- 1. Navigate to the ECMTS\_HOME directory:
- 2. Start the uninstallation by issuing one of the following platform-specific commands:

- On Linux and UNIX operating systems: INSTALL\_DIR/UninstalI\_ECMTextSearch/Uninstal]
- ECMTextSearch silent
- On Windows operating systems: ECMTS\_HOME| Uninstal]ECMTextSearch|UninstallECMTextSearch. exe silent

The uninstall program does not remove all data from the ECMTS\_HOME directory: For example, the uninstal1.log file remains after running the uninstall program. Some or all of the following directories might not be removed by the uninstall program and must be removed manually:

- ECMTS\_HOMEI config
- ECMTS\_HOME| ]icense
- ECMTS\_HOME' resource
- ECMTS\_HOME| temp
- ECMTSHOME|Uninstall ECMTextSearch

Tip: You might want to back up collection or configuration data that is stored in the ECMTS\_HOMEIconfig directory for future use.

## Results

The Db2 Text Search server is uninstalled and cannot be used anymore for text search index administration or full-text query execution: However; the text index collection and configuration data remains intact:

## Chapter 5. Configuring Dbz Text Search

Your options for configuring Db2 Text Search depend on whether you are performing the initial configuration or a reconfiguration and which platform you are using:

## Before you begin

Before reconfiguration of the Db2 Text Search, the text search instance service, as outlined in "Stopping the Db2 Text Search instance service" on page 77 . stop

For partitioned instances you need to be on the coordinating member Or instance owning partition when the configuration tool. This is the instance host where the integrated text search server is initially configured and is the lowest numbered partition server host: using

## Procedure

- Determine whether Db2 Text Search is configured: Run the configuration tool by issuing the following command:
- In the output of the printAII option, the authentication token is an empty string
- if Db2 Text Search is not configured.
- Configure Db2 Text Search for the first time:
- Rerun the silent installation as described in "Installing and configuring Db2 Text Search with a response file" on page 45.
- On Linux and UNIX operating systems, use one of the following methods to configure Db2 Text Search:
- Rerun the GUI installation as described in "Installing and configuring Db2 Text Search with the Db2 Setup Wizard" on page 44.
- Use the configuration tool. Refer to "Initial configuration of an integrated Db2 Text Search server on page 59. Note that the configuration tool to perform a manual configuration requires you to manually configure most of the parameters, whereas using the installer requires you to configure only two parameters. using
- Use one of the following commands to configure Db2 Text Search, depending on the instance type and operation:
- For root installs, you can issue dbzisetup command in the GUI to configure existing Db2 instance by selecting Db2 Text Search when it is configured. You also can issue the dbziupdt command with -j to configure integrated Db2 Text Search server: Note that when you create an instance the dbzicrt command with -j option, Db2 Text Search is also configured by default: being option using
- For non-root installs, issue the dbzisetup command to configure the instance in the GUI, or issue the dbznrupdt or dbznrupgrade command with the -j option.

On Windows operating systems, use one of the following methods to configure Db2 Text Search:

- Rerun the silent installation as described in "Installing and configuring Db2 Text Search with a response file" on page 45.

- Rerun the GUI installation as described in "Installing and configuring Db2 Text Search with the Db2 Setup Wizard" on page 44.
- Issue the dbziupdt command with the -j Note that when you create an instance using dbzicrt command with the -j option, Db2 Text Search is also configured by default: option.

The Db2 Text Search internally uses Java developer kit whose location is pointed by JDK\_PATH of db2 dbm cfg command and this Java developer kit has to come from IBM: To verify if the Java developer kit is from IBM, run the following command: get

- Determine whether the Java developer kit is from IBM:

JDK\_PATH/jre/bin/java ~version

This command will display the Java version information and IBM should display as of string if the Java developer kit is from IBM. part

- Re-configure Db2 Text Search:

After you have configured Db2 Text Search, you cannot use the GUI installer to re-configure it You must make any updates to the configuration manually

- Rerun the silent installation as described in "Installing and configuring Db2 Text Search with a response file" on page 45.

On Linux and UNIX operating systems, use one of the following methods to re-configure Db2 Text Search:

- Use the Configuration Tool. Refer to "Initial configuration of an integrated Db2 Text Search server" on page 59.
- For root installs, you can issue dbzisetup command in the GUI to configure an existing instance by selecting the Db2 Text Search instance being configured. You also can issue the dbziupdt command with -j option to configure integrated Db2 Text Search server:
- Use one of the following commands to re-configure Db2 Text Search, depending the instance type and operation: on
- For non-root installs, issue the dbzisetup command to configure the instance in the GUI, Or issue the dbznrupdt or dbznrupgrade command with the -j option.

On Windows operating systems, use one of the following methods to re-configure Db2 Text Search:

- Rerun the silent installation as described in "Installing and configuring Db2 Text Search with a response file" on page 45.
- Use the Configuration Tool. Refer to "Initial configuration of an integrated Db2 Text Search server" on page 59.
- Run the dbziupdt, Or dbziupgrade command, specifying the -j option as shown to meet your needs:
- ~j "TEXT\_SEARCH" attempts to configure Db2 Text Search with the default service name and generated port value:
- ~j "TEXT\_SEARCH, [servicename] reserves the service name with an automatically generated port number or with the same port number assigned to that service name if the service name is already reserved in the services file:
- "TEXT\_SEARCH, [port number] reserves the port with the default service name\_
- ~j "TEXT\_SEARCH, [servicename] [port#] reserves the specified service name and port number

Note: On Windows operating systems, the PATH in the Db2 command window configure an instance that is not in the current Db2 copy first switch to the appropriate Db2 command window for that copy points

## Initial configuration of an integrated Db2 Text Search server

The Configuration Tool is a command-line tool that you can use to perform the change the current configuration:

## Before you begin

To customize most of the configuration settings, must stop the Db2 Text Search instance services you

## About this task

The most convenient method for the initial configuration after installation is to use the Db2 installer: For a manual initial configuration as well as any configuration updates, you must use the configuration tool.

## Procedure

To perform the initial configuration of the Db2 Text Search server use the following steps. See the topic about the Configuration Tool for further details.

- 1 Run the configToo] command with the configureParams to set the configuration option path:
- Review the following configuration options and change the defaults as needed:
- ~-defaultDataDirectory: location of the text index collections, each collection will be stored in its own subdirectory:
- ~logPath: location of Text Search server and trace files: log

~installPath: to Db2 Text Search install directory which is DBZPATHIdbztss on Windows and the DBZDIR/db2tss directory on Linux and UNIX, where DBZDIR is the location of the Db2 copy: path

- ~tempDirPath: to the temporary directory path

~startupHeapSize: maximum size of the text search server heap

- configToo] configureParams -configPath &lt;absolute-path-to-config-folderz ~defaultDataDirectory dataPath ~installPath ipath

For example, to configure the defaultDataDirectory and installPath options, issue the following command:

- On Windows operating systems, specify the command as shown. You need to specify only configPath; all of the other parameters are assigned default and values. configToo] ~configPath absolute-path-to-config-folder paths
- 2 Db2 Text Search authenticates text search index administration and text search requests by using an authentication token. Generate the authentication token by issuing the configTool command with the generateToken parameter; as follows:

configToo] generateToken ~configPath absolute-path-to-config-folder -seed value

- 3\_ Specify the HTTP port by issuing the configTool command with theconfigureHTTPListener parameter; as follows:

configToo] configureHTTPListener configPath absolute-path-to-config-folder ~adminHTTPPort port-number

Note: The value of the port should be between 1024 and 65535.

The administrative HTTP port allows communication between text search processes TCP IP the installation of a Db2 database product or instance creation, you can specify a service name and port if you have root authority These are for updating the services file During using during used

- 4 Update the services file:

Refer to "Updating the services file on the server for TCP /TP communications on page 63.

When you use the Configuration Tool for configuration, the tool does not update the services file: Therefore, you must the services file manually, update

Note: Only root users can the services file Non-root users must have the system administrator run the dbzrfe command first; update

## Updating Dbz Text Search server information

Db2 Text Search server information is used in the database to connect to the Text Search server to administer and search in text search indexes. Valid are therefore required to ensure proper functioning of the system and must be defined in the text search SYSIBMTS TSSERVERS administrative view: settings catalog

## Before you begin

Updating text search server information requires the SYSTS\_ADM role and DBADM privileges on the specified database:

## About this task

The server information consists mainly of connection information, like the server host name, the server token value and the server port number; and server characteristics, like server locale, whether the text search setup is enabled for rich text support, and an indication whether the search server utilized by the Db2 instance is integrated (configured by Db2 as part of the Db2 instance) or separate stand-alone installation of the text search server:

The is required initially for the following scenarios: update

- an incomplete enablement warning message is encountered when enabling the database for text search:
- initial configuration of a stand-alone text search server
- partitioned databases
- Db2 Text Search upgrades
- and further on, following any to text search server connection information. updates
- stored procedures are for administration from a client machine used

During database enablement the SYSIBMTS.TSSERVERS administrative view is updated with initial connection information for the integrated server; if the necessary authorization to access the configuration is available Review and update

the text server information in SYSIBMTS.TSSERVERS with the relevant text search server data and run the SYSTS\_CONFIGURE procedure to apply the updated information. For multiple databases in the instance, configure each database with the information for the same text search server

When re-configuration is needed, ensure that no text search administrative operation is active and shut down the text search server before applying any changes.

Certain aspects relating to the text search installation and Db2 instance configuration text search have to be updated. include: for They

- An indication whether the search server utilized by the Db2 instance is integrated (configured by Db2 as part of the Db2 instance), or if it is a separate stand-alone installation of the text search server
- An indication if the text search setup is enabled for rich text support:

## Procedure

To updating Db2 Text Search server information:

- 1\_ Get the needed text search server property values, such as host name, token, and port number; by issuing the configTool command with the printA1I For more details, see the topic about configTool. option.
- 2 Review the entries in the SYSIBMTS TSSERVERS administrative view and make any necessary update:
- If the view is empty then use an INSERT statement\_ For example: INSERT IntO SYSIBMTS. TSSERVERS (HOST, PORT, TOKEN, key , SERVERTYPE, SERVERSTATUS) values 55000 , XbSZgos= XbSer2gkdfshuyos== 0) ;
- If the view already contains a row then use UPDATE statement\_ For example:
- (HOST \_ PORT\_ TOKEN)
- ('tsmachl. ibm. com 55002 \_ k3j4fjkgu-' ) ;

Make sure to use the actual hostname or IP address instead of localhost if multiple database partitions are used, or administrative operations are executed from client: This not only to local installs of a stand-alone text search server; but also to integrated servers. applies

- 3\_ Execute the SYSTS\_CONFIGURE procedure: For more details, see the topic about the SYSTS\_CONFIGURE procedure:
- 4\_ Verify the values in the SYSIBMTS.TSSERVERS administrative view are those returned by configuration tool.
- 5. Start the text search service to verify that the text search server can be contacted:

## Configuring a stand-alone Db2 Text Search server

Use the configuration tool to customize some default properties after installing the stand-alone Db2 Text Search server You can configure the relevant system level properties and the security properties for your system.

Before configuring the properties, ensure that the stand-alone Db2 Text Search server is shut down and that the text search services are stopped. Do not restart the text search server until you finish both the configuration of the stand-alone text search server and complete required configuration updates of the enabled databases in the associated Db2 instance\_

You can use the configuration tool to view text search server properties even when the text search server is stopped:

## System configuration

Make sure to review and configure at minimum the following properties with the configuration tool:

- configureHTTPListener: Configures the Db2 Text Search server port and host name
- generateToken: Generates the authentication token and encryption key
- defaultDataDirectory: Configures the parameters for the collection

Remember: If the value for configPath contains blanks, must enclose the value in quotation marks: you

For details, and additional optional configuration see the topic about the configuration tool for Db2 Text Search:

## Security configuration

Every API request from Db2 database server to stand-alone Db2 Text Search server is authenticated by an authentication token. An initial token is generated during the installation of the stand-alone text search server

- 1\_ Use the configuration tool to explicitly provide a seed value and generate the authentication token: The maximum length of the token string is 32 bytes.
- 3. Store the connection information including the token in the SYSIBMTS.TSSERVER administrative view for each enabled database:
- 2. Run the configuration tool on the Db2 instance to set the matching token value:

You can use the Db2 Text Search configuration tool to show the current authentication token and encryption values. However; it is impossible to determine the seed value used by the stand-alone Db2 Text Search server: Generate the token explicitly with the configTool utility and the master configuration on the Db2 instance to match the configured values for the token. key update

To configure the properties for the text search server run the configuration tool by entering the appropriate platform-specific command:

- On Linux and UNIX platforms: configTool .sh configuration\_ command -configPath value [-Iocale value] ~command\_specific\_arguments
- On Windows platforms: configTool .bat configuration\_command -configPath value

~command\_specific\_arguments

For example, to the current authentication token on a Linux server; use the following command: print configTool .sh printToken -configPath /opt/ibm/ ECMTextSearch/config

Note: For a stand-alone Db2 Text Search server on Linux and UNIX platforms, the the integrated Text Search server supports the script names without the suffix:

## Updating the services file on the server for TCPIIP communications

This task is part of the main task of Configuring TCP/IP communications for a Db2 instance.

## About this task

The TCP /IP services file specifies the ports that server applications can listen on for client requests. If you specified a service name in the svcename field of the DBM configuration file, the services file must be updated with the service name to port number /protocol mapping: If you specified port number in the svcename field of the DBM configuration the services file does not need to be updated. file,

Update the services file and specify the ports that you want the server to listen on for incoming client requests. The default location of the services file depends on the operating system:

Linux and UNIX operating systems

Windows operating systems

## Procedure

Using a text editor; add the Connection to the services file: example: For entry dbzc\_dbzinstl 3700/tcp # Dbz connection service port

where:

represents the connection service name

3700 represents the connection port number

tcp represents the communication protocol that you are using

## Installing Db2 Accessories Suite for Db2 Text Search

Db2 Accessories Suite enables indexing and search for documents with rich text and proprietary formats with Db2 Text Search: You can start a new install or run the install on of an existing installation. top

## Before you begin

To install Db2 Accessories Suite on Linux and UNIX, you need to logged on to the Db2 server as system administrator: On Windows, you must logon as a user with Local Administrator authority

Download Db2 Accessories Suite. For the download link, see: https: , WWWibm.com \_ services / forms / preLogin dozsource-swg-dm-dbzaccsuite. Install the most up-to-date version of the Db2 Accessories Suite release or fix to ensure proper functioning of the feature: pack

Ensure the installer file, the license file, and the release info file are in the same directory

On Windows, install Visual C++ Redistributable for Visual Studio 2012 available at download / details aspx?id-30679 , or the text extractor in the accessories suite will fail to run due to lack of the proper version of VC++ runtime support: please

## Procedure

To install Db2 Accessories Suite:

- 1. the Db2 Text Search instance service: To stop the service, issue the dbzts STOP FOR TEXT command. Stop
- 2. on to the Db2 database server as a user with the necessary permissions which have privilege in Db2 Text Search installation directory, for example, on Linux platform, the directory locates under &lt;DBZPATH&gt;/dbztss directory, where &lt;DBZPATH&gt; represents the Db2 database server installation directory Log writing
- 3 There are two installation modes. One option is console installation, while the other is silent installation.
- To complete a console install:
- a Run the accessories suite filter installer:
- Linux and UNIX platforms
- There are approaches on the Windows platform. two
- Run the installer insta]  AccSuiteV1O.exe from the command window
- Double click the installer binary file:
- C The db2tss directory must already exist: If it is missing, Db2 Text Search has not been properly installed and configured.
- b After accepting the license, enter the location of the db2tss subdirectory in the latest Db2 copy when prompted for the install
- d. Review the summary and confirm the installation.
- To complete a silent install:
- a. Modify the response file by setting the LICENSE ACCEPTED parameter as true and assigning the correct install full USER\_INSTALL\_DIR which should contain the dbztss directory path
- b\_ Run the accessories suite filter installer with silent model.
- Run the instal AccSuiteV1O.bin silent -f instal properties command from the command line Linux and UNIX platforms. Ter . on
- Run the installAccSuiteV1O.exe silent ~f installer.properties command from the command window on the Windows platform:

## Results

You have successfully installed Db2 Accessories Suite:

## What to do next

You can now enable rich text document support for Db2 Text Search: See, "Enabling Db2 Text Search for rich text document support" on page 76 for more details.

## Uninstalling the Db2 Accessories Suite for Db2 Text Search

You can uninstall a stand-alone Db2 Text Search by the Uninstall DBZAS command: using

## Before you begin

In order to uninstall Db2 Accessories Suite on Linux and UNIX platforms, you must be logged on to the Db2 database server as a system administrator: On Windows platforms must be logged on as a user with Local Administrator authority: you

## Procedure

To uninstall Db2 Accessories Suite:

- 1 the Db2 Text Search instance service: To the service, run db2ts "STOP FOR TEXT" Stop stop
- 2. on to the Db2 database server with as a user who has the necessary privileges for the operating system. Log
- 3\_ Disable rich text document support for all text search instances which were enabled with rich text feature before. For details, see the topic about disabling Db2 Text Search for rich text document support:
- 4 Uninstall Db2 Accessories Suite installer: To uninstall the installer:
- On Linux and UNIX operating systems:
- DBZASV1O/Uninstall DBZAS.bin

where &lt;DBZDIR&gt; is the location of the latest Db2 copy:

- On the Windows operating system: DBZAS . exe

where &lt;DBZPATH&gt; is the location where you installed the latest Db2 copy

## Results

You have uninstalled the Db2 Accessories Suite.

## Chapter 6. Upgrading DB2 Text Search

## Upgrading Dbz Text Search for administrator or root installation

To obtain the latest functionality upgrade Db2 Text Search instance. You must upgrade the Db2 server; instance, and all databases when you are upgrading the text search instance. your

## Before you begin

Before you to upgrade Db2 Text Search as administrator or root, complete the following steps: being

- 2. the Db2 database instance and the Db2 Text Search instance service. Stop
- 1\_ in as the instance owner or user with SYSADM authority Log
- 3\_ Back up the Db2 Text Search configuration directory:
- For Linux and UNIX operating systems, it is located under: SINSTHOME/sq]lib/dbztss/config
- where INSTHOME represents the instance home path:
- For Windows systems, it is located under: &lt;INSTPROF&gt;

where &lt;INSTPROF&gt; represents the instance profile directory and &lt;INSTNAME&gt; indicates the name of the instance to be upgraded.

- 4 If you enabled Db2 Text Search for rich text document support, disable rich text document support: more information about how to disable rich text document support, see the topic about disabling Db2 Text Search for rich text document support: For

## About this task

The following steps describe the process to upgrade Db2 Text Search Version 9.7 or Version 10.1 root installations on Linux or UNIX operating system, Or for administrators on the Windows platform:

## Procedure

- 1. on to the Db2 server as root on Linux and UNIX operating systems or user with Local Administrator authority on Windows operating systems. If you are upgrading a multipartitioned instance, you must perform instance upgrade from the instance-owning partition: Log
- 2 Install a new copy of V1I.1 with a custom installation and make sure that Db2 Text Search is selected. Db2 Text Search is an optional component that is available only when you select a custom installation. You also can choose to install a new V1I.I copy over an earlier Db2 version by selecting Work-With-Existing mode and selecting Db2 Text Search as the component to be upgraded. You do not have to upgrade the Db2 instances after the installation with this approach:
- 3 Upgrade the Db2 Text Search server for your Db2 instances by issuing the configTool upgradeConfigFolder command This command must be run as instance owner; and not root\_

- For Linux and UNIX operating systems:

SDBZDIR/dbztss/bin/configToo] upgradeConfigFolder ~sourceConfigFolder SDBZDIR/cfg/dbztss/config targetConfigFolder SINSTHOME/sq]lib/dbztss/config where, INSTHOME is the instance home directory and DBZDIR is the location of the newly installed V1L.1 copy

- For Windows operating systems:
- ~sourceConfigFolder "&lt;DBZPATH&gt;| CFG | DBZTSS I CONFIG" -targetConfigFolder "&lt;INSTPROFDIR&gt; &lt;INSTANCENAME&gt; | DBZTSS| CONFIG"

where, &lt;DBZPATH&gt; is the location of the newly installed V1I.l copy and &lt;INSTPROFDIR&gt; is the instance directory profile

Note: For Windows systems, if the Db2 instance was not configured previously for Db2 Text Search and the Db2 version to be upgraded is Version 9.7 Fix Pack 1 or later; you can skip this step.

The configToo] upgradeConfigFolder command replaces, modifies, and merges text search configuration and data files and directories.

## The config directory

The command copies the following files into the &lt;ECMTS\_HOME&gt;Iconfig directory if the files do not already exist in this directory:

- constructors xml
- ecmts\_logging properties
- ecmts\_config\_logging:properties

The following files are copied and any existing files are overwritten:

- constructors Xsd
- ecmts config\_logging:properties
- mimetypes xml
- monitoredEventsConfig xml

The configuration settings from the following files are merged to the configuration.xm] file: Values are added for new settings, and values are maintained for existing settings.

- config xml
- jettyxml

The following files are not modified:

- authentication xml
- keytxt
- All files in the collections subdirectory

## The directory log

The configTool upgradeConfigFolder command does not upgrade text search filters for an integrated text search server:

The command does not change the contents of the existing directory However; when new files are generated, those new files might replace existing files. log log log

- 4 Upgrade the current Db2 instance by issuing the dbziupgrade command.
- For Linux and UNIX operating systems, the command is located under the SDBZDIR/instance directory where DBZDIR is the location of the newly
- dbziupgrade -j "TEXT\_SEARCH [[,service-name] | [,port-number]]" DBZINST
- For Windows operating systems, the property file is located in &lt;DBZPATH Ibin directory, where &lt;DBZPATH&gt; is the location of the newly installed Db2 V1I.1 copy
- dbziupgrade DBZINST "TEXT SEARCH [[,service-name] [,port-number]]

For more information, see the topic about dbziupgrade command:

Note: If you installed a new V1I.l copy with the upgrade option, and selected Db2 Text Search as feature to be upgraded, then you can this skip step:

- For Linux and UNIX operating systems: SDBZDIR/dbztss/bin/bkuptscfg.sh SINSTNAME
- 5 Back up the values for all configurable properties of Db2 Text Search that were used in the previous release by running the following script:
- where, DBZDIR represents the location of the newly installed V1l.1 copy, and INSTNAME represents the name of the instance to be upgraded
- For Windows operating systems: &lt;INSTANCENAME&gt; &lt;DBZPATH&gt;

where, &lt;DBZPATH&gt; represents the location of the newly installed V1L.I copy, &lt;INSTANCENAME&gt; represents the name of the instance to be upgraded.

- For Linux and UNIX operating systems, the property file is located in the SINSTHOME/sq] ib/db2tss/config/dbztssrvupg.cfg directory, where INSTHOME represents the instance home directory:

The backed-up configurable properties are redirected into one property file:

- For Windows operating systems, the property file is located in the &lt;INSTPROFDIR&gt; where &lt;INSTPROFDIR&gt; represents the instance profile directory and &lt;INSTANCENAME&gt; represents the name of the instance to be upgraded: You can find the name of the instance profile directory by issuing the dbzset DBZINSTPROF command.

Requirement: You must complete a backup for the values of all configurable properties of Db2 Text Search that are used in previous releases. Failure to create backup results in a database upgrade failure.

- 7 Upgrade the databases by issuing the DB2 UPGRADE DATABASE command. If the DBZ  UPGRADE DATABASE command returns the ADM4OO3E error message, upgrade the Db2 Text Search and indexes manually by the SYSTS\_UPGRADE\_CATALOG and SYSTS\_UPGRADE\_INDEX stored procedures catalog using
- Set the DBZINSTANCE environment variable to the current upgraded instance:
- 8\_ For each upgraded database, verify whether the text search server properties information in the text search SYSIBMTS TSSERVERS catalog table is correct by comparing the property values backed up in 7. If the value of the token or port number in the catalog table is empty or incorrect, you must step

- the text server information manually: For details about how to update, see the topic about updating Db2 Text Search server information. update
- Review the values for all Db2 Text Search configurable properties. Compare with the values that you backed up to ensure that have correct values\_ Issue the following command to check the configuration values: they
- 10. If you disabled Db2 Text Search for rich text document support, you have to install Db2 V1O.5 Accessories Suite For more information, see the topic about installing Db2 Accessories Suite:
- 11. Then enable rich text document support: For more information, see the topic about enabling Db2 Text Search for rich text and proprietary format support
- 12. Verify that the upgrade was successful by starting the Db2 Text Search instance service. If you disabled rich text document support, verify that rich text document support is enabled by issuing text search queries and compare with pre-upgrade results

## Upgrading Dbz Text Search for non-root installation (Linux and UNIX)

If you are upgrading Db2 Text Search Version 11.1, You must upgrade the Dbz server; instance, and all databases:

## Before you begin

Complete the following tasks before you begin to upgrade your text search server:

- 1. Enable the root-based features for your user ID. You might have to ask a system administrator with root access to issue the dbzrfe command.
- 2. in as the instance owner or as a user with SYSADM authority: Then the Db2 instance and the Db2 Text Search instance service Log stop
- 3. Back up the old Db2 copy into a &lt;backup-dir&gt; directory:
- 4 If you enabled Db2 Text Search for rich text document support, disable rich text document support: For more information about how to disable rich text document support, see disabling Db2 Text Search for rich text document support:
- 5\_ on to the Db2 server as a non-root user: Review the database instance type to ensure it can be upgraded as a non-root installation: Log

## Procedure

To upgrade Db2 Text Search:

dbznrupgrade -b &lt;backup-dir&gt; -j "TEXT\_SEARCH"

- 1. Install a new Db2 Version 11.1 copy with the dbznrupgrade upgrade command. Select the Db2 Text Search component that you want to upgrade: If you specified the -f nobackup parameter and the Db2 database product installation failed, you must manually install the Db2 database product by selecting the Db2 Text search component from the feature tree and then upgrade the non-root instance by issuing the following command:
- &lt;backup-dirz specifies the directory where the configuration files from the old Db2 version are stored. For details about the upgrade non-root instance command, see dbznrupgrade command:
- 2 Back up values for all configurable properties of Db2 Text Search that is used in the previous release before the database upgrade by running the following script:

SINSTHOME/sq]lib/dbztss/bin/bkuptscfg.sh

The backed-up configurable properties are redirected into the

- 3 Upgrade the existing databases by issuing the UPGRADE DATABASE command.
- 4. For each upgraded database, verify whether the text search properties information in the text search table SYSIBMTS.SYSTSSERVERS is correct by comparing the information with the property values from step 6. If the value of token or port number in the table is empty or incorrect, you must the text server information manually For more information about the upgrading non-root instance, see updating Db2 Text Search server information. catalog catalog update
- 5\_ Upgrade the Db2 Text Search server for your instances by issuing the configToo] upgradeInstance command:
- For Linux and UNIX operating systems:
- sourceConfigFolder SDBZDIR/cfg/db2tss/config
- SDBZDIR/dbztss/bin/configTool upgradeConfigFolder
- -targetConfigFolder SINSTHOME/sq]lib/dbztss/config

INSTHOME is the instance home directory and DBZDIR is the location of the newly installed V1L.l copy

- 6\_ Compare the values that you backed up in step 6 with the values for all the Db2 Text search configurable properties to ensure that all the values are correct: Issue the following command to check the configuration values: ~configPath configuration-directory
- 7 . If you disabled Db2 Text Search for rich text document support, you must install the Db2 V1O.5 Accessories Suite. For information about the Accessories Suite, see installing Db2 Accessories Suite for Db2 Text Search:
- 9\_ Verify that the upgrade was successful by starting the Db2 Text Search instance service If you disabled rich text document support, verify that rich text document support is enabled by issuing text search queries and compare with pre-upgrade results
- 8 Then enable rich text document support: For more information about enabling support, see enabling Db2 Text Search for rich text and proprietary format support:

## Upgrading a multi-partition instance without Dbz Text Search

To obtain the latest functionality upgrade your Db2 Text Search instance: You need to upgrade the Db2 server; instance, and all databases when upgrading the text search instance\_

## About this task

Starting in Db2 Version 10.1, text search supports indexes in a partitioned database environment\_ The following steps describe the process to upgrade a Db2 Version 10.1 or Version 9.7 multi-partition instance for root install. Db2 Text Search should not be installed on the instances.

## Procedure

- 1\_ in as the instance owner or user with SYSADM authority: Log

- 2. Install new copy of the Db2 Text Search version you are upgrading and perform a custom installation. Db2 Text Search is an component that is only available when you select a custom installation. to, optional
- 4. Upgrade the existing databases by issuing DBZ UPGRADE DATABASE command,
- 3. Upgrade your instances by issuing the dbziupgrade command: dbziupgrade /j text search [[,service-name] | [,port-number]]
- 5. For each upgraded database, the text server information manually: For more information, see the topic about updating Db2 Text Search server information. update

## Upgrading a stand-alone Dbz Text Search Server

If you already installed the stand-alone Db2 Text Search server; you must install fixes to your existing installation to obtain the latest supported features and functionality: Upgrade the text search server by setting parameters in the response file and running the current installation program:

## Before you begin

Before you install a read all the attached release notes to determine the prerequisites or migration procedures that apply fix,

## About this task

If the existing stand-alone server was installed as Windows service by the installation program, the upgrade process stops and removes the current Windows service. You can configure the response file to install stand-alone text search as a new Windows service

## Procedure

To upgrade the stand-alone Db2 Text Search server:

- 1\_ Set the following parameters in the ecmts\_response.txt response file that is provided with the new version of the stand-alone text search sever: For more information, see the comments in the response file:

## LICENSE ACCEPTED

Specifies true to indicate that you accept the terms of the licence agreement The licence agreement is in the license directory that is provided with the installation setup file: You must copy the license directory to the location where will run the installation program. You must set the value of the LICENSE\_ACCEPTED parameter to true to upgrade the stand-alone text-search: you

## USERINSTALL DIR

Specifies the directory that contains the existing ECM Text Search installation.

## IA IF PREVIOUS\_SETUP EXISTS

Specify the following option:

## UPGRADE

The installation program upgrades the existing installation and does not overwrite any collections and settings.

## IA\_BACKUPECMTS\_HOME

Specify one of the following backup options:

## BACKUP NONE

No directories are backed up.

## BACKUP CONFIGURATION

Backs up the following directories under the &lt;ECMTS\_Home&gt; directory:

- bin
- lib
- resource
- stellant

The contents of the config directory are also backed up, except for the co] lections subdirectory:

## BACKUP\_ALL

The entire &lt;ECMTS\_Home&gt; directory is backed up.

Attention: configuration files or data that are not under the &lt;ECMTS\_Home&gt; directory are not backed up Any

- 2 Set any additional parameters in the response file as required. The values that you specify are when the installation program runs. If you do not specify an authentication token or port, the previously defined values are If you upgrade the stand-alone server\_ on computer on which it is installed as Windows service, you must specify the name of the service in the applied applied.
- 3\_ Run the setup file for operating system from the directory that contains the setup file and response file. If the stand-alone server is running, the installation program stops the server the upgrade process your during

## Chapter 7. Configuring and administering text search indexes

## Command-line tools for Db2 Text Search

Five command-line tools are included with Db2 Text Search to facilitate its use\_

## The Configuration Tool

For performing both the initial and subsequent configurations of Db2 Text Search

## The Administration Tool

For performing various administrative tasks related to the Db2 Text Search server

## The Synonym Tool

For synonym dictionaries to text search indexes and removing synonym dictionaries from text search indexes adding

## The Word Tool Stop

For removing frequently occurring terms, referred to as words, from text search queries stop

## The Formatter Tool Log

For viewing and saving messages and trace messages system

## Issuing text search commands

You can issue commands by running the dbzts command shell or by one of the administrative SQL routines that is stored procedure for Db2 Text Search: calling

## About this task

To use the dbzts command shell, pass the command as a parameter: The dbzts command shell acts like the Db2 command shell in that a command must contain the connection information if a remote database is used. Unlike the Db2 command shell, however; dbzts does not provide a session; instead, each command is a separate unit and thus must establish a connection separately You do not have to specify the database connection if you are running the command locally for the default database specified the DBZDBDFT environment variable: Set the DBZDBDFT environment variable at the operating level. If you also set it the dbzset command, ensure that the same value is used: string \_ using system using an administrative SQL routine enables you to issue administration calls from Db2 client on which you have not installed Db2 Text Search: You can call either the generic SYSTS\_ADMIN\_CMD administrative SQL routine with a command as a parameter or the specific administrative SQL routine for that command Using string

Note: Error messages resulting from db2ts commands are written in the client locale, but messages resulting from the administrative routines are written in the locale specified by the message-locale argument or in en\_US if you do not specify locale:

Because some commands are not related to a specific database, for example, START FOR TEXT and STOP FOR TEXT, you can run them only the dbzts command shell: using

## Rich text and proprietary format support

## Enabling Dbz Text Search for rich text document support

Rich text support can be enabled on properly configured Db2 Text Search servers.

## Before you begin

To enable rich text document support for Db2 Text Search servers you must, as the instance owner; run the richtextTool utility with the enable option.

Before enabling rich text document support, each Db2 Text Search server must be prepared for rich text document support: For more information, see "Installing Db2 Accessories Suite for Db2 Text Search" on page 63

## Restrictions

In order to run richtextTool enable, you must be logged on as the instance owner:

## Procedure

- 1\_ on as the instance owner: Log
- 2. Stop the Db2 Text Search instance service To stop the service, run dbzts STOP FOR  TEXT .
- 3\_ Run the richtextTool utility from Db2 command window to enable support:
- For Linux and UNIX operating systems: SINSTHOME/sq]lib/dbztss/bin/richtextToo] enable DBZDIR
- where INSTHOME is the instance home directory and DBZDIR is the location of the latest Db2 copy
- For Windows operating systems: DBZPATH dbztssibinlrichtextTool .bat enable DBZPATH
- where DBZPATH is the location where you installed the latest Db2 copy:
- 4 Start the Db2 Text Search instance service\_ To start the service, run dbzts START

## Results

You have enabled rich text support for a Db2 Text Search server:

## Disabling support for rich text and proprietary formats

Support for rich text and proprietary formats can be disabled at any time on the integrated Db2 Text Search servers.

## Before you begin

To disable rich text document support for Db2 Text Search servers you must, as the instance owner; run the richtextTool utility with the disable option:

## Restrictions

To run the richtextTool disable command, YOu must login as the instance owner:

## Procedure

- 1. on as the instance owner: Log
- 2 the Db2 Text Search instance service: To stop the service, run dbzts "STOP FOR TEXT" For more information about this command, see "Stopping the Db2 Text Search instance service: Stop
- 3\_ Run the richtextTool utility from the Db2 command window to disable support:
- For Linux and UNIX operating systems: SINSTHOME /sq]ib/dbztss/bin/richtextToo] disable DBZ-install-directory
- where INSTHOME is the instance home directory
- For Windows operating systems: DBZ-install-directory
- where DBZPATH is the location where you installed your Db2 database server copy
- 4 Start the Db2 Text Search instance service. To start the service, run dbzts "START FOR TEXT"\_ For more information about this command, see "Starting the Db2 Text Search instance service\_

## Results

You have disabled rich text support for a Db2 Text Search server:

## Starting the Db2 Text Search instance service

Before you can create and search text indexes, you must start the Db2 Text Search instance service:

## About this task

To start the integrated Db2 Text Search instance service, enter the following command:

dbzts "START FOR TEXT'

To start the stand-alone text search server; run the startup script from the &lt;ECMTS\_HOME&gt; directory:

- On Windows: &lt;ECMTS\_HOME |bin|startup
- On Linux and UNIX:
- &lt;ECMTS\_HOME&gt;/bin/startup.sh

You can check the status of the Text Search server with the following command: dbzts "START FOR TEXT status"

## Stopping the Db2 Text Search instance service

When you stop the Db2 Text Search instance services, the text search server closes all commands that are currently active:

## About this task

The active commands are closed as follows:

- creating the collection for the text search index is completed, implying that a CREATE INDEX FOR TEXT operation could fail in a multi-partition as a text search index is partitioned into multiple collections setup,
- processes the current documents in the queue: Does not accept other documents. An initial is marked as attempted and restart, an incremental repeats processing all entries in the staging table: update update
- if collection already started to remove files irreversibly, the is completed, otherwise the command is rolled back drop drop
- if you the index with the updateautocommit option, the documents that are already submitted when the text search server closes are implicitly committed and are processed: The rest of the documents are not processed. For example, consider that the text server is shut down unintentionally As it shuts down, there are 1000 documents to be indexed and the update index command was issued with the updateautocommit set to 100. If you check the number of documents that are indexed with the adminToo] you will see an arbitrary value (not multiple of 100) as NumOfDocuments indexed. In other words, partial commit occurs shutdown: update option during

New commands are not accepted while the text search server completes the stop processing

## Procedure

To the Db2 Text Search server: stop

- for the integrated Db2 Text Search instance service, enter the following command:

dbzts "STOP FOR TEXT"

- for the stand-alone text search server; run the shutdown script from the &lt;ECMTS\_HOME&gt; directory, where &lt;ECMTS\_ HOME&gt; represents the installation directory of the stand-alone text search server:
- On Windows:
- &lt;ECMTS HOME|binlshutdown
- On Linux and UNIX:

&lt;ECMTS\_HOME&gt; /bin/shutdown. sh

## Enabling a database for Db2 Text Search

You must enable each database that contains columns of text to be searched. You can enable a database forDb2 Text Search by the dbzts ENABLE DATABASE FOR TEXT command or the SYSPROC.SYSTS\_ENABLE stored procedure: using

## Before you begin

The authorization ID of the statement must hold the SYSTS\_ADM role and DBADM authority:

## About this task

When enable a database, you can use the following views to get information about the text search indexes in the database and their properties: you

## SYSIBMTS.TSDEFAULTS

Shows the database default values for index, text, and processing characteristics

## SYSIBMTS.TSLOCKS

Shows information about command locks set at the database and index level

## SYSIBMTS TSINDEXES

Shows all text search indexes and their settings

## SYSIBMTS.TSCONFIGURATION

Shows the index configuration parameters

## SYSIBMTS.TSCOLLECTIONNAMES

Shows the collection names for each index

## SYSIBMTS.TSSERVERS

Shows the Text Search server connection information

After you enable a database for text search, it remains enabled until you explicitly disable it:

To prepare the database for use with Db2 Text Search, use one of the following methods:

- Enter the following command:

dbzts ENABLE DATABASE FOR TEXT CONNECT TO databaseName

The enable operation attempts to populate the connection information for the text search server in the SYSIBMTS TSSERVERS administrative view: However; the information might be incomplete or insufficient: After the command completes either successfully or with a warning for incomplete enablement, review the values in SYSIBMTS TSSERVERS view and as necessary: update

You must do this only once for each database: You do not have to enable a database each time that you and restart the instance services\_ step stop

For example, to enable a database named SAMPLE, enter the following command:

dbzts ENABLE DATABASE FOR TEXT CONNECT TO SAMPLE"

- Call one of the administrative SQL routines, as follows:
- CALL SYSPROC. SYSTSADMIN CMD ENABLE DATABASE FOR TEXT en\_US" 2 )
- CALL SYSPROC.SYSTS\_ENABLE( 'en\_US ' 2)

## Disabling a database for Db2 Text Search

Disable a database when you no longer intend to perform text searches in that database:

## About this task

When you disable a database for text search, catalog tables and administrative views are dropped from the SYSIBMTS schema.

## Procedure

To disable a database for text search, use one of the following methods:

- 1 any text search indexes defined in the database, the DROP INDEX command: Drop using
- 2 To disable database for text search, use one of the following methods:
- Issue the DISABLE DATABASE FOR TEXT command: dbzts "DISABLE DATABASE FOR TEXT CONNECT TO databaseName

- Call the SYSPROCSYSTS\_DISABLE procedure:
- CALL SYSPROC. SYSTS\_DISABLE ( 'en\_US 2)

Note: Text search indexes can also be dropped the FORCE However; it is possible that some data, specifically a text search collection, will remain after you disable the database. This can occur because the FORCE option allows you to text search indexes even if the Db2 Text Search server cannot be reached. Such a remaining collection needs to be explicitly removed with the CLEANUP operation. using option. drop

## Deleting orphaned DBZ Text Search collections

You can delete orphaned collections with the dbzts CLEANUP FOR TEXT command or use the following process to identify and remove orphaned collections by using the administration tool.

## About this task

A text search index is associated with a single collection for non-partitioned or single-partition databases, and with n collections for multi-partition databases with n the number of relevant data partitions. Although dbzts commands and procedures operate on text search indexes, the text search tools operate on the text search collections\_ When a text search index no longer exists but its corresponding text search collection does, it is called an orphaned collection:

collection will orphaned in the following scenarios: get

- the FORCE with the DISABLE or DROP index operation using option
- dropping a database that contains the text index

These operations succeed even if the Text Search server is not reachable:

A collection may also an orphaned or an invalid status in some failure scenarios. For example, a disk crash may cause an inconsistency in the text index metadata. get

To determine whether any orphaned collections exist:

- 1. Use the administration tool to report all text search collections. Issue the following command:
- adminToo] status -configPath &lt;absolute-path-to-configuration-folderz
- 2. Query the SYSIBMTS.TSCOLLECTIONNAMES administrative view to report all text search indexes on the current database:
- SELECT collectionname FROM SYSIBMTS. TSCOLLECTIONNAMES
- Perform this query on all the databases enabled for Db2 Text Search, and combine the results into a list:
- The administration tool lists all text search collections, while the query on the SYSIBMTS.TSCOLLECTIONNAMES view lists only text search indexes on the current database.
- 3\_ Compare the lists returned by the administration tool and by the SELECT statement text search collection returned by the administration tool but not by the SELECT statement is an orphaned collection: The only exception to this rule is the default collection that is created when the Db2 Text Search server is started. Any

Remove the orphaned text search collection with the following command:

adminToo] delete -configPath &lt;absolute-path-to-configuration-folder&gt; ~co]lectionName collection-name

Important: The action performed by the adminTool delete command is not recoverable and is equivalent to dropping an index Or rendering index inconsistent: an

## Example

You currently have Db2 Text Search enabled for a database called DBCP1208, which is running on a UNIX To determine whether any orphaned text search collections exist, use the administration tool and SELECT statement: system:

adminTool .sh status ~configPath SHOME/sq]lib/db2tss/config

| Co] lectionName IndexSize         | NumofDocuments   |    |
|-----------------------------------|------------------|----|
| Default 13,159B                   |                  |    |
| tigertail_ DBCP1208  TS5427170000 | 13,159B          | 17 |
| tigertail_ DBCP1208 TS012817 000  | 13,159B          |    |
| tigertail_DBCP1208_TS082817_00    | 13,159B          | 16 |
| tigertail_ DBCP1208 TS152817      | 13,159B          | 18 |
| tigertail_ DBCP1208 TS212817 000  | 13,159B          | 16 |
| tigertail_ DBCP1208 TS302817 000  | 13,159B          | 17 |
| tigertail_DBCP1208_TS392817_0000  | 13,159B          | 10 |
| tigertail_ DBCP1208 TS462817 000  | 13,159B          | 10 |
| tigertail_ DBCP1208 TS542817 000  | 13,159B          | 12 |
| tigertail_ DBCP1208 TS022917 0000 | 13,159B          | 10 |
| tigertail_DBCP12O8_TS112917_0000  | 13,159B          | 16 |
| tigertail_ DBCP1208_TS192917 000  | 13,159B          | 11 |
| tigertail_ DBCP1208_TS262917 0000 | 13,159B          | 12 |
| tigertail_DBCP1208_TS867530_0000  | 13,159B          | 16 |

dbz select collectionname from sysibmts.tsco] lectionnames

## COLLECTIONNAME

tigertail DBCP1208\_TS542717\_0000

tigertail DBCP1208\_TS082817 000

tigertail DBCP1208\_TS012817\_0000

tigertail

DBCP12O8\_TS152817

000

tigertail DBCP12O8\_TS212817 000

tigertail\_DBCP1208\_TS392817 000

tigertail\_DBCP1208\_TS302817\_0000

tigertail\_ DBCP12O8\_TS462817 0000

tigertail DBCP1208\_TS542817 0000

tigertail\_DBCP12O8\_TS112917\_0000

tigertail\_DBCP12O8\_T262917\_0000

tigertail\_ DBCP1208 TS192917 0000

13 record(s) selected\_

Comparing the two outputs, you see that the text search collection tigertail\_DBCP1208\_TS867530\_0000 does not have a corresponding text search index Use the administration tool to delete that orphaned collection:

adminTool.sh delete -configPath SHOME/sq]lib/dbztss/config

## Synonym dictionaries for Dbz Text Search

synonym dictionary contains words that are synonyms of each other: You can use a synonym dictionary to search for synonyms of your query terms in a text search index, thus improving the results of your search queries.

synonym dictionary, you can search for words to your organization, such as acronyms and technical jargon: specific Using

By default, a synonym dictionary is not used for a search: To use a synonym dictionary, you must explicitly add it to a specific text search index The text search index needs to be at least once before can add a synonym dictionary: After the synonym dictionary has been added, you can modify it as frequently as you want updated you

A synonym dictionary consists of synonym groups that you define in an XML file, as shown in the following example:

&lt;?xm] version= 1.0" encoding="UTF-8"2&gt; &lt;synonymgroups version="1.0"&gt;

- &lt;synonymgroup&gt;
- &lt;synonym-globe&lt;/ synonym&gt;
- &lt;S ynonymzsphere&lt;/ synonym&gt;
- synonymgroup&gt;
- &lt;synonymzorb&lt;/synonym&gt;
- &lt;synonymgroup&gt;
- &lt;synonymzwpts&lt;/synonym&gt;
- &lt;synonymzwor]dwide patent tracking system&lt;/synonym&gt;
- synonymgroup&gt;
- synonymgroups&gt;

## Adding a synonym dictionary for Db2 Text Search

You can easily add a synonym dictionary to a text search index by the Synonym Tool. using

## Before you begin

- You must activate the Db2 Text Search instance service before you can add a synonym dictionary to a text search index
- You must have the text search index at least once: updated
- You must also have a synonym XML file that specifies synonym groups.

## Procedure

To add synonym dictionary:

- 2. Determine the name of the text search collection associated with the text search index to which you want to add the synonym dictionary: You can use the Administration Tool to report all text search collections, as follows: adminTool status ~configPath absolute-path-to-config-folder
- 1. the XML file to any directory on the Db2 Text Search server: Copy
- 3\_ Use the Synonym Tool to add the synonym dictionary to the specific text search index\_ You can add the synonyms in append O replace mode, meaning that you either add them to or replace the existing synonyms defined for that text search index
- synonymToo] importSynonym -synonymFile absolute-path-to-syn-file ~collectionName collection-name -replace true or false ~configPath absolute-path-to-config-folder

Note: If the XML format is not valid or if the XML file is empty, an error is returned\_

## Example

For example, to add the synonym file synfile.xm] in append mode, use the following command:

synonymToo] importSynonym ~synonymFile SHOME/sq]lib/misx/xm] Te.xm] -co]lectionName tigertail\_ DBCP12O8\_TS867530\_0000 -replace false ~configPath SHOME/sq]lib/db2tss/config synfi

## Removing a synonym dictionary for Db2 Text Search

You need to remove synonym dictionaries on collection-by-collection basis, so you must use the Synonym Tool on all collections that exist for a text search index

## About this task

To remove synonym dictionary, use the following command:

synonymToo] removeSynonym ~co]lectionName collection-name -configPath absolute-path-to-config-folder

Where collection-name specifies the text search collection and absolute-path-to-configfolder specifies the absolute to the text search configuration folder: path

## Text search index creation

text search index is a compilation of significant terms extracted from text documents. Each term is associated with the document from which it was extracted:

You create a text search index once for each column that contains text to be searched. When you create a text search index, you also create the following objects:

## staging table

This keeps track of all changed rows in the user table:

## An auxiliary staging table (optional)

This keeps track of inserts and in the user table via integrity processing: updates

## An event table

This collects information about the status of an index command or any errors encountered during its processing: If errors occur indexing, index events are added to the event table: update during update

## Triggers on the user table

These add information to the staging table whenever a document in the column is added, deleted, or changed. The information is necessary for index synchronization when indexing time next occurs.

Note: If you use the LOAD command to populate your documents, triggers are not activated, and incremental indexing of the loaded documents will not work Instead, use the IMPORT command, which does activate triggers.

Alternatively you can add the auxiliary infrastructure for integrity processing, this will recognize changes for example, with the LOAD INSERT command\_

After create a text search index, it is empty and, therefore, not searchable, until you which is used by the scheduler to check periodically whether an of the text search index is required and that the command is to be run if necessary: you update update update

## Creating a text search index

After you enable a database for Db2 Text Search, you can create text search indexes on columns that contain the text that you want to search:

## Before you begin

Creating a text search index requires one of following authorization levels:

- CONTROL privilege on the index table
- INDEX privilege on the index table with either the IMPLICIT\_SCHEMA authority on the database or the CREATEIN privilege on the index table schema
- DBADM with DATAACCESS authority

To schedule automatic index updates, the instance owner must have DBADM authority o CONTROL privileges on the administrative task scheduler tables.

primary must exist for this table: If a primary does not exist, you must create one before creating the index: key key

## About this task

If you do not want to manually apply document changes from the table to the text search index, you can specify the UPDATE FREQUENCY parameter to schedule automated Use the UPDATE MINIMUM parameter to control whether the only runs when minimum number of changes is made to the table For example, to specify that MYSCHEMA MYTEXTINDEX is to be after at least five changes have occurred and that the services are to check Monday and Wednesday at 12 midnight and 12 noOn, issue the following command: updates. update updated update every

dbzts CREATE INDEX MYSCHEMA. MYTEXTINDEX FOR TEXT ON PRODUCT (NAME) UPDATE FREQUENCY d(1,3) h(0,12) m(0) UPDATE MINIMUM 5 "

CALL SYSPROC. SYSTS\_CREATE ( 'myschema 'myText Index product (name) UPDATE FREQUENCY D(1,3) H(0,12) UPDATE MINIMUM 5 en\_US" 2) M(0)

When you create an index, YOu can specify its locale (language and territory) by the LANGUAGE To have your documents automatically scanned to determine the locale, set the LANGUAGE to AUTO. If you do not specify LANGUAGE, a default is used. This default is derived using the DEFAULTVALUE from DEFAULTVALUE is set at the time the database is enabled for text search: This value is derived from the database territory if the database territory can be mapped to one of the document locales supported. If the database territory cannot be used to determine a supported document locale, DEFAULTVALUE is set to AUTO.) using option.

Restrictions

- text column in an index must be one of the following supported types:
- CHAR
- VARCHAR
- LONG VARCHAR
- CLOB
- GRAPHIC
- VARGRAPHIC
- LONG VARGRAPHIC
- DBCLOB
- BLOB
- XML
- Text search related objects must follow not only DB2 naming conventions, their identifiers must also contain these characters only:
- [A-Za-z][A-Za-z0-9@#S\_]* or

This limitation to the following: applies

- the name of the schema containing the text search index
- the name of the table the text search index is associated with
- the name of the text column
- the name of the text search index

## Procedure

Create a text search index one of the following methods: using

- Issue the CREATE INDEX command: index-name

dbzts "CREATE INDEX FOR TEXT ON table-name (column-name

- Call the SYSPROC.SYSTS\_CREATE stored procedure:

CALL SYSPROC. SYSTS\_CREATE ( ' index-schema index-name table-name (column-name) options locale 2 )

Note: Schema name and index name are case-sensitive when the stored procedure is used:

## Example

For example, the PRODUCT table in the SAMPLE database includes columns for the product ID, name, price, description, and so on To create a text search index called MYSCHEMA MYTEXTINDEX for the NAME column, issue the command or called the stored procedure, as follows:

dbzts CREATE INDEX FOR TEXT ON   PRODUCT (NAME)

CALL SYSPROC.SYSTS\_CREATE ( 'MYSCHEMA MYTEXTINDEX" PRODUCT (NAME) en\_US" 2)

Similarly, to create a text search index called MYSCHEMA MYXMLINDEX for the XML column DESCRIPTION, enter the following command:

dbzts CREATE INDEX MYSCHEMA. MYXMLINDEX FOR TEXT ON PRODUCT (DESCRIPTION)

or

CALL SYSPROC.SYSTS\_CREATE ( 'MYXMLINDEX ' PRODUCT   (DESCRIPTION) 2)

## Creating a text search index on binary data types

When creating a text search index, you have the of specifying a code page for a binary column. SO helps the Db2 Text Search engine identify the character encoding: option Doing

## About this task

To specify the code page when creating the text search index, use the following command:

dbzts "CREATE INDEX index-name FOR table-name CODEPAGE code-page

When you store data in a column having a binary data type, such as BLOB or FOR BIT DATA, the data is not converted This means that the documents retain their original code pages, which can cause problems when you create a text search index because you might have two different code pages. Therefore, you need to determine whether you are using the code page of the database or the code page page was used to create the text search index, you can find out by issuing the following statement:

"SELECT CODEPAGE FROM  SYSIBMTS. TSINDEXES where INDSCHEMA= ' schema-name and INDNAME = index-name

## Creating a text search index on unsupported data types

If documents are in a column of an unsupported data type, such as user-defined type (UDT), you must provide a function that takes the user type as input and provides an output type that is one of the supported types.

## About this task

text column in an index must be one of the following supported types:

- CHAR
- VARCHAR
- LONG VARCHAR
- CLOB
- GRAPHIC
- VARGRAPHIC
- LONG VARGRAPHIC
- DBCLOB
- BLOB
- XML

To convert the data type of the column to one of valid types, use one of the following methods:

- Run the dbzts CREATE INDEX command with the name of a transformation function:

dbzts "CREATE INDEX index-name FOR TEXT ON table-name (function-name(text-column-name) ) "

- Use a user-defined external function (UDF), which is specified by function-name, that accesses text documents in a column that is not of a supported type for text searching, performs a data-type conversion of that value, and returns the value as one of the supported data types.

## Example

In the following example, there is a table UDTTABLE that contains column of a user-defined type (UDT) named "COMPRESSED\_TEXT" , which is defined as CLOB(IM): To create an index on that data type, first create a UDF called UNCOMPRESS, which receives a value of type COMPRESSED\_TEXT Next, create your text search index in the following way:

dbzts "CREATE INDEX UDTINDEX FOR TEXT ON UDTTABLE (UNCOMPRESS(text) )

## Sample: Creating N-gram and morphological indexes for text plain

## About this task

Use the following instructions to setup and synchronize Db2 Text Search indexes for morphological and N-gram indexing in the SAMPLE database. Search for linguistically meaningful Chinese words.

## Procedure

- 1 Create two tables for morphological and N-gram indexing: The tables have columns for the book name, author; story, ISBN number and the year the book was published.
- 2 Issue the CREATE INDEX command to create a text search index on the STORY column of MORPHOBOOKS table: The name of the text search index is MORPHOINDEX
- 3\_
- Issue the CREATE INDEX command to create a text search index on the STORY column of NGRAMBOOKS table. The name of the text search index is NGRAMINDEX

```
CREATE TABLE morphobooks isbn VARCHAR( 18) not PRIMARY KEY , bookname VARCHAR(30) . author VARCHAR(30) story blob(1G) _ year integer )
```

```
dbz CREATE TABLE ngrambooks isbn VARCHAR ( 18) not null PRIMARY KEY , bookname VARCHAR(30) . author VARCHAR(30) . story blob(16) _ year integer )
```

```
dbzts CREATE INDEX dbzts.morphoindex FOR TEXT ON morphobooks (story) LANGUAGE zh_TW INDEX  CONFIGURATION  (CJKSEGMENTATION morphological ' ) CONNECT
```

dbzts CREATE INDEX dbzts.ngramindex FOR TEXT ON ngrambooks (story) LANGUAGE zh\_TW INDEX CONFIGURATION (CJKSEGMENTATION ngram' )

- 4 Load data into the tables: two

dbz import from Idata/books.del of DEL Iobs from replace into morphobooks dbz import from Idata/books.del of DEL Iobs from replace into ngrambooks"

```
The books. del file has the '0-13-086755-4" "bookl" "Julie" "books zh_TWl.Iob.0.449/' 2004 The Books_zhTWI. Iob object has the following content: entry: large
```

- 5. Synchronize the text search indexes with data from the corresponding table by issuing following commands:
- dbzts   "UPDATE INDEX dbzts.morphoindex FOR TEXT CONNECT TO samp]e"

dbzts "UPDATE INDEX dbzts.ngramindex FOR TEXT CONNECT TO sample"

- 6\_ A search for linguistically meaningful Chinese words is successful here for both morphological and N-gram segmentation

Figure 15. Query results for meaningful Chinese words

<!-- image -->

The output indicates that the result from morphological segmentation is the same as N-gram segmentation

- 7 . Search for meaningless Chinese words to see the difference between morphological and N-gram segmentation

```
#+ 3elecced. db2 "gelec #+' bocki 3elecced
```

Only N-gram segmentation returns book name\_

## Sample: Creating N-gram and morphological indexes for rich text and proprietary formats

## About this task

Use the following instructions to setup and synchronize Db2 Text Search indexes for morphological and N-gram indexing in the SAMPLE database Search for meaningless Chinese words.

## Procedure

- 1 Create two tables for morphological and N-gram indexing: The tables contain columns k and b, where column k is the primary and column b will have rich text data. key,
- 2 Issue the CREATE INDEX command to create a text search index on column b of table RICHTEXT\_MORPHO. The name of the text search index is MORPHOINDEX
- 3 Issue the CREATE INDEX command to create a text search index on on column b of table RICHTEXT\_NGRAM The name of the text search index is NGRAMINDEX.
- 4\_ Load data into the two tables:

```
db2 "create table richtext_morpho( k varchar(50)not null , b blob (1G) primary key (k) ) dbz "create table richtext_ngram(
```

```
k varchar(50)not null _ b blob (1G) primary key (k) )
```

```
dbzts CREATE INDEX dbzts_ ndex FOR TEXT ON richtext_morpho (b) LANGUAGE zh CN FORMAT INSO INDEX  CONFIGURATION (CJKSEGMENTATION morphological ' ) CONNECT TO samp]e
```

```
dbzts CREATE INDEX dbzts.ngramindex FOR TEXT ONrichtext ngram (b) LANGUAGE zhCN  FORMAT InSO INDEX   CONFIGURATION (CJKSEGMENTATION ngram" ) CONNECT
```

dbz import from Idata/cjk\_richtext.del of DEL Iobs from Idata/ replace into richtext\_morpho dbz import from Idata/ cjk\_richtext.del of DEL Iobs from Idata/ replace into richtext\_ngram

The cjk\_richtext.del file has the entries:

"rt CJK.pdf" "rt CJK.pdf.0.864885/ "rt CJK.pdf.doc" "rt\_CJK. doc.0.90112/" "rt\_CJK.pdf.txt "rt\_CJK. pdf\_ pdf\_

rt\_CJK.pdf.doc and rt\_CJK.pdf.txt files all have the same content: One segment of the content in Simplified Chinese is as follows: pdf,

IBM Rational License Key Center Rationa] IBM Rational License Key Center License Center License Key Center 2 License Center License Center Key Key Key

Racioral Iicerse %ey

I3h Racioral

Licerse Cercer

1

Licerse Cercer Ze;

Licerse Cerces

Figure 17. Sample segment of content in Simplified Chinese

- 5. Synchronize the text search indexes with data from the corresponding table by issuing following commands:

dbzts "UPDATE INDEX dbzts morphoindex FOR TEXT CONNECT TO samp]e"

dbzts "UPDATE INDEX dbzts.ngramindex FOR TEXT CONNECT TO samp]e"

- 6\_ A search for linguistically meaningful Chinese words is successful here for both morphological and N-gram segmentation.

```
k rt doc iicerse record(3) 3elecced_ d2 Igrar wrere doc 3 record(s) 3elecced_
```

The output indicates that the result from morphological segmentation is the same as N-gram segmentation

- 7 \_ Search for meaningless Chinese words to see the difference between morphological and N-gram segmentation:

```
db2 "gelecc k fror wrere record(3) 3elecced d2 "3elect k wrere iicerse rt doc 3 record(3) 3elecced_
```

Only N-gram segmentation returns book name

## Text search index maintenance

After you create text search indexes, there are several maintenance tasks that you need to perform: There are several ways to perform these tasks, including various administration commands, stored procedures, and the Administration Tool. using

The routine text search index maintenance tasks include the following ones:

- that are associated with: they
- Running periodic Unless you specified that automatic updates are to be performed, you must the text search indexes to reflect changes in the indexed text columns updates update
- Monitoring the event table

You can use the event table to determine whether there are document errors or whether the index frequency needs to change update

Less frequent maintenance tasks include altering and dropping text search indexes.

## Administration commands for Db2 Text Search

There are a number of commands that allow you to administer Db2 Text Search at the instance, database, table, and text-index levels. You run all of the commands db2ts. using

Use the instance-level administration commands to start and the Db2 Text Search instance services and clean up text search indexes that are no longer usable: stop

## dbzts START FOR TEXT

Starts the Db2 Text Search instance services

## dbzts STOP FOR TEXT

the Db2 Text Search instance services Stops

## dbzts CLEANUP FOR  TEXT

Cleans up any text search collections that are not usable

Use the database-level administration commands to set up or disable databases for Db2 Text Search and clear command locks:

## dbzts ENABLE DATABASE

Enables the current database to create, manage, and use text search indexes

## dbzts DISABLE DATABASE FOR TEXT

Disables Db2 Text Search for a database and drops a number of text search tables and views catalog

## dbzts CLEAR COMMAND LOCKS

Deletes command locks for all indexes in database

Use table- and index-level commands to create and manipulate text search indexes on columns of a table:

## dbzts CREATE INDEX

Creates a text search index

## dbzts DROP INDEX

Drops a text search index associated with a text column

## dbzts ALTER INDEX

Changes the characteristics of a text search index

## dbzts UPDATE INDEX

Populates or a text search index based on the current contents of a text column updates

## dbzts CLEAR EVENTS FOR TEXT

Deletes events from the SYSIBMTS.TSEVENT view, an events view that provides information about indexing status and errors

## dbzts CLEAR COMMAND LOCKS FOR   INDEX

Deletes all command locks for a specific text search index

## dbzts RESET PENDING  FOR  TABLE

Identifies all dependent tables that are maintained for text search and executes set integrity, if necessary

## dbzts HELP

Displays the list of dbzts command options and information about specific error messages

## Db2 Text Search stored procedures

Db2 Text Search provides several administrative SQL routines for running commands and for returning the result messages of the commands that you run and the result message reason codes:

You can run the following dbzts commands the administrative SQL routines: using

Enable a database SYSPROC . SySTS ENABLE

Configure a database SYSPROC. SySTS\_CONFIGURE

Disable a database SYSPROC . SySTSDISABLE

Create a text index SYSPROC . SYSTSCREATE

Update a text index

SYSPROC. SySTSUPDATE

Alter a text index SYSPROC . SYSTS\_ALTER

Drop a text index SYSPROC. SYSTSDROP

Clear events for a text index

Clear command locks SYSPROC . SySTS CLEARCOMMANDLOCKS

Reset pending status SYSPROC . SySTSADMIN CMD

SYSPROC. SySTS\_CLEANUP

- Cleanup inactive indexes

## Updating a text search index

You can a text search index automatically or manually: Automatic updates occur based on how you defined the frequency for the text search index You can update indexes manually by issuing a command or by calling a stored procedure: update update

## Before you begin

Updating a text search index requires the SYSTS\_MGR role and either the CONTROL privilege or DATAACCESS authority on the target table:

## About this task

After creating and updating (filling) the text search index for the first time, you must keep it up to date: For example, when you add a text document to a database or change an existing document in a database, you must index the document to keep the content of the text search index synchronized with the content of the database. Also, when you delete a text document from database, you must remove its terms from the text search index:

You should plan periodic indexing carefully because indexing text documents is a time- and resource-consuming task The time taken depends on many factors, including how the documents are, how many documents you added or changed since the previous text search index update, and how powerful your processor is. big

The Administration Tool's status option can be used to retrieve information about the progress of document updates while the dbzts UPDATE INDEX command is running: If an index update is still in progress when a new update starts, the new fails. update

- Automatic updates

To have text search index updates performed automatically, use one of the following commands to set an UPDATE FREQUENCY:

- dbzts CREATE INDEX
- dbzts ALTER INDEX

The UPDATE FREQUENCY parameter has a minimum setting of five minutes. The UPDATE MINIMUM parameter specifies the minimum number of text changes that must be queued.

If there are not enough changes in the staging table for the specified and time, the text search index is not day updated.

- Manual updates
- There are also times when you want to a text search index immediately: For example, after you create a text search index, when the index is still empty, or after you have added several text documents to a database and want to search\_ update

To fill or synchronize (update) a text search index with the table data, use one of the following methods:

- Issue the UPDATE INDEX command:
- dbzts  "UPDATE INDEX   index-name FOR TEXT"

## Example

For example, suppose that there are two text search indexes on the PRODUCT table: MYSCHEMA MYTEXTINDEX on the NAME column and MYSCHEMA MYXMLINDEX on the DESCRIPTION column. A new entry is added to PRODUCT as follows:

INSERT ('100-104-01 Wheeled Snow Shovel 99.99 NULL, NULL, NULL, XMLPARSE (DOCUMENT &lt;product http: / /posample.org/wheel shovel pid-" 100-104-01"&gt;&lt;descriptionz&lt;name Wheeled Snow Shovel&lt;/name&gt; &lt;details Wheeled Snow Shovel Iever assisted\_ ergonomic foam grips, gravel wheel = clears away snow 3 times &lt;/descripti onz&lt;/product&gt;'))

To make the information in the new searchable, issue the following command: entry dbzts "UPDATE INDEX MYSCHEMA. MYTEXTINDEX FOR TEXT"

To make the information in the new searchable, use the following stored procedure: entry dbz sysproc.systs\_update( 'MYSCHEMA MYXMLINDEX ' en\_US ' 2)

## Sample: Incrementally updating a Db2 Text Search index on range-partitioned tables

Incremental updates of Db2 Text Search indexes on range-partitioned tables require the extended text-maintained staging infrastructure to apply changes from attaching or detaching partitions.

## About this task

When the extended staging infrastructure is enabled for the text search indexes, document updates are captured through an update trigger into the primary staging table, and document inserts and deletes are captured in the auxiliary staging table through integrity processing:

When the extended staging infrastructure is not enabled, you cannot use an incremental to process changes related to attaching or detaching ranges or to process documents that you loaded into an added partition by the LOAD command with the INSERT parameter You must re-create the text index to synchronize it with the base table: update using

By default, the extended text-maintained infrastructure will be added for text search indexes on range-partitioned tables, however; for scenarios where the text search index is not refreshed with incremental updates, you can create the text search index with the AUXLOG option set to OFF as shown in the following example: dbzts create index samp]eix for text administration tables in my 'tablespace index configuration(auxlog off) connect to mydb

In this case, only primary staging table is added, and document changes are recognized through triggers, which excludes changes for example, from attach o detach operations. You must specify the ADMINISTRATION TABLES IN parameter when creating indexes on range-partitioned tables; otherwise, an error is generated:

## Example

## Scenario 1: To attach a partition for a table with the extended text search staging infrastructure

- 1. Create range-partitioned table
- db2 "create table uc 007customer archive (pk integer not null primary key, customer varchar(128) not nul] year integer not address blob ( 1M) not nul1) partition by range(year) (starting(2000)ending (2001)every 1)
- 2 Create the text search index
- dbzts create index 007 idx for text on archive (address) administration tables in mytablespace"
- View the index name and logging information. dbz "select indexname stagingviewname\_ auxstagingname from sysibmts.tsindexes
- Update the text search index dbzts update index uc\_007\_idx for text"
- 4.
- 5.
- Create another table and import data into the table: db2 "create table uc\_007\_customer\_2001 (pk integer not nul] primary key , customer varchar(128) not year integer not null address blob(1M) not dbz import from uc 007 2001.del of del from Idata modified by codepage-1208 insert into uc\_007\_customer2001"
- 6. Add the data from the new table as a new partition.
- dbz alter table uc\_007 customer archive attach partition p2O01 starting(2001) ending(2002) exclusive from uc\_007\_customer\_2001
- 7 . View the contents\_

dbz "select from sysibmts.systsaux] ix253720'

- The output is as follows:

PK

GLOBALTRANSID

GLOBALTRANSTIME

OPERATIONTYPE

record(s) selected.

- 8\_ The changes are not visible, so integrity processing is required: Integrity processing places dependent tables in pending mode: dbz "set integrity for uc\_007\_customer\_archive immediate checked"
- 9\_ View the contents\_

dbz "select from sysibmts.systsaux ix253720" log\_

The following error message is returned:

PK

GLOBALTRANSID

GLOBALTRANSTIME

OPERATIONTYPE

SQLO668N Operation not a] Iowed for reason code 1" on table "SYSIBMTS "SYSTSAUXLOG\_IX253720" SQLSTATE-57016

- 10. Perform integrity processing for the text search staging tables. The command processes all text indexes for the table:

dbzts reset pending for table uc\_007 customer archive for text dbz select from sysibmts.systsaux x253720"

The output is as follows:

|   PK | GLOBALTRANSID                                               | GLOBALTRANSTIME                                                                        |   OPERATIONTYPE |
|------|-------------------------------------------------------------|----------------------------------------------------------------------------------------|-----------------|
|    2 | x' 000000000002215B x' 000000000002215B x' 000000000002215B | x'20081020204612500381000000 x'20081020204612500602000000 x'20081020204612500734000000 |               1 |

- 11. Use incremental to process data from the newly attached partition. update

dbzts "update index uc\_007 idx for text

## Scenario 2: To detach partition for a table with extended text search staging infrastructure

- 1 Alter the table from the partition.

db2 alter table uc 007customer archive detach partition p2O05 into t4p2005

The following message is retuned:

SQL3601W The statement caused one or more tables to automatically be placed in the Set Integrity Pending state. SQLSTATE-01586

- 2 Issue the RESET PENDING command to perform integrity processing for the text search staging tables

dbzts "reset pending table uc\_007 customer\_archive for text for

Use incremental to process data from the newly detached partition. update dbzts "update index uc\_007 idx for text"

## Clearing text search index events

If you no longer need the messages in the event view of an index, You can clear (delete) them:

## Before you begin

details, including authorization requirements, see the description for the CLEAR EVENTS FOR INDEX command or the SYSTS\_CLEAR\_EVENTS procedure: For

## About this task

Information about indexing events, such as the start and end times, the number of indexed documents, or document errors that occurred during the update, are stored in the event view of a text search index This information can help you determine the cause of a problem. update

## Procedure

To clear the event view of a text search index, use one of the following methods:

- Run the dbzts CLEAR EVENTS FOR INDEX command, as follows: dbzts "CLEAR EVENTS FOR  INDEX index-name FOR TEXT"
- Use the SYSPROC.SYSTS\_CLEAR\_EVENTS administrative SQL routine, as follows:
- CALL SYSPROC. SYSTS\_CLEAR\_EVENTS ( index-schema

```
index-name locale" 2)
```

## Altering a text search index

You can alter the properties of a text search index update

## Before you begin

For details, including authorization requirements, see the description for the ALTER INDEX command or the SYSTS\_ALTER procedure:

## Procedure

To alter an index, use one of the following methods:

- Run the following command: dbzts "ALTER INDEX index-name FOR TEXT update-characteristics"

Where update-characteristics is a characteristic such as the frequency of the text search index update

- Call the SYSPROC.SYSTS\_ALTER administrative SQL routine: CALL SYSPROC.SYSTS\_ALTER( 'dbzts myText Index 'alter-option 'en US ' 2)

Where alter-option is a characteristic such as the frequency of the text search index update

## Results

The text index properties are updated with the new values, except if the text search index is locked by another operation, in which case an error message is displayed, informing you that the text search index is currently locked and that no changes

## Example

You can use either method to change both the frequency of a text search index and the minimum number of changes required to trigger an update: (If you do not specify any parameters, the current are left unchanged.) For example, to change the update frequency for the text search index MYTEXTINDEX update settings

sO that it is from Monday to Friday at 12 noon and 3 p.m , provided that at least 100 changes have occurred to the indexed column, issue the following command: updated dbzts "ALTER INDEX MYTEXTINDEX FOR TEXT UPDATE FREQUENCY d(1,2,3,4,5) h(12,15) m(00) UPDATE MINIMUM 100"

To stop the periodic updating of MYTEXTINDEX, issue the following command: dbzts "ALTER INDEX MYTEXTINDEX FOR TEXT  UPDATE FREQUENCY NONE"

## Viewing text search index status

To information about the current text search indexes within a database, you can query the administrative views or use the Administration Tool. get

## About this task

Text search index properties can be viewed in the SYSIBMTS TSINDEXES administrative view. For example, to list all text search indexes with their status, issue the following query:

dbz "select indschema indname indstatus from SYSIBMTS. TSINDEXES"

To check the status of all text search collections and their properties the Administration Tool, use the following command: using adminToo] status -configPath absolute-path-to-config-folder

## Changing the location of a Dbz Text Search collection

You might need to change the location of a collection, for example, for computer and disk administration and maintenance purposes.

## Before you begin

You can change the location of a text search collection only when the collection location in the SYSIBMTS. TSINDEXES table is empty:

## About this task

To change the location of a collection:

## Procedure

- 1. Verify that the collection location is empty dbz select indschema indname co]lectiondirectory , co] lectionnameprefix from sysibmts.tsindexes'
- 2. If the targeted collection has no directory information, the Db2 Text Search server: stop
- 3 Edit the collection configuration col lection.xm] file: The default location of the collection configuration file is &lt;ECMTS\_HOME |configlcol ections| &lt;collection\_name&gt;Icol lection.xm] .
- a Specify the location of the index data.
- &lt;indexes&gt;
- &lt;index&gt;
- &lt;type Text&lt;/type&gt;
- b Specify the location of the synonym configuration.

- &lt;indexes&gt;
- &lt;index&gt;
- &lt;type Synonym&lt;/type&gt;

## Note:

- Escape characters as required in XML. For example, escape a backslash character (the default separator on Windows) by "| path using
- If the collection configuration and index data is located in the collection directory, can specify a path that is relative to the location of the co] lection.xm] file, for example: you
- &lt;indexes&gt; &lt;index&gt; &lt;type Synonym&lt;/type&gt; &lt;pathzdata/text&lt;/path&gt;
- 4
- 5. Restart the Db2 Text Search services:

## Backing up and restoring text search indexes

## Procedure

- To back up a database with Db2 Text Search indexes:
- 1.
- Get a current list of text index locations for Db2 Text Search indexes. dbz select indschema \_ indname\_ co]lectiondirectory, collectionnameprefix from sysibmts.tsindexes
- If a value for collectiondirectory is not specified, then locations are set using the defaultDataDir parameter:
- 2 Ensure that no Db2 Text Search administrative command is running:
- 3\_ the Db2 Text Search services:
- dbzts stop for text Stop
- 4. Back up the database: Issue the following command: db2 backup database db\_name
- 5. Back up the text search configurations, index directories and subdirectories.
- 6. Restart Db2 Text Search services:
- To restore database with Db2 Text Search indexes:
- 1. Make sure that no Db2 Text Search administrative command is running:
- 2. the Db2 Text Search services: Stop
- dbzts stop for text
- 3\_
- Restore the database. Issue the following command:
- db2 restore database db\_name
- 4. Restore the backup of text search configuration and index locations to the same as before: path
- 5. Restart Db2 Text Search services\_ dbzts start for text

## Dropping a text search index

When you no longer intend to perform text searches in a text column, you can drop the text search index

## Before you begin

details, including authorization requirements, see the command description for DROP INDEX or the procedure SYSTS\_DROP For

## About this task

When you a text search index, the following other objects are also dropped: drop

- Index staging and event tables
- Triggers on the user table

If the text search index has associated schedule, make sure no task is running: Otherwise the scheduled task may need to be removed manually: an

Always the text search indexes a table before dropping table space: If you table spaces that contains text search indexes, you may create what is called orphaned collection. When you create a text search index, a collection (the file representation of the index) is created with an automatically generated name. If the collection remains after the index has been dropped, it can lead to problems with future queries if the following are also true: drop on drop an system

- table is created with the same table name,
- the same database connection is used, being
- text index with the same name as before is created this table, and on
- the same query is reissued as before:

In this case, a cached query plan might be reused, which could result in query result: wrong

The dbzts CLEANUP FOR TEXT command can only obsolete collections and relevant text index catalog records. Administration Tool can be used to remove orphaned collections in this case drop

If you plan to a database that is enabled for text search, make sure all text search indexes are dropped to avoid orphaned collections. drop

## Procedure

To a text search index, use one of the following methods: drop

- Issue the DROP INDEX command:
- dbzts "DROP INDEX index-name FOR TEXT
- Call the SYSPROC.SYSTS\_DROP stored procedure: CALL SYSPROC. SYSTS\_DROP( ' index-schema index-name locale' = 2)

Where locale is the five-character locale code, such as en\_ US, that specifies the language in which messages will be written to the file: log

## What to do next

Note: If any orphaned collections exist after a text search index, you can remove them the Administration Tool: drop you using new one on the same text column, you must first disconnect from and then reconnect to the database:

## Sample: Scheduling a Db2 Text Search index update

Schedule a Db2 Text Search index and verify execution result update

## Before you begin

Complete the following tasks before you start any scheduler jobs:

- 1. Set the ATS\_ENABLE registry variable
- 2 Check that the SYSTOOLSPACE table space exists
- 3. Ensure that the database is activated

For details about the prerequisites for scheduling a Db2 Text Search index update, see the topic about setting up the administrative task scheduler:

## About this task

Create a scheduler task using the Db2 Scheduler and execute the task in the specified frequency

## Procedure

- 1 Create a text search index and specify the frequency: dbzts create index simix for text on simp]e(comment) update frequency (D(*) H(*) M(30) ) " update
- 2\_ Connect to your database:
- dbz connect to testdb
- 3\_ Find the scheduler task name
- dbz "select indexidentifier from sysibmts tsindexes
- For the following steps, lets assume the numeric part of the index identifier is 12345. So, the scheduler name is TSSCH\_12345.
- 4\_ Find the scheduler task in the SYSTOOLS.ADMIN\_TASK\_LIST administrative view.
- dbz "select from systools.admin Tist" task\_
- 5
- Verify text index status\_ dbz "select from sysibmts.tsevent\_123456" update
- 6. If no message is shown, but data was available for an update, verify that the scheduler task was started:
- dbz "select from systoo]s.admin task status

Otherwise, use the scheduler task name to restrict the SELECT operation to the data belonging to the new scheduler task for the example shown previously:

dbz "select from systoo] s.admin\_task\_status where name

## Chapter 8. Searching with text search indexes

After you populate a text search index with data, you can search that index Db2 Text Search supports searches in SQL, XQuery, and SQL, XML.

You can use the following search functions:

- The SQL function CONTAINS and the XML function xmlcolumn-contains, to create queries for specific words or phrases
- The SQL function SCORE, to obtain the relevancy of a found text document

Searches on text search indexes can range from the simple, such as queries for the occurrence of a single word in title, to the complex, such as queries that use Boolean operators or term boosting: In addition to the operators that allow you to refine the complexity of your search, features such as synonym dictionaries and linguistic support can enhance searches on text search indexes.

## Search functions for Db2 Text Search

After you a text search index, you can search using the CONTAINS or SCORE SQL scalar search function or using the xmlcolumn-contains function: update

Searches on text search indexes can range from the simple, such as queries for the occurrence of a single word in title, to the complex, as queries that use Boolean operators or term boosting: In addition to the operators that allow you to refine the complexity of your search, features such as synonym dictionaries and linguistic support can enhance searches on text search indexes. such

You can use the following search functions:

- The SQL function CONTAINS and the XML function xmlcolumn-contains, to create queries for specific words Or phrases
- The SQL function SCORE, to obtain the relevancy of a found text document

The scalar text search functions, CONTAINS and SCORE, are seamlessly integrated within SQL You can use the search functions in the same places that you would use standard SQL expressions within SQL queries. The SQL SCORE scalar function returns an indicator of how well the text documents matched a given text search condition. The SELECT of the SQL query determines which information is returned to you: phrase

The CONTAINS function searches for matches of a word or phrase and can be used with wildcard characters to search for substring matches in a manner similar to the SQL LIKE predicate and can search for exact matches in a manner similar to the SQL operator: However; there are distinctions between the CONTAINS function and using the SQL LIKE predicate or the operator: The LIKE predicate and the operator search for patterns in document, while CONTAINS uses linguistic processing: that is, it searches for different forms of the search term: For example, even without wildcard characters, searches for the term work also return documents containing working and worked. Moreover, you can add synonym dictionary to the text search index, increasing the scope of a search: For example, you can group Taptop and ThinkPad together s0 are string key using using they

returned from searches for notebook computers For XML documents, the XML search argument syntax allows you to search for text inside tags and attributes As well, XQuery searches are case sensitive:

Note that the Db2 optimizer estimates how many text documents can be expected to match CONTAINS predicate and how costly different access plan alternatives will be: The optimizer chooses the cheapest access plan.

The function xmlcolumn-contains is a built-in Db2 function that returns XML documents from Db2 XML data column based on a text search performed by the Db2 Text Search engine. You can use xmlcolumn-contains in XQuery expressions to retrieve documents based on search of specific document elements For example, if your XML documents contain product descriptions and prices for toys that you sell, you can use xmlcolumn-contains in an XQuery expression to search the description and elements and return only the documents that have the term outdoors but not poo] and cost less than $25.00. price

There are distinctions between the xmlcolumn-contains function and the XQuery contains function: The XQuery contains function searches for a substring inside a it looks for an exact match of the search term or The XQuery xmlcolumn-contains function, however, has similar functionality to the CONTAINS function, except that it operates on XML columns only As well, it returns XML documents containing the search term or phrase, whereas contains returns only a value such as 1, 0, or NULL to indicate whether the search term was found: key using string; phrase.

## Full-text search methods

You can use an SQL statement or XQuery to search through text search indexes

## Procedure

To search a text search index for a term or phrase, use one of the following methods: specific

- Search with SQL.

To search a text search index for a term or with an SQL statement; use the CONTAINS function as follows: specific phrase dbz "SELECT column-name FROM table-name WHERE   CONTAINS (

example, the following query searches the PRODUCT table for the names and prices of various snow shovels: For dbz "SELECT NAME , PRICE FROM PRODUCT WHERE   CONTAINS (NAME \_ snow shovel" ' )

- Search with XQuery

To search a text search index for a specific term Or phrase XQuery, use the db2-fn xmlcolumn-contains() function: using example, the following query searches the PRODUCT table for the names and of various snow shovels: For prices

dbz xquery for |Sinfo in db2-fn:xmlcolumn-contains PRODUCT . DESCRIPTION ' snow shovel " ' return &lt;result&gt; {ISinfo/description/name ISinfo/description/price} &lt;/resultz"

Note: Depending on the operating system shell that you are you might need different escape character in front of the dollar sign of the variable information. The previous example uses the backward slash ) as an escape character for UNIX operating systems. using'

## Basic search

You can use boolean operators and modifiers in your search queries. The more specific the search term that you use, the more the results. precise

## Example

Example 1: Searches for documents that contain the terms 'wizard' and 'dragon'. The default operator is AND if there is no boolean operator specified. explicit select title from books where contains(story, 'dragon wizard' )-1

Example 2: Searches for documents that contain the phrase 'dragon wizard'. It will not include documents that contain for example, the term 'dragons'.

select title from books where contains(story, "dragon wizard")-1

Example 3: Searches for documents that contain the term 'dragon' and optionally the term 'wizard'. Documents that contain both terms will receive a higher score select title from books where contains(story, dragon %wizard' )=1

Example 4: Searches for documents that contain the terms 'dragon' or 'wizard' , but not the term 'hobbit' .

select title from books where contains(story, (dragon OR wizard) NOT   hobbit' )=l

Example 5: Searches for documents that contains synonyms of your query terms by the synonyms dictionary: using select title from books where contains(story, 'dragon wizard SYNONYM-ON ' ) =1

## Fuzzy search

Use a search to find documents that contain words with similar spelling to the term that you are searching: fuzzy search query searches for character sequences that are not only the same but similar to the query term. Use the tilde (~) at the end of a term to do a search: For example, the following query finds documents that include the terms analytics, analyze, analysis, and so on\_ fuzzy symbol fuzzy

analytics~

You can add an optional parameter to specify the degree of similarity of the search results to the search term: Specify value greater than or equal to 0 and less than 1\_ You must precede the value by a 0 and a decimal point, for example, 0.8. A value closer to 1 matches terms with higher similarity: If you do not specify the parameter; the default is 0.5.

analytics~0.8

You can search on a term but not on a phrase: To apply search to multiple words in a query you must apply a search factor for each term\_ For example, the following query finds documents that include terms that are similar to summer and time: fuzzy fuzzy fuzzy

time~0.7

## Example

1. Create a table called BOOKS: create table books isbn varchar(18) not null primary author varchar(30) story varchar(100) , year integer) = Step 2. Create a text search index on the STORY column: dbzts create index bookidx for text on books(story) connect to test Step 3. Import data into the table: insert into books values ( '0-13-086755-1 ' John The Bue Can 2001) insert into books values ('0-13-086755-2 Mike Cats and Dogs 2000) insert into books values ('0-13-086755-3 Peter' Hats on the Rack 1999) insert into books values ('0-13-086755-4 Agatha Cat among the Pigeons 1997) insert into books values ('0-13-086755-5 Edgar Cars Un] imited 2010) insert into books values ('0-13-086755-6 Roy " Carson and Lemon 2008) 4. Update the text search index: dbzts update index bookidx for text connect to test 5. Issue search with the CONTAINS function: select author, year, story from books where contains(story, 'cat~0.4' ) = 1 The following is the sample output: AUTHOR  YEAR STORY John 2001 The Blue Can Mike 2000 Cats and Dogs Agatha 1997 Cat among the Pigeons 3 record(s) selected. To see the associated score, issue the following query that is modified for increased fuzziness: select author, year, story, integer(score(story cat~0.3 ')*1000) as score from books where contains(story, cat~0.3 ') 1 order by score desc The following is the sample output: AUTHOR  YEAR STORY SCORE Agatha 1997 Cat among the Pigeons 32 John 2001 The Blue Can 17 Mike 2000 Cats and Dogs 17 Peter 1999 Hats on the Rack 1 Edgar 2010 Cars Unl imited Step key , Step fuzzy Step

5 record(s) selected.

## Restrictions

- Special characters are not supported in search queries. fuzzy
- If you include wildcard characters in the search terms, only the wildcard search is done: fuzzy
- Terms in fuzzy search queries do not go through language processing (lemmatization, synonym expansion, and stop word removal): Therefore, search queries do not find terms that are similar to synonyms. fuzzy

## Proximity search

A proximity search retrieves documents that contain search words which are located within a specified distance from each other:

To start a proximity search use the tilde symbol at the end of a and specify the distance in words as valid integer number: When determining the distance consider that sentence breaks count as 10 position increments. Special characters are not supported in proximity search queries phrase

## Example

1. Create table called BOOKS: create table books isbn varchar(18) not primary author varchar(30) story varchar(100) , year integer) = Step 2 Create text search index the STORY column: dbzts "create index bookidx for text on books (story) connect to test" ; 3\_ Import data into the table: insert into books values ( '0-13-086755-1 ' John Understanding Astronomy\_ 2001) insert into books values ('0-13-086755-2 ' Mike The cat hunts some mice\_ 2000) insert into books values ( '0-13-086755-3 ' Peter' Some men were standing beside the table\_ 1999) insert into books values ('0-13-086755-4 ' Astrid' The outstanding adventure of Pippi Longst \_ 1997 ) insert into books values ('0-13-086755-6 ' Agatha Cat among the pigeons 2004) insert into books values ('0-13-086755-7 ' John Pigeons Tand in the square and cat plays with ba] 1 2001) insert into books values ('0-13-086755-8 ' Sam' Pigeon on the roof 2007) Step 4. Update the text search index: dbzts update index bookidx for text connect to test" Step key, on Step

Issue a proximity search for the terms cat and pigeon within 4 words of each other in document and use the following search syntax within the Db2 Text Search CONTAINS phrase:

select author, year substr(story,1,30) as title from books where contains(story, cat pigeon"~4' 1

## Searching for special characters

Special characters, such as common punctuation characters, are indexed as of a text You can search for characters the same way as you search for other query terms part update. special

To find character in document; include the character in the query expression. In some cases, you might have to escape characters. special special special

You cannot search for an exact match on two consecutive, identical special characters. Queries of this type return documents that contain only one of the special characters.

## Escaping special characters

Special characters can serve different functions in the query syntax

To search for a special character that has a special function in the query syntax, you must escape the special character by adding a backslash before it, for example:

- To search for the string 'where?"\_ escape the question mark as follows: 'where
- To search for the string "c: | temp; escape the colon and backslash as follows: temp'

Not escaping such characters can result in syntax errors\_ special

Table 3. Special characters that must be escaped to be searched

| Special character                        | Notes on behavior when not escaped                                                                                                               |
|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Ampersand                                |                                                                                                                                                  |
| Asterisk                                 | Used as wildcard character                                                                                                                       |
| At sign                                  | A syntax error is generated when an at sign is the first character of a query In expressions, the at sign is used to refer to an attribute xmlxp |
| Brackets [ ]                             | Used in xmlxp expressions to search the contents of elements and attributes:                                                                     |
| Braces                                   | Generates syntax error:                                                                                                                          |
| Backslash                                |                                                                                                                                                  |
| Caret                                    | Used for weighting (boosting) terms                                                                                                              |
| Colon                                    | Used to search in the contents of fields                                                                                                         |
| Equal sign (=)                           | Generates syntax error                                                                                                                           |
| Exclamation point                        | A syntax error is returned when an exclamation point is the first character of a query:                                                          |
| Forward slash                            | In expressions, forward slash is used as an element separator: xmlxp path                                                                        |
| Greater than symbol (>) Less than symbol | Used in xmlxp expressions to compare the value of an attribute. Otherwise, these characters generate syntax errors.                              |
| Minus sign (-)                           | When minus sign is the first character of a term, only documents that do not contain the term are returned_                                      |
| Parentheses                              | Used for grouping:                                                                                                                               |
| Percent sign %                           | Specifies that a search term is optional.                                                                                                        |
| Plus sign                                |                                                                                                                                                  |
| Question mark (?)                        | Handled as wildcard character:                                                                                                                   |
| Semicolon                                |                                                                                                                                                  |
| Single quotation mark ()                 | Single quotation marks are used to contain xmlxp expressions                                                                                     |
| Tilde                                    | Handled as proximity and search operators fuzzy                                                                                                  |
| Vertical bar                             |                                                                                                                                                  |

Escaping special characters that do not serve a special function in the query syntax is The following table shows some examples of special characters that do not require escaping: optional

Table 4. Examples of special characters that do not require escaping

| Special character   | Notes                                                                     |
|---------------------|---------------------------------------------------------------------------|
| Comma               |                                                                           |
| Dollar sign         |                                                                           |
| Period              | In expressions, a period is used to search the content of elements: xmlxp |
| Pound sign          |                                                                           |
| Underscore          |                                                                           |

## Special characters adjacent to query terms

When a character is adjacent to word in query, documents that contain the special character and word in the same order are returned\_ special

For example, searching for "30S" finds documents that contain "30S" but does not find documents that contain "S30". However; searching for "30 $" (with a space) finds all documents that contain "30" and "S" anywhere in the documents including both "30S" and "$30".

When a character is adjacent to word in a query, the word is not removed from the query: For example, searching for at&amp;t" does not remove the word "at". However; searching for "at &amp; t' with spaces removes the word at"\_ special stop stop stop stop

When a character separates two words, the sequence of tokens is searched as sequence: For example, searching for "jack\_jones' finds documents that contain "jack\_jones' but not documents that contain "jack\_and\_jones" special

Words that are adjacent to special characters are lemmatized. For example, searching for "catskdogs" in English finds documents that contain "catkdog"

You can use special characters in wildcard search expressions For example, searching for "ja finds documents that contain "jack\_jones". However, cannot use wildcard characters to find special characters. For example, searching for ca*s finds documents that contain cats, categories, cast-members, Or cas, but not documents that contain ca\_S. you

## Indexing special characters

During tokenization and language processing, Db2 Text Search identifies and indexes characters as punctuation: special

Special characters are token delimiters. For example, "jack\_jones' is tokenized as three separate tokens: "jack" , and "jones" Emails, URLS, and file are broken down into tokens For example: paths

- Jack\_jones@ibm com is tokenized as jack jones ibm com
- [www.ibm.com is tokenized as http WWW ibm com

Special characters do not occupy token position in the file: For example, "jack\_jones" is indexed with the underscore in the same token position as "jack".

Special characters also do not occupy a token position when spaces are included: For example, "jack\_jones" is indexed in the same as "jack jones' way

The token position is used for exact phrase search and for proximity search. For example, if a document contains the expression jack\_jones, searching for the exact "jack jones' finds this document. phrase

When sequence of special characters are indexed separately, are searched in no particular order: For example, searching for '#S' also finds documents that contain "S#' they

## Special characters in CJK languages

To find sequence of characters that includes characters in a Chinese, Japanese or Korean (CJK) document, the query expression must include the characters. This is different to non-CJK languages, where a whitespace can substitute for a special character: special special

If a document is mixed language, for example, a Chinese language document contains some English terms, a search with whitespace will still substitute for special characters for the non-CJK terms\_

For example, if an indexed document contains john\_smith, you can search for john\_smith or "john smith" (exact match, without the underscore) and both queries return the document that contains john\_smith:

Note: The characters ? and have semantic meaning as wildcards and escape character; but are not searchable as characters. special

## Structural full-text search in XML documents

Db2 Text Search supports using XML search for searching XML documents\_

By subset of the XPath language with extensions for text search, XML search indexes and searches XML documents. You can use structural elements names, attribute names, and attribute values) separately or combine them with free text in queries. using (tag

The following search features are supported by XML search:

- Boolean operators (basic search)
- Exact match
- Fuzzy search
- Proximity search
- words Stop
- Synonyms
- Wildcard characters

In addition to the search features previously listed, XML search also includes the following features: key

## XML structural search

By XML search syntax in text search queries, you can search XML documents for structural elements names, attribute names, and attribute values) and text that is scoped by those elements. Note that plain searches do not search the attribute field in an XML document: using (tag

## XML query tokenization

The text that is used in the XML search predicate expression as XML query terms is tokenized the same way that text in non-XML query terms is tokenized, except that spelling corrections, fielded terms, and nested XML search terms are unsupported  Synonyms, wildcard characters, phrases, and lemmatization are supported.

## Disregarding of XML namespaces

Namespace prefixes are not retained in the indexing of XML and attribute names\_ You can index and search XML documents by declaring and namespaces, but namespace prefixes are discarded indexing and removed from XML search queries tag during using

## Numeric values

Predicates comparing attribute values to numbers are supported.

## Complete match

The operator (equal sign) with a string argument in a predicate means that a complete match of all tokens in the string with all tokens in the identified text span is required, with the order significant: being

The subset of XPath that is implemented in XML search differs from standard XPath in the following ways:

- It does not support iteration and ranges in expressions. path
- It disallows absolute names in predicate expressions. path
- It eliminates filter expressions: that is, it allows filtering only in the predicate expression, not in the expression: path
- It implements only one axis (tag) and allows propagation only in the forward direction:

The following table lists some valid XML search queries.

Table 5. Valid XML search queries

| Query          | Description                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------|
|                | The root node; any document                                                                     |
| Isentences     | document with top-level tag of sentences Any                                                    |
| sentences      | document with tag at any level of sentences Any                                                 |
| sentences      | document with tag at any level of sentences Any                                                 |
| paragraph      | document with top-level tag of sentences having a direct child tag of paragraph Any             |
| paragraph /    | document with top-level tag of sentences having direct child of paragraph Any tag               |
| @author        | document with top-level book tag having an attribute author Any                                 |
| Ibook/ @author | document with a top-level book tag having descendant at any level with attribute author Any tag |

Table 5. Valid XML search queries (continued)

| Query                                                                                            | Description                                                                                                                                                                     |
|--------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| /book[@author contains("barnes") and @title contains("lemon")]                                   | document with top-level book tag with the attributes author and title with values that contain the normalized shown Any strings                                                 |
| /book[@author contains( "barnes") and (@title contains("lemon") or @title contains("flaubert"))] | document with top-level book tag with the specified author attribute and either of the specified title attributes Any two                                                       |
| Iprogram[. contains(' 'hello, world_ )                                                           | document with top-level program tag containing at least the tokens hello and world Any                                                                                          |
| /book[paragraph contains("flaubert")]/ / sentence                                                | document with a top-level tag book tag with direct child tag of paragraph containing "flaubert" and, referring to the book having descendant tag sentence at any level Any tag, |
| /auto[@price <30000]                                                                             | document with top-level auto tag an attribute price with a numeric value that is less than 30000 Any having                                                                     |
| microbe[@size <3.0e-06]                                                                          | document containing microbe tag at any level with a size attribute with value that is less than 3.0e-06 Any_                                                                    |

Note: The following characters are unsupported in the XML search syntax:

plain search does not search the attribute field in the XML document

## Searching text search indexes using SCORE

You can use the SCORE function to find out the extent to which a document matches a search argument:

## About this task

SCORE returns double-precision floating-point number between 0 and 1 that indicates how well document meets the search criteria: The better a document matches the query, the more relevant the score and the larger the result value:

The score is calculated dynamically based on the content of a text index collection at the time of the query and is therefore only meaningful for a non-partitioned text index

Scoring algorithms may differ for different text index formats or query types Note that deleted documents impact the relative value returned by SCORE until are removed from the text search index: However; significant differences in scores would be observed only when chunks of data have been deleted from the index they large

## Example

To search in the SAMPLE database for the number of employees who indicated on their resumes that know how to program in Java or COBOL, YOu can issue the following query: they

SELECT EMPNO \_ INTEGER (SCORE (RESUME , programmer AND (java OR cobol ) ' ) 100) AS RELEVANCE FROM EMPRESUME WHERE RESUME  FORMAT ascii ORDER BY RELEVANCE DESC

However; the following query CONTAINS is superior: The Db2 optimizer evaluates the CONTAINS predicate in the WHERE clause first and thereby avoids that this is possible only if the SCORE and CONTAINS arguments in the query are identical: using

SELECT EMPNO , INTEGER (SCORE (RESUME , programmer 100) AS RELEVANCE FROM EMP\_RESUME WHERE RESUME\_FORMAT ascii AND   CONTAINS (RESUME = programmer 1 ORDER BY RELEVANCE DESC

## Dbz Text Search argument syntax

A search argument comprises one or more terms and optional search parameters, separated by white space, that you specify to search text documents.

When you specify term, the search engine returns documents that contain that term and, by default, variations on that term For example, if you search by the term documents containing king and kings are returned. If you search by multiple terms, the search engine returns only documents containing all the terms using king, using

If you want to search by an exact phrase, surround the phrase in quotation marks. Use a search to find documents that contain words with spelling similar to that of the search term: A common reason to perform search is to include documents that contain misspellings in the search result using fuzzy fuzzy

Perform a proximity search to retrieve documents containing search words that are located within a specified distance from each other:

## Remember:

- Searches are not case sensitive, sO search in Spanish for the exact term "DOS" might return documents containing DOS or dos.
- Text search queries must not exceed Db2 SQL query limits.

The more specific the search term that you use, the more precise the results However; you can also refine your searches by options such as the following ones: using

## Boolean operators

Use the AND operator to search for documents that contain all the specified terms The AND operator is the default conjunction operator: If there is no logical operator between the two terms, AND is used.

Use the AND operator to search for documents that contain all the specified terms The OR operator links the two or more terms and finds a matching document if either of the terms exists in document:

## Occurrence modifiers

Use a plus sign (+) to specify that terms are required  The plus sign modifier is distinct from the AND operator because the plus sign (+) modifier indicates that the second term must be an exact match: No synonym is used:

Use a minus sign (-) or the NOT modifier to specify that terms are prohibited.

## The boost modifier

Use the caret character to give higher importance to occurrences of a particular term: The caret (^ character provides a boost to the term or phrase that precedes it when the specified number is greater than 1. If you want to reduce the ranking of the term or phrase in the returned list, specify number that is greater than 0 but less than 1.

## Wildcard characters

Use a question mark (?) to specify that a single character can be added to your search term. Use an asterisk (*) to specify that any number of characters can be added to your search term. Use these wildcard characters to search terms and data for spelling variations and increase search scope:

Important: Using the asterisk wildcard at the beginning of a search term negatively affects the performance of the search query:

Wildcard searches with an asterisk apply a term expansion to find documents. If the number of matching terms in the text index collection exceeds the expansion limit, only a subset of documents that match the Also, wildcard searches find regular characters, not special characters For example, searching for US-*-abc finds strings such as US-xxx-abc US-X-abc, and US-x#-abc but not US-#-abc.

## The percentage sign (%)

Use a percentage sign (%) to specify that a term or phrase is optional.

## The backslash ( |) escape character

Use a backslash (1) to include special characters in your search: All of the following characters are characters in text search queries: special

- %

## Double quotation marks

Use quotation marks ') around your search term or phrase to have only exact matches returned

## Parentheses

Use parentheses to have search terms and the relationship between them treated as single item.

For XML search queries that are sent to the XML parser; write the queries by opaque terms in subset of the XPath language The query parser recognizes an opaque term by the syntax that you use in the query: using

For any language-specific processing during a search, a locale is assumed for the search-argument parameter: This query language is the locale of the text search index that is used when you perform the search function.

The search argument syntax is as follows:

Search argument

QualifiedClause ((Operator) (QualifiedClause))

## Operator

AND OR

## QualifiedClause

(Modifier) Clause (^number)

Modifier

NOT

Clause   Unqualified term opaque term

- An unqualified term is a term or a term can be a word, such as king; an exact word, such as king' or word that includes a wildcard, such as king* or king?. Similarly, a phrase can be a group of words, such as cabbages and kings; an exact phrase, such as The King and I or a phrase that includes wildcard, such as al1 the king" S hx or a]1 the kin? S horses. phrase.
- An opaque query term is not parsed by the linguistic query parser; opaque terms are identified by their syntax The opaque term that is used for text search queries is @xpath, for example, @xpath: ' /Taga/ TagB [ . contains("king")]

## Examples

Table 6. Boolean operators

| Operator                   | Example                                                                                                                               | Query results   |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| ANDKing AND Lear Lear King | Returns documents that contain the terms and Lear. If you enable synonym dictionary; words such as monarch can also be returned_ King |                 |

Table 6. Boolean operators (continued)

| Operator   | Example           | Query results                                             |
|------------|-------------------|-----------------------------------------------------------|
| OR         | Hamlet OR Othello | Returns documents that contain either Hamlet or Othel Io. |

Table 7. Occurrence modifiers

| Modifier   | Example   | Query result                                                                                                    |
|------------|-----------|-----------------------------------------------------------------------------------------------------------------|
| NOT        |           | Returns documents that contain Hamlet but not Othel Io.                                                         |
|            | Lear King | Returns documents that contain the terms Lear and King: Documents containing Lear and monarch are not returned. |

| Modifier                                 | Example                    | Query result                                                                                                                                                                                                                                                                         |
|------------------------------------------|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| terml or phrasel^number term2 or phrase2 | Hamlet^2 Hamlet Othello^.5 | Returns documents containing Ham]et and Othel lo but gives more importance to the term Hamlet. In both example queries, each occurrence of the term Hamlet is given twice as much importance as each occurrence of Othel 1o is given.                                                |
|                                          | king* *ing k*ng            | Returns documents that contain possible combinations of the search term with the wildcard character: The example query might return results such as and kingdom in the first example, and kissing in the second example, and king and skiing in the third example king king          |
|                                          | WWW com                    | Searching wildcards not return terms that contain special characters. The example query might return WWW ibm. Com but does not return WWW . # com_ using does                                                                                                                        |
|                                          | mea? be?n ?ean             | Returns documents that contain possible combinations of the search term with the wildcard character: The first example returns results such as mea] and mean, the second example returns results such as bean and been, and the third example returns results such as mean and bean_ |
|                                          | King James %Edition        | Returns documents that contain both and james, but edition is an term _ king optional                                                                                                                                                                                                |

Table 8.

| Modifier                                   | Example                                          | Query result                                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------------------|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 'phrase" exact term 'phrase with wildcard" | "King Lear" "king" John Kennedy' John ? Kennedy" | Returns documents that contain the exact word or phrase. The first The second example returns the word king and no other forms, such as kings or kingly. You can use quotation marks with wildcards _ The third example returns occurrences of John Kennedy with or without various middle names or initials_ The fourth example returns John initial Kennedy. |
|                                            | (Ham]et OR Othel 1o) AND plays                   | Returns documents that contain the following terms: The term Hamlet or Othello The term plays                                                                                                                                                                                                                                                                  |
|                                            | (11+11)|:2                                       | Returns documents that contain (1+1).2. Use the backslash character to escape characters that are of the query syntax special part                                                                                                                                                                                                                             |

## Search syntax for XML documents

Using an XML search expression, you can use the Db2 Text Search engine to search specific portions of an XML document in Db2 XML column:

## Syntax

XML

search

query |

## XML search query:

F location-path

## @xm]xp:

The keyword that starts a text search query on an XML document:

Note: The keyword @xpath has been deprecated:

## XML search query

A text search query used by Db2 Text Search to search XML documents. The query is enclosed in single quotation marks. The XML search query is an XML search expression that consists of a location specifying the portion of the XML document to search and an optional predicate that specifies the search criteria. path

## location-path

An XML search expression that uses a subset of the XPath abbreviated syntax to specify an XML document node or attribute. More information is provided in the "Location section: path"

## search-predicate

The optional search criteria used by Db2 Text Search when searching an XML document: More information is provided in the "Search predicate" section:

The Db2 Text Search engine returns the XML document if it finds the text specified in the search-predicate in the specified nodes or attributes of the XML document:

## Location path

When performing a text search on an XML document, Db2 Text Search uses local node and attribute names and subset of the XPath syntax to specify nodes and attributes in an XML document: Db2 Text Search supports the following XML search elements:

- Local node or attribute names
- (period) as the current context node
- or as the separator character
- as the abbreviated for attribute symbol
- Name normalization

XML node and attribute names are not normalized when are indexed for use by the Db2 Text Search engine: are not converted to lowercase, tokenized, or modified in any way: Case is significant in XML node and attribute names, SO the strings that you use for them in queries must match exactly the names appearing in documents to match: they they get

When creating a text search index, you can use XML documents that contain XML namespace specifiers, but namespace specifiers are not retained in the index. For example, the tag &lt;nsdoc:heading &gt; is indexed under heading only, and the query term @xmlxp:' /nsdoc:heading' is parsed as @xmlxp:' /heading'. XML namespace prefixes are discarded during query parsing:

- Namespace handling

## Examples

The following example is a valid text search query using XML search that searches for the term snow shovel in the description node of product information:

@xm]xp: ' /info/product/description[. contains ( snow shovel ") ]

The following example is a not a valid text search query XML search because it uses the XML search abbreviation for parent:node(): using

@xmIxp: linfolproduct/description/ /@ID[. contains ("A2")]

## Search predicate

## Syntax

<!-- image -->

## search-expression

Db2 Text Search XML search query: Db2 Text Search uses a search expression to search node or attribute values in an XML document:

You can use the following operators to create search expressions:

- Logical operators: AND, OR, and NOT
- Containment operators: contains and excludes
- Comparison operators: =, &gt;, &lt;, &gt;=, and !=

## Note:

Comparison operators can be applied to attribute values only, not node values root&gt; , the following query is invalid:

select id from testtable where contains (i Iroot/aaa[ . 20] ' ' ')&gt;0 tem,

An example of a valid query would be:

select id from testtable where contains(item, Iroot/aaa/@id[. 20] )&gt;0

You can combine the comparison and containment operators with the logical operators AND, OR and NOT to create complex search expressions. You can also use parentheses to group expressions.

Use single or double quotation marks to enclose a string: A string that contains quotation marks cannot be enclosed by the same type of quotation marks. For example, string enclosed in single quotation marks cannot contain a single quotation mark

In XML search predicates, comparison operators take precedence over logical operators, and all logical operators have the same precedence. You can use parentheses to ensure intended evaluation precedence:

Free text in XML documents (text between tags, not inside tag itself) and attribute values are normalized before indexing: Free text in XML queries (in containment operators) is normalized in the same way that it is in non-XML

## Example

The following example uses an XML search query to search for products that contain the term snow shovel in the product description and that have a lower than $29.99. price snow shovel") ) and (@price 29.99) ]]

## Comparison expressions

Comparison expressions compare the value of an attribute with a specified value:

## Syntax

## path-expression

The expression using a subset of the XML search abbreviated syntax to specify node or attribute: path

## operator

The type of comparison to perform: The operator can be one of the following types:

- path-expression value is equal to literal.
- path-expression value is greater than literal.
- path-expression value is less than literal.
- path-expression value is greater than or equal to literal.
- path-expression value is less than or equal to literal.
- path-expression value is not equal to literal.

## literal

A string or number to compare against the path-expression node or attribute value: used

Enclose the string in single or double quotation marks. A string that contains quotation marks cannot be enclosed by the same type of quotation marks. For example, string enclosed in single quotation marks cannot contain single quotation mark Use the backslash character (1) to escape double quotation

If the string contains double quotation marks, you can enclose the string in single quotation marks The following example shows a string containing double quotation marks enclosed in single quotation marks:

he said "Hello, World"

If the a string contains single quotation marks, you can enclose the in escaped double quotation marks. The following example shows a string containing a single quotation mark enclosed in double quotation marks: the cat string

Db2 Text Search features such as phrases, wildcards, and synonyms are not supported in XML search queries:

## Example

The following example uses the operator to find product IDs to the string 100-200-101: equal xmlxp:' /info/product/@pid[. 100-200-101" ]

## Note:

The only comparison operators that are supported with string arguments are and SO operators are supported with numeric arguments Numeric arguments are supported for comparison to attribute values, but not to tag (node) content I+,

## Containment expressions

Containment expressions determine whether the value of a node or an attribute contains a specified value:

## Syntax

```
~path-expression contains (~literal  )excludes
```

## path-expression

The XML search expression that specifies an XML node or attribute:

## contains

An expression that specifies that path-expression value contains literal.

## excIudes

An expression that specifies that path-expression value excludes literal.

## literal

A string used to compare against the path-expression node or attribute value

Use single or double quotation marks to enclose a string: A string cannot contain enclosing quote type: for example, a string enclosed in single quotation marks cannot contain single quotation mark. Use the backslash character

If the contains double quotation marks, you can enclose the string in single quotation marks\_ string

The following example shows a string containing double quotation marks enclosed in Single quotation marks:

he said World"

If the contains single quotation marks, you can enclose the in escaped double quotation marks. The following example shows a containing single quotation mark enclosed in double quotation marks: the cat string string string

## Example

The following example uses the XQuery abbreviated syntax for expressions to specify that the description node excludes the term ice scraper: path

@xmlxp: /infolproduct/description[ . excludes ( 'ice scraper' )]

## Enhancing performance for full-text queries

To enhance performance searches, use one or more of the following approaches: during

## Procedure

- Use the EXPLAIN statement to check the access plan of the Dbz optimizer when searching with SQL.
- Avoid the SCORE function without the CONTAINS function. Also, to and any search options) that you specify for the CONTAINS function exactly matches the string (including white spaces) that you use for the SCORE function. using
- Ensure that the Db2 compiler has the correct table statistics. Use the RUNSTATS command to the statistics. update

- Review the database STMT\_ CONC configuration parameter: When the parameter is set to use the LITERAL option, performance degradation may occur for text search queries.

## Chapter 9. SQL and XML built-in search functions

You can use the following Db2 built-in search functions in Db2 Text Search: The schema of these functions is SYSIBM.

## CONTAINS

Returns a NULL or an INTEGER value of 0 or 1 depending on whether the input text document matches the text search condition

## SCORE

Returns a NULL or DOUBLE value between 0 and 1 indicating the extent to which the text document meets the search criteria.

## xmlcolumn-contains

Returns NULL or an INTEGER value 1 or 0 depending on whether the input text document of XML data type matches the text search condition

## CONTAINS function

The CONTAINS function searches a text search index using criteria that you specify in a search argument and returns a value that indicates whether match is found:

## Function syntax

<!-- image -->

## Notes:

- 1 string-constant must conform to the rules for search-argument-options.

## search-argument-options:

<!-- image -->

## Notes:

- 1 You cannot specify the same clause more than once\_

The schema is SYSIBM:

## Function parameters

## column-name

A qualified or unqualified name of a column that has a text search index that is to be searched. The column must exist in the table or view

identified in the FROM clause in the statement and the column of the table, or the column of the underlying base table of the view, must have an associated text search index (SQLSTATE 38H12). The underlying expression of the column of a view must be a simple column reference to the column of an underlying table, either directly or through another; nested view:

## search-argument

An expression that returns a value that is a value (except a LOB) that contains the terms to be searched for and is not all blanks or the empty (SQLSTATE 42815). The value that results from the expression should be less than or equal to 4096 bytes (SQLSTATE 42815). The value is converted to Unicode before it is used to search the text search index The maximum number of terms per query must not exceed 1024 (SQLSTATE 38H10). string string string

## string-constant

A string constant that specifies the search argument options that are in effect for the function

The options that you can specify as part of the search-argument-options are as follows:

## QUERYLANGUAGE = locale

Specifies the locale that the Db2 Text Search engine uses when performing a text search on a Db2 text column. The value can be any of the supported locales: If you do not specify QUERYLANGUAGE, the default is the locale of the text search index If the LANGUAGE parameter of the text search index is AUTO, the default value for QUERYLANGUAGE is en\_US.

## RESULTLIMIT value

If the optimizer chooses a plan that calls the search engine for each row of the result set to obtain the SCORE, then the RESULTLIMIT option has no effect on performance. However; if the search engine is called once for the entire result set, RESULTLIMIT acts like a FETCH FIRST clause.

When multiple text searches that specify RESULTLIMIT in the same query, use the same search-argument. If you use different search-argument values, you might not receive the results that you expect: using

For partitioned text indexes, the result limit is to each partition separately applied

## SYNONYM = OFF ON

Specifies whether to use a synonym dictionary that is associated with the text search index: The default is OFF. To use synonyms, add the synonym dictionary to the text search index the Synonym Tool. using

OFF Do not use synonym dictionary:

- ON Use the synonym dictionary associated with the text search index

The result of the function is a large integer: If the second argument can be null, the result can be null; if the second argument is null, the result is null. If the third argument is nully the result is as if you did not specify the third argument:

CONTAINS returns the integer value 1 if the document contains match for the criteria specified in the search argument: Otherwise, it returns 0.

CONTAINS is a non-deterministic function:

Note: You must take additional steps when using parameter markers as a search argument inside the text search functions. Parameter markers do not have a type when precompiled in JDBC and ODBC programs, but the search argument in the\_ text search functions must resolve to a value. Because the unknown type of the parameter marker cannot be resolved to a string value (SQLCODE -418), you must explicitly cast the parameter marker to the VARCHAR data type. string

## Examples

- The following query is used to find all of the employees who have COBOL in their resumes. The text search argument is not case-sensitive.
- In the following C program, the exact term ate is searched for in the COMMENT column:
- The following query is used to find any 10 students who wrote online essays that contain the fossi] fuel in Spanish, which is combustible fosin. A synonym dictionary was created for the associated text search index Because only 10 students are needed, the query is optimized by the RESULTLIMIT to limit the number of results from the underlying text search server phrase using option

```
SELECT EMPNO FROM EMP RESUME WHERE RESUME FORMAT ascii AND  CONTAINS (RESUME _ COBOL ' )
```

```
char search_arg[100] ; input host variable */ EXEC SQL DECLARE C3 CURSOR FOR SELECT CUSTKEY FROM  CUSTOMERS WHERE  CONTAINS ( COMMENT , search_arg) ORDER BY CUSTKEY; strcpy(search arg, "ate") ; EXEC SQL OPEN C3;
```

```
SELECT FIRSTNME, LASTNAME FROM STUDENT ESSAYS WHERE CONTAINS (TERM_PAPER, combustible fosi]' QUERYLANGUAGE= es ES RESULTLIMIT
```

## SCORE function

The SCORE function searches a text search index criteria that you specify in search argument and returns document satisfies the query as compared with the other documents in the column. using

## Function syntax

<!-- image -->

## Notes:

- 1 string-constant must conform to the rules for search-argument-options.

## search-argument-options:

<!-- image -->

## Notes:

- You cannot specify the same clause more than once\_

The schema is SYSIBM

## Function parameters

## column-name

A qualified or unqualified name of a column that has a text search index that is to be searched: The column must exist in the table or view identified in the FROM clause in the statement and the column of the table, or the column of the underlying base table of the view, must have an associated text search index (SQLSTATE 38H12). The underlying expression of the column of a view must be a simple column reference to the column of an underlying table, either directly or through another; nested view.

## search-argument

An expression that returns a value that is a string value (except a LOB) that contains the terms to be searched for and is not all blanks or the empty string (SQLSTATE 42815). The string value that results from the expression should be less than or equal to 4096 bytes (SQLSTATE 42815). The value is converted to Unicode before it is used to search the text search index The maximum number of terms per query must not exceed 1024 (SQLSTATE 38H1O).

## string-constant

A constant that specifies the search argument that are in effect for the function: string options

The options that you can specify as part of the search-argument-options are as follows:

## QUERYLANGUAGE = locale

Specifies the locale that the Db2 Text Search engine uses when performing a text search on Db2 text column. The value can be any of the supported locales If you do not specify QUERYLANGUAGE, parameter of the text search index is AUTO, the default value for QUERYLANGUAGE is en\_US.

## RESULTLIMIT value

If the optimizer chooses a plan that calls the search engine for each row of the result set to obtain the SCORE, then the RESULTLIMIT has no effect on performance: However; if the search engine is called once for the entire result set, RESULTLIMIT acts like a FETCH FIRST clause: option

When multiple text searches that specify RESULTLIMIT in the same query, use the same search-argument. If you use different search-argument values, you might not receive the results that you expect: using

For partitioned text indexes, the result limit is to each partition separately: applied

Note: If the number of results is an issue, limit the number of results through refinement of the search terms, rather than by using RESULTLIMIT. Because RESULTLIMIT returns at most the specified number of results with no consideration of their scores, the highest-ranking documents might not be included:

## SYNONYM OFF ON

Specifies whether to use a synonym dictionary that is associated with the text search index. The default is OFF. To use synonyms, add the synonym dictionary to the text search index the Synonym Tool. using

OFF Do not use a synonym dictionary:

- ON Use the synonym dictionary associated with the text search index

The result of the function is a double-precision floating-point number: If the second argument can be null, the result can be null; if the second argument is null, the result is null. If the third argument is null, the result is as if you did not specify the third argument:

The result is greater than 0 but less than 1 if the column contains a match for the search criteria specified by the search argument: The more frequently a match is found, the larger the result value: If the column does not contain match, the result is 0\_

SCORE is a non-deterministic function.

Note: You must take additional steps when parameter markers as a search argument inside the text search functions. Parameter markers do not have type when precompiled in JDBC and ODBC programs, but the search argument in the text search functions must resolve to a string value: Because the unknown type of the parameter marker cannot be resolved to a string value (SQLCODE -418), you must explicitly cast the parameter marker to the VARCHAR data type: using

## Example

- The following query is used to generate a list of employees in order of how well their resumes satisfy the query 'programmer AND (java OR cobol)" , with relevance value that is normalized between 0 and 100: along

```
SELECT EMPNO _ INTEGER (SCORE (RESUME _ programmer AND (java OR cobol ) ') 100) AS RELEVANCE FROM  EMP RESUME WHERE   RESUME_FORMAT ascii' programmer (java OR cobol ) ' ) ORDER BY RELEVANCE DESC
```

## Usage notes

- The SCORE value reflects a document's relative relevance when compared to the SCORE value of all documents from the same text index collection: partitioned database a text index may consist of multiple collections, however document scores are not normalized across partitions Comparing Or sorting SCORE values across text index collections is therefore not meaningful and does not provide proper measure of relevance for documents in a partitioned text index For

## xmlcolumn-contains function

The db2-fn:xmlcolumn-contains function returns sequence of XML documents from an XML data column based on a text search performed by the Db2 Text Search engine for specified search terms.

## Syntax

<!-- image -->

## Notes:

- 1 options-string-literal must conform to the rules for search-argument-options

## search-argument-options:

<!-- image -->

## Notes:

- 1 You can specify each option only once:

## string-literal

Specifies the name of a XML data type column to be searched by db2-fn:xmlcolumn-contains. The value of string-literal is case sensitive and must match the case of the table and column name You must qualify the column name table name or a view name\_ The SQL schema name is optional: If you do not specify the SQL schema name, the value of CURRENT SCHEMA is used\_ using

The column must have a text search index

## search-argument

An expression that returns an atomic value or an empty sequence: The string cannot be all space characters or an empty string: The string must be castable to the type VARCHAR according to the rules of XMLCAST with maximum length of 4096 bytes. string

## options-string-literal

Specifies the search argument options that are in effect for the function:

The options that You can specify as part of the search-argument-options are as follows:

## QUERYLANGUAGE locale

Specifies the locale that the Db2 Text Search engine uses when performing a text search on a Db2 text column. The value can be any of the supported locales: If you do not specify QUERYLANGUAGE, the default is the locale f the text search index If the LANGUAGE parameter of the text search index is AUTO, the default value for QUERYLANGUAGE is en US.

## RESULTLIMIT = value

If the optimizer chooses a plan that calls the search engine for each row of the result set to obtain the SCORE, then the RESULTLIMIT has no effect on performance. However; if the search engine is called once for the entire result set, RESULTLIMIT acts like a FETCH FIRST clause\_ option

When multiple text searches that specify RESULTLIMIT in the same query, use the same search-argument. If you use different search-argument values, you might not receive the results that you expect: using

For partitioned text indexes, the result limit is applied to each partition separatelyFor an example of what might happen when multiple text searches and a solution, see the last example in "Examples" on page 130. using

## SYNONYM OFF ON

Specifies whether to use a synonym dictionary that is associated with the text search index The default is OFF. To use synonyms, add the synonym dictionary to the text search index the Synonym Tool. using

OFF Do not use synonym dictionary:

- ON Use the synonym dictionary associated with the text search index

## Returned values

The returned value is a sequence that is the concatenation of the non-null XML values from the column that is specified by string-literal. The non-null XML values are returned in nondeterministic order: The XML values are the XML documents where the SQL CONTAINS function search-argument for the column specified by string-literal would return 1. If there are no such XML values, an empty sequence is returned: using

If search-argument is an empty sequence, an empty sequence is returned. If search-argument is an empty string or containing all space characters, an error is returned. If the third argument is null, the result is as if you did not specify the third argument: string

If the column that you specify string-literal does not have a text search index , an error is returned: using

The db2-fnxmlcolumn-contains function is related to the db2-fn:sqlquery function, and both functions can produce the same result: However; the arguments of the two functions differ in case sensitivity: The first argument, string-literal, in the db2-fn:xmlcolumn-contains function is processed by XQuery and is case sensitive:

Because table names and column names in a Db2 database are uppercase by default, the first argument of db2-fn:xmlcolumn-contains is usually uppercase. The first argument of the db2-fn:sglquery function is processed by SQL, which automatically converts identifiers to uppercase:

The following function calls are equivalent and return the same results assuming that the PRODUCT table is in the schema currently assigned to CURRENT SCHEMA:

```
db2-fn:xm]column-contains PRODUCT. DESCRIPTION" "snow shovel" ) dbz-fn:sqlquery("select description from product where contains (description, snow shovel ' ) ) 1")
```

## Examples

The following examples use the Db2 Text Search engine to perform searches. The columns searched are XML columns and have a text search index being

The first function searches for XML documents stored in the PRODUCTDESCRIPTION column that contain the words snow and shovel . The function sets the maximum number of returned documents to two. If the text search returns a large number of documents, you can optimize the search by using the RESULTLIMIT to limit the maximum number of documents returned: option db2-fn:xm]column-contains PRODUCT. DESCRIPTION' snow shovel RESULTLIMIT-2' )

The function returns the XML documents that match the search criteria. The documents might contain more than just a product description: For example, the following XML fragment consists of two product descriptions from an XML column. Each document contains a product description and information such as the product name, weight, and product ID. price,

```
<description> Basic 22 inch</name> <details Basic Snow Shovel , 22 inches wide, straight handle with ip</details> <price>9.9g</price> <weight>1 kg</weight> </description> </product> <product pid="100-101-01"> <description> <name Snow Shovel Deluxe 24 inch</name> <detailszA Deluxe Snow Shovel 24 inches wide, ergonomic curved hand]e with D-Grip</details> </description> </product>
```

&lt;product xm ns= "http: / /posamp]e.org" 100-100-01"&gt; pid=

The following function searches the XML column STUDENT\_ESSAYS.ABSTRACTS for 10 student essays that contain the phrase fossil fuel in Spanish, which is combustible fosi1. The function specifies es\_ES (Spanish as in Spain) as the language to use for the text search and uses the synonym dictionary that was created for the associated text search index: The function optimizes the search by using RESULTLIMIT to limit the number of results spoken db2-fn:xm]column-contains ( 'STUDENT\_ESSAYS.ABSTRACTS combustible fosi] QUERYLANGUAGE-es\_ES RESULTLIMIT-10 SYNONYM-ON ' )

The following example uses db2-fnxmlcolumn-contains to find XML documents stored in the PRODUCTDESCRIPTION column that contain the word ergonomic. The expression returns the name of the product whose is less than 20. price xquery

declare default element namespace 'http: / /posample.org' PRODUCT. DESCRIPTION ergonomic ' ) /product/description[price 20] /name

The previous expression returns only the name elements from the returned XML documents. For example, if the term ergonomic is in the product description of the product Snow Shovel, Deluxe 24 inch, the expression returns a name element similar to the following one:

&lt;name xmIns-"http: / /posample.org &gt;Snow Shovel = Deluxe 24 inch&lt;name&gt;

The following expression uses db2-fnxmlcolumn-contains to find the XML documents from the PRODUCTDESCRIPTION column that contain the words ice and scraper: The expression uses the product IDs from the product descriptions to find purchase orders in the PURCHASEORDER table that contain the product IDs. The expression returns the customer IDs from purchase orders that contain the product IDs from the matched XML description documents.

```
xquery element namespace for Spo in db2-fn:sqIquery( ' select XMLETement (Name po" XMLETement (Name "custid" purchaseorder.custid) XMLETement (Name porder" purchaseorder.porder) ) from purchaseorder' Iet Sproduct db2-fn:xm]column-contains ( 'PRODUCT. DESCRIPTION " ice scraper' ) /product where Sproduct/@pid Spo/porder/PurchaseOrder/item/partid order by Spolcustid return Spo/custid
```

The expression returns custid elements containing the customer IDs The elements are in ascending order: For example, if three purchase orders matched and the purchase orders had customer IDs 1001, 1002, and 1003, the expression returns the following elements:

&lt;custid xmlns= "http:/ /posamp]e.org"&gt;1001&lt;/custid&gt;

&lt;custid xmIns= "http:/ /posamp]e.org"&gt;1002&lt;/custid&gt;

&lt;custid xmlns="http: posample.org &gt;1003&lt;/custid&gt;

If there are multiple text searches in the same query, the Db2 Text Search engine combines the multiple text search results and returns them. For example, the following xquery statement searches for employee resumes that contain the exact phrases ruby o rails and ajax web.

## XQUERY

db2-fn:xm]column-contains ( 'EMP\_RESUME. XML\_FORMAT ruby on rails AND "ajax web" ' )

Use a single back slash to escape the colon of the attribute of a XQuery:

xquery for Si in dbz-fn:xm]column-contains ( 'DBCP12O8.T\_AUTO.T\_XML' @xpath: contains ( "purpose and @al Iue for en|:attributel" and @s]ope "9"] ') return Si/*/fn:string

## Chapter 10. Administration commands for Db2 Text Search

There are a number of commands that allow you to administer Db2 Text Search at the instance, database, table, and text-index levels. You run all of the commands db2ts. using

Use the instance-level administration commands to start and the Db2 Text Search instance services and clean up text search indexes that are no longer usable: stop

## dbzts START FOR  TEXT

Starts the Db2 Text Search instance services

## dbzts STOP FOR  TEXT

the Db2 Text Search instance services Stops

## dbzts CLEANUP FOR TEXT

Cleans up any text search collections that are not usable

Use the database-level administration commands to set up or disable databases for Db2 Text Search and clear command locks:

## dbzts ENABLE DATABASE FOR  TEXT

Enables the current database to create, manage, and use text search indexes

## dbzts DISABLE DATABASE FOR TEXT

Disables Db2 Text Search for a database and drops a number of text search tables and views catalog

## dbzts CLEAR COMMAND LOCKS

Deletes command locks for all indexes in database

Use table- and index-level commands to create and manipulate text search indexes on columns of a table:

## dbzts CREATE INDEX

Creates a text search index

## dbzts DROP INDEX

Drops a text search index associated with a text column

## dbzts ALTER INDEX

Changes the characteristics of a text search index

## dbzts UPDATE INDEX

Populates or updates a text search index based on the current contents of a text column

## dbzts CLEAR EVENTS FOR TEXT

Deletes events from the SYSIBMTS.TSEVENT view, an events view that provides information about indexing status and errors

## dbzts CLEAR COMMAND LOCKS FOR  INDEX

Deletes all command locks for specific text search index

## dbzts RESET PENDING FOR TABLE

Identifies all dependent tables that are maintained for text search and executes set integrity, if necessary

## dbzts HELP

Displays the list of dbzts command options and information about specific error messages

## DB2 Text Search commands

## dbzts ALTER INDEX

The dbzts ALTER INDEX command changes the characteristics of an index update

For execution, you must the command with dbzts at the command line: prefix

## Authorization

The privileges that are held by the authorization ID of the statement must include the SYSTS\_MGR role and at least one of the following authorities:

- DBADM authority
- ALTERIN privilege on the base schema
- CONTROL or ALTER privilege on the base table on which the text search index is defined

To change an existing schedule, the authorization ID must be the same as the index creator or must have DBADM authority

## Required connection

Database

## Command syntax

ALTER

INDEX-index-name-~FOR

connection options

## update characteristics:

<!-- image -->

## update frequency:

<!-- image -->

update characteristics ||

options

## incremental update characteristics:

<!-- image -->

## Command parameters

## ALTER INDEX index-name

The schema and name of the index as specified in the CREATE INDEX command, It uniquely identifies the text search index in database.

## UPDATE  FREQUENCY

Specifies the frequency with which index updates are made: The index is updated if the number of changes is at least the value that is set for UPDATE MINIMUM parameter: The frequency NONE indicates that no further index updates are made: This can be useful for a text column in that does not change. It is also useful when you intend to manually the index (by the UPDATE INDEX command): You can do automatic updates only if you have issued the START FOR TEXT command and the Db2 Text Search instance services are running: update update using

where DEFAULTNAME-'UPDATEFREQUENCY' .

## NONE

No automatic updates are to the text index further index updates are started manually: applied Any

- The of the week when the index is updated. days
- Every of the week: day

## integerl

Specific days of the week, from Sunday to Saturday: 0 - 6

- The hours of the specified when the index is days updated.
- Every hour of the

## integerz

Specific hours of the from midnight to 11 pm: 0 23

- M The minutes of the specified hours when the index is updated.

## integer3

Specified as top of the hour (0), or in multiples of 5-minute increments after the hour: 0, 5,10, 15,20, 25,30, 35, 40, 45, 50 or 55

If you do not specify the UPDATE FREQUENCY option, the frequency settings remain unchanged.

## UPDATE MINIMUM minchanges

Specifies the minimum number of changes to text documents that must occur before the index is incrementally updated. Multiple changes to the same text document are treated as separate changes. If you do not specify the UPDATE MINIMUM option, the is left unchanged. setting

## INDEX   CONFIGURATION (option-value)

Specifies an optional input argument of type VARCHAR(32K) that allows altering text index configuration settings The following option is supported:

Table 9. Specifications for option-value

| Option       | Value      | Data type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                               |
|--------------|------------|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SERIALUPDATE | updatemode | Integer     | Specifies whether the update processing for partitioned text search index must be run in parallel or in serial mode: In parallel mode, the execution is distributed to the database partitions and run independently on each node. In serial mode, the execution is run without distribution and stops when failure is encountered. Serial mode execution usually takes longer but requires less resources. 0 = parallel mode serial mode |

Table 9. Specifications for option-value (continued)

| Option           | Value        | Data type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|------------------|--------------|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UPDATEAUTOCOMMIT | commitsize   | String      | Specifies the number of rows or number of hours after which commit is run to automatically preserve the previous work for either initial or incremental updates: If you specify the number of rows: After the number of documents that are updated reaches the COMMITCOUNT number, the server a commit: COMMITCOUNT counts the number of documents that are updated by the primary not the number of staging table entries_ If you specify the number of hours: The text index is committed after the specified number of hours is reached. The maximum number of hours is 24. For initial updates, the index update processes batches of documents from the base table. After the commitsize value is reached, update processing completes a COMMIT operation and the last processed is saved in the staging table with the operational identifier '4'. Use this to restart update processing either after failure or after the number of specified commitcycles are completed. If you specify a commitcycles the mode is modified to incremental to initiate capturing changes by the LOGTYPE BASIC option to create triggers on the text table: However; until the initial update is complete, log entries that are generated by documents that have not been processed in previous are removed from the staging table: the UPDATEAUTOCOMMIT option for an initial text index update leads to significant increase of execution time_ For incremental updates, log entries that are processed are removed correspondingly from the staging table applies using key, key key update using cycle Using |
| COMMITTYPE       | committype   | String      | Specifies rows or hours for the UPDATEAUTOCOMMIT index configuration option.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| COMMITCYCLES     | commitcycles | Integer     | Specifies the number of commit The default is 0 for unlimited If cycles are not explicitly specified, the operation uses as many cycles as required based on the batch size that is specified with the UPDATEAUTOCOMMIT option to finish the processing: You can use this option with the UPDATEAUTOCOMMIT setting with committype cycles. update update                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

## activation options

This input argument of type integer sets the status of a text index

## ACTIVE

Sets the text index status to active

## INACTIVE

Sets the text index status to inactive

## UNILATERAL

Specifies unilateral change that affects the status of Db2 Text Search indexes. If you specify this argument, only the status of a Db2 Text Search index is changed to active or inactive: Without the UNILATERAL argument, the activation status of the Db2 Text Search and Db2 Net Search Extender indexes is jointly switched s0 that only one of the text indexes is active:

## CONNECT TO database-name

This clause specifies the database to which a connection is established. The database must be on the local If specified, this clause takes precedence over the environment variable DBZDBDFT You can omit this clause if the following statements are all true:

- The DBZDBDFT environment variable is set to valid database name
- The user running the command has the required authorization to connect to the database server:

## USER username USING password

This clause specifies the user name and password that is used to establish the connection\_

## Usage notes

All limits and naming conventions that apply to Db2 database objects and queries also apply to Db2 Text Search features and queries Db2 Text Search related identifiers must conform to the Db2 naming conventions. Also, there are some additional restrictions, such as identifiers of the following form:

[A-Za-z] [A-Za-20-9@#$\_]

or

[A-Za-z

You cannot issue multiple commands concurrently on a text search index if might conflict: If a command is issued while another conflicting command is running, an error occurs and the command fails, after which you can to run the command again. Some of the conflicting commands are: they try

- ALTER INDEX
- CLEAR EVENTS FOR INDEX
- DROP INDEX
- UPDATE INDEX
- DISABLE DATABASE FOR TEXT

Changes to the database: Updates the Db2 Text Search catalog information:

The result of activating indexes depends on the original index status The following table describes the results.

Table 10. Status changes without invalid index:

| Initial Db2 Text Search or Net Search Extender Status   | Request Active   | Request Active Unilateral   | Request Inactive   | Request Inactive Unilateral   |
|---------------------------------------------------------|------------------|-----------------------------|--------------------|-------------------------------|
| Active Inactive                                         | No change        | No change                   | Inactive Active    | Inactive Inactive             |
| Inactive Active                                         | Active Inactive  | Error                       | No change          | No change                     |
| Inactive Inactive                                       | Active Inactive  | Active Inactive             | Inactive Active    | No change                     |

SQL20427N and CIE0379E error messages are returned for active index conflicts.

You can specify the UPDATEAUTOCOMMIT index configuration without type and for compatibility with an earlier version. It is associated by default with the COMMITTYPE rows and unrestricted option cycles option cycles.

You can specify the UPDATEAUTOCOMMIT, COMMITTYPE and COMMITSIZE index configuration options for an UPDATE INDEX operation to override the configured values. Values that you submit for a specific update operation are applied only once and not persisted.

## dbzts CLEANUP FOR TEXT

Cleans up Db2 Text Search collections within an instance or within a database:

When a cleanup operation is executed for a database, invalid text indexes and their associated collections are dropped. When a cleanup operation is executed for the instance, obsolete collections are removed. A collection can become obsolete if a database containing text search indexes is dropped before Db2 Text Search has been disabled for the database.

Note: While the commands operate on text search indexes, text search server tools operate on text search collections. A text search collection refers to the underlying representation of a text search index: The relationship between a text search index and its associated collections is l:1 in non-partitioned and In in a partitioned setup, where n is the number of data partitions. Query the SYSIBMTS.TSCOLLECTIONNAMES table to determine the text search collections for a text search index For additional information, see the topic about Administration Tool for Db2 Text Search: setup catalog

For execution, the command needs to be prefixed with db2ts at the command line:

## Authorization

To issue the command on instance level, you must be the owner of the text search server process. For the integrated text search server, this is the instance owner:

To issue the command on database level, the privileges held by the authorization ID of the statement must include the SYSTS\_ ADM role and the DBADM authority:

## Required connection

This command must be issued from the Db2 database server:

## Command syntax

Instance Ievel

CLEANUP FOR TEXT

Database Tevel

CLEANUP FOR TEXT\_~connection-options

## Command parameters

None

## dbzts CLEAR COMMAND LOCKS

Removes all command locks for a specific text search index or for all text search indexes in the database. A command lock is created at the beginning of a text search index command, and is destroyed when it is done: It prevents undesirable conflict between different commands.

Use of this command is required in the rare case that locks remain in place due to an unexpected system behavior, and need to be cleaned up explicitly:

For execution, the command needs to be prefixed with dbzts at the command line:

## Authorization

The privileges held by the authorization ID of the statement used to clear locks on the index must include both of the following authorities:

- SYSTS\_MGR role
- DBADM authority or CONTROL privilege on the base table on which the index is defined

The privileges held by the authorization ID of the statement used to clear locks on the database connection must include the SYSTS\_ADM role:

## Required connection

Database

## Command syntax

CLEAR COMMAND LOCKS

FOR TEXT-

FOR

INDEX\_index-name

connection options

## connection options:

CONNECT

To

database-name

~USING ~password

## Command parameters

## FOR INDEX index-name

The name of the index as specified in the CREATE INDEX command.

## CONNECT TO database-name

This clause specifies the database to which a connection will be established: The database must be on the local system. If specified, this clause takes precedence over the environment variable DBZDBDFT . This clause can be omitted if the following are all true:

- The DBZDBDFT environment variable is set to a valid database name\_
- The user running the command the required authorization to connect to the database server: has

## USER username USING password

This clause specifies the authorization name and password that will be used to establish the connection

## Usage notes

You would invoke this command because the process owning the command lock is dead. In this case, the command (represented by the lock) may not have completed, and the index may not be operational  You need to take appropriate action. For example, the process executing the DROP INDEX command dies suddenly: It has deleted some index data, but not all the and collection information: The command lock is left intact: After clearing the DROP INDEX command lock, you may want to re-execute the DROP INDEX command. In another example, the process executing the UPDATE INDEX command is interrupted. It has processed some documents, but not all, and the command lock is still in After reviewing the text search index status and clearing the UPDATE INDEX command lock, you can re-execute the UPDATE INDEX command\_ catalog place.

When this command is issued, the content of the Db2 Text Search view SYSIBMTS.TSLOCKS is updated.

## dbzts CLEAR EVENTS FOR TEXT

This command deletes indexing events from an index's event table used for administration. The name of this table can be found in the view SYSIBMTS. TSINDEXES in column EVENTVIEWNAME.

Every index operation that processes at least one document produces informational and, in some cases, error entries in the event table: For automatic updates, this table has to be regularly inspected. Document specific errors have to be corrected (by changing the document content). After correcting the errors, the events can be cleared (and should be, in order not to consume too much space) update

For execution, the command needs to be prefixed with db2ts at the command line:

## Authorization

The privileges held by the authorization ID of the statement must include both of the following authorities:

- SYSTS\_MGR role
- DBADM with DATAACCESS authority or CONTROL privilege on the table on which the index is defined

## Required connection

Database

## Command syntax

<!-- image -->

## Command parameters

## index-name

The name of the index as specified in the CREATE INDEX command. The index name must adhere to the naming restrictions for Db2 indexes.

## CONNECT TO database-name

This clause specifies the database to which The database must be on the local system. If specified, this clause takes precedence over the environment variable DBZDBDFT: This clause can be omitted if the following are all true:

- The DBZDBDFT environment variable is set to a valid database name
- The user running the command has the required authorization to connect to the database server:

## USER username USING password

This clause specifies the authorization name and password that will be used to establish the connection

## Usage notes

All limits and naming conventions, that apply to Db2 database objects and queries, also apply to Db2 Text Search features and queries. Db2 Text Search related identifiers must conform to the Db2 naming conventions. In addition, there are some additional restrictions. For example, these identifiers can only be of the form: [A-Za-z] [A-Za-20-9@#$\_]

<!-- formula-not-decoded -->

When regular updates are scheduled (see UPDATE FREQUENCY options in CREATE INDEX or ALTER INDEX commands), the event table should be regularly checked: To cleanup the Db2 Text Search event table for a text search index, use the CLEAR EVENTS FOR INDEX command after you have checked the reason for the event and removed the source of the error:

Be sure to make changes to all rows referenced in the event table: By changing the rows in the user table, you ensure that the next UPDATE INDEX attempt can be made to successfully re-index the once erroneous documents

Note that multiple commands cannot be executed concurrently on a text search index if may conflict: If this command is issued while a conflicting command is running, an error will occur and the command will fail, after which you can try to run the command again. Some of the conflicting commands are: they

- CLEAR
- UPDATE  INDEX
- ALTER INDEX
- DROP   INDEX
- DISABLE DATABASE FOR  TEXT

Changes to the database: The event table is cleared:

## dbzts CREATE INDEX

The dbzts CREATE INDEX command creates a text search index for a text column: You can then search the column data by text search functions. using

The text search index does not contain any data until you run the text search UPDATE INDEX command or the Db2 Administrative Task Scheduler runs the UPDATE INDEX command according to the defined frequency for the index: update

To issue the CREATE INDEX command, you must prefix the command name with dbzts.

## Authorization

The authorization ID of the dbzts CREATE INDEX command must hold the SYSTS\_MGR role and CREATETAB authority on the database and one of the following items:

- CONTROL privilege on the table on which the index will be defined
- INDEX privilege on the table on which the index will be defined and one of the following items:
- IMPLICIT\_SCHEMA authority on the database, if the implicit or schema name of the index does not exist explicit
- DBADM authority

To schedule automatic index updates, the instance owner must have DBADM authority or CONTROL privileges on the administrative task scheduler tables.

## Required connection

CREATE  INDEX

index

name

name

table

name

~-text column name\_)- ~function name

text default information

update characteristics

storage options connection options

<!-- image -->

<!-- image -->

## text default information:

CODEPAGE

code\_page\_

FORMAT\_~format

## update characteristics:

~UPDATE FREQUENCY

NONE

update frequency

incremental

update characteristics

## update frequency:

D-

integer3

integerl

integer?

## incremental update characteristics:

~UPDATE MINIMUM minchanges

## storage options:

COLLECTION DIRECTORY-

directory

ADMINISTRATION

TABLES

IN--tablespace\_

name

## index configuration options:

INDEX    CONFIGURATION \_

option

value

## option value:

<!-- image -->

## server configuration options:

<!-- image -->

## Command parameters

## INDEX index\_name

Specifies the name of the index to create. This name (optionally, schema qualified) will uniquely identify the text search index within the database: The index name must adhere to the naming restrictions for Db2 indexes

## ON table name

Specifies the table name containing the text column: In Db2 Version 10.5 Fix Pack 1 and later fix packs, you can create a text search index on nickname. You cannot create text search indexes on federated tables, materialized query tables, or views\_

## text\_column name

Specifies the name of the column to index The data type of the column must be one of the following types: CHAR, VARCHAR, CLOB, DBCLOB, BLOB, GRAPHIC, VARGRAPHIC, or XML. If the data type of the column is not one of these data types, use a transformation function with the name function\_schemafunction\_name to convert the column type to one of the valid types. Alternatively, you can specify a user-defined external function that accesses the text documents that you want to index

You can create only a single text search index for a column:

## function\_ name (text\_column\_name)

Specifies the schema-qualified name of an external scalar function that accesses text documents in column that is not of a supported data type for text searching: The name must conform to Db2 naming conventions. This parameter performs column type conversion. This function must take only one parameter and return only one value:

## CODEPAGE code\_page

Specifies the Db2 code page (CODEPAGE) to use when indexing text

documents\_ The default value is specified by the value in the view SYSIBMTS TSDEFAULTS, where DEFAULTNAME= ' CODEPAGE This parameter only to binary data types, such as the column type or return type from transformation function must be BLOB or FOR BIT DATA applies

## LANGUAGE locale

Specifies the language that Db2 Text Search uses for language-specific processing of a document indexing: To have your documents automatically scanned to determine the locale, specify AUTO for the locale If you do not specify a locale, the database territory determines the default for the LANGUAGE parameter: during option. setting

## FORMAT format

Specifies the format of text documents in the column: The supported formats include TEXT , XML, HTML, and INSO. Db2 Text Search requires this information when indexing documents. If you do not specify the format, the default value is The default value is in the view SYSIBMTS.TSDEFAULTS, where DEFAULTNAME= ' FORMAT For columns of data type XML, the default format 'XML'; is used, regardless of the value of DEFAULTNAME To use the INSO format you must install rich text support used.

## UPDATE   FREQUENCY

Specifies the frequency of index updates. The index is updated if the number of changes is at least the value of the UPDATE MINIMUM parameter: You can do automatic if the Db2 Text Search instance services are running, which you start by the START FOR TEXT command\_ updates issuing

The default frequency value is taken from the view SYSIBMTS TSDEFAULTS, where DEFAULTNAME is set to UPDATEFREQUENCY

## NONE

No further index updates are made: The NONE option can be useful for a text column in table with data that does not change. It is also useful if you intend to manually the index by the UPDATE INDEX command. update using

- The of the week when the index is updated. days
- Every of the week day

## integerl

Specific days of the week, from Sunday to Saturday: 0 6\_

- The hours of the specified when the index is updated. days
- Every hour of the day:

## integerz

Specific hours of the from midnight to 11 p.m:: 0 23. day,

- M The minutes of the specified hours when the index is updated.

## integer3

The top of the hour (0) or 5-minute increments after the hour: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, or 55.

## UPDATE MINIMUM minchanges

Specifies the minimum number of changes to text documents before the index is updated incrementally according to the frequency that you specify for the UPDATE FREQUENCY parameter: Only positive integer values are allowed. The DEFAULTNAME='UPDATEMINIMUM' .

The UPDATE INDEX command ignores the value of the UPDATE MINIMUM parameter unless you specify the USING UPDATE MINIMUM for that command. option

A small value for the UPDATE MINIMUM parameterincreases consistency between the table column and the text search index: However; it also increases the load on the system.

## COLLECTION DIRECTORY directory

Specifies the directory in which the text search index collection is stored: You must specify the absolute path, where the maximum length of the absolute name is 215 characters. The process owner of the text search server instance service must have read and write access to this directory path

The COLLECTION DIRECTORY parameter is supported only for an integrated text search server For additional information about collection locations, review the usage notes. setup.

## ADMINISTRATION TABLES IN tablespace\_ name

Specifies the name of an existing nontemporary table space for the administration tables that are created for the index

For a nonpartitioned database, if you do not specify a table space, the table space of the base table for which you are creating the index is used.

For partitioned database, you must use the ADMINISTRATION TABLES IN parameter: To ensure that the staging tables for the text search index are distributed in the same manner as the corresponding base table, the table space must be in the same partition group as the table space of the base table:

## INDEX  CONFIGURATION (option\_value)

Specifies more index-related options as option-value string Options and values are as follows: pairs.

Table 11. Option-value pairs

| Option   | Value   |                             | Description                                                                                                                                                                                 |
|----------|---------|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| COMMENT  | text    | fewer than 512 bytes String | Adds a comment value to the REMARKS column in the Db2 Text Search catalog view TSINDEXES. It also appends the comment value as the description of the collection to the table string string |

| Option           | Value        | Data type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|------------------|--------------|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UPDATEAUTOCOMMIT | commitsize   | String      | Specifies the number of rows or number of hours after which commit is run to preserve the previous work for either initial or incremental updates. If specify the number of rows, after the number of updated documents reaches the COMMITCOUNT number; the server applies a commit: COMMITCOUNT counts the number of documents that are updated by the primary not the number of staging table entries If you specify the number of hours, the data in text index is committed after the specified number of hours is reached. The maximum number of hours is 24. an initial update, the index update processes batches of documents from the base table: After the commitsize value is reached, processing completes a COMMIT operation, and the last processed is saved in the staging table with the operational identifier '4.' This is to restart update processing after failure or after the completion of the specified number of commitcycles If you specify commitcycles value, the mode is changed to incremental to initiate capturing changes by using the LOGTYPEBASIC option to create triggers on the text table: However; until the initial update is complete, entries that were generated by documents that were not processed in previous are removed from the staging table: Using the UPDATEAUTOCOMMIT option for an initial text index update significantly increases execution time For incremental updates, entries that are processed are removed from the staging table with each interim commit_ you using key, For update key key used update log cycle log |
| COMMITTYPE       | committype   | String      | Specifies rows or hours for the UPDATEAUTOCOMMIT index configuration option. The default is rows:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| COMMITCYCLES     | commitcycles | Integer     | Specifies the number of commit cycles The default is 0, meaning unlimited If you do not specify the number of cycles, the update operation uses as many as required to finish the processing, based on the batch size that you specify for the UPDATEAUTOCOMMIT You can use the COMMITCYCLES option with the UPDATEAUTOCOMMIT option with a committype option cycles. cycles update                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

| Option      | Value        | Data type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------|--------------|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| INITIALMODE | initialmode  | String      | Specifies how the updates are processed. The possible values of the INITIALMODE are as follows: FIRST The primary is the default value of the INITIALMODE SKIP The update mode is immediately set to incremental, triggers are added for the LOGTYPEBASIC option, but no initial is performed. NOW The update is started after the index is created as the final of the CREATE INDEX command operation: This is supported only for single-node setups. option update option. update part option                                                                                                                                                                                           |
| LOGTYPE     | ltype        | String      | Specifies whether triggers are added to populate the primary log table: The values are as follows: BASIC The primary staging table is created, and triggers are created on the text table to recognize any changes: This is the default value for text search indexes on base tables. This is not supported for nicknames. CUSTOM The primary staging table is created, but no triggers are created on the text table: To identify changes for incremental updates, especially if you do not plan to use the ALLROWS option for updates The CUSTOM is supported for nicknames Note: The default value of the LOGTYPE option is CUSTOM for text search indexes on nicknames. option option |
| AUXLOG      | value auxlog | String      | Controls the creation of the additional infrastructure to capture changes that are not recognized by a trigger: The default setting for range-partitioned tables is ON. You can change the default value in the default table by setting AuxLogNorm for non-range-partitioned tables and AuxLogPart for range-partitioned tables. For text search indexes on nicknames, only the OFF option is supported for theAUXLOG log option:                                                                                                                                                                                                                                                        |

Table 11. Option-value pairs  (continued)

| Option          | Value                  | Data type                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-----------------|------------------------|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CJKSEGMENTATION | cjksegmentation_method | String value of fewer than 512 bytes | Specifies the segmentation method that applies to documents that use the Chinese, Japanese, or Korean language (zh_CN, zh_TW, ja_JP, or ko_KR locale set), including such documents when automatic language detection is enabled (when you specify the LANGUAGE parameter with the AUTO option) . Supported values are: MORPHOLOGICAL NGRAM If you do not specify value, the value stored in the SYSIBMTS.TSDEFAULTS view is used. Specifically, the value in the DEFAULTVALUE column of the row whose DEFAULTNAME value is CJKSEGMENTATION: The specified segmentation method is added to the SYSIBMTS. TSCONFIGURATION administrative view: You cannot change the method after creating the text index |

Important: You must enclose non-numeric values, such as comments, in single quotation marks A single quotation mark character within a string value must be represented by consecutive single quotation marks, as shown in the following example: two

INDEX CONFIGURATION   (COMMENT Index on User' 's Guide co]umn )

## SERVERID serverId

If a multiple server setup is used, specifies the serverId from SYSIBMTS . SYSTSSERVERS in which the index is to be created: If there are no multiple servers, the default server is used to create the index:

## partition options

Reserved for internal IBM use.

## CONNECT TO database\_name

Specifies the database to which a connection is established: The database must be on the local system. This parameter takes precedence over the DBZDBDFT environment variable: You can omit this parameter if the following statements are both true:

- The DBZDBDFT environment variable is set to a valid database name.
- The user running the command has the required authorization to connect to the database server:

## USER username USING password

Specifies the authorization name and password that are used to establish the connection

## Usage notes

All limits and naming conventions that apply to Db2 database objects and queries also apply to Db2 Text Search features and queries. Db2 Text Search identifiers must conform to the Db2 naming conventions. There are some additional restrictions. For example, these identifiers can be of the form: [A-Za-z] [A-Za-20-9@#s\_]

or

[A-Za-Z ] [A-Za-z0-90#$\_ ] *

Successful execution of the CREATE INDEX command has the following effects:

- The Db2 Text Search server data is updated. A collection with the name instance\_database\_name\_index\_identifier\_number is created per database partition, as in the following example:
- tigertail\_MYTSDB\_TS250517\_0000

You can retrieve the collection name from the COLLECTIONNAME column in the SYSIBMTS.TSCOLLECTIONNAMES view:

- The Db2 Text Search catalog information is updated.
- An index staging table is created in the specified table space with Db2 indexes. In addition, an index event table is created in the specified table space: If you specified the AUXLOG ON option, a second staging table is created to capture changes through integrity processing:
- If Db2 Text Search coexists with Db2 Net Search Extender and an active Net Search Extender index exists for the table column, the new text search index is set to inactive:
- The new text search index is not automatically populated. The UPDATE INDEX command must be executed either manually or automatically (as a result of an schedule defined for the index through the specification of the UPDATE FREQUENCY option) for the text search index to be populated. update being
- If specified frequency, schedule task is created for the Db2 Administrative Scheduler: you

The following key-related restrictions apply:

- You must define a primary for the table: In Db2 Text Search, you can use a multicolumn Db2 primary without type limitations. The maximum number of primary columns is two fewer than the maximum number of primary columns that are allowed by Dbz. key key key key
- The maximum total length of all primary key columns for a table with Db2 Text Search indexes is 15 bytes fewer than the maximum total primary length that is allowed by Db2. See the restrictions for the Db2 CREATE INDEX statement: key

You cannot issue multiple commands concurrently on a text search index if might conflict: If you issue this command while a conflicting command is running, an error occurs, and the command fails, after which you can to run the command A conflicting command is DISABLE DATABASE FOR TEXT. they try again:

You cannot change the auxiliary property for text index after creating the index log

The AUXLOG is not supported for nicknames for data columns that support an MQT with deferred refresh: It is also not supported for views option

To create a text search index on nickname, the nickname must be a non-relational flat file nickname: Non-relational XML nicknames are not supported

For compatibility with an earlier version, you can specify the UPDATEAUTOCOMMIT index configuration without type and This is associated by default with the COMMITTYPE rows and unrestricted option cycles. option cycles. option

To override the configured values, can specify the UPDATEAUTOCOMMIT, COMMITTYPE, and COMMITSIZE index configuration options for an UPDATE INDEX operation. Values that you submit for a are only once and not persisted. you specific update applied

If you specify theINITIALMODE SKIP option, the text search index manager populates the index Use this to control the sequence in which data from the text table is initially processed. option

The following rules apply to the LOGTYPE index configuration option:

- If you use the LOGTYPE CUSTOM use the SYSIBMTS. TSSTAGING administrative view to insert entries for new, changed, and deleted documents. setting, log
- To view the setting for an index, check the value of the LOGTYPE in the SYSIBMTS.TSCONFIGURATION administrative view: option
- To view the default type that is applied to new text indexes, check the value of the LOGTYPE option in the SYSIBMTS TSDEFAULTS administrative view. log
- The LOGTYPE is not valid with the ALLROWS of the CREATE INDEX command because the ALLROWS forces an initial and no tables are created. option option option update log

For a partitioned database environment, administration tables that are specific to text search indexes, such as staging tables, and text search indexes are distributed in manner like that used for the corresponding base table: When creating a text search index, use the ADMINISTRATION TABLES IN parameter so that the specified table space is in the same partition group as the table space of the base table:

The CJKSEGMENTATION option applies to zh\_CN,\_zh\_TW, ja\_JP and ko\_KR locale sets for Chinese, Japanese, and Korean languages: The MORPHOLOGICAL or NGRAM that you specify for the segmentation method is added to the SYSIBMTS.TSCONFIGURATION administration view: option

If you create an index with the LANGUAGE parameter set to the AUTO option, you can specify the CJKSEGMENTATION The specified segmentation method to Chinese, Japanese, and Korean language documents. You cannot change the value that you set for the cjksegmentation\_method after index creation is complete. applies option. option

If you create a text search index by setting the LANGUAGE parameter to AUTO and the CJKSEGMENTATION to MORPHOLOGICAL, searches for valid strings on morphological index might not return the expected results. In such a case, use the CONTAINS function with the QUERYLANGUAGE to obtain the results, as shown in the following sample statement: option option

select bookname from ngrambooks where contains (story,

If you use the INITIALMODE SKIP option, combined with the LOGTYPE ON and AUXLOG ON options, you must manually insert the entries into the staging table, but only for the initial All subsequent are handled automatically: log update. updates

## dbzts DISABLE DATABASE FOR TEXT

This command reverses the changes (for example, drops the text-search related tables and view) made by the command ENABLE DATABASE FOR TEXT.

When issued, this command:

- Disables the Db2 Text Search feature for the database

- Drops text search tables and views and related database objects catalog
- If the FORCE is specified, all text index information is removed from the database and all associated collections are deleted: See the "db2ts DROP INDEX command for reference\_ option

## Authorization

The privileges held by the authorization ID of the statement must include both of the following authorities:

- DBADM with DATAACCESS authority:
- SYSTS ADM role

## Required connection

Database

## Command syntax

DISABLE

DATABASE FOR

TEXT

connection options

~FORCE

## connection options:

CONNECT

database-name

## Command parameters

## FORCE

Specifies that all text search indexes be forcibly dropped from the database:

If this option is not specified and text search indexes are defined for this database, the command will fail:

If this is specified and Db2 Text Search service has not been started (the dbzts START FOR TEXT command has not been issued), the text search indexes (collections) are not dropped and need to be cleaned up manually with the dbzts CLEANUP command. option

## CONNECT TO database-name

- The DB2DBDFT environment variable is set to a valid database name

This clause specifies the database to which a connection will be established. The database must be on the local If specified, this clause takes precedence over the environment variable DBZDBDFT: This clause can be omitted if the following are all true: system.

- The user running the command the required authorization to connect to the database server: has

## USER username USING password

This clause specifies the authorization name and password that will be used to establish the connection

## Usage notes

This command does not influence the Db2 Net Search Extender enablement status of the database. It deletes the Db2 Text Search tables and views that are created by the ENABLE FOR TEXT command. catalog

Before dropping a Db2 database that has text search index definitions, issue this command and make sure that the text indexes and collections have been removed successfully:

If some indexes could not be deleted the FORCE option, the collection names are written to the db2diag log file: using

Note: The user is discouraged from usage that results in orphaned collections, such as, collections that remain defined on the text search server but are not used by Db2. Here are some cases that cause orphaned collections:

- When DROP DATABASE CLP command is executed without running DISABLE DATABASE FOR TEXT command
- When a DISABLE DATABASE FOR TEXT command is executed the FORCE using option.
- Some other error conditions.

Multiple commands cannot be executed concurrently on a text search index if may conflict: If this command is issued while a conflicting command is running, an error will occur and the command will fail, after which you can try to run the command again. Some of the conflicting commands are: they

- DROP INDEX
- UPDATE INDEX
- CLEAR EVENTS FOR INDEX
- ALTER INDEX
- DISABLE DATABASE FOR  TEXT

## dbzts DROP INDEX

The dbzts DROP INDEX command an existing text search index drops

For execution, the command needs to be prefixed with dbts at the command line:

## Authorization

The privileges held by the authorization ID of the statement must include the SYSTS\_MGR role and one of the following privileges or authorities:

- CONTROL privilege on the table on which the index is defined
- DROPIN privilege on the schema on which the index is defined
- If the text search index has an existing schedule, the authorization ID must be the same as the index creator; or must have DBADM authority

## Required connection

Database

## Command syntax

<!-- image -->

## Command parameters

## DROP INDEX index-name FOR  TEXT

The schema and name of the index as specified in the CREATE INDEX command. It uniquely identifies the text search index in drop\_options

Reserved for internal IBM use.

## CONNECT TO database-name

This clause specifies the database to which a connection is established. The database must be on the local system. If specified, this clause takes precedence over the environment variable DBZDBDFT. This clause can be omitted if the following statements are all true:

- The DBZDBDFT environment variable is set to a valid database name.
- The user running the command has the required authorization to connect to the database server:

## USER username USING password

This clause specifies the authorization name and password that are used to establish the connection:

## Usage notes

Multiple commands cannot be executed concurrently on a text search index if the command might conflict: If this command is issued while a conflicting command is running, an error occurs and the command fails, after which you can try to run the command again. The following commands are some common conflicting commands:

- DROP   INDEX
- UPDATE INDEX
- CLEAR EVENTS FOR  INDEX
- ALTER INDEX
- DISABLE DATABASE FOR TEXT

STOP FOR TEXT command that runs in parallel with the DROP operation will not cause conflicting command message, instead, if the text search server is shut down before DROP has removed the collection, an error will be returned that the text search server is not available:

After a text search index is dropped, text search is no longer possible on the corresponding text column: If you plan to create a new text search on the same text column, you must first disconnect from the database and then reconnect before creating the new text search index

The dbzts DROP INDEX FOR TEXT command makes the following changes to the database:

- Updates the Db2 Text Search information. catalog
- Drops the index staging and event tables.
- Deletes triggers on the user text table:
- Destroys the collection associated with the Db2 Text Search index definition

## dbzts ENABLE DATABASE FOR TEXT

The dbzts ENABLE DATABASE FOR TEXT command enables Db2 Text Search for the current database:

It creates administrative tables and views, sets default values for parameters, and must run successfully before you can create text search indexes on columns in tables within the database. The command needs to be prefixed with db2ts at the command line:

After enabling the database, it is necessary to specify the connection information for the text search server in the SYSIBMTS TSSERVERS view. The enable operation includes an attempt to populate the server data and will show warning if the server configuration cannot be accessed. In any case, it is recommended to verify the connection information in the view For details, see the topic about updating Db2 Text Search server information:

## Authorization

- The privileges held by the authorization ID of the statement must include the SYSTS ADM role and the DBADM authority

## Required connection

Database

## Command syntax

ENABLE DATABASE FOR TEXT

ADMINISTRATION TABLES IN

tablespace-name

AUTOGRANT

connection options

## connection options:

CONNECT To database-name

<!-- image -->

## Command parameters

## ADMINISTRATION TABLES IN tablespace-name

Specifies the name of an existing regular table space for administration tables created while enabling the database for Db2 Text Search: It is recommended that the table space is in the database partition group IBMCATGROUP For partitioned database, the bufferpool and table space should be defined with 32 KB page size:

If the clause is not specified, SYSTOOLSPACE is used as default table space. In this case, ensure that SYSTOOLSPACE already exists. If it does not exist, the SYSPROC.SYSINSTALLOBJECTS procedure may be used to create it:

Note: Use quotation marks to specify a case-sensitive table space name.

## AUTOGRANT

This has been deprecated and does not grant privileges to the instance owner anymore. Its use is no longer suggested and might be removed in a future release option

## CONNECT TO database-name

This clause specifies the database to which connection is established. The database must be on the local system. If specified, this clause takes precedence over the environment variable DBZDBDFT. This clause can be omitted if the following statements are all true:

- The DBZDBDFT environment variable is set to a valid database name.
- The user running the command has the required authorization to connect to the database server:

## USER username USING password

This clause specifies the authorization name and password used to establish the connection\_

## Example

Example 1: Enable a database for Db2 Text Search creating administration tables in table space named tsspace and return any error messages in English: CALL SYSPROC.SYSTS\_ENABLE ( ' ADMINISTRATION TABLES IN tsspace US ' 2) 'en\_

The following is an example of output from this query:

```
Value of output parameters Parameter Name MESSAGE Parameter Value Operation completed successfully. Return Status
```

## Usage notes

When executed successfully, this command does the following actions:

- Enables the Db2 Text Search feature for the database:
- Establishes Db2 Text Search database configuration default values in the view SYSIBMTS TSDEFAULTS.
- Creates the following Db2 Text Search administrative views in the SYSIBMTS schema:
- SYSIBMTS.TSDEFAULTS
- SYSIBMTS.TSLOCKS

- SYSIBMTS.TSINDEXES
- SYSIBMTS.TSCONFIGURATION
- SYSIBMTS. TSCOLLECTIONNAMES
- SYSIBMTS.TSSERVERS

## dbzts HELP

dbzts HELP displays the list of available Db2 Text Search commands, or the syntax of an individual command:

Use the dbzts HELP command to get help on error messages as well. specific

For execution, the command needs to be prefixed with dbzts at the command line:

## Authorization

None-

## Command syntax

<!-- image -->

## Command parameters

## HELP 2

Provides help information for a command or a reason code

## command

The first keywords that identify Db2 Text Search command:

- ALTER
- CLEANUP
- CLEAR (for both CLEAR COMMAND LOCKS and CLEAR EVENTS FOR INDEX)
- CREATE
- DISABLE
- DROP
- ENABLE
- RESET PENDING
- START
- STOP
- UPDATE

## sqlcode

SQLCODE for message returned by db2ts command (within or outside the administration stored procedure) or text search query:

## sqlstate

Sqlstate returned by command, administration stored procedure, or text search query:

## error-identifier

An identifier is part of the text-search-error-msg that is embedded in error messages. This identifier starts with 'CIE' and is of the form CIEnnnnn where nnnnn is a number: This identifier represents the specific error that is returned upon an error text search: It may also be returned in an informational message upon completion of a text search command or in the message printed at the completion of a text search administration procedure: If the identifier does not start with CIE' , then dbzts help cannot provide information about the error-identifier. For example, db2ts cannot provide help for a message with an error-identifier such as during

## Usage notes

When a UNIX shell, it might be necessary to supply the arguments to dbzts double quotation marks, as in the following example: dbzts using using

Without the quotation marks, the shell tries to match the wildcard with the contents of the working directory and it may give unexpected results.

If the first keyword of any db2ts command is specified, the syntax of the identified command is displayed: For the two db2ts commands that share the same first keyword (CLEAR COMMAND LOCKS and CLEAR EVENTS FOR INDEX), the syntax of both commands will be displayed when dbzts help clear is issued, but each command may be specifically displayed by the second keyword to distinguish them, for example db2ts help clear events. If a parameter is not specified after ? or HELP, db2ts lists all available db2ts commands\_ adding

Specifying sqlcode, sqlstate, or CIE error-identifier will return information about that code, state, or error identifier: For example, dbzts help SQL20423

or dbzts 38H10

or dbzts ? CIE00323

## dbzts RESET PENDING command

Issues a SET INTEGRITY statement for all text-maintained staging tables that are associated with a particular table:

Certain commands cause the Db2 Text Search staging tables to go into pending mode, which blocks other database or text search operations. If you use the dbzts RESET PENDING command, you do not have to find all text indexes and associated staging tables and then issue a SET INTEGRITY statement for each table:

After detaching a data partition, you must issue the RESET PENDING command to the staging-table content: update

## Authorization

This command requires the SYSTS\_MGR role and at least one of the following authorities or privileges:

- DATAACCESS authority
- CONTROL on the base table on which the text index is created

Note: Currently ALL privileges are granted to the SYSTS\_MGR to allow for the creation or dropping of new index tables However; if a dependent object like an index is implicitly created on the index table, then authorization is not propagated: To delete the dependent object, grant CONTROL privilege to the user:

## Required connection

You must issue this command from the Db2 database server:

## Command syntax

<!-- image -->

RESET PENDING FOR TABLE table-schema. table-name\_\_FOR TEXT

connection-options

## Connection-options:

CONNECT

~USER-~userid--USING ~password

## Command parameters

## table-name

The name of the table for which the text-maintained staging infrastructure was added and for which integrity processing is required.

## table-schema

The schema of the table for which a command was issued that resulted in pending mode.

## Usage notes

Use the RESET PENDING command after issuing a command that causes the underlying tables to be put into pending mode, such as the LOAD command with the INSERT parameter; or after issuing a command that requires a SET INTEGRITY statement to refresh dependent tables, such as the ALTER TABLE DETACH statement:

## dbzts SET COMMAND LOCK command

The dbzts SET COMMAND LOCKS command creates a manual lock when an administrative operation is on the collection level: applied

## Authorization

To set a command lock, you must have the corresponding privileges as for clearing the lock: For example, to set a lock on a specific index, the SYSTS\_MGR role and the corresponding table privileges are required.

## Command syntax

-FOR

TEXT

FOR INDEX-\_index-name

## Command parameters

## SET COMMAND LOCKS FOR   INDEX index-name

Specifies the name of the index, which uniquely identifies the text search index within the database:

## Usage notes

The lock is visible in the SYSIBMTS.TSLOCKS administrative view. It prevents other administrative operations, but allows index search to continue. You must explicitly remove the lock with the CLEAR COMMAND LOCKS operation.

## dbzts START FOR TEXT

The dbzts START FOR TEXT command starts the Db2 Text Search instance services that support other Db2 Text Search administration commands and the ability to reference text search indexes in SQL queries.

The dbzts START FOR TEXT command also includes starting processes for rich text support on the host machine running the Db2 Text Search server; if the server is configured for rich text support:

This command must be issued from the Db2 database server:

To start instance services in a partitioned database environment an integrated text search you must run the command on the integrated text search server host machine. By default, the integrated text search server host machine is the host of the lowest-numbered database partition server: using setup,

## Authorization

Instance owner: No database privilege is required

## Command syntax

```
START FOR TEXT STATUS ~VERIFY
```

## Command parameters

## STATUS

Verifies the status of the Db2 Text Search server: A\_ verbose informational message is returned indicating the STARTED or STOPPED status of the server:

## VERIFY

Verifies the started status of the Db2 Text Search server and exits with a standard message and return code 0 indicating that the operation is successful. A non-zero code is returned for any other state of the text search server or if the status cannot be verified.

## Examples

```
Check that the text search server is started: Linux/UNIX: dbzts START FOR TEXT VERIFY Operation completed successfully . echo $? Windows C:|> dbzts START FOR TEXT VERIFY CIEOOOO1 Operation completed successfully. echo %ERRORLEVEL?
```

## Usage notes

- In partitioned database environment, the dbzts START FOR TEXT command with theSTATUS and VERIFY parameters can be issued on any one of the partition server hosts. To start the instance services, you must run the dbzts START FOR TEXT command on the integrated text search server host machine: The integrated text search server host machine is the host of the lowest-numbered database partition server: If custom collection directories are used, ensure that no lower numbered partitions are created later: This restriction is especially relevant for Linux and UNIX platforms If you configure Db2 Text Search when creating an instance, the configuration initially determines the integrated text search server host: That configuration must always remain the host of the lowest-numbered database partition server:
- On Windows platforms, there is a Windows service associated with each Db2 instance for Db2 Text Search: The service name can be determined by issuing the following command:

DBZTS &lt;instance name&gt; [~&lt;partition numberz]

- Apart from the the dbzts START FOR TEXT command, you can also start the service the Control Panel or the NET START command using using

## dbzts STOP FOR TEXT

The dbzts STOP FOR TEXT command stops Db2 Text Search instance services. If the running services include processes for rich text support then those services are stopped as well:

This command must be issued from the Db2 database server:

When running this command from the command line, the command with dbzts at the Db2 command line: prefix

This command provides the convenience of stopping a stand-alone text search server which can also be achieved in its own installation environment the provided script: If the instance services are already stopped, the command only checks and reports its status to the user using

## Authorization

Instance owner: No database privilege is required

## Command syntax

```
STOP FOR TEXT STATUS ~VERIFY-
```

## Command parameters

## STATUS

Verifies the status of the Db2 Text Search servers. A verbose informational message is returned indicating the STARTED or STOPPED status of the servers\_

## VERIFY

Verifies the stopped status of the Db2 Text Search server: It exits with the standard message and return code 0 to indicate the command ran successfully Otherwise, the text search server returns a non-zero code to indicate failure.

## Usage notes

- In a partitioned database environment, the dbzts START FOR TEXT command with the STATUS and VERIFY parameters can be issued on any one of the partition server hosts.
- To avoid interrupting the execution of currently running commands, ensure no other administrative commands like the dbzts UPDATE INDEX FOR TEXT command are still active before issuing the dbzts STOP FOR TEXT command.
- In partitioned database environment on Windows platforms using an integrated text search server; the instance services by issuing the dbzts STOP FOR TEXT command on the integrated text search server host machine: By default, the integrated text search server host machine is the host of the lowest-numbered database partition server Running the command on the integrated text search server host machine ensures that all processes and services are stopped. If the command is run on different partition server host, the DBZTS service must be stopped separately command such as NET STOP stop using

## dbzts UPDATE INDEX

The dbzts UPDATE INDEX command updates the text search index to reflect the current contents of the text column with which the index is associated. You can do search the However the search operates on the partially index until the is complete: during updated update update execution, you must the command with db2ts at the command line: For prefix

## Authorization

The privileges that are held by the authorization ID of the statement must include the SYSTS\_MGR role and at least one of the following authorities:

- DATAACCESS authority
- CONTROL privilege on the table on which the text index is defined
- INDEX with SELECT privilege on the base table on which the text index is defined

In addition, for an initial update the authorization requirements apply as outlined in the CREATE TRIGGER statement:

## Required connection

Database

## Command syntax

UPDATE

TEXT

~UPDATE OPTIONS

connection options

## connection options:

CONNECT To database-name

## Command parameters

## UPDATE INDEX index-name

Specifies the name of the text search index to be updated. The index name must adhere to the naming restrictions for Db2 indexes.

## UPDATE OPTIONS

An input argument of type VARCHAR(32K) that specifies If no are specified the is started unconditionally: The possible values are: update options. options update

| UPDATE OPTIONS value    | Description                                                                                                                                                                                                                                                                                                              |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| USING  UPDATE MINIMUM   | This enforces the use of the UPDATE MINIMUM value that is defined for the text search index and processes if the specified minimum number of changes occurred option updates                                                                                                                                             |
| FOR DATA REDISTRIBUTION | This option specifies that a text search index in partitioned database must be refreshed after data partitions are added or removed and subsequent data redistribution operation must be completed. Search results might be inconsistent until the text search index is updated with the FOR DATA REDISTRIBUTION option_ |
| ALLROWS                 | This option specifies that an initial must be attempted unconditionally: update                                                                                                                                                                                                                                          |

| UPDATE OPTIONS value        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UPDATEAUTOCOMMIT commitsize | Specifies the number of rows or number of hours after which a commit is run to automatically preserve the previous work for either initial or incremental updates If you specify the number of rows: After the number of documents that are updated reaches the COMMITCOUNT number; the server applies a commit: COMMITCOUNT counts the number of documents that are updated by the primary not the number of staging table entries_ If you specify the number of The text index is committed after the specified number of hours is reached. The maximum number of hours is 24. For initial updates, the index processes batches of documents from the base table: After the commitsize value is reached, update processing completes COMMIT operation and the last processed is saved in the staging table with operational identifier '4'. This is used to restart update processing either after failure or after the number of specified commitcycles are completed. If a commitcycles is specified, the update mode is modified to incremental to initiate capturing changes by the LOGTYPE BASIC option to create triggers on the text table. However; until the initial update is complete, entries that are generated by documents that have not been processed in previous are removed from the staging table: the UPDATEAUTOCOMMIT option for an initial text index update leads to significant increase of execution time. For incremental updates, entries that are processed are removed correspondingly from the staging table with each interim commit. using key, hours: update key key using log cycle Using log |
| COMMITTYPEcommittype        | Specifies rows or hours for the UPDATEAUTOCOMMIT index configuration option. The default is rows                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

| UPDATE OPTIONS value     | Description                                                                                                                                                                                                                                                                                                                                                       |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| COMMITCYCLEScommitcycles | Specifies the number of commit The default is 0 for unlimited cycles. If cycles are not explicitly specified, the operation uses as many as required based on the batch size that is specified with the UPDATEAUTOCOMMIT to finish the processing: You can use this with the UPDATEAUTOCOMMIT setting with committype. cycles. update cycles option update option |

## CONNECT TO database-name

This clause specifies the database to which a connection is established. The database must be on the local If specified, this clause takes precedence over the environment variable DBZDBDFT. You can omit this clause if the following statements are all true: system.

- The DBZDBDFT environment variable is set to valid database name
- The user running the command has the required authorization to connect to the database server:

## USER username USING password

This clause specifies the authorization name and password that are to establish the connection\_ used

## Usage notes

All limits and naming conventions that apply to Db2 database objects and queries also apply to Db2 Text Search features and queries. Db2 Text Search related identifiers must conform to the Db2 naming conventions. In addition, there are some additional restrictions. For example, these identifiers can only be of the form: [A-Za-z] [A-Za-20-9@#$\_]

or

<!-- formula-not-decoded -->

If synonym dictionaries are created for a text index, issuing the ALLROWS and FOR DATA REDISTRIBUTION options removes dictionaries from existing collections. You can associate new collections with the text index after database partitions are added. The synonym dictionaries for all associated collections have to be added update again.

The command does not complete sucessfully until all index processing is completed. The duration depends on the number of documents to be indexed and the number of documents already indexed. You can retrieve the collection name from the SYSIBMTS. TSCOLLECTIONNAMES view (column COLLECTIONNAME): update

Multiple commands cannot be issued concurrently on a text search index if might conflict: If you run this command while a conflicting command is running, an error occurs and the command fails, after which you can to run the command The following commands are some of the common conflicting commands: they try again.

- UPDATE INDEX

- CLEAR EVENTS FOR   INDEX
- ALTER INDEX
- DROP INDEX
- DISABLE DATABASE FOR TEXT

Note: In cases of individual document errors, the documents must be corrected: The primary keys of the erroneous documents can be looked up in the event table for the index The next UPDATE INDEX command reprocesses these documents if the corresponding rows in the user table are modified:

The UPDATE INDEX command include changes to the database, such as:

- Insert rows to the event table (including parser error information from Db2 Text Search):
- Delete from the index staging table in case of incremental updates.
- The collection is updated.
- Before first update, create triggers on the user text table
- New or changed documents are parsed and indexed:
- Deleted documents are discarded from the index

You can specify the UPDATEAUTOCOMMIT index configuration option without type and for compatibility with an earlier version. It is associated by default with the COMMITTYPE rows and unrestricted cycles option cycles.

When you specify UPDATEAUTOCOMMIT, COMMITTYPE or COMMITSIZE values for the update operation, override existing configured values only for the specific and are not persisted. they update

## Chapter 11. Dbz Text Search stored procedures

Db2 Text Search provides several administrative SQL routines for running commands and for returning the result messages of the commands that you run and the result message reason codes:

You can run the following db2ts commands the administrative SQL routines: using

- Enable a database SYSPROC. SYSTS ENABLE
- Configure a database SYSPROC. SYSTSCONFIGURE
- Disable a database SYSPROC . SySTSDISABLE
- Create a text index SYSPROC . SYSTSCREATE
- Update a text index SYSPROC. SySTSUPDATE
- Alter a text index SYSPROC . SYSTS\_ALTER
- Drop a text index SYSPROC. SYSTSDROP
- Clear events for a text index SYSPROC . SSTS\_CLEAR\_EVENTS
- Clear command locks SYSPROC . SySTS CLEARCOMMANDLOCKS
- Reset pending status SYSPROC . SySTSADMIN CMD
- Cleanup inactive indexes SYSPROC. SySTS\_CLEANUP

## Chapter 12. Text search administrative views

Db2 Text Search creates and maintains several administrative views that describe the text search indexes in database and their properties.

Do not any f these views unless specifically instructed to do so\_ update

The following views reflect the current configuration of your system:

- Database-level views:
- SYSIBMTS TSDEFAULTS
- SYSIBMTS.TSLOCKS
- SYSIBMTS.TSSERVERS
- Index-level views:
- SYSIBMTS. TSINDEXES
- SYSIBMTS.TSCONFIGURATION
- SYSIBMTS.TSCOLLECTIONNAMES
- SYSIBMTS.TSEVENT\_nnnnnn
- SYSIBMTS.TSSTAGING\_ nnnnnn

## Text Search Administrative Views

## SYSIBMTS.TSDEFAULTS view

SYSIBMTS.TSDEFAULTS displays all the default values for all text search indexes in database.

The default values are available as attribute-value in this view: pairs

Table 12. SYSIBMTS.TSDEFAULTS view

| Column name   | Data type     | Nullable?   | Description                                            |
|---------------|---------------|-------------|--------------------------------------------------------|
| DEFAULTNAME   | VARCHAR (30)  | NO          | Database default parameters for text search            |
| DEFAULTVALUE  | VARCHAR (512) | NO          | Values for database default parameters for text search |

The following values are used as defaults for the db2ts CREATE INDEX, ALTER INDEX, UPDATE INDEX, and CLEAR EVENTS FOR INDEX commands:

- AUXLOGNORM: The staging infrastructure can be enabled for a text search index with index configuration AUXLOG ON. Do not enable the extended text-maintained staging infrastructure for non-partitioned tables by default: explicit
- CJKSEGMENTATION: Specifies the segmentation method to use when indexing documents for Chinese, Japanese and Korean languages The supported value includes: MORPHOLOGICAL and NGRAM The default value is NGRAM:
- AUXLOGPART: The staging infrastructure can be disabled for a text index with index configuration AUXLOG OFF. By default, enable the extended text-maintained staging infrastructure for range-partitioned tables explicit
- CODEPAGE: The initial default code page for new indexes is the database code page:

- DOCUMENTRESULTQUEUESIZE: This value is used to limit how much database memory is reserved per operation for a collection: The default value is 30,000 while the range is 100 100,000. Note that on multi-partition a single text index that is configured for parallel execution will reserve memory space for each collection that needs an update update setup, update.
- FORMAT: The initial default for the document format is plain text
- MAXCONCURRENTUPDATES: Controls the number of collection that can be executed in parallel at any given time: For multiple partition setups, the number of collections for each text index is determined according to the table distribution. However; only active partition count\_ The default is 8 updates updates
- LANGUAGE: The initial default for document indexing is en\_US.
- MAXCONCURRENTCOLLECTIONS: Controls the number of collections that can be created. For a single-node database, the number of collections equals the number of text indexes, for multi-partition setups, the number of collections per text index matches the table distribution. The default is 160.
- MAXDOCUMENTSIZEINMB: Controls the size of documents that are accepted for processing: A text that exceeds the limit will result in warning message in the event table: The value is 100.
- UPDATEFREQUENCY: The initial default for the schedule for new indexes is NONE. update
- UPDATEMINIMUM: The initial default for updating new indexes is 1, meaning that incremental updates can be done after every change
- UPDATEAUTOCOMMIT: The initial default for updating new indexes is 0, meaning that there will be no intermediate commits when documents are read from Db2 text columns. This value is reserved, and you cannot change it:

You cannot use dbzts commands to change the default values at the database level.

## SYSIBMTS.TSLOCKS view

You can view command lock information at the database and index level using SYSIBMTS.TSLOCKS.

Table 13. SYSIBMTS.TSLOCKS view

| Column name    | Data type    | Nullable?   | Description                                                                                                                                                              |
|----------------|--------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| COMMAND        | VARCHAR(3O)  | NO          | Name of the command that created the lock. Possible values are: CREATE INDEX, ALTER INDEX, DROP INDEX , UPDATE INDEX, CLEAR EVENTS, DISABLE DATABASE, CONFIGURE, CLEANUP |
| LOCKSCOPE      | VARCHAR(30)  | NO          | of the lock: Possible values are: DATABASE or INDEX. Scope                                                                                                               |
| INDSCHEMA      | VARCHAR(128) | NO          | Schema name of the text search index (only for LOCKSCOPE = INDEX)                                                                                                        |
| INDNAME        | VARCHAR(128) | NO          | Unqualified name of the text search index (only for LOCKSCOPE INDEX)                                                                                                     |
| PARTITION      | INTEGER      | NO          | Partition number on which the text search lock is created                                                                                                                |
| LOCKCREATETIME | TIMESTAMP    | NO          | Time when the lock was granted stamp                                                                                                                                     |

There are three distinct scenarios to be aware of for locking strategies:

- An operation is started and no applicable lock is encountered: The procedure sets the lock and continues execution. For both successful and failed execution, the lock is removed:

- An operation is started and encounters an applicable lock: The request is returned with a conflicting command message:
- An operation is started and encounters an applicable lock, even though no associated operation is currently running: A failure occurred for an earlier operation that prevented proper removal of the lock This can occur in extreme situations like disk failures or crashes. In such a case the locks need to be removed by issuing a CLEAR COMMAND LOCKS operation at the index or database level as appropriate, after the cause of failure is addressed and system consistency is verified:

## SYSIBMTS.TSSERVERS view

Each row represents of the SYSIBMTS TSSERVERS view displays information about Db2 Text Search server configured for the database:

You can query the view to obtain information about the text search server that is marked as the one to be used:

from SYSIBMTS. TSSERVERS where SERVERSTATUS 0"

Table 14. SYSIBMTS.TSSERVERS view

| Column name   | Data type    | Nullable?   | Description                                                                                                                                                                                                                                                        |
|---------------|--------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SERVERID      | INTEGER      | NO          | Unique ID generated for the text search server:                                                                                                                                                                                                                    |
| HOST          | VARCHAR(256) | NO          | Host name or IP address of the text search server For partitioned databases, stand-alone text search server deployments or when administrative operations are executed remote clients, make sure to use the actual host name or IP address, not 'localhost' . from |
| PORT          | INTEGER      | NO          | Port number for the text search server: (ADMIN /SEARCH)                                                                                                                                                                                                            |
| TOKEN         | VARCHAR(256) | NO          | Authentication token for the text search server:                                                                                                                                                                                                                   |
| KEY           | VARCHAR(128) | NO          | The server for the text search server key                                                                                                                                                                                                                          |
| DEFAULTLOCALE | VARCHAR(33)  | NO          | Default client locale assumed for messages from text search server                                                                                                                                                                                                 |
| SERVERTYPE    | INTEGER      | NO          | The value indicates the type for each text search server: 0 the default (integrated) text search server non-zero value a stand-alone text search server local stand-alone text search server 2 a remote stand-alone text search server                             |
| SERVERSTATUS  | INTEGER      | NO          | Indicates whether the text search server can be used to create new text search indexes_ The default value is 0, indicating that the server is active and usable:                                                                                                   |

## SYSIBMTS.TSINDEXES view

The current text search index properties are shown in the SYSIBMTS.TSINDEXES

The following example uses the index schema and name: dbz "SELECT COLNAME from SYSIBMTS. TSINDEXES where INDSCHEMA-schema-name and INDNAME-index-name"

The SYSIBMTS.TSINDEXES view is described in the following table:

Table 15. SYSIBMTS.TSINDEXES view

| Column name         | Data type    | Nullable?   | Description                                                                                                                                                                                                                                                                    |
|---------------------|--------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| INDSCHEMA           | VARCHAR(128) | NO          | Schema name for the text search index                                                                                                                                                                                                                                          |
| INDNAME             | VARCHAR(128) | NO          | Unqualified name of the text search index_                                                                                                                                                                                                                                     |
| TABSCHEMA           | VARCHAR(128) | NO          | Schema name of the base table                                                                                                                                                                                                                                                  |
| TABNAME             | VARCHAR(128) | NO          | Unqualified name of the base table_                                                                                                                                                                                                                                            |
| COLNAME             | VARCHAR(128) | NO          | Column that the text search index was created on.                                                                                                                                                                                                                              |
| CODEPAGE            | INTEGER      | NO          | Document code page for the text search index                                                                                                                                                                                                                                   |
| LANGUAGE            | VARCHAR(S)   | NO          | Document language for the text                                                                                                                                                                                                                                                 |
| FORMAT              | VARCHAR(30)  | YES         | Document format_                                                                                                                                                                                                                                                               |
| FUNCTIONSCHEMA      | VARCHAR(128) | YES         | Schema for the column type:                                                                                                                                                                                                                                                    |
| FUNCTIONNAME        | VARCHAR(18)  | YES         | Name of the column-type conversion function:                                                                                                                                                                                                                                   |
| COLLECTIONDIRECTORY | VARCHAR(512) | YES         | Directory for the text search index files.                                                                                                                                                                                                                                     |
| UPDATEFREQUENCY     | VARCHAR(300) | NO          | Trigger criterion for applying updates to the index                                                                                                                                                                                                                            |
| UPDATEMINIMUM       | INTEGER      | YES         | Minimum number of entries in the log table before an incremental update is performed. A lower value means better consistency between the table column and the text search index. However; lower value also increases the resources that are required for text search indexing: |
| EVENTVIEWSCHEMA     | VARCHAR(128) | NO          | Schema for the event view that is created for the text search index (always SYSIBMTS)                                                                                                                                                                                          |
| EVENTVIEWNAME       | VARCHAR(128) | NO          | Name of the event view that is created for the text search index                                                                                                                                                                                                               |
| STAGINGVIEWSCHEMA   | VARCHAR(128) | YES         | Schema for the view that is created for the text search index (always SYSIBMTS) log                                                                                                                                                                                            |
| STAGINGVIEWNAME     | VARCHAR(128) | YES         | Name of the log view that is created for the text search index_                                                                                                                                                                                                                |
| REORGAUTOMATIC      | INTEGER      | YES         | Reserved (not supported in this release) The value is always 1_                                                                                                                                                                                                                |
| RECREATEONUPDATE    | INTEGER      | NO          | Reserved (not supported in this release)_ The value is always 0.                                                                                                                                                                                                               |
| ATTRIBUTES          | VARCHAR(18)  | YES         | Reserved (not supported in this release).                                                                                                                                                                                                                                      |
| INDEXMODELNAME      | VARCHAR(128) | YES         | Reserved (not supported in this release)                                                                                                                                                                                                                                       |

Table 15. SYSIBMTS.TSINDEXES view (continued)

| Column name          | Data type    | Nullable?   | Description                                                                                                                                                                                                         |
|----------------------|--------------|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| COLLECTIONNAMEPREFIX | VARCHAR(128) | NO          | Prefix of the collection name on the text search server:                                                                                                                                                            |
| COMMENT              | VARCHAR(512) | YES         | Comment that is specified for parameter that is related to index properties of the CREATE INDEX command_                                                                                                            |
| AUXSTAGINGSCHEMA     | VARCHAR(48)  | YES         | Schema of the text-maintained staging table:                                                                                                                                                                        |
| AUXSTAGINGNAME       | VARCHAR(48)  | YES         | Name of the text-maintained staging table:                                                                                                                                                                          |
| INDSTATUS            | VARCHAR(1O)  | NO          | Index status: ACTIVE indicates an active index. INACTIVE indicates an inactive index: (This value is not used for DB2 Text Search:) INVALID indicates an invalidated index, usually side effect of a DB2 operation. |
| SERIALMODE           | INTEGER      | NO          | For distributed setups: 0-parallel 1-serial update update                                                                                                                                                           |
| INDEXMODELNAME       | VARCHAR(128) | YES         | Reserved (not supported in this release).                                                                                                                                                                           |

## SYSIBMTS.TSCONFIGURATION view

Information about index configuration parameters is available in the SYSIBMTS.TSCONFIGURATION view:

Each row represents a configuration parameter of the text search index

Following is an example of a query against the view that uses the index name: dbz "SELECT VALUE from SYSIBMTS. TSCONFIGURATION where INDSCHEMA-schema-name and INDNAME-ind-name and PARAMETER parameter

Table 16. SYSIBMTS.TSCONFIGURATION view

| Column name   | Data type    | Nullable?   | Description                               |
|---------------|--------------|-------------|-------------------------------------------|
| INDSCHEMA     | VARCHAR(128) | NO          | Schema name of the text search index      |
| INDNAME       | VARCHAR(128) | NO          | Unqualified name of the text search index |
| PARAMETER     | VARCHAR(30)  | NO          | Name of a configuration parameter         |
| VALUE         | VARCHAR(512) | NO          | Value of the parameter                    |

The PARAMETER column contains the names of the text search index configuration parameters specified with the CREATE INDEX statement and the names of some of the parameters from the SYSIBMTS.TSDEFAULTS view.

## SYSIBMTS.TSCOLLECTIONNAMES view

The SYSIBMTS.TSCOLLECTIONNAMES view displays the names of collections.

Each row represents a collection for a text search index

Table 17. SYSIBMTS.TSCOLLECTIONNAMES view

| Column name    |              | Nullable?   | Description                                                                                                                                                                                                        |
|----------------|--------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| INDSCHEMA      | VARCHAR(128) | NO          | Schema name of the text search index                                                                                                                                                                               |
| INDNAME        | VARCHAR(128) | NO          | Unqualified name of the text search index                                                                                                                                                                          |
| COLLECTIONNAME | VARCHAR(132) | NO          | Name of the associated collection on the text search server: In partitioned database systems, each text index partition is represented as collection. The collection name includes the partition number as suffix: |

## SYSIBMTS.TSEVENT view

The event view provides information about indexing status and error events.

A database might have multiple views with the SYSIBMTS.TSEVENT. Each view is differentiated by the nnnnnn value, an internal identifier that points to the corresponding text index that the view is associated with: To determine the text search index associated with a particular view, query the view SYSIBMTS TSINDEXES, searching for the schema name and view name in the columns EVENTVIEWSCHEMA and EVENTVIEWNAME. The query returns single row that describes the text search index and user table in question. prefix

The number of columns in this view depends on the number of primary columns in the user table: The columns PK1\_PKnn match the primary columns of the user table and have corresponding data type and lengths definitions. The data type of each of the columns in the view exactly corresponds to the data type of the corresponding primary column\_ key key key

Each row in this view represents a message from an UPDATE INDEX command on the text search index For instance, row might indicate that an UPDATE INDEX command has started or has completed. Alternatively, a row might describe a problem that occurred when a text document was indexed\_ You can identify the text document by retrieving the primary column values from the row in this view and looking them up in the user table being key

You can clear events by the db2ts CLEAR EVENTS FOR INDEX command using

Table 18. Event view

| Column name   | Data type   | Nullable?   | Description                                                                                          |
|---------------|-------------|-------------|------------------------------------------------------------------------------------------------------|
| OPERATION     | INTEGER     | YES         | The operation (insert, update, or delete) on the base table to be reflected in the text search index |
| TIME          | TIMESTAMP   | YES         | Time stamp of event entry creation                                                                   |

Table 18. Event view (continued)

| Column name   | Data type                                                   | Nullable?   | Description                                                                                                                                                                                                                                                      |
|---------------|-------------------------------------------------------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SEVERITY      | INTEGER                                                     | YES         | If the message corresponds to single document, one of the following values: 1 Informational 4 = Parts of the document were indexed but there was warning, as indicated by the message 8 = The document was not indexed, as indicated by the message 0= Otherwise |
| SQLCODE       | INTEGER                                                     | YES         | SQLCODE for the associated error; if any                                                                                                                                                                                                                         |
| MESSAGE       | VARCHAR(1024)                                               | YES         | Text information about the specific error                                                                                                                                                                                                                        |
| PARTITION     | INTEGER                                                     | YES         | Reserved for internal IBM use_                                                                                                                                                                                                                                   |
| PKO1          | Data type of the first primary column of the base table key | YES         | Value of the first primary column of the base table of the text search index for the row processed when the event occurred key being                                                                                                                             |
| PKnn          | Data type of the last primary column of the base table key  | YES         | Value of the last primary column of the base table of the text search index for the row processed when the event occurred key being                                                                                                                              |

Informational events, such as starting, committing, and finishing processing are also available in this view. In this case, PKO1, PKnn and OPERATION all have NULL values: The code page and the locale of MESSAGE correspond to the database update settings.

## SYSIBMTS.TSSTAGING view

The staging table stores the change operations on the user table that requires synchronization with the text search index

Triggers are created on the user table when the default LOGTYPE BASIC option is enabled to insert change information into the staging table: Alternatively, if the LOGTYPE CUSTOM is enabled, you must populate the staging table manually: In addition, with the auxiliary option, integrity processing detects changes to the user table: The UPDATE INDEX FOR TEXT command reads the entries and deletes them after successful synchronization: option log

The database might have multiple views with the SYSIBMTS.TSSTAGING\_\_ Each view is differentiated by the nnnnnn value, an internal identifier that points to the corresponding text index that the view is associated with: To determine the text search index that is associated with particular view, query the view SYSIBMTS TSINDEXES, searching for the schema name and view name in the columns STAGINGVIEWSCHEMA and STAGINGVIEWNAME: The query returns single row that describes the text search index and user table in question. prefix

The number of columns in this view depends on the number of primary columns in the user table: The columns PKI\_PKnn match the primary columns of the user table and have corresponding data type and lengths definitions. The data type of each of the columns in the view exactly corresponds to the data type of the corresponding primary column\_ key key key

Each row in this view represents an insert, a delete, or an operation on a user table row or text document. You can identify the text document by retrieving the primary column values from the row in this view and looking them up in the user table update key

You can use the following query to obtain information about the view: dbz "SELECT STAGINGVIEWSCHEMA, STAGINGVIEWNAME from SYSIBMTS . TSINDEXES where INDSCHEMA-schema-name and INDNAME-index-name

Table 19. SYSIBMTS.TSSTAGING view

| Column Name         | Data type                                         | Nullable?   | Description                                                                                                                                                                                                                                                                          |
|---------------------|---------------------------------------------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OPERATION           | INTEGER                                           | NO          | The operation the base table to be reflected on the text search index This column has the following four values: 0 insert 2= delete 4 = restart: You must not set or use this value for manual insert as it leads to wrong operation message for incremental index updates on update |
| TIME                | TIMESTAMP                                         | NO          | Sequence ID of a row (when an insert, an update, or delete trigger is fired). This is timestamp but might not exactly represent the time of the operation_                                                                                                                           |
| BKUPSTATUS| INTEGER |                                                   | NO          | Processing status of the row: -1 unprocessed 0 means processed >0 Backup count If the backup is enabled for index:)                                                                                                                                                                  |
| PKO1                | Data type of the columns in the indexed table key | YES         | First primary column of the base table_ key                                                                                                                                                                                                                                          |
| PKnn                | Data type of the columns in the indexed table key | YES         | Last primary key column of the base table:                                                                                                                                                                                                                                           |

## Index

## A

| ALTER INDEX Text Search   |
|---------------------------|
| command 134               |

| cataloging TCP IP nodes 63                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CLEANUP FOR TEXT Text Search command 139                                                                                                                                   |
| CLEAR COMMAND LOCKS Text Search command 140                                                                                                                                |
| CLEAR EVENTS FOR INDEX Text Search command 141 commands                                                                                                                    |
| db2ts ALTER INDEX 134 db2ts CLEANUP FOR TEXT 139 db2ts CLEAR COMMAND LOCKS 140 db2ts CLEAR EVENTS FOR INDEX 141 db2ts CREATE INDEX 143 db2ts DISABLE DATABASE FOR TEXT 152 |
| db2ts DROP INDEX 154 db2ts ENABLE DATABASE FOR                                                                                                                             |
| TEXT 156 db2ts HELP 158 db2ts RESET PENDING 159 db2ts SET COMMAND LOCKS 160 db2ts START FOR TEXT 161 db2ts STOP FOR TEXT 162                                               |
| db2ts UPDATE INDEX 163                                                                                                                                                     |
| CREATE INDEX Text Search                                                                                                                                                   |
| command 143                                                                                                                                                                |

## D

| Db2 servers installing Windows 46                                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------|
| Db2 Setup wizard installing Db2 servers (Linux) Db2 servers (UNIX) 49                                                                     |
| Db2 Text Search synonym dictionary administration commands administrative routines 93, 169 administrative views database-level 171 adding |
| 92, 133 index-level 171 SYSIBMTS.TSDEFAULTS 171 SYSIBMTS.TSSERVERS 173                                                                    |
| ALTER INDEX command 134                                                                                                                   |
| authorizations database administrator 23                                                                                                  |
| instance owner 23 roles 22                                                                                                                |

141

| Db2 Text Search (continued)                                   | Db2 Text Search (continued)                               |
|---------------------------------------------------------------|-----------------------------------------------------------|
| authorizations (continued) user performing text search 23     | authorizations (continued) user performing text search 23 |
| queries                                                       | queries                                                   |
| backing up 99                                                 | backing up 99                                             |
| basic search 105                                              | basic search 105                                          |
| capacity planning and                                         | capacity planning and                                     |
| optimization 25                                               | optimization 25                                           |
| 98                                                            | 98                                                        |
| changing location of collection CLEAR EVENTS FOR TEXT         | changing location of collection CLEAR EVENTS FOR TEXT     |
| command 141 code pages supported 20                           | command 141 code pages supported 20                       |
| collection location 98                                        | collection location 98                                    |
| command-line tools 75                                         | command-line tools 75                                     |
| commands                                                      | commands                                                  |
| ALTER INDEX 134                                               |                                                           |
| CLEAR EVENTS FOR TEXT                                         | CLEAR EVENTS FOR TEXT                                     |
| CREATE INDEX 143                                              | CREATE INDEX 143                                          |
| DISABLE DATABASE FOR                                          | DISABLE DATABASE FOR                                      |
| TEXT 152 DROP INDEX 154                                       | TEXT 152 DROP INDEX 154                                   |
| HELP 158                                                      | HELP 158                                                  |
| RESET PENDING 159                                             | RESET PENDING 159                                         |
| UPDATE INDEX 163                                              | UPDATE INDEX 163                                          |
| Configuration Tool 59                                         | Configuration Tool 59                                     |
| configuration tuning 25                                       | configuration tuning 25                                   |
| Configuration Tool 59                                         | Configuration Tool 59                                     |
| Db2 Setup Wizard 44                                           | Db2 Setup Wizard 44                                       |
| methods 57                                                    | methods 57                                                |
| overview 41                                                   | overview 41                                               |
| response file 45                                              | response file 45                                          |
| stand-alone server                                            | 54, 55, 61                                                |
| CONTAINS function                                             | 103, 123                                                  |
| CREATE INDEX command data types                               | 143                                                       |
| converting unsupported 19 supported 19                        | converting unsupported 19 supported 19                    |
| DISABLE DATABASE FOR TEXT command 152                         | DISABLE DATABASE FOR TEXT command 152                     |
| disabling databases 79                                        | disabling databases 79                                    |
| disabling rich text support                                   | 76                                                        |
| disk consumption 31                                           | disk consumption 31                                       |
| document formats 19                                           | document formats 19                                       |
| converting unsupported supported 19                           |                                                           |
| document truncation 20 DROP INDEX command 154                 | document truncation 20 DROP INDEX command 154             |
| enabling databases 78 enabling rich text support event tables | 76                                                        |
| overview 83 descriptors 35                                    | overview 83 descriptors 35                                |
| file                                                          | file                                                      |
| filter libraries 63                                           | filter libraries 63                                       |
| functions 103 43                                              | functions 103 43                                          |
| hardware requirements                                         | hardware requirements                                     |
| 26                                                            | 26                                                        |
| memory consumption heap                                       |                                                           |
| HELP command 158 incremental index updates 94                 | HELP command 158 incremental index updates 94             |
| indexes binary data types 86                                  | indexes binary data types 86                              |

| Db2 Text Search (continued)                             |
|---------------------------------------------------------|
| indexes (continued) 83                                  |
| creating                                                |
| creating (binary data types) 86                         |
| incremental updates 11, 94                              |
| index-specific parameters for                           |
| updates 33                                              |
| location 32                                             |
| optimizing 29, 30                                       |
| performance 29                                          |
| planning 29                                             |
| special characters 109                                  |
| threads 27 indexing                                     |
| installing                                              |
| Db2 Accessories Suite filter libraries 63 Db2 Wizard 44 |
| db2_install command 46 Setup                            |
| disk space requirements 54                              |
| overview 41                                             |
| response file 45                                        |
| stand-alone server 54, 55 integrated server             |
| languages 20, 36                                        |
| linguistic processing 13                                |
| locales 36                                              |
| log tables 83                                           |
| maximum size 26 heap                                    |
| morphological indexing 89 87 ,                          |
| multiple predicates 36                                  |
| upgrade 70                                              |
| overview 1,3                                            |
| configuration 38 parser                                 |
| performance 29, 35 proximity search 107                 |
| queries 35                                              |
| queue memory size 28                                    |
| reconfiguring 57 , 59                                   |
| removing synonym dictionary                             |
| RESET PENDING command 159 restoring                     |
| process 99                                              |
| RESULTLIMIT function 38                                 |
| rich text                                               |
| Db2 Accessories Suite 63 enabling 76                    |
| overview 17                                             |
| roles                                                   |
| database administrator 23                               |
| instance owner 23                                       |
| user performing searches 23 scenario 14                 |
| scheduling task 101                                     |
| 37, 103                                                 |
| 35                                                      |
| syntax 113                                              |
| 103                                                     |
| search functions                                        |
| searching indexes                                       |
| performance implications                                |
| SCORE function                                          |
| search arguments                                        |

103

Db2 Text Search (continued)

removing messages

175

| DB2 Text Search (continued) Index Manager                                                                                                                                | search 105 improving search performance 121 23 fuzzy   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| searching updating commands 75 overview 19 SCORE function 125 SET COMMAND LOCKS command 160 special characters adjacent to query terms CJK languages 110 SQL 104 issuing | 109                                                    |
| starting STOP FOR TEXT command text search collections deleting orphaned identifying orphaned                                                                            | 162                                                    |
| 80 80 triggers 30 unsupported data types 86 updating text index 93 XQuery                                                                                                |                                                        |
| full-text search methods db2ts commands ALTER INDEX 134 CLEANUP FOR TEXT                                                                                                 | 104                                                    |
| 139 CLEAR COMMAND LOCKS CLEAR EVENTS FOR INDEX                                                                                                                           | 140 141 143                                            |
| CREATE INDEX DISABLE DATABASE FOR TEXT 152 154                                                                                                                           |                                                        |
| 176DROP INDEX ENABLE DATABASE FOR TEXT HELP 158                                                                                                                          | 159 160                                                |
| RESET PENDING SET COMMAND LOCKS START FOR TEXT STOP FOR TEXT 162                                                                                                         | 161                                                    |
| UPDATE INDEX 163                                                                                                                                                         |                                                        |
| DISABLE DATABASE FOR TEXT Text Search command 152                                                                                                                        |                                                        |
|                                                                                                                                                                          | 154                                                    |
| DROP INDEX Text Search                                                                                                                                                   |                                                        |
| command                                                                                                                                                                  |                                                        |

156

## E

| ENABLE DATABASE FOR TEXT Text   |
|---------------------------------|
| Search command 156              |

| HELP command    |
|-----------------|
| Text Search 158 |

| searching (continued)                                    |
|----------------------------------------------------------|
| SCORE function 112                                       |
| characters 107 special                                   |
| security overview 21, 24                                 |
| server configuration 25                                  |
| software requirements 43                                 |
| SQL 123 stand-alone installation 46                      |
| stand-alone server                                       |
| configuring 61 deploying                                 |
| stopping instance services 77 synonym dictionaries       |
| adding 82                                                |
| overview 82                                              |
| removing 83                                              |
| system 34 tuning                                         |
| TCP /IP port requirements 34                             |
| triggers 83                                              |
| uninstalling Db2 Accessories Suite 65                    |
| 55                                                       |
| uninstalling server                                      |
| UPDATE INDEX command 163                                 |
| updating server information 60                           |
| user roles 22                                            |
| viewing index status 98                                  |
| XML columns 128                                          |
| XML documents 110, 117 39                                |
| XML namespaces                                           |
| XML search functions 123                                 |
| xmlcolumn-contains function 103                          |
| XQuery xmlcolumn-contains 128                            |
| DB2 Text Search administrative views                     |
| database-level 172                                       |
| event table 176                                          |
| index-level 173, 175, 176, 177                           |
| table 177 log                                            |
| staging table 177                                        |
| SYSIBMTS. TSCOLLECTIONNAMES                              |
| SYSIBMTS.TSCONFIGURATION                                 |
| SYSIBMTS.TSEVENT 176                                     |
| SYSIBMTS.TSINDEXES 173                                   |
| SYSIBMTS.TSLOCKS 172                                     |
| SYSIBMTS TSSTAGING 177                                   |
| altering indexes 97                                      |
| 30                                                       |
| asynchronous indexing                                    |
| changing update characteristics 97                       |
| CLEAR COMMAND LOCKS command 140                          |
| clearing text search index events 96                     |
| commands                                                 |
| CLEANUP FOR TEXT 139                                     |
| CLEAR COMMAND LOCKS 140 ENABLE DATABASE FOR              |
| TEXT 156                                                 |
| SET COMMAND LOCKS 160 START FOR TEXT 161                 |
| STOP FOR TEXT 162                                        |
| 100                                                      |
| dropping indexes command 156                             |
| ENABLE DATABASE FOR TEXT escaping special characters 108 |

| installation silent   |
|-----------------------|
| Linux 53              |
| UNIX 53               |
| Windows 52            |

| Linux installing   |    |
|--------------------|----|
| Db2 servers        | 49 |
| response file      | 53 |

## R

| RESET PENDING Db2 Text Search command 159 response files   |
|------------------------------------------------------------|
| installation                                               |
| Linux 53                                                   |
| UNIX 53                                                    |
| Windows 52                                                 |

## S

| SCORE function searching text search indexes 125 services file updating for TCP /IP communications 63   |
|---------------------------------------------------------------------------------------------------------|
| SET COMMAND LOCKS Text Search command 160 silent installation                                           |
| Linux 53 UNIX 53 Windows 52 START FOR TEXT Text Search                                                  |
| command 161                                                                                             |
| STOP FOR TEXT Text Search command 162 synonym dictionaries                                              |
| adding 82 overview 82 removing 83                                                                       |
| SYSIBMTS.TSINDEXES view 173                                                                             |
| SYSIBMTS.TSSERVERS view                                                                                 |

| TCP /IP updating services file    |
|-----------------------------------|
| text indexes proximity search 107 |
| Text Search see Db2 Text Search   |
| text searches                     |
| Db2 Text Search 76                |

## U

| UNIX           |
|----------------|
| installing     |
| Db2 servers 49 |

| UNIX (continued)              |
|-------------------------------|
| response file installation 53 |
| UPDATE INDEX Text Search      |
| command 163                   |

| views for Db2 Text Search database-level information overview 171 SYSIBMTS.TSDEFAULTS 171 index-level information overview 171   |
|----------------------------------------------------------------------------------------------------------------------------------|
| views for DB2 Text Search database-level information SYSIBMTS.TSLOCKS 172 index-level information                                |
| SYSIBMTS. TSCOLLECTIONNAMES 176                                                                                                  |
| SYSIBMTS.TSCONFIGURATION 175                                                                                                     |
| SYSIBMTS.TSEVENT 176                                                                                                             |
| 173                                                                                                                              |
| SYSIBMTS.TSINDEXES                                                                                                               |
| SYSIBMTS TSSTAGING 177                                                                                                           |

## W

| Windows installing                     |
|----------------------------------------|
| Db2 servers (with Db2 Setup wizard) 46 |
| response files installing using 52     |

| XML Db2 Text Search EBNF grammar 110 search syntax 117              |     |
|---------------------------------------------------------------------|-----|
| XML columns text search 128 XML namespaces 39                       | 128 |
| xmlcolumn-contains function XQuery functions xmlcolumn-contains 128 |     |

Printed in USA