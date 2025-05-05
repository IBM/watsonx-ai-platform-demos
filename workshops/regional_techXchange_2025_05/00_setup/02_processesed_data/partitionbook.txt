## Partition and Clustering Guide

<!-- image -->

## Partition and Clustering Guide

<!-- image -->

## Notice regarding this document

This document in PDF form is provided as a courtesy to customers who have requested documentation in this format: It is provided As-Is without warranty or maintenance commitment:

## Contents

| Redistributing data across database partitions by using the REDISTRIBUTE DATABASE PARTITION   | 79   |
|-----------------------------------------------------------------------------------------------|------|
| GROUP command                                                                                 |      |
| Redistributing database partition groups the STEPWISE_REDISTRIBUTE_DBPG procedure using       | 80   |
| Monitoring data redistribution operation                                                      | 82   |
| Redistribution event files log                                                                | 83   |
| Recovery from errors related to data redistribution                                           | 84   |

## Figures

| 1   | Intrapartition parallelism 3                                                                               |
|-----|------------------------------------------------------------------------------------------------------------|
| 2_  | Interpartition parallelism                                                                                 |
| 3_  | Simultaneous interpartition and intrapartition parallelism 5 Single database partition on single processor |
| 4   | 6                                                                                                          |
| 5_  | Single partition database symmetric multiprocessor environment                                             |
| 6_  | Massively parallel processing (MPP) environment 8                                                          |

10.

11.

| 7   | Several symmetric multiprocessor (SMP) environments in a cluster                     |    |
|-----|--------------------------------------------------------------------------------------|----|
| 8   | Partitioned database with symmetric multiprocessor environment                       | 10 |
| 9   | Partitioned database with symmetric multiprocessor environments clustered together _ | 11 |
|     | Database partition groups in database                                                |    |
|     | Data distribution using                                                              | 22 |
|     | distribution map                                                                     |    |

## Tables

|   13 | Types of Possible Parallelism in Each Hardware Environment 11   |
|------|-----------------------------------------------------------------|
|    2 | Database partition expressions 52                               |

- 3 Environment variables that control the rah command 62

## Chapter 1. Partitioned database environments

A partitioned database environment is a database installation that supports the distribution of data across database partitions.

- A database partition is a part of a database that consists of its own data, indexes, configuration files, and transaction logs: A partitioned database environment is database installation that supports the distribution of data across database partitions.
- A single-partition database is a database having only one database partition: All data in the database is stored in that single database partition. In this case,
- A multi-partition database is a database with two or more database partitions. Tables can be located in one or more database partitions. When a table is in a database partition group consisting of multiple database partitions, some of its rows are stored in one database partition, and other rows are stored in other database partitions.

Usually, a single database partition exists on each physical machine, and the processors on each system are used by the database manager at each database partition to manage its part of the total data in the database:

Because data is distributed across database partitions, you can use the power of multiple processors on multiple physical machines to satisfy requests for information. Data retrieval and update requests are decomposed automatically into sub-requests, and executed in parallel among the applicable database partitions. The fact that databases are split across database partitions is transparent to users issuing SQL statements\_

User interaction occurs through one database partition, known as the coordinator partition for that user: The coordinator partition runs on the same database partition as the application, or in the case of a remote application, the database partition to which that application is connected. database partition can be used as coordinator partition. Any

The database manager allows you to store data across several database partitions in the database: This means that the data is physically stored across more than one database partition, and yet can be accessed as though it were located in the same place. Applications and users accessing data in multi-partition database are unaware of the physical location of the data.

Although the data is physically split; it is used and managed as logical whole: Users can choose how to distribute their data by declaring distribution keys. Users can also determine across which and over how database partitions their data is distributed by selecting the table space and the associated database partition group in which the data is to be stored. Suggestions for distribution and replication can be done the Db2 Design Advisor: In addition, an updatable distribution map is used with hashing algorithm to specify the mapping of distribution values to database partitions, which determines the placement and retrieval of each row of data: As a result, Yu can spread the workload across multi-partition database for large tables, and store smaller tables on one or more database partitions. Each database partition has local indexes on the data it stores, resulting in increased performance for local data access many using key

## Parallelism

Note: You are not restricted to all tables divided across all database partitions in the database. The database manager supports declustering, which means that you can divide tables and their table spaces across a subset of database partitions in the system. having partial

An alternative to consider when you want tables to be positioned on each database partition, is to use materialized query tables and then replicate those tables. You can create materialized query table containing the information that you need, and then replicate it to each database partition:

A non-root installation of a Db2 database product does not support database partitioning: Do not manually the dbznodes.cfg file: A manual update returns an error (SQL6OB1N): update

## Related information:

<!-- image -->

(artname: sout:gif) Best practices: Managing data growth

Components of a task, such as database query, can be run in parallel to dramatically enhance performance: The nature of the task, the database configuration, and the hardware environment, all determine how the Db2 database product will perform a task in parallel.

These factors are interrelated. Consider them all when you work on the physical and logical of a database. The following types of parallelism are supported by the Db2 database design system:

- I/0
- Query
- Utility

## Inputloutput parallelism

parallel IO. Parallel I/0 refers to the process of writing to, or reading from, two or more I/0 devices simultaneously; it can result in significant improvements in throughput:

## Query parallelism

There are two types of query parallelism: interquery parallelism and intraquery parallelism.

Interquery parallelism refers to the ability of the database to accept queries from multiple applications at the same time Each query runs independently of the others, but the database manager runs all of them at the same time. Db2 database products have always supported this type of parallelism:

Intraquery parallelism refers to the simultaneous processing of parts of a single query; either intrapartition parallelism, interpartition parallelism, or both: using

## Intrapartition parallelism

Intrapartition parallelism refers to the ability to break up a query into multiple parts Some Db2 utilities also perform this type of parallelism.

Intrapartition parallelism subdivides what is typically considered to be a single database operation such as index creation, database loading, or SQL queries into multiple parts, many or all of which can be run in parallel within a single database partition.

Figure 1 shows a query that is broken into three pieces that can be run in parallel, with the results returned more quickly than if the query were run in serial fashion. The pieces are copies of each other To use intrapartition parallelism; you must configure the database appropriately You can choose the degree of parallelism or let the system do it for you: The degree of parallelism represents the number of pieces of a query running in parallel:

<!-- image -->

(artname: 00000226.gif)\_

Figure 1. Intrapartition parallelism

## Interpartition parallelism

Interpartition parallelism refers to the ability to break up a query into multiple parts across multiple partitions of a partitioned database, on one machine or multiple machines. The query is run in parallel. Some Db2 utilities also perform this type of parallelism.

Interpartition parallelism subdivides what is typically considered a single database operation such as index creation, database loading, or SQL queries into multiple parts, many or all of which can be run in parallel across multiple partitions of a partitioned database on one machine or on multiple machines.

Figure 2 on page 4 shows a query that is broken into three pieces that can be run in parallel, with the results returned more quickly than if the query were run in serial fashion on single database partition:

The degree of parallelism is largely determined by the number of database partitions create and how you define your database partition groups. you

<!-- image -->

(artname: 00000225.gif) Figure 2. Interpartition parallelism

## Simultaneous intrapartition and interpartition parallelism

You can use intrapartition parallelism and interpartition parallelism at the same time This combination provides dimensions of parallelism, resulting in an even more dramatic increase in the speed at which queries are processed. two

(artname: Q0000159.gif) Figure 3. Simultaneous interpartition and intrapartition parallelism

<!-- image -->

## Utility parallelism

Db2 utilities can take advantage of intrapartition parallelism: can also take advantage of interpartition parallelism; where multiple database partitions exist, the utilities run in each of the database partitions in parallel. They

The load utility can take advantage of intrapartition parallelism and I/0 parallelism: Loading data is CPU-intensive task. The load utility takes advantage of multiple processors for tasks such as parsing and formatting data. It can also use

In partitioned database environment; the LOAD command takes advantage of intrapartition, interpartition, and I/0 parallelism by parallel invocations at each database partition where the table resides

During index creation, the scanning and subsequent sorting of the data occurs in parallel. The Db2 system exploits both I/0 parallelism and intrapartition parallelism when creating an index: This helps to speed up index creation when a CREATE INDEX statement is issued, restart (if an index is marked invalid), and the reorganization of data during during

Backing up and restoring data are heavily I/0-bound tasks. The Db2 system exploits both I/0 parallelism and intrapartition parallelism when performing backup and restore operations. Backup exploits /0 parallelism by reading from multiple table space containers in parallel, and asynchronously writing to multiple backup media in parallel.

## Database partition and processor environments

This section provides an overview of both single database partition and multiple database partition configurations. The former include single processor (uniprocessor) and multiple processor (SMP) configurations, and the latter include database partitions with one processor (MPP) or multiple processors (cluster of SMPs) , and logical database partitions

Capacity refers to the number of users and applications able to access the database: This is in part determined by memory, agents, locks, I/0, and storage management. Scalability refers to the ability of a database to and continue to exhibit the same operating characteristics and response times. Capacity and scalability are discussed for each environment: large grow

## Single database partition on a single processor

This environment is made up of memory and disk, but contains only single CPU (see Figure 4). The database in this environment serves the needs of a department Or small office, where the data and system resources (including a single processor or CPU) are managed by a single database manager:

## Uniprocessor environment

(artname: 00000236.5 Figure 4. Single database partition on single processor gif)

<!-- image -->

## Capacity and scalability

In this environment you can add more disks. Having one or more I/0 servers for each disk allows for more than one I/0 operation to take place at the same time.

single-processor is restricted by the amount of disk space the processor can handle. As workload increases, a single CPU might not be able to process user requests any faster; regardless of other components, such as memory Or disk, that you might add. If you have reached maximum capacity Or scalability, you can consider moving to single database partition system with multiple processors system

## Single database partition with multiple processors

This environment is typically made up of several equally powerful processors within the same machine (see Figure 5), and is called a symmetric multiprocessor (SMP) system. Resources, such as disk space and memory, are shared.

With multiple processors available, different database operations can be completed more quickly Db2 database systems can also divide the work of a single query among available processors to improve processing Other database operations, such as loading data, backing up and restoring table spaces, and creating indexes on existing data, can take advantage of multiple processors speed.

## Symmetric multiprocessor (SMP) environment

(artname: 00000217 Figure 5. Single database symmetric multiprocessor environment

<!-- image -->

## Capacity and scalability

You can increase the I/0 capacity of the database partition associated with your processor by increasing the number of disks. You can establish I/0 servers to specifically deal with I/0 requests. Having one or more I/0 servers for each disk allows for more than one I/0 operation to take place at the same time scalability, you can consider moving to system with multiple database partitions.

## Multiple database partition configurations

You can divide a database into multiple database partitions, each on its own machine. Multiple machines with multiple database partitions can be grouped together: This section describes the following database partition configurations:

- Database partitions on systems with multiple processors
- Database partitions on systems with one processor
- Logical database partitions

## Database partitions with one processor

In this environment, there are many database partitions. Each database partition resides on its own machine, and has its own processor; memory, and disks (Figure 6). All the machines are connected by a communications facility: This environment is referred to by many different names, including: cluster, cluster of uniprocessors, massively parallel processing (MPP) environment, and shared-nothing configuration: The latter name accurately reflects the arrangement of resources in this environment: Unlike an SMP environment; an MPP environment has no shared memory or disks. The MPP environment removes the limitations introduced through the sharing of memory and disks

A partitioned database environment allows a database to remain a logical whole, despite being physically divided across more than one database partition: The fact that data is distributed remains transparent to most users. Work can be divided among the database managers; each database manager in each database partition works against its own part of the database.

(artname: 00000194.gif) Figure 6. Massively parallel processing (MPP) environment

<!-- image -->

## Capacity and scalability

In this environment you can add more database partitions to your configuration: On some platforms the maximum number is 512 database partitions. However; there might be practical limits on managing a high number of machines and instances\_

If you have reached maximum capacity or scalability, you can consider moving to system where each database partition has multiple processors.

## Database partitions with multiple processors

An alternative to a configuration in which each database partition has a single processor; is a configuration in which each database partition has multiple processors. This is known as an SMP cluster (Figure 7).

This configuration combines the advantages of SMP and MPP parallelism. This means that a query can be performed in single database partition across multiple processors. It also means that a query can be performed in parallel across multiple database partitions.

(artname: 00000218.gif) Figure 7. Several symmetric multiprocessor (SMP) environments in a cluster

<!-- image -->

## Capacity and scalability

In this environment you can add more database partitions, and you can add more processors to existing database partitions

## Logical database partitions

A logical database partition differs from physical partition in that it is not given control of an entire machine. Although the machine has shared resources, database partitions do not share the resources. Processors are shared but disks and memory are not

Logical database partitions provide scalability Multiple database managers running on multiple logical partitions can make fuller use of available resources than single database manager can: Figure 8 on page 10 illustrates the fact that You can more scalability on an SMP machine by more database partitions; this adding gain

is particularly true for machines with processors. By distributing the database, you can administer and recover each database partition separately: many

## Big SMP environment

<!-- image -->

(artname: 00000189.

Figure 9 on page 11 illustrates that you can multiply the configuration shown in Figure 8 to increase processing power:

<!-- image -->

(artname: 90000219.gif)

Figure 9. Partitioned database with symmetric multiprocessor environments clustered together

Note: The ability to have two or more database partitions coexist on the same machine (regardless of the number of processors) allows flexibility in designing high availability configurations and failover strategies. Upon machine failure, a database partition can be automatically moved and restarted on second machine that already contains another database partition of the same database: greater

## Summary of parallelism best suited to each hardware environment

The following table summarizes the types of parallelism best suited to take advantage of the various hardware environments\_

Table 1 Types of Possible Parallelism in Each Hardware Environment

| Hardware Environment                                 | I/O Parallelism   | Intra-Query Parallelism     | Intra-Query Parallelism     |
|------------------------------------------------------|-------------------|-----------------------------|-----------------------------|
|                                                      |                   | Intra-Partition Parallelism | Inter-Partition Parallelism |
| Single Database Partition, Single Processor          | Yes               | No                          | No                          |
| Single Database Partition, Multiple Processors (SMP) | Yes               | Yes                         | No                          |
| Multiple Database Partitions, One Processor (MPP)    | Yes               | No                          | Yes                         |

Table 1. Types of Possible Parallelism in Each Hardware Environment (continued)

| Hardware Environment                                                | I/O Parallelism   | Intra-Query Parallelism     | Intra-Query Parallelism     |
|---------------------------------------------------------------------|-------------------|-----------------------------|-----------------------------|
|                                                                     |                   | Intra-Partition Parallelism | Inter-Partition Parallelism |
| Multiple Database Partitions, Multiple Processors (cluster of SMPs) | Yes               | Yes                         | Yes                         |
| Logical Database Partitions                                         | Yes               | Yes                         | Yes                         |

## Chapter 2. Column-organized tables in a Partitioned database environment

column-organized tables in a massively parallel processing (MPP) environment may improve performance or reduce cost, depending on the nature of your workload. Using

There are no general guidelines to determine whether a particular workload should use column-organized tables. This should be examined on a case by case basis. In general, the same guidelines for performance in non-massively parallel processing (MPP) environments apply in MPP environments. In certain scenarios, vector processing of column data in a partitioned database environment provides significant improvements to storage, query performance, and ease of use through simplified design and tuning:

If already have column-organized tables, but not in a massively parallel processing (MPP) environment, consider moving to an MPP environment\_ The following are some of the benefits of column-organized tables in an MPP environment: you

- Column-organized table storage capacity can be increased. The maximum column-organized table size in a non-MPP environment is 64TB of compressed data A partitioned database environment distributes the table across additional database members. Each new member allows the maximum table size to increase\_
- The columnar workload's resources such as processors, memory and disks are increased by having multiple servers in parallel. Consider this factor of MPP only when the maximum resources of your non-MPP environment have already been applied. Consider whether or not the target workload will benefit from performance objectives, and the cost and operational considerations of each option.

You must decide whether or not column-organized tables in an MPP environment will meet the performance of your target workload and be cost efficient: For example, MPP environments may increase operational costs Since there will be multiple database partitions to monitor and maintain: goals

If you would like to create a new MPP environment with column-organized tables, ensure the prerequisites for column-organized tables in non-partitioned databases are met before doing so. If you plan to introduce column-organized tables into an existing MPP environment there are three approaches you can take:

- Replacing all existing tables
- Replacing some tables
- Creating new and independent tables

## Prerequisities for adopting column-organized tables in partitioned databases

If you would like to introduce column-organized tables into a partitioned database, the database must meet the prerequisites for column-organized tables in non-partitioned databases.

If you are creating a new massively parallel processing (MPP) environment and plan to populate it with column-organized tables, follow the general system and configuration recommendations for column-organized tables. Set DBZ\_WORKLOAD to ANALYTICS before you create the database: This automatically configures the database for columnar workloads. sizing

If you want to introduce column organized tables into an existing MPP environment, follow the recommendations mentioned above: However; run the AUTOCONFIGURE utility with the APPLY NONE option to view the recommended configuration changes when running column-organized tables.

There are three approaches you can take to introducing column-organized tables into your partitioned database environments. These are the replacement, hybrid, Or independent methods:

- Replacement
- Replace all traditional row-organized tables with column-organized tables
- Hybrid
- Convert some of the row-organized tables to column-organized tables, or add new column-organized tables to an existing rOW table schema.
- Independent
- Introduce a new, independent columnar workload with no interaction with any existing workload or rOw table schema.

## Replacing all row-organized tables with column-organized tables in a partitioned database environment

Use the dbzconvert command to convert your roW-organized tables into column-organized tables

## Before you begin

Switching to column-organized tables will affect the performance and use of resources of the system. Review the best practices for column-organized tables for recommendations on the memory cores, and storage to provide for your desired dataset size

## About this task

There are several ways to convert row-organized tables to column-organized tables. One way is to use the dbzconvert command. If the database is not recoverable, simply run the dbzconvert command: If it is recoverable, you must run the command, make a backup of the database, and then rerun the command to complete the conversion:

## Procedure

To replace all row-organized tables with column-organized tables in a non-recoverable database:

- Run the dbzconvert command on the desired database: dbzconvert ~d &lt;name\_of\_database&gt;

To all row-organized tables with column-organized tables in a recoverable database: replace

- Complete the first part of the conversion by running dbzconvert with the ~stopBeforeSwap parameter; backup the database where you plan to store the converted tables, and then complete the conversion by running the command again:

dbzconvert &lt;name\_of\_database&gt; ~S topBeforeSwap;

BACKUP DB &lt;name 0f database&gt; ONLINE TO &lt;destination&gt;

BACKUP DB &lt;name\_of\_database&gt; TABLESPACE &lt;target\_data\_table\_space&gt; ONLINE To &lt;destinationz;

dbzconvert &lt;name\_of\_database&gt; ~continue;

Where:

- ~stopBeforeSwap specifies that db2convert stops before it performs the SWAP of the ADMIN\_MOVE\_TABLE procedure and prompts you to complete an online backup operation before continuing: phase
- ~continue completes the conversion process.

## Adopting a hybrid environment

Use the dbzconvert command to retain some roW-organized tables, but the rest with column-organized tables. replace

## Before you begin

- Ensure you implement best practices for column-organized table configuration
- To minimize the impact of the configuration changes on the row-table applications, set the DEGREE value for the row-table applications to 1 and the column-table applications to ANY. Use the MAXIMUM\_DEGREE attribute to achieve this:

## About this task

One of the ways to convert roW-organized to column-organized tables is the dbzconvert command. If the database is recoverable, you must backup the database before completing the conversion, as in the replacement method.

## Procedure

To replace only some roW-organized tables with column-organized tables in a non-recoverable database:

Run the db2convert command on the database schema and tables you would like to be column-organized:

dbzconvert -d &lt;name 0f database&gt; &lt;schema&gt; ~t &lt;table name&gt;

## Where:

- specifies the schema name of one or more tables to convert\_
- specifies the unqualified name of the table to convert:

## Creating an independent column-organized; partitioned environment

Introduce a columnar workload to co-exist with, but not interact with, existing rOw applications by loading new dataset into the database.

## Before you begin

- Review the best practices for column-organized table configuration

- To minimize the impact of the configuration changes on the row-table applications, set the DEGREE value for the row-table applications to 1 and the column-table applications to ANY Use the MAXIMUM\_DEGREE attribute to achieve this.

## About this task

Create new column-organized tables in the database, then load the desired information into them:

## Procedure

To introduce independent columnar workloads to the database:

- 1. Create a table by running the CREATE TABLE command with the ORGANIZE BY COLUMN option:
- 2 Load data into the table the INGEST, INSERT, IMPORT, or LOAD command: LOAD FROM &lt;file\_with\_data&gt; of &lt;file\_with\_data' s\_directory&gt; REPLACE &lt;new\_table using

```
CREATE TABLE <new_table_name> <co]umn 1> <datatype> _ <co]umn 2> <datatype> <co]umn 3> <datatypez) ORGANIZE BY COLUMN;
```

name&gt;

## Chapter 3. Database partitioning across multiple database partitions

The database manager allows great flexibility in spreading data across multiple database partitions of a partitioned database.

Users can choose how to distribute their data by declaring distribution keys, and can determine which and how many database partitions their table data can be spread across by selecting the database partition group and table space in which the data is to be stored:

In addition, a distribution map (which is updatable) specifies the mapping of distribution values to database partitions This makes it possible for flexible workload parallelization across partitioned database for large tables, while allowing smaller tables to be stored on one or small number of database partitions if the application designer s0 chooses. Each local database partition can have local indexes on the data it stores to provide high performance local data access. key

In a partitioned database, the distribution is used to distribute table data across a set of database partitions. Index data is also partitioned with its corresponding tables, and stored locally at each database partition. key

Before database partitions can be used to store data, must be defined to the database manager: Database partitions are defined in file called dbznodes.cfg: they

The distribution for a table in table space on partitioned database partition group is specified in the CREATE TABLE statement or the ALTER TABLE statement When specified through the CREATE TABLE statement the distribution selection is dependent on the DISTRIBUTE BY clause in use: key key

- If DISTRIBUTE BY HASH is specified, the distribution keys are the keys explicitly included in the column list following the HASH keyword.
- If DISTRIBUTE BY RANDOM is specified, the distribution is selected by the database manager in an effort to spread data evenly across all database partitions the table is defined on. There are two methods that the database manager uses to achieve this: key
- Random by generation: If the table does not have a unique Or primary the database manager will include a column in the table to generate and store generated value to use in the hashing function. The column will be created with the IMPLICITLY HIDDEN clause so that it does not appear in queries unless explicitly included: The value of the column will be automatically generated as new rows are added to the table: By default, the column name is RANDOM\_DISTRIBUTION\_KEY. If it collides with the existing column, a non-conflicting name will be generated by the database manager: key,
- Random by unique: If the table includes a unique or primary key, it uses the unique characteristics of the columns to create random spread of the data. The columns of the unique or primary are used as the distribution key key keys:
- If DISTRIBUTE BY REPLICATION is specified, this means that a copy of all of the data in the table exists on each database partition, so no distribution are selected. This can only be specified for materialized query table keys option

- If not specified, a distribution for a table is created by default: A table in a table space that is in a single partition database partition group will have a distribution only if it is explicitly specified. key key

Rows are placed in a database partition as follows:

- 1. A hashing algorithm (database partitioning function) is applied to all of the columns of the distribution which results in the generation of a distribution map index value: key,
- 2. The database partition number at that index value in the distribution map identifies the database partition in which the IOw is to be stored.

The database manager supports partial declustering, which means that a table can be distributed across subset of database partitions in the (that is, a database partition group). Tables do not have to be distributed across all of the database partitions in the system system.

The database manager has the capability of recognizing when data accessed for a join or subquery is located at the same database partition in the same database partition group. This is known as table collocation. Rows in collocated tables with the same distribution values are located on the same database partition: The database manager can choose to perform join or subquery processing at the database partition in which the data is stored. This can have significant performance advantages. being key

Random distribution tables that are random by generation method generally cannot take advantage of table collocation because the distribution is based on the generated value of the RANDOM\_DISTRIBUTION\_KEY column. using key

## Collocated tables must:

- Be in the same database partition group, one that is not being redistributed. (During redistribution, tables in the database partition group might be different distribution maps are not collocated:) using they
- Have distribution keys with the same number of columns.
- Have the corresponding columns of the distribution be database partition-compatible: key
- Single-partition tables are collocated only if are defined in the same database partition group. they

## Chapter 4. Database partition groups

A database partition group is named set of one or more database partitions that to database. belong database partition group that contains more than one database partition is known as multiple partition database partition group. Multiple partition database partition groups can only be defined with database partitions that belong to the same instance:

Figure 10 shows an example of a database with five database partitions.

- Database partition group 2 contains one database partition.
- Database partition group 1 contains all but one of the database partitions
- Database partition group 3 contains two database partitions.
- A single database partition in Group 3 is shared (and overlaps) with Group 1.
- The database partition in Group 2 is shared (and overlaps) with Group 1.

## Database

<!-- image -->

(artname: 00000372-gif) Figure T0. Database partition groups in a database

When a database is created, all database partitions that are specified in the database partition configuration file named dbznodes.cfg are created as well. Other database partitions can be added or removed with the ADD DBPARTITIONNUM or DROP DBPARTITIONNUM VERIFY command, respectively: Data is divided across all of the database partitions in a database partition group:

When a database partition group is created, a distribution map is associated with the group. The distribution map, with a distribution and a hashing algorithm are used by the database manager to determine which database partition in the database partition group will store a given TOW of data. along key

## Default database partition groups

Three database partition groups are defined automatically at database creation time:

- IBMCATGROUP for the SYSCATSPACE table space, holding system catalog tables
- IBMTEMPGROUP for the TEMPSPACEL table space, holding temporary tables created during database processing
- IBMDEFAULTGROUP for the USERSPACEL table space, holding user tables and indexes. A user temporary table space for a declared temporary table or a created temporary table can be created in IBMDEFAULTGROUP or any user-created database partition group, but not in IBMTEMPGROUP

## Table spaces in database partition groups

When a table space is associated with multiple partition database partition group (during execution of the CREATE TABLESPACE statement), all of the tables within partition group. A table space that is associated with particular database partition group cannot later be associated with another database partition group.

## Creating a database partition group

Create a database partition group by using the CREATE DATABASE PARTITION GROUP statement: This statement specifies the set of database partitions on which the table space containers and table data are to reside. This statement also performs the following actions:

- It creates a distribution map for the database partition group.
- It generates distribution map ID.
- It inserts records into the following catalog views:
- SYSCATDBPARTITIONGROUPDEF
- SYSCATDBPARTITIONGROUPS
- SYSCATPARTITIONMAPS

## Altering a database partition group

Use the ALTER DATABASE PARTITION GROUP statement to add database partitions to (or them from) database partition group. After adding or dropping database partitions, use the REDISTRIBUTE DATABASE PARTITION GROUP command to redistribute the data across the set of database partitions in the database partition group. drop

## Database partition group design considerations

Place tables in single-partition database partition groups, except when you want to take advantage of collocation with a larger table: Collocation is the placement of rows from different tables that contain related data in the same database partition. Collocated tables help the database manager to use more efficient join strategies Such tables can exist in a single-partition database partition group. Tables are considered to be collocated if are in a multiple partition database partition group, have the same number of columns in the distribution and if the data types of corresponding columns are compatible. Rows in collocated tables with the same distribution value are on the same database partition. Tables can be in separate table spaces in the same database partition grOup, and still be considered collocated small they placed key

Avoid extending medium-sized tables across too many database partitions. For example, 100-MB table might perform better on 16-partition database partition group than on 32-partition database partition group.

You can use database partition groups to separate online transaction processing (OLTP) tables from decision support (DSS) tables: This will help to ensure that the performance of OLTP transactions is not adversely affected.

If you are using a multiple partition database partition group, consider the following points:

- Each database partition must be assigned a unique number; because the same database partition might be found in one or more database partition groups.
- In multiple partition database partition group, you can only create unique index if the index is a superset of the distribution key:
- To ensure fast recovery of a database partition containing system catalog tables, avoid placing user tables on the same database partition. Place user tables in database partition groups that do not include the database partition in the IBMCATGROUP database partition group.

## Distribution maps

In a partitioned database environment; the database manager must know where to find the data that it needs. The database manager uses map, called a distribution map, to find the data:

distribution map is an internally generated array containing either 32 768 entries for multiple-partition database partition groups, Or a Single entry for single-partition database partition groups. For a single-partition database partition group, the distribution map has only one entry containing the number of the database partition where all the rows of a database table are stored: For multiple-partition database partition groups, the numbers of the database partition group are specified in a way such that each database partition is used one after the other to ensure an even distribution across the entire map. Just as city map is organized into sections grid, the database manager uses distribution key to determine the location (the database partition) where the data is stored: using

For example, assume that you have a database on four database partitions (numbered 0-3). The distribution map for the IBMDEFAULTGROUP database partition group of this database is:

<!-- formula-not-decoded -->

If a database partition group had been created in the database database partitions 1 and 2, the distribution map for that database partition group is: using

1 2 1 2 1 2 1

If the distribution for a table to be loaded into the database is an integer with possible values between 1 and 500 000, the distribution is hashed to a number between 0 and 32 767. That number is used as an index into the distribution map to select the database partition for that IOW: key key

Figure 11 on page 22 shows how the row with the distribution value (cl, c2, c3) is mapped to number 2, which, in turn, references database partition n5. key

<!-- image -->

Partition number

A distribution map is a flexible way of controlling where data is stored in a multi-partition database. If you must change the data distribution across the database partitions in your database, you can use the data redistribution This utility allows to rebalance or introduce skew into the data distribution. utility: you

You can use the db2GetDistMap API to obtain a copy of a distribution map that you can view. If you continue to use the sqlugtpi API to obtain the distribution information, this API might return error message SQL2Z68N, because it can only retrieve distribution maps containing 4096 entries.

## Distribution keys

distribution key is a column (or group of columns) that is to determine the database partition in which particular row of data is stored. used distribution is defined on a table the CREATE TABLE statement: The selection of the distribution is dependent on the DISTRIBUTE BY clause in use: key using key

- If DISTRIBUTE BY HASH is specified, the distribution keys are the explicitly included in the column list following the HASH keyword. keys
- If DISTRIBUTE BY RANDOM is specified, the distribution key is selected by the database manager in an effort to data evenly across all database partitions the table is defined on There are two methods that the database manager uses to achieve this: spread
- Random by unique: If the table includes a unique O primary it uses the unique characteristics of the columns to create a random spread of the data. The columns of the unique or primary are used as the distribution key, key key
- Random by generation: If the table does not have a unique or primary the database manager will include a column in the table to generate and store generated value to use in the hashing function. The column will be created with theIMPLICITLY HIDDEN clause so that it does not appear in queries unless explicitly included. The value of the column will be automatically generated RANDOM\_DISTRIBUTION\_KEY. If it collides with the existing column, a non-conflicting name will be generated by the database manager: key,
- If DISTRIBUTE BY REPLICATION is selected, this means that a copy of all of the data in the table exists on each database partition, So no distribution keys are selected: This option can only be specified for materialized query table:

- If not specified, and the table is defined in a table space that is divided across more than one database partition, a distribution for a table is created by default from the first column of the primary If no primary key is defined, the default distribution is the first column defined in that table that has a data type other than or a LOB data type. Tables in partitioned databases must have at least one column that is neither nor LOB data type key key: key long long
- If not specified and the table is in a table space that is in single partition database partition group, no distribution is defined. Tables without a distribution are only allowed in single-partition database partition groups. You can add or drop distribution keys later; the ALTER TABLE statement: Altering the distribution can only be done to a table whose table space is associated with a single-partition database partition group. key key using key

Choosing a distribution good key

- How tables are to be accessed
- The nature of the query workload
- The join strategies employed by the database system

If collocation is not a major consideration, a distribution key for a table is one that spreads the data evenly across all database partitions in the database partition group. The distribution for each table in a table space that is associated with a database partition group determines if the tables are collocated  Tables are considered collocated when: good key

- The tables are placed in table spaces that are in the same database partition group
- The distribution in each table have the same number of columns keys
- The data types of the corresponding columns are partition-compatible:

These characteristics ensure that rows of collocated tables with the same distribution values are located on the same database partition. key

An inappropriate distribution can cause uneven data distribution. Do not choose columns with unevenly distributed data or columns with a small number of distinct values for the distribution The number of distinct values must be great enough to ensure an even distribution of rows across all database partitions in the database partition group: The cost of applying the distribution algorithm is proportional to the size of the distribution The distribution cannot be more than 16 columns, but fewer columns result in better performance: Do not include unnecessary columns in the distribution key key: key: key key:

Random distribution can remove the work of the distribution selection: This method will instruct the database manager to pick the distribution It will pick them to ensure that data is evenly across all database partitions in the database partition group. However; if the random distribution method is random by generation, you will lose the ability to control collocation and joining of tables cannot be done in an efficient manner: If those will be issues for the expected usage of the table, then explicit selection of the distribution keys is recommended key guess keys: spread

Consider the following points when defining a distribution key:

- The distribution definition cannot be altered: key
- Creation of a multiple-partition table that contains only BLOB, CLOB, DBCLOB, LONG VARCHAR, LONG VARGRAPHIC, XML, or structured data types is not supported:

- Include the most frequently joined columns in the distribution key:
- Include columns that often participate in GROUP BY clause in the distribution key:
- unique or primary must contain all of the distribution columns Any key key key
- In an online transaction processing (OLTP) environment, ensure that all columns in the distribution participate in a transaction through equality predicates. For example, assume that you have an employee number column, EMP\_NO, that is often used in transactions such as: key

UPDATE emp\_table SET WHERE emp\_ no host-variable

In this case, the EMP\_NO column makes a single column distribution for EMP\_TABLE. good key

Database partitioning is the method by which the placement of each row in the table is determined. The method works as follows:

- 1. A hashing algorithm is applied to the value of the distribution and generates number between zero (0) and 32 767 . key,
- 2. The distribution map is created when a database partition group is created Each of the numbers is sequentially repeated in round-robin fashion to fill the distribution map.
- 3. The number is used as an index into the distribution map. The number at that location in the distribution map is the number of the database partition where the row is stored\_

## Table collocation

If two or more tables frequently contribute data in response to certain queries, you will want related data from these tables to be physically located as close together as possible: In a partitioned database environment, this process is known as table collocation.

Tables are collocated when are stored in the same database partition group, and when their distribution keys are compatible Placing both tables in the same database partition group ensures a common distribution map. The tables might be in different table spaces, but the table spaces must be associated with the same database partition group The data types of the corresponding columns in each distribution must be partition-compatible. Collocation is not possible for random distribution tables using the random by generation method. they key

When more than one table is accessed for a join Or a subquery, the database manager determines whether the data to be joined is located at the same database partition. When this happens, the join or subquery is performed at the database partition where the data is stored, instead of to move data between database partitions This ability has significant performance advantages having

## Partition compatibility

The base data types of corresponding columns of distribution keys are compared and can be declared partition-compatible. Partition-compatible data types have the property that two variables, one of each type, with the same value, are mapped to the same number by the same partitioning algorithm.

Partition-compatibility has the following characteristics:

- base data type is compatible with another of the same base data type
- Partition compatibility is not affected by the nullability of a column:
- Internal formats are used for DATE, TIME, and TIMESTAMP data types. are not compatible with each other, and none are compatible with character or graphic data types. They
- Partition-compatibility is affected by collation. Locale-sensitive UCA-based collations require an exact match in collation, except that the strength (S) attribute of the collation is ignored. All other collations are considered equivalent for the purposes of determining partition compatibility
- Character columns defined with FOR BIT DATA are only compatible with character columns without FOR BIT DATA when a collation other than a locale-sensitive UCA-based collation is used:
- NULL values of compatible data types are treated identically; those of non-compatible data types might not be
- Base data types of a user-defined type are to analyze partitioncompatibility used
- Decimals of the same value in the distribution are treated identically, even if their scale and precision differ: key
- Trailing blanks in character (CHAR, VARCHAR, GRAPHIC, or VARGRAPHIC) are ignored by the hashing algorithm. strings
- BIGINT, SMALLINT; and INTEGER are compatible data types.
- When a locale-sensitive UCA-based collation is used, CHAR, VARCHAR, GRAPHIC, and VARGRAPHIC are compatible data types: When another collation is used, CHAR and VARCHAR of different lengths are compatible types and GRAPHIC and VARGRAPHIC are compatible types, but CHAR and VARCHAR are not compatible types with GRAPHIC and VARGRAPHIC
- Partition-compatibility does not apply to LONG VARCHAR, LONG VARGRAPHIC, CLOB, DBCLOB, and BLOB data types, because are not supported as distribution keys they

## Replicated materialized query tables

A materialized query table is defined by a query that also determines the data in the table. Materialized query tables can be used to improve the performance of queries. If the database manager determines that a portion of a query can be resolved by using materialized query table, the query might be rewritten to use the materialized query table:

In partitioned database environment, you can replicate materialized query tables and use them to improve query performance: A replicated materialized query table is based on table that might have been created in a single-partition database partition group, but that you want replicated across all of the database partitions in another database partition group. To create the replicated materialized query table, use the CREATE TABLE statement with the REPLICATED option.

By replicated materialized query tables, you can obtain collocation between tables that are not typically collocated. Replicated materialized query tables are particularly useful for joins in which you have a large fact table and small dimension tables. To minimize the extra storage required and the effect of to every replica, tables that are to be replicated should be small and updated infrequently: using having update

Note: You should also consider replicating larger tables that are updated infrequently: the onetime cost of replication is offset by the performance benefits that can be obtained through collocation.

By specifying a suitable predicate in the subselect clause that is used to define the replicated table, you can replicate selected columns, selected rows, or both.

DELETE or UPDATE statements that contain non-deterministic operations are not supported with replicated materialized query tables.

## Chapter 5. Setting up partitioned database environments

The decision to create multi-partition database must be made before you create your database. As part of the database design decisions you make, you will have to determine if you should take advantage of the performance improvements database partitioning can offer:

## About this task

In partitioned database environment, you still use the CREATE DATABASE command or the sqlecrea() function to create a database. Whichever method is used, the The dbznodes. cfg file is the database partition server configuration file:

Except on the Windows operating system environment, any editor can be to view and the contents of the database partition server configuration file (dbznodes.cfg) On the Windows operating system environment, use db2ncrt and db2nchg commands to create and change the database partition server configuration file used update

Before creating a multi-partition database, you must select which database partition will be the partition for the database: You can then create the database directly from that database partition, or from a remote client that is attached to that database partition. The database partition to which you attach and execute the CREATE DATABASE command becomes the partition for that particular database: catalog catalog

The partition is the database partition on which all system catalog tables are stored. All access to system tables must go through this database partition. AIl federated database objects (for example, wrappers, servers, and nicknames) are stored in the system tables at this database partition. catalog catalog

If possible, you should create each database in a separate instance. If this is not possible (that is, you must create more than one database per instance) , you should spread the catalog partitions among the available database partitions. Doing this reduces contention for catalog information at a single database partition:

Note: You should regularly do a backup of the catalog partition and avoid putting user data on it (whenever possible), because other data increases the time required for the backup:

When you create database, it is automatically created across all the database partitions defined in the dbZnodes.cfg file:

When the first database in the system is created, a system database directory is formed. It is appended with information about any other databases that you create: When working system database directory is sqldbdir and is located in the sqllib directory under your home directory, Or under the directory where Db2 database was installed: When working on UNIX , this directory must reside on shared file system, (for example, NFS on UNIX platforms) because there is only one system database directory for all the database partitions that make up the partitioned database environment: When working on Windows, the system database directory is located in the instance directory:

Also resident in the sqldbdir directory is the system intention file: It is called sq]dbins, and ensures that the database partitions remain synchronized. The file must also reside on a shared file system since there is only one directory across all database partitions The file is shared by all the database partitions making up the database:

Configuration parameters have to be modified to take advantage of database partitioning: Use the GET DATABASE CONFIGURATION and the GET DATABASE MANAGER CONFIGURATION commands to find out the values of individual entries in a specific database, or in the database manager configuration file: To modify individual entries in a specific database, or in the database manager configuration file, use the UPDATE DATABASE CONFIGURATION and the UPDATE DATABASE MANAGER CONFIGURATION commands respectively

The database manager configuration parameters affecting a partitioned database environment include conn\_elapse, fcm\_num\_buffers, fcm\_ num channels, max\_connretries, max\_coordagents, max\_time\_diff, num\_poolagents, and start\_stop\_time:

## Adding database partition servers to an instance (Windows)

On Windows, use the dbzncrt command to add a database partition server to an

## About this task

Note: Do not use the dbzncrt command if the instance already contains databases. Instead, use the START DBM ADD DBPARTITIONNUM command: This ensures that the database is correctly added to the new database partition server: DO NOT EDIT the dbznodes.cfg file, since changing the file might cause inconsistencies in the partitioned database environment:

The command has the following required parameters:

dbzncrt In:partition\_ number Iu:username,password Ip:logical\_ \_port

## In:partition\_number

The unique database partition number to identify the database partition server\_ The number can be from 1 to 999 in ascending sequence:

## lu:username;password

The logon account name and password of the Db2 service:

## Ip:logical ~port

The logical port number used for the database partition server if the logical port is not zero (0). If not specified, the logical port number assigned is 0.

The logical port parameter is only optional when you create the first database partition on computer: If yOu create a logical database partition, YOU must specify this parameter and select a logical port number that is not in use. There are several restrictions:

- On every computer there must be a database partition server with logical port 0\_
- The port number cannot exceed the port range reserved for FCM communications in the services file in %SystemRoot% | system32 drivers |etc directory: For example, if you reserve a range of four ports for the current

instance, then the maximum port number would be 3 (ports 1, 2, and 3; port 0 is for the default logical database partition) The port range is defined when dbzicrt is used with the /r:base\_port, end\_port parameter:

There are also several optional parameters:

## Ig:network\_name

Specifies the network name for the database partition server: If you do not specify this parameter; Db2 uses the first IP address it detects on your system.

Use this parameter if you have multiple IP addresses on computer and you want to specify specific IP address for the database partition server: You can enter the network\_name parameter using the network name or IP address:

## Ih:host\_name

The TCP /IP host name that is used by FCM for internal communications if the host name is not the local host name\_ This parameter is required if you add the database partition server on a remote

## li:instance\_name

The instance name; the default is the current instance.

## Im:computer\_ name

The computer name of the Windows workstation on which the database partition resides; the default name is the computer name of the local computer

## lo:instance\_owning\_computer

The computer name of the computer that is the instance-owning computer; the default is the local computer This parameter is required when the dbzncrt command is invoked on any computer that is not the instance-owning computer:

For example, if you want to add a new database partition server to the instance TESTMPP (s0 that you are running multiple logical database partitions) on the instance-owning computer MYMACHIN, and you want this new database partition to be known as database partition 2 using logical port 1, enter:

dbzncrt In:2 Ip:1 /u:my\_id,my\_pword Ii:TESTMPP IM: TEST /o:MYMACHIN

## Setting up multiple logical partitions

There are several situations in which it is advantageous to have several database partition servers running on the same computer:

This means that the configuration can contain more database partitions than computers: In these cases, the computer is said to be running multiple logical partitions if participate in the same instance: If participate in different instances, this computer is not hosting multiple logical partitions they they

With multiple logical partition support, YOu can choose from three types of configurations:

- A standard configuration, where each computer has only one database partition server
- multiple logical partition configuration, where a computer more than one database partition server has

- A configuration where several logical partitions run on each of several computers

Configurations that use multiple logical partitions are useful when the system runs queries on a computer that has symmetric multiprocessor (SMP) architecture. The ability to configure multiple logical partitions on computer is also useful if a computer fails. If a computer fails (causing the database partition server or servers on it to fail), you can restart the database partition server (or servers) on another computer the START DBM DBPARTITIONNUM command. This ensures that user data remains available: using

Another benefit is that multiple logical partitions can use SMP hardware configurations. In addition, because database partitions are smaller; you can obtain better performance when performing such tasks as backing up and restoring database partitions and table spaces, and creating indexes.

## Configuring multiple logical partitions

There are two methods of configuring multiple logical partitions.

## About this task

- Configure the logical partitions (database partitions) in the dbznodes.cfg file You can then start all the logical and remote partitions with the db2start command or its associated API

Note: For Windows, you must use dbzncrt to add database partition if there is no database in the system; Or, db2start addnode command if there is one or more databases. Within Windows, the dbznodes. cfg file should never be manually edited:

- Restart a logical partition on another processor on which other logical partitions are already running: This allows you to override the hostname and port number specified for the logical partition in dbznodes.cfg:

To configure logical database partition in db2nodes.cfg, you must make an entry in the file to allocate a logical port number for the database partition. Following is the syntax you should use:

nodenumber hostname Iogical-port netname

Note: For Windows, you must use dbzncrt to add a database partition if there is no database in the system; Or, dbzstart addnode command if there is one or more databases. Within Windows, the db2nodes.cfg file should never be manually edited:

The format for the dbznodes.cfg file on Windows is different when compared to the same file on UNIX. On Windows, the column format is:

nodenumber hostname computername Iogical\_ netname ~port

Use the fully-qualified name for the hostname. The /etc/hosts file also should use the fully-qualified name\_ If the fully-qualified name is not used in the dbznodes.cfg file and in the/etc/hosts file, you might receive error message

You must ensure that you define enough ports in the services file of the etc directory for FCM communications

## Enabling inter-partition query parallelism

Inter-partition parallelism occurs automatically based on the number of database partitions and the distribution of data across these database partitions.

## About this task

You must modify configuration parameters to take advantage of parallelism within database partition or within non-partitioned database. For example, intra-partition parallelism can be used to take advantage of the multiple processors on symmetric multi-processor (SMP) machine

## Procedure

- To enable parallelism when loading data:

The load utility automatically makes use of parallelism, or you can use the following parameters on the LOAD command:

- CPU PARALLELISM
- DISK PARALLELISM

In partitioned database environment, inter-partition parallelism for data loading occurs automatically when the target table is defined on multiple database partitions Inter-partition parallelism for data loading can be overridden by specifying OUTPUT\_DBPARTNUMS. The load utility also intelligently enables database partitioning parallelism depending on the size of the target database partitions MAX NUMPART AGENTS can be used to control the maximum degree of parallelism selected by the load utility Database partitioning parallelism can be overridden by specifying PARTITIONING\_DBPARTNUMS when ANYORDER is also specified.

- The table must be enough to benefit from parallelism large
- To enable parallelism when creating an index:
- Multiple processors must be enabled on an SMP computer
- To enable I/0 parallelism when backing up a database or table space:
- Use more than one target media.
- Configure table spaces for parallel I/O by defining multiple containers, or use single container with multiple disks, and the appropriate use of the DBZ PARALLEL\_I0 registry variable. If you want to take advantage of parallel I/O, you must consider the implications of what must be done before you define any containers. This cannot be done whenever you see need; it must be planned for before you reach the where you need to backup your database or table space: point
- Use the PARALLELISM parameter on the BACKUP command to specify the degree of parallelism.
- Use the WITH num-buffers BUFFERS parameter on the BACKUP command to ensure that enough buffers are available to accommodate the degree of The number of buffers should equal the number of target media you have plus the degree of parallelism selected plus a few extra.
- As large as feasible: 4 MB or 8 MB (1024 or 2048 pages) is a rule of thumb. good

Also, use backup buffer size that is:

- At least as large as the largest (extent size number of containers) product of the table spaces backed up. being
- To enable I/0 parallelism when restoring a database or table space:

- Use more than one source media:
- Configure table spaces for parallel I/O. You must decide to use this option before you define your containers. This cannot be done whenever you see a need; it must be planned for before you reach the where you to restore your database or table space: point need
- Use the PARALLELISM parameter on the RESTORE command to specify the degree of parallelism:
- Use the WITH num-buffers BUFFERS parameter on the RESTORE command to ensure that enough buffers are available to accommodate the degree of parallelism. The number of buffers should equal the number of target media have plus the degree of parallelism selected plus few extra you

Also, use a restore buffer size that is:

- As large as feasible. 4 MB or 8 MB (1024 or 2048 pages) is a rule of thumb. good
- At least as large as the largest (extent size number of containers) product of the table spaces restored. being
- even multiple of, the backup buffer size.

## Enabling intrapartition parallelism for queries

To enable intrapartition query parallelism, modify one Or more database or database manager configuration parameters, precompile o bind options, or a register: Alternatively, use the MAXIMUM DEGREE on the CREATE or ALTER WORKLOAD statement, or the ADMIN\_SET\_INTRA PARALLEL procedure to enable or disable intrapartition parallelism at the transaction level special option

## Before you begin

Use the following controls to specify what degree of intrapartition parallelism the optimizer is to use:

- CURRENT DEGREE special register (for dynamic SQL)
- DEGREE bind (for static SQL) option
- dft\_degree database configuration parameter (provides the default value for the previous two parameters)

Use the following controls to limit the degree of intrapartition parallelism at run time. The runtime settings override the optimizer settings.

- max querydegree database manager configuration parameter
- SET RUNTIME DEGREE command
- MAXIMUM DEGREE workload option

Use any of the following controls to enable or disable intrapartition parallelism:

- ADMIN\_SET\_INTRA PARALLEL stored procedure
- intra\_parallel database manager configuration parameter
- MAXIMUM DEGREE workload option

## About this task

Use the GET DATABASE CONFIGURATION or the GET DATABASE MANAGER CONFIGURATION command to find the values of individual entries in a specific database or instance configuration file: To modify one or more of these entries, use the UPDATE DATABASE CONFIGURATION or the UPDATE DATABASE MANAGER CONFIGURATION command:

## intra\_parallel

Database manager configuration parameter that specifies whether or not the database manager can use intrapartition parallelism: The default is NO, which means that applications in this instance are run without intrapartition parallelism. For example: update dbm cfg using intra\_para] ]el yes; dbm cfg; get

## max querydegree

Database manager configuration parameter that specifies the maximum degree of intrapartition parallelism that is used for any SQL statement running this instance\_ An SQL statement does not use more than this value when running parallel operations within database partition. The default is -1, which means that the system uses the degree of intrapartition parallelism that is determined by the optimizer; not the user-specified value: For example: on update dbm cfg using max querydegree any; get dbm cfg;

The intra\_parallel database manager configuration parameter must also be set to YES for the value of max\_querydegree to be used:

## dft\_degree

Database configuration parameter that specifies the default value for the DEGREE precompile or bind option and the CURRENT DEGREE The default is 1\_ A value of -1 (or ANY) means that the system uses the degree of intrapartition parallelism that is determined by the optimizer: For example: special register:

connect to samp]e; update db cfg using dft\_degree -1; db cfg; connect reset; get

DEGREE  Precompile or bind option that specifies the degree of intrapartition parallelism for the execution of static SQL statements on a symmetric multiprocessing (SMP) system. For example:

connect to prod; prep demoapp.sqc bindfile; bind demoapp.bnd degree 2;

## CURRENT DEGREE

Special register that specifies the degree of intrapartition parallelism for the execution of dynamic SQL statements. Use the SET CURRENT DEGREE statement to assign a value to the CURRENT DEGREE For example: special register:

connect to sample; set current degree 1' ; connect reset;

The intra\_parallel database manager configuration parameter must also be set to YES to use intrapartition parallelism: If it is set to NO, the value of this special register is ignored, and the statement will not use intrapartition parallelism: The value of the intra\_parallel database manager configuration parameter and the CURRENT DEGREE register can be overridden in a workload by the MAXIMUM DEGREE workload attribute: special setting

## MAXIMUM DEGREE

CREATE WORKLOAD statement (or ALTER WORKLOAD statement) that specifies the maximum runtime degree of parallelism for a workload. option

For example, suppose that bank\_trans is a packaged application that mainly executes short OLTP transactions, and bank\_report is another packaged application that runs complex queries to generate a business intelligence (BI) report: Neither application can be modified, and both are bound with degree 4 to the database: While bank\_trans is running, it is assigned to workload trans, which disables intrapartition parallelism. This OLTP application will run without any performance degradation associated with intrapartition parallelism overhead. While bank\_report is running, it is assigned to workload bi, which enables intrapartition parallelism and specifies a maximum runtime degree of 8. Because the compilation degree for the package is 4, the static SQL statements in this application run with only a degree of 4. If this BI application contains dynamic SQL statements, and the CURRENT DEGREE register is set to 16, these statements run with degree of 8. special connect to sample;

```
create workload trans appIname ( 'bank_trans ) maximum degree enable;
```

```
create workload bi appIname ( bank_report' ) maximum degree 8 enable;
```

connect reset;

## ADMIN\_SET INTRA PARALLEL

Procedure that enables or disables intrapartition parallelism for a database application. Although the procedure is called in the current transaction, it takes effect starting with the next transaction. For example, assume that the following code is\_part of the demoapp application which uses the ADMIN\_SET\_INTRA PARALLEL procedure with both static and dynamic SQL statements:

EXEC SQL CONNECT TO prod;

```
EXEC SQL CALL SYSPROC. ADMIN_SET_INTRA_PARALLEL ( 'NO ' ) ; Commit that the effect of this cal] starts in the next statement:
```

```
for this static statement: EXEC SQL SELECT COUNT (*) Into numRecords EXEC SQL COMMIT;
```

```
EXEC SQL COMMIT; A11 statements in the next two transactions run without intrapartition para] Iel ism: strcpy(stmt "SELECT deptname FROM org" ) ; EXEC SQL PREPARE rstmt FROM stmt; EXEC SQL DECLARE cl CURSOR FOR rstmt; EXEC SQL OPEN cl; EXEC SQL FETCH cl Into deptname; EXEC SQL CLOSE cl; FROM org;
```

```
Enable intrapartition parallel ism: EXEC SQL CALL SYSPROC. ADMIN_SET_ INTRA_PARALLEL ( 'YES ' ) ; Commit that the effect of this cal] starts in the next statement: EXEC SQL COMMIT; strcpy(stmt the degree of paral Iel ism to 4: EXEC SQL EXECUTE  IMMEDIATE stmt; dynamic statements in the next two transactions run with intrapartition paral Iel ism and degree 4: strcpy(stmt SELECT deptname FROM org" ) ; EXEC SQL PREPARE rstmt FROM stmt EXEC SQL DECLARE c2 CURSOR FOR rstmt; EXEC SQL OPEN c2; EXEC SQL FETCH c2 Into deptname; EXEC SQL CLOSE c2; static statements in the next two transactions run with intrapartition parallel ism and degree 2: EXEC SQL SELECT COUNT ( *) Into numRecords FROM org; EXEC SQL COMMIT;
```

The degree of intrapartition parallelism for dynamic SQL statements is specified through the CURRENT DEGREE special register; and for static SQL statements, it is specified through the DEGREE bind option. The following commands are to prepare and bind the demoapp application: used

```
connect to prod; prep demoapp.sqc bindfile; bind demoapp.bnd degree 2;
```

## Chapter 6. Adding database partitions in partitioned database environments

You can add database partitions to the partitioned database system either when it is running, Or when it is stopped. Because new server can be time consuming, you might want to do it when the database manager is already running: adding

Use the ADD DBPARTITIONNUM command to add database partition to a This command can be invoked in the following ways: system

- As an on the START DBM command option
- With the ADD DBPARTITIONNUM command
- With the sqleaddn API
- With the sqlepstart API

If system is stopped, use the START DBM command. If it is running you can use any of the other choices. your

When you use the ADD DBPARTITIONNUM command to add a new database partition to the system, all existing databases in the instance are expanded to the new database partition. You can also specify which containers to use for temporary table spaces for the databases. The containers can be:

- The same as those defined for the catalog partition for each database: (This is the default:)
- The same as those defined for another database partition:
- Not created at all. You must use the ALTER TABLESPACE statement to add temporary table space containers to each database before the database can be used \_

Note: uncataloged database is not recognized when adding a new database partition. The uncataloged database will not be present on the new database partition. An attempt to connect to the database on the new database partition returns the error message SQL1O13N. Any

You cannot use database on the new database partition to contain data until one or more database partition groups are altered to include the new database partition.

You cannot change from a single-partition database to a multi-partition database by a database partition to your This is because the redistribution of data across database partitions requires distribution on each affected table: The distribution keys are automatically generated when a table is created in multi-partition database: In a single-partition database, distribution keys can be explicitly created with the CREATE TABLE or ALTER TABLE SQL statements. adding system. key

Note: If no databases are defined in the system and you are running Enterprise Server Edition on UNIX operating system, edit the dbznodes.cfg file to add new database partition definition; do not use any of the procedures described, as apply only when database exists: they

Windows Considerations: If you are using Enterprise Server Edition on Windows operating system and have no databases in the instance, use the dbzncrt command to scale the database system. If, however, you already have databases, use the START DBM ADD DBPARTITIONNUM command to ensure that database partition is created for each existing database when you scale the system. On Windows operating systems, do not manually edit the database partition configuration file (dbznodes.cfg), because this can introduce inconsistencies to the file:

## Adding an online database partition

You can add new database partitions that are online to a partitioned database environment while it is running and while applications are connected to databases:

## Procedure

To add an online database partition to a running database manager using the command line:

- 1\_ On any existing database partition, run the START DBM command.
- On all platforms, specify the new database partition values for DBPARTITIONNUM, ADD DBPARTITIONNUM, HOSTNAME, PORT, and NETNAME parameters. On the Windows platform, you also specify the COMPUTER, USER, and PASSWORD parameters

You can also specify the source for any temporary table space container definitions that must be created with the databases. If you do not provide table space information, temporary table space container definitions are retrieved from the partition for each database: catalog

For example, to add three new database partitions to existing database, issue the following commands: an

START DBM DBPARTITIONNUM 3 ADD DBPARTITIONNUM  HOSTNAME   HOSTNAME3 PORT  PORT3;

START DBM DBPARTITIONNUM ADD DBPARTITIONNUM  HOSTNAME   HOSTNAME4 PORT   PORT4;

- START DBM DBPARTITIONNUM 5 ADD DBPARTITIONNUM HOSTNAME HOSTNAMES PORT PORTS;
- 2 Optional: Alter the database partition group to incorporate the new database partition. This action can also be an option when redistributing the data to the new database partition.
- 4 Optional: Back up all databases on the new database partition. Although optional, this would be helpful to have for the new database partition and for the other database partitions particularly if you redistributed the data across both the old and the new database partitions
- 3\_ Optional: Redistribute data to the new database partition. This action is not really optional if you want to take advantage of the new database partitions You can also include the alter database partition group option as part of the redistribution operation. Otherwise, altering the database partition group to incorporate the new database partitions must be done as a separate action before redistributing the data to the new database partition:

## Restrictions when working online to add a database partition

The status of the new database partition following its addition to the instance depends the status of the original database partition. Applications may or may not be aware of the new database partition following its addition to the instance if the application uses WITH HOLD cursors\_ on

When a new database partition to a single-partition database instance: adding

- If the original database partition is down when the database partition is added, then the new database partition is up when the add database partition operation completes:
- If the original database partition is up when the database partition is added, then the new database partition is down when the add database partition operation completes

Applications WITH HOLD cursors that are started before the add database partition operation runs are not aware of the new database partition when the add database partition operation completes. If the WITH HOLD cursors are closed before the add database partition operation runs, then applications are aware of the new database partition when the add database partition operation completes using

## Adding a database partition offline (Linux and UNIX)

You can add new database partitions that are offline to a partitioned database system: The newly added database partition becomes available to all databases when the database manager is started again.

## Before you begin

- Install the new server if it does not exist before you can create a database partition on it:
- Synchronize operating system files with those on existing processors.
- Make the executables accessible shared filesystem mounts or local copies. using
- Ensure that the sqlib directory is accessible as shared file system.
- Ensure that the relevant operating system parameters (such as the maximum number of processes) are set to the appropriate values
- Register the host name with the name server or in the hosts file in the /etc directory on all database partitions The host name for the computer must be registered in rhosts to run remote commands rsh or rah: using
- ADD PARTITION registry variable to TRUE to enforce that the added database partitions is offline.

## Procedure

- To add database partition to a stopped partitioned database server using the command line:
- Issue STOP DBM to all the database partitions. stop
- 2. Run the ADD DBPARTITIONNUM command on the new server:
- A database partition is created locally for every database that exists in the system: The database parameters for the new database partitions are set to the default value, and each database partition remains empty until you move data to it: Update the database configuration parameter values to match those on the other database partitions
- 3. Run the START DBM command to start the database Note that the database partition configuration file (dbznodes.cfg) has already been by the database manager to include the new server during the installation of the new server: system. updated
- 4. Update the configuration file on the new database partition as follows:
- a. On any existing database partition, run the START DBM command.

Specify the new database partition values for DBPARTITIONNUM, ADD DBPARTITIONNUM, HOSTNAME, PORT , and NETNAME parameters as well as the COMPUTER, USER, and PASSWORD parameters.

You can also specify the source for any temporary table space container definitions that must be created with the databases. If you do not provide table space information, temporary table space container definitions are retrieved from the partition for each database: catalog

For example, to add three new database partitions to an existing database, issue the following commands:

START DBM DBPARTITIONNUM 3 ADD DBPARTITIONNUM HOSTNAME HOSTNAME3 PORT PORT3 ;

START DBM DBPARTITIONNUM ADD DBPARTITIONNUM HOSTNAME   HOSTNAME4 PORT  PORT4;

START DBM DBPARTITIONNUM 5 ADD DBPARTITIONNUM HOSTNAME   HOSTNAMES PORT  PORTS;

When the START DBM command is complete, the new server is stopped.

- When you stop all the database partitions in the system, the node configuration file is updated to include the new database partitions The node configuration file is not updated with the new server information until STOP DBM is executed. This ensures that the ADD DBPARTITIONNUM command, which is called when you specify the ADD DBPARTITIONNUM parameter to the START DBM command, runs on the correct database partition: When the utility ends, the new server partitions are stopped.
- b\_ the entire database manager by running the STOP DBM command: Stop
- 5 Start the database manager by running the START DBM command.

The newly added database partition is now started with the rest of the system.

When all the database partitions in the system are running, you can run system-wide activities, such as creating or dropping a database.

Note: You might have to issue the START DBM command twice for all database partition servers to access the new dbznodes.cfg file:

- 7 . Optional: Redistribute data to the new database partition. This action is not really optional if you want to take advantage of the new database partition. You can also include the alter database partition group as part of the redistribution operation. Otherwise, altering the database partition group to incorporate the new database partition must be done as separate action before redistributing the data to the new database partition. option
- 6\_ Optional: Alter the database partition group to incorporate the new database partition. This action might also be an when redistributing the data to the new database partition. option
- 8 optional, this would be helpful to have for the new database partition and for the other database partitions particularly if you redistributed the data across both the old and the new database partitions
- You can also the configuration file manually, as follows: update
- 2. Issue the following command to start the new database partition: START DBM DBPARTITIONNUM partitionnum
- 1. Edit the dbznodes.cfg file and add the new database partition to it
- Specify the number you are assigning to the new database partition as the value of partitionnum.

- If the new server is to be a logical partition (that is, it is not database partition 0), use dbzset command to the DBPARTITIONNUM registry variable. Specify the number of the database partition you are adding update
- This command creates database partition locally for every database that exists in the system: The database parameters for the new database partitions are set to the default value, and each database partition remains empty until you move data to it: Update the database configuration parameter values to match those on the other database partitions
- 4. Run the ADD DBPARTITIONNUM command on the new database partition:
- 5. When the ADD DBPARTITIONNUM command completes, issue the START DBM command to start the other database partitions in the system.
- Do not perform any system-wide activities, such as creating Or dropping a database, until all database partitions are successfully started.

## Adding a database partition offline (Windows)

You can add new database partitions to a partitioned database system while it is stopped. The newly added database partition becomes available to all databases when the database manager is started again.

## Before begin you

- You must install the new server before you can create a database partition on it:
- Set the default value of the DB2 FORCE\_OFFLINE ADD\_PARTITION registry variable to TRUE to enforce that any added database partitions is offline:

## Procedure

To add a database partition to a stopped partitioned database server the command line: using

- 1. Issue STOP DBM to stop all the database partitions
- 2 Run the ADD DBPARTITIONNUM command on the new server
- A database partition is created locally for every database that already exists in the system. The database parameters for the new database partitions are set to the default value, and each database partition remains empty until you move data to it: Update the database configuration parameter values to match those on the other database partitions.
- 3\_ Run the START DBM command to start the database system. Note that the database partition configuration file has already been updated by the database manager to include the new server the installation of the new server: during
- a On any existing database partitions, run the START DBM command.
- Update the configuration file on the new database partition as follows:
- Specify the new database partition values for DBPARTITIONNUM, ADD DBPARTITIONNUM, HOSTNAME, PORT , and NETNAME parameters as well as the COMPUTER, USER, and PASSWORD parameters.

You can also specify the source for any temporary table space container definitions that need to be created with the databases. If you do not provide table space information, temporary table space container definitions are retrieved from the catalog partition for each database:

For example; to add three new database partitions to an existing database, issue the following commands:

- START DBM  DBPARTITIONNUM 3 ADD DBPARTITIONNUM HOSTNAME HOSTNAME3 PORT PORT3 ;

START DBM DBPARTITIONNUM ADD DBPARTITIONNUM  HOSTNAME HOSTNAME4

START DBM  DBPARTITIONNUM 5 PORT PORTS;

When the START DBM command is complete, the new server is stopped.

- When you stop all the database partitions in the system, the node configuration file is updated to include the new database partitions. The node configuration file is not with the new server information until STOP DBM is executed: This ensures that the ADD DBPARTITIONNUM command, which is called when you specify the ADD DBPARTITIONNUM parameter to the START DBM command, runs on the correct database partitions. When the utility ends, the new server partitions are stopped. updated
- b\_ the database manager by running the STOP DBM command. Stop
- 5. Start the database manager by running the START DBM command.
- The newly added database partitions are now started with the rest of the system.
- When all the database partitions in the system are running you can run system-wide activities, such as creating or dropping a database:

Note: You might have to issue the START DBM command twice for all database partition servers to access the new dbznodes.cfg file:

- 7 . Optional: Redistribute data to the new database partition. This action is not really optional if you want to take advantage of the new database partition. You can also include the alter database partition group as part of the redistribution operation. Otherwise, altering the database partition group to incorporate the new database partition must be done as a separate action before redistributing the data to the new database partition. option
- 6\_ Optional: Alter the database partition group to incorporate the new database partition. This action could also be an when redistributing the data to the new database partition. option
- 8 Optional: Back up all databases on the new database partition. Although optional, this would be helpful to have for the new database partition and for the other database partitions particularly if you have redistributed the data across both the old and the new database partitions.

## Error recovery when adding database partitions

database partitions does not fail as a result of nonexistent buffer pools, because the database manager creates system buffer to provide default automatic support for all buffer pool page sizes. Adding pools

However; if one of these system buffer is used, performance might be seriously affected, because these buffer pools are very small. If a system buffer pool is used, a message is written to the administration notification System buffer are used in database partition addition scenarios in the following circumstances: pools log: pools

- You add database partitions to a partitioned database environment that has one or more temporary table spaces with a page size that is different from the default of 4 KB. When database partition is created, only the IBMDEFAULTDP buffer exists, and this buffer has a page Size of 4 KB. system pool pool
- 1. You use the START DBM command to add database partition to the current multi-partition database:

Consider the following examples:

START DBM DBPARTITIONNUM 2 ADD DBPARTITIONNUM  HOSTNAME newhost PORT 2

- You use the ADD DBPARTITIONNUM command after manually the dbznodes.cfg file with the new database partition description: update you

One way to prevent these problems is to specify the WITHOUT TABLESPACES clause on the ADD DBPARTITIONNUM or the START DBM commands. After this, use the CREATE BUFFERPOOL statement to create the buffer the appropriate SIZE and PAGESIZE values, and associate the system temporary table spaces to the buffer pool the ALTER TABLESPACE statement\_ doing \_ pools using using

- You add database partitions to an existing database partition group that has one or more table spaces with page size that is different from the default page size, which is 4 KB. This occurs because the non-default page-size buffer created on the new database partition have not been activated for the table spaces. pools

Note: In previous versions, this command used the NODEGROUP keyword instead of the DATABASE PARTITION GROUP keywords.

Consider the following example:

- You use the ALTER DATABASE PARTITION GROUP statement to add a database partition to a database partition group, as follows:

START DBM CONNECT To mppl

ALTER DATABASE PARTITION GROUP ngl ADD DBPARTITIONNUM  (2)

One way to prevent this problem is to create buffer for each page size and then to reconnect to the database before issuing the following ALTER DATABASE PARTITION GROUP statement: pools

START DBM CONNECT TO mppl CREATE BUFFERPOOL bpl SIZE 1000 PAGESIZE 8192 CONNECT RESET CONNECT To mppl ALTER DATABASE PARTITION GROUP ngl ADD DBPARTITIONNUM  (2)

Note: If the database partition group has table spaces with the default page size, message SQL1759W is returned:

## Chapter 7 . Tables in partitioned database environments

There are performance advantages to creating a table across several database partitions in partitioned database environment: The work associated with the retrieval of data can be divided among the database partitions:

## Before you begin

Before creating a table that will be physically divided or distributed, you need to consider the following:

- Tables can be collocated by placed in the same table space or by placed in another table space that, together with the first table space, is associated with the same database partition group being being
- Table spaces can span more than one database partition: The number of database partitions span depends on the number of database partitions in database partition group: they

## About this task

Creating table that will be a part of several database partitions is specified when you are creating the table: There is an additional when creating table in a partitioned database environment: the distribution A distribution is a that is part of the definition of a table: It determines the database partition on which each row of data is stored. option key: key key

If you do not specify the distribution explicitly, a default distribution is automatically defined. key key

You must be careful to select an appropriate distribution because it cannot be changed later. Furthermore, any unique indexes (and therefore unique or primary keys) must be defined as a superset of the distribution That is, if distribution is defined, unique keys and primary keys must include all of the same columns as the distribution (they might have more columns). key key: key key

The size of a database partition of a table is the smaller amount of a specific limit associated with the type of table space and page size used, and the amount of disk space available: For example, assuming large DMS table space with a 4 KB page size, the size of a table is the smaller amount of 8 TB multiplied by the number of database partitions and the amount of available disk space: See the related links for the complete list of database manager page size limits.

To create a table in a partitioned database environment the command line, enter: using

```
CREATE TABLE name> <co]umn name> <data_type> IN <tagle_space_name> INDEX IN <index space_name> LONG space name> DISTRIBUTE BY HASH <column name>) <long_
```

Following is an example:

```
CREATE TABLE MIXREC  (MIX_CNTL INTEGER NOT NULL, MIX_DESC CHAR(20) MIX_CHR CHAR(9) NOT NULL, MIX_Int  INTEGER NOT NULL, NULL, MIX_DEC DECIMAL NOT NULL, MIX_FLT FLOAT NOT NULL, MIX_DATE DATE NOT NULL, MIX_TIME TIME NOT NULL, MIX TMSTMP TIMESTAMP NOT NULL) IN MIXTS1Z DISTRIBUTE BY HASH (MIX_INT)
```

In the preceding example, the table space is MIXTS12 and the distribution is MIX\_INT: If the distribution is not specified explicitly, it is MIX\_CNTL. (If no primary is specified and no distribution is defined, the distribution is the first non-long column in the list: ) key key key key key row of a table, and all information about that row, always resides on the same database partition.

## Chapter 8. Enabling communication between database partitions using FCM communications

In a partitioned database environment, most communication between database partitions is handled by the fast communications manager (FCM):

To enable the FCM at a database partition and allow communication with other database partitions, you must create a service entry in the database partition's services file of the etc directory as shown later in this section: The FCM uses the specified port to communicate. If you have defined multiple database partitions on the same host, you must define a range of ports, as shown later in this section.

Before attempting to manually configure memory for the fast communications manager (FCM), it is recommended that you start with the automatic setting, which is also the default setting, for the number of FCM Buffers (fcm\_num\_buffers) and for the number of FCM Channels (fcm\_ num\_channel s) Use the system monitor data for FCM activity to determine if this is appropriate setting

## Windows Considerations

The TCP /IP port range is automatically added to the services file by:

- The install program when it creates the instance or adds a new database partition
- The dbzncrt utility when it adds the first database partition on the computer
- The dbzicrt utility when it creates a new instance

The syntax of a service entry is as follows:

DBZ\_instance port\_ #comment Itcp

## DB2\_instance

The value for instance is the name of the database manager instance. All characters in the name must be lowercase: Assuming an instance name of

## portltcp

The TCP /IP port that you want to reserve for the database partition.

## #comment

comment that you want to associate with the entry The comment must be preceded by a pound sign (#). Any

If the services file of the etc directory is shared, you must ensure that the number of ports allocated in the file is either than or equal to the largest number of multiple database partitions in the instance: When allocating ports, also ensure that you account for any processor that can be used as a greater

If the services file of the etc directory is not shared, the same considerations apply, with one additional consideration: you must ensure that the entries defined for the Db2 database instance are the same in all services files of the etc directory (though other entries that do not apply to your partitioned database environment do not have to be the same):

If you have multiple database partitions on the same host in an instance, you must define more than one port for the FCM to use: To do this, include two lines in the

services file of the etc directory to indicate the range of ports that you are allocating: The first line specifies the first port, and the second line indicates the end of the block of ports In the following example, five ports are allocated for the database partitions For example:

9000 / tcp

END

9004/tcp

Note: You must specify END in uppercase only You must also ensure that you include both underscore ( ) characters:

## Chapter 9. Managing database partitions

You can start or stop partitions, partitions, Or trace partitions drop

## Before you begin

To work with database partitions, you need authority to attach to an instance Anyone with SECADM or ACCESSCTRL authority can grant you the authority to access specific instance:

## Procedure

- To start or to stop specific database partition, use the START DATABASE MANAGER command or the STOP DATABASE MANAGER command with the DBPARTITIONNUM parameter:
- To trace the activity on a database partition, use the options specified by IBM Support:
- To specific database partition from the dbznodes.cfg configuration file, use the STOP DATABASE MANAGER command with the DROP DBPARTITIONNUM parameter: Before the DROP DBPARTITIONNUM parameter; run the DROP DBPARTITIONNUM VERIFY command to ensure that there is no user data on this database partition drop using

Attention: Use the trace utility only when directed to do so by IBM Support or by a technical support representative:

The trace utility records and formats information about Db2 operations. more details, see the "db2trc Trace commandtopic: For

## Listing database partition servers in an instance (Windows)

On Windows, use the dbznlist command to obtain list of database partition servers that participate in an instance

## About this task

The command is used as follows:

dbznlist

When this command as shown, the default instance is the current instance (set by the DBZINSTANCE environment variable): To specify a particular instance, you can specify the instance using: using dbznlist li:instName

where instName is the particular instance name you want:

You can also optionally request the status of each database partition server by using:

dbznlist Is

The status of each database partition server might be one of: starting, running stopping, or stopped:

## Eliminating duplicate entries from a list of machines in a partitioned database environment

If you are running multiple logical database partition servers on one computer; your dbznodes.cfg file contains multiple entries for that computer

## About this task

In this situation, the rah command needs to know whether you want the command to be executed only once on each computer or once for each logical database partition listed in the dbznodes.cfg file: Use the rah command to specify computers. Use the db2\_ command to specify logical database partitions.

Note: On Linux and UNIX operating systems, if you specify computers, rah normally eliminates duplicates from the computer list, with the following exception: if you specify logical database partitions, db2 prepends the following assignment to your command:

export DBZNODE-nnn (for Korn shel1 syntax)

where nnn is the database partition number taken from the corresponding line in the dbznodes.cfg s0 that the command is routed to the desired database partition server: file,

When specifying logical database partitions, you can restrict the list to include all logical database partitions except one, or specify only one the &lt;&lt;-nnn&lt; and &lt;&lt;+nnn&lt; sequences. You might want to do this if you want to run command to the database partition first, and when that has completed, run the same command at all other database partition servers, possibly in This is usually required when running the RESTART DATABASE command. You need to know the database partition number of the partition to do this. using prefix catalog parallel. catalog

If you execute RESTART DATABASE the rah command, duplicate entries are eliminated from the list of computers. However if you specify the prefix, then duplicates are not eliminated, because it is assumed that use of the prefix implies sending to each database partition server; rather than to each computer: using\_

## Specifying the list of machines in a partitioned database environment

By default, the list of computers is taken from the database partition configuration file, dbznodes.cfg:

## About this task

Note: On Windows, to avoid introducing inconsistencies into the database partition configuration file, do not edit it manually: To obtain the list of computers in the instance, use the dbznlist command:

## Procedure

To override the list of computers in dbznodes.cfg:

- Specify a name to the file that contains the list of computers by exporting (on Linux and UNIX operating systems) or (on Windows) the environment variable RAHOSTFILE: path setting

- Specify the list explicitly, as a string of names separated by spaces, by exporting (on Linux and UNIX operating systems) or setting (on Windows) the environment variable RAHOSTLIST.

Note: If both of these environment variables are specified, RAHOSTLIST takes precedence:

## Changing the database configuration across multiple database partitions

When you have a database that is distributed across more than one database partition, the database configuration file should be the same on all database

## About this task

Consistency is required since the SQL compiler compiles distributed SQL statements based on information in the database partition configuration file and creates an access plan to satisfy the needs of the SQL statement: Maintaining different configuration files on database partitions could lead to different access plans, depending on which database partition the statement is prepared. Use dbz\_al1 to maintain the configuration files across all database partitions

## Adding containers to SMS table spaces on database partitions

You can add a container to an SMS table space only on a database partition that currently has no containers.

## Procedure

To add a container to an SMS table space the command line, enter the following: using

```
ALTER TABLESPACE name ADD ('path' ) ON DBPARTITIONNUM (database_partition_number)
```

The database partition specified by number; and every partition in the range of database partitions, must exist in the database partition group on which the table space is defined. A database\_partition\_number might only appear explicitly or within range in exactly one db-partitions-clause for the statement:

## Example

The following example shows how to add a new container to database partition number 3 of the database partition group used by table space "plans" on a UNIX operating system:

ALTER

```
TABLESPACE plans ADD ( ' /dev/rhdisko' ON  DBPARTITIONNUM  (3)
```

## Using database partition expressions

In most cases, must use the same storage for each partition in a partitioned database environment, and all of the storage must exist before you issue a statement: One exception is when you use database partition expressions within the storage paths you paths path:

this allows the database partition number to be reflected in the storage such that the resulting name is different on each partition. Doing path

You can specify a database partition expression for container string syntax when creating either SMS or DMS containers: You typically specify the database partition expression when multiple logical database partitions in partitioned database system. The expression ensures that container names are unique across database partition servers. If you specify an expression, the database partition number is of the container name Or, if you specify additional arguments, the result of the argument is part of the container name using part

Important: The SMS table space type has been deprecated in Version 10.1 for user-defined permanent table spaces and might be removed in a future release: The SMS table space type is not deprecated for catalog and temporary table spaces. For more information, see "SMS permanent table spaces have been deprecated" at http: / / wwwibm.com / support / knowledgecenter /SSEPGG\_10.1.0 / com.ibm.db2.luw.wn.doc / doc/ 10058748.html:

Important: Starting with Version 10.1 Fix Pack 1, the DMS table space type is deprecated for user-defined permanent table spaces and might be removed in a future release. The DMS table space type is not deprecated for and temporary table spaces. For more information, see 'DMS permanent table spaces have been deprecated" at http:, 'knowledgecenter , SSEPGG\_10.1.O / com.ibm.db2luw.wn.doc/ doc/ i0060577.html. catalog

Use the argument SN" ([blankJSN) to indicate a database partition expression: You can use database partition expression anywhere in the storage name, and you can specify multiple database partition expressions. Terminate the database partition expression with space character; whatever follows the space is appended to the storage name after the database partition expression is evaluated. If there is no space character in the storage name after the database partition expression, it is assumed that the rest of the string is part of the expression. If you specify number before the N argument, (S[number]N), the partition number is formatted with leading zeros. path path path

You must specify the argument by using one of the forms in the following table: Operators are evaluated from left to right: A percent sign (%) represents the modulus operator: The database partition number in the following examples is assumed to be 10.

Table 2. Database partition expressions

| Syntax                       | Example    | Value   |
|------------------------------|------------|---------|
| [blank]SN                    | "SN"       | 10      |
| [blank]S[number]N            | "S4N"      | 0010    |
| [blankJSN+[number]           |            | 110     |
| [blank]SN%[number]           | "SN%/5"    |         |
| [blankJSN+[number] %[number] | "SN+1%5"   |         |
| [blank]SN %[number]+[number] | "SN%/o4+2" |         |

If you specified storage by using a database partition expression, must use the same storage string, including the database partition expression, to path you path

drop the path: This path string is in the DB\_STORAGE\_PATH\_WITH\_DPE field of the ADMIN\_GET\_STORAGE\_PATHS table function: This element is not shown if you did not include a database partition expression in the original path:

## Examples

- 1 On a with database partitions: system two

(device Idev/rcont SN 20000)

The following containers are created:

Idev/rcontl on database partition

Idev/rconto on database partition

- 2\_ On a with three database partitions: system

ALTER STOGROUP  IBMSTOGROUP ADD

The following are added: paths

IDBZ /patho on database partition

IDBZ /pathz on database partition 2

DBZ /pathl on database partition

- 3 On a system with four database partitions:

CREATE TABLESPACE TS2 MANAGED BY DATABASE USING (file IDBZ/containers/TSZ/container SN+100 " 10000)

The following containers are created:

IDBZ/containers/TSZ/containerloo on database partition

IDBZ/containers TSZ/containerl0z on database partition 2

IDBZ/containers/TSZ/containerl0l on database partition

IDBZ/containers/TSZ/containerl03 on database partition 3

- 4\_ On a system with two database partitions:

CREATE TABLESPACE   TS3 MANAGED BY SYSTEM USING ('/TS3/cont SN%2 [TS3/cont

The following containers are created:

[TS3/contz On database partition 0

[TS3/conto On database partition 0

[TS3/contl On database partition

[TS3/cont3 On database partition

- 5. If there are 10 database partitions, the containers use the following syntax:

Idbdirlnode SN /contl'

[filel

Idirl

- SN%10 /container

The containers are created as:

Idbdirlnode5/contl'

5/container

/1005/filel

Idir/2000/dmscont

## Changing database partitions (Windows)

On Windows, use the db2nchg command to change database partitions.

## About this task

- Move the database partition from one computer to another:

dbznodes. cfg file:

- Change the TCP /IP host name of the computer: If you are planning to use multiple network adapters, you must use this command to specify the TCP /TP address for the "netname" field in the
- Use a different logical port number:
- Use a different name for the database partition server:

The command has the following required parameter:

dbznchg In:node\_number

The parameter /n: is the number of the database partition server that want to change. This parameter is required. you

## Optional parameters include:

## li:instance\_name

Specifies the instance that this database partition server participates in. If you do not specify this parameter; the default is the current instance:

## u:username ,password

Changes the logon account name and password for the Db2 database service If you do not specify this parameter; the logon account and password remain the same

## Ip:logical\_port

Changes the logical port for the database partition server: This parameter must be specified if you move the database partition server to different computer: If you do not specify this parameter; the logical port number remains unchanged:

## Ih:host name

Changes the TCP /TP host name used by FCM for internal communications. If you do not specify this parameter; the host name is unchanged:

## m: computer\_name

Moves the database partition server to another computer: The database partition server can be moved only if there are no existing databases in the instance.

## Ig:network\_name

Changes the network name for the database partition server:

Use this parameter if you have multiple IP addresses on computer and you want to use a specific IP address for the database partition server: You can enter the network\_name using the network name or the IP address.

For example, to change the logical port assigned to database partition 2, which participates in the instance TESTMPP; to use the logical port 3, enter the following command:

dbznchg In:2 /i:TESTMPP /p:3

The Db2 database manager provides the capability of accessing Db2 database system registry variables at the instance level on a remote computer

Currently, Db2 database system registry variables are stored in three different

registry variables stored at the instance level (including the database partition level) can be redirected to another computer by DBZREMOTEPREG: When DBZREMOTEPREG is set, the Db2 database manager accesses the Db2 database system registry variables from the computer pointed to by DBZREMOTEPREG. The db2set using dbzset DBZREMOTEPREG-remote\_workstation

where remote\_workstation is the remote workstation name

## Note:

- Care must be taken in setting this since all Db2 database instance profiles and instance listings will be located the specified remote computer name option on
- If your environment includes users from domains, ensure that the account associated with the Db2 instance service is a domain account: This ensures that the Db2 instance has the appropriate privileges to enumerate groups at the domain level: logon

This feature might be used in combination with setting DBINSTPROF to to a remote LAN drive on the same computer that contains the registry point

## Redistributing data in a database partition group

To create an effective redistribution for your database partition group and redistribute your data, issue the REDISTRIBUTE DATABASE PARTITION GROUP command or call the sqludrdt API. plan

## Before you begin

To work with database partition groups, you must have SYSADM, SYSCTRL, or DBADM authority

## Procedure

To redistribute data in database partition group:

- Issue REDISTRIBUTE DATABASE PARTITION GROUP command in the command line processor (CLP):
- Issue the REDISTRIBUTE DATABASE PARTITION GROUP command by using the ADMIN\_CMD procedure:
- Call the sqludrdt API

## Issuing commands in partitioned database environments

In partitioned database environment, you might want to issue commands to be run on using the rah command or the db2\_al1 command: The rah command allows you to issue commands that you want to run at computers in the instance

If you want the commands to run at database partition servers in the instance, you run the db2\_al1 command. This section provides overview of these commands\_ The information that follows applies to partitioned database environments only an

On Windows, to run the rah command or the db2\_al/ command, you must be logged on with user account that is member of the Administrators group.

On Linux and UNIX operating systems, your login shell can be a Korn shell or any other shell; however; there are differences in the way the different shells handle commands containing special characters.

Also, on Linux and UNIX operating systems, rah uses the remote shell program specified by the DBZRSHCMD registry variable: You can select between the two remote shell programs: ssh (for additional security), or rsh (or remsh for HP-UX) If DBZRSHCMD is not set, rsh (or remsh for HP-UX) is used. The ssh remote shell program is used to prevent the transmission of passwords in clear text in UNIX operating system environments.

If a command runs on one database partition server and you want it to run on all of them, use db2\_al1. The exception is the dbztrc command, which runs on all the logical database partition servers on computer: If you want to run dbztrc on all logical database partition servers on all computers, use rah:

Note: The db2\_al1 command does not support commands that require interactive user input:

## rah and db2 all commands overview

You can run the commands sequentially at one database partition server after another; or you can run the commands in

On Linux and UNIX operating systems, if you run the commands in parallel, you can either choose to have the output sent to a buffer and collected for display (the default behavior) or the output can be displayed at the computer where the command is issued On Windows, if you run the commands in parallel, the output is displayed at the computer where the command is issued:

To use the rah command, type:

rah command

To use the db2\_al1 command, type:

command

To obtain help about rah syntax, type:

rah 2

The command can be almost anything that you can type at an interactive prompt, including, for example, multiple commands to be run in sequence: On Linux and UNIX operating systems, you separate multiple commands using a semicolon (). On Windows, you separate multiple commands using an ampersand (&amp;). Do not use the separator character following the last command

The following example shows how to use the db2\_al1 command to change the database configuration on all database partitions that are specified in the database partition configuration file. Because the character is inside double quotation marks, the request runs concurrently: placed db2\_al1 DBZ  UPDATE DB CFG FOR sample USING LOGFILSIZ 100"

Note: The dbz\_al1 command does not support commands that require interactive user input:

## rah and db2\_all commands

This topic includes descriptions of the rah and db2\_ commands: ~all

## Command

## Description

rah

Runs the command on all computers.

## db2\_all

Runs a non-interactive command on all database partition servers that you specify db2\_al1 does not support commands that require interactive user input:

## db2\_kill

Abruptly stops all processes being run on multiple database partition servers and cleans up all resources on all database partition servers This command renders your databases inconsistent: Do not issue this command except under direction from IBM Software Support or as directed to recover from sustained trap:

## db2\_call\_stack

On Linux and UNIX operating systems, causes all processes running on all database partition servers to write call traceback to the syslog:

On Linux and UNIX operating systems, these commands execute rah with certain implicit settings such as:

- Run in parallel at all computers
- Buffer command output in Itmp/ SUSER/db2\_kill, /tmp/SUSER/ db2\_calI\_stack respectively

The command db2 call\_stack is not available on Windows Use the dbzpd ~stack command instead:

## Specifying the rah and db2\_all commands

You can specify rah command from the command line as the parameter; or in response to the prompt if you do not specify any parameter:

characters: special

Use the prompt method if the command contains the following &amp; ; &lt; &gt; { } [ ] unsubstituted

If you specify the command as the parameter on the command line, you must enclose it in double quotation marks if it contains any of the characters just listed. special

Note: On Linux and UNIX operating systems, the command is added to your command history just as if you typed it at the prompt

All special characters in the command can be entered normally (without being enclosed in quotation marks, except for |) If you require a in your command, you must type two backslashes (1 |)

Note: On Linux and UNIX operating systems, if you are not Korn shell, all characters in the command can be entered normally (without enclosed in quotation marks, except for unsubstituted $, and the single quotation mark ()) If you require one of these characters in your command, you must V For example, if you require a in your command, you must type four backslashes ( | using special being

If you require a double quotation mark (") in command, you must precede it by three backslashes, for example, 1 your

## Note:

- 1. On Linux and UNIX operating systems, you cannot include a single quotation mark () in your command unless your command shell provides some way of entering single quotation mark inside a singly quoted string:
- 2. On Windows, you cannot include a single quotation mark () in your command unless command window provides some way of entering a single quotation mark inside a singly quoted string: your

When you run any korn-shell shell-script that contains logic to read from stdin in the background, explicitly redirect stdin to source where the process can read without getting stopped the terminal (SIGTTIN message). To redirect stdin, you can run a script with the following form: on shelI\_script &lt;/dev/nul1 &amp;

if there is no input to be supplied:

In similar way, always specify &lt;/dev/nul1 when running db2\_al] in the background. For example:

;run command" &lt;/dev/nul1 &amp;

By this you can redirect stdin and avoid getting stopped on the terminal. doing

An alternative to this method, when you are not concerned about output from the remote command, is to use the "daemonize" option in the db2\_al1 prefix:

db2\_al1 ;daemonize\_this\_command" &amp;

## Running commands in parallel (Linux; UNIX)

By default, the command is run sequentially at each computer; but you can specify to run the commands in parallel using background rshells by prefixing the command with certain prefix sequences. If the rshell is run in the background, then each command puts the output in a buffer file at its remote computer

Note: The information in this section to Linux and UNIX operating systems only applies

This process retrieves the output in pieces: two

- 1\_ After the remote command completes.
- 2. After the rshell terminates, which might be later if some processes are still running:

The name of the buffer file is tmp/SUSER/rahout by default, but it can be specified by the environment variables SRAHBUFDIR o SRAHBUFNAME.

When you specify that you want the commands to be run concurrently, by default, this script prefixes an additional command to the command sent to ali hosts to check that SRAHBUFDIR and SRAHBUFNAME are usable for the buffer file: It creates SRAHBUFDIR: To suppress this, export an environment variable RAHCHECKBUF-no. You can do this to save time if you know that the directory exists and is usable:

Before using rah to run a command concurrently at multiple computers:

- Ensure that a directory tmp/SUSER exists for your user ID at each computer: To create directory if one does not exist, run:
- rah )mkdir Itmp/ SUSER"
- Add the following line to your kshrc (for Korn shell syntax) or profi]e, and also type it into your current session:
- export RAHCHECKBUF=no
- Ensure that each computer ID at which you run the remote command has an entry in its rhosts file for the ID which runs rah; and the ID which runs rah has an in its rhosts file for each computer ID at which you run the remote command: entry

## Monitoring rah processes (Linux; UNIX)

While any remote commands are still running or buffered output is still accumulated, processes started by rah monitor activity to write messages to the terminal indicating which commands have not been run, and retrieve the buffered output: being

## About this task

Note: The information in this section applies to Linux and UNIX operating systems only:

The informative messages are written at an interval controlled by the environment variable RAHWAITTIME. Refer to the help information for details on how to specify this. All informative messages can be suppressed by exporting RAHWAITTIME-0.

The primary monitoring process is a command whose command name (as shown The first informative message tells you the (process id) of this process All other monitoring processes appear as ksh commands running the rah script (or the name of the symbolic link) If you want, you can stop all monitoring processes by the command: pid kill pid

where pid is the process ID of the primary monitoring process. Do not specify a signal number: Leave the default of 15. This does not affect the remote commands at all, but prevents the automatic display of buffered output: Note that there might be two or more different sets of monitoring processes executing at different times during the life of a single execution of rah: However; if at any time you the current set, then no more are started. stop

If regular login shell is not a Korn shell (for example /bin/ksh), you can use rah, but there are some slightly different rules on how to enter commands containing the following characters: your special

- unsubstituted

For more information, type rah "2" Also, in a Linux or UNIX operating system, if the login shell at the ID which executes the remote commands is not a Korn shell, then the login shell at the ID which executes rah must also not be a Korn shell. (rah decides whether the shell of the remote ID is a Korn shell based on the local ID): The shell must not perform any substitution or processing on a string enclosed in single quotation marks. It must leave it exactly as is\_ special

## Extension of the rah command to use tree logic (AIX and Solaris)

To enhance performance, rah has been extended to use tree\_logic on systems. That is, rah will check how many database partitions the list contains, and if that number exceeds a threshold value, it constructs a subset of the list and sends a recursive invocation of itself to those database partitions large

At those database partitions, the recursively invoked rah follows the same logic until the list is small enough to follow the standard logic (now the "leaf-of-tree' logic) of sending the command to all database partitions on the list: The threshold can be specified by the RAHTREETHRESH environment variable, or defaults to 15.

In the case of a multiple-logical-database partitions-per-physical-database partition system, db2\_al1 will favor sending the recursive invocation to distinct physical database partitions, which will then rsh to other logical database partitions on the same physical database partition, thus also reducing inter-physical-database partition traffic: (This only to db2\_al1, not rah, because always sends only to distinct physical database partitions) applies rah point

## rah and db2\_all command prefix sequences

A sequence is one or more special characters. prefix

Type one or more sequences immediately preceding the characters of the command without any intervening blanks If you want to specify more than one sequence, you can type them in any order; but characters within any multicharacter sequence must be typed in order: If you type any sequences, you must enclose the entire command, including the sequences in double quotation marks, as in the following examples: prefix prefix prefix

- On Windows operating systems: rah dbz db cfg for sample" db2 al1 "|dbz db cfg for sample" get get

On Linux and UNIX operating systems: rah };ps -F pid,ppid,etime,args SUSER" dbz "};ps -F pid,ppid,etime args SUSER"

The prefix sequences are:

## Sequence

## Purpose

- Runs the commands in sequence in the background:
- &amp; Runs the commands in sequence in the background and terminates the command after all remote commands have completed, even if some processes are still running This might be later if, for example, child processes (on Linux and UNIX operating systems) or background processes (on Windows operating systems) are still running: In this case, the command starts a separate background process to retrieve any remote output generated after command termination and writes it back to the originating computer

Note: On Linux and UNIX operating systems, specifying &amp; degrades performance, because more rsh commands are required.

- Runs the commands in parallel in the background.

- Runs the commands in parallel in the background and terminates the command after all remote commands have completed as described previously for the I&amp; case\_
- Note: On Linux and UNIX operating systems, specifying &amp; degrades performance, because more rsh commands are required.
- Same as I&amp;. This is an alternative shorter form:

Note: On Linux and UNIX operating systems, specifying degrades performance relative to I, because more rsh commands are required.

- Prepends dot-execution of user's profile before executing command:

Note: Available on Linux and UNIX operating systems only:

- Prepends dot-execution of file named in SRAHENV (probably kshrc) before executing command:

Note: Available on Linux and UNIX operating systems only:

- J} Prepends dot-execution of user's profile followed by execution of file named in SRAHENV (probably kshrc) before executing command:

Note: Available on Linux and UNIX operating systems only:

- Suppresses execution of user's and of file named in SRAHENV. profile

Note: Available on Linux and UNIX operating only: systems

- Echoes the command invocation to the computer
- Sends to all the computers except this one

## &lt;&lt;-nnn&lt;

Sends to all-but-database partition server nnn (all database partition servers in dbznodes.cfg except for database partition number nnn, see the first paragraph following the last sequence in this table). prefix nnn is the corresponding 1-, 2-, or 3-digit database partition number to the nodenum value in the dbznodes. cfg file:

&lt;-nnn&lt; is only applicable to db2\_al1.

## &lt;tnnn&lt;

Sends to only database partition server nnn (the database partition server in dbznodes.cfg whose database partition number is nnn, see the first paragraph following the last prefix sequence in this table)

nnn is the corresponding 1-, 2-, or 3-digit database partition number to the nodenum value in the dbznodes.cfg file:

&lt;tnnn&lt; is only applicable to db2\_al1.

## (blank character)

Runs the remote command in the background with stdin, stdout, and stderr all closed. This is valid only when running the command in the background, that is, only in a sequence which also includes or It allows the command to complete much sooner (as soon as the remote command has been initiated): If you specify this prefix sequence on the rah option prefix

command line, then either enclose the command in single quotation marks, or enclose the command in double quotation marks, and precede the character by For example, prefix

```
rah mydaemon or rah mydaemon
```

When run as a background process, the rah command never waits for any output to be returned:

- Substitutes occurrences of &gt; with the computer name\_
- Substitutes occurrences of by the computer index, and substitutes occurrences of ## by the database partition number:
- The computer index is a number that associated with a computer in the database system. If you are not running multiple logical partitions, the computer index for a computer corresponds to the database partition number for that computer in the database partition configuration file: To obtain the computer index for a computer in a multiple logical partition database environment, do not count duplicate entries for those computers that run multiple logical partitions For example, if MACHI is running two logical partitions and MACH2 is also running two logical partitions, the database partition number for MACH3 is 5 in the database partition configuration file The computer index for MACH3, however; would be 3.
- On Windows operating systems, do not edit the database partition configuration file: To obtain the computer index, use the dbznlist command\_
- When is specified, duplicates are not eliminated from the list of computers.

## Usage notes

- Prefix sequences are considered to be part of the command. If you specify a prefix sequence as part of a command, you must enclose the entire command, including the prefix sequences, in double quotation marks.

## Controlling the rah command

This topic lists the environment variables to control the rah command:

Table 3. Environment variables that control the rah command

| Name                                                                  | Meaning              | Default    |
|-----------------------------------------------------------------------|----------------------|------------|
| SRAHBUFDIR Note: Available Linux and UNIX operating systems only: on  | Directory for buffer | tmp/ SUSER |
| SRAHBUFNAME Note: Available on Linux and UNIX operating systems only: | File name for buffer | rahout     |

Table 3. Environment variables that control the rah command (continued)

| Name                                                                                             | Meaning                                                                                                                                                          | Default                                                |
|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| SRAHOSTFILE (on Linux and UNIX operating systems); RAHOSTFILE (on Windows operating systems)     | File containing list of hosts                                                                                                                                    | dbznodes. cfg                                          |
| SRAHOSTLIST (on Linux and UNIX operating systems); RAHOSTLIST (on Windows operating systems)     | List of hosts as string                                                                                                                                          | extracted from SRAHOSTFILE                             |
| SRAHCHECKBUF Note: Available on Linux and UNIX operating systems only:                           | If set to "no bypass checks                                                                                                                                      | not set                                                |
| SRAHSLEEPTIME (on Linux and UNIX operating systems); RAHSLEEPTIME (on Windows operating systems) | Time in seconds this script waits initial output from commands run in for                                                                                        | 86400 seconds for db2_kill, 200 seconds for all others |
| SRAHWAITTIME (on Linux and UNIX operating systems); RAHWAITTIME (on                              | On Windows operating systems, interval in seconds between successive checks that remote jobs are still running: On Linux and UNIX operating systems, interval in | 45 seconds                                             |
| SRAHENV Note: Available on Linux and UNIX operating                                              | Specifies file name to be executed if SRAHDOTFILES-E or K or PE or B                                                                                             | SENV                                                   |

systems only:

Table 3. Environment variables that control the rah command (continued)

| Name                                                                                   | Meaning                                                                                                                                                                                  | Default   |
|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| SRAHUSER (on Linux and UNIX operating systems); RAHUSER (on Windows operating systems) | On Linux and UNIX operating systems, user ID under which the remote command is to be run: On Windows operating systems, the logon account associated with the Db2 Remote Command Service | SUSER     |

Note: On Linux and UNIX operating systems, the value of SRAHENV where rah is run is used, not the value (if any) set by the remote shell

## Specifying which files run with rah (Linux and UNIX)

This topics lists the files that are run if no sequence is specified. prefix

Note: The information in this section to Linux and UNIX operating applies

P profile

E File named in SRAHENV (probably kshrc)

K Same as E

PE profile followed by file named in SRAHENV (probably kshrc)

B Same as PE

N None (or Neither)

Note: If your login shell is not a Korn shell, any dot files you specify to be executed are executed in a Korn shell process, and so must conform to Korn shell syntax for example, if your login shell is a € shell, to have your cshrc environment set up for commands executed by rah, should either create a Korn shell INSTHOME/ . profile equivalent to your cshrc and specify in your INSTHOME/ .cshrc: So, you setenv RAHDOTFILES

or you should create a Korn shell INSTHOME \_ kshrc equivalent to your cshrc and specify in your INSTHOME/ .cshrc:

setenv RAHDOTFILES E setenv RAHENV INSTHOME / kshrc

Also, it is your cshrc must not write to stdout if there is no tty (as when invoked by rsh) You can ensure this by enclosing any lines which write to stdout by, for example, if tty then echo "executed cshrc" endif

## Setting the default environment profile for rah on Windows

To set the default environment profile for the rah command, use file called dbzrah.env, which should be created in the instance directory:

## About this task

Note: The information in this section applies to Windows only

The file should have the following format:

```
This is comment Tine DBZ INSTANCE-instancename DBZDBDFT-database End of file
```

You can specify all the environment variables that you need to initialize the environment for rah:

## Determining problems with rah (Linux, UNIX)

This topic gives suggestions on how to handle some problems that you might encounter when you are running rah:

Note: The information in this section to Linux and UNIX operating systems only: applies

- 1 rah hangs (or takes a very time) long

This problem might be caused because:

- rah has determined that it needs to buffer output, and you did not export RAHCHECKBUF-no Therefore, before running your command, rah sends a command to all computers to check the existence of the buffer directory, and to create it if it does not exist:
- One or more of the computers where you are sending your command is not responding: The rsh command will eventually time out but the time-out interval is usually about 60 seconds. long, quite
- 2 You have received messages such as:
- Login incorrect
- Permission denied

Either one of the computers does not have the ID running rah correctly defined in its /etc/hosts file, or the ID running rah does not have one of the computers correctly defined in its rhosts file: If the DBZRSHCMD registry variable has been configured to use ssh, then the ssh clients and servers on each computer might not be configured correctly:

Note: You might need to have greater security regarding the transmission of passwords in clear text between database partitions. This will depend on the remote shell program you are rah uses the remote shell program specified by the DBZRSHCMD registry variable. You can select between the remote shell programs: ssh (for additional security) , or rsh (or remsh for HP-UX): If this registry variable is not set, rsh (or remsh for HP-UX) is used. using: two

- The ID running rah does not have one of the computers correctly defined in its rhosts file, or if the DBZRSHCMD registry variable has been configured to use ssh, then the ssh clients and servers on each computer might not be configured correctly:
- 3 When running commands in parallel background remote shells, although the commands run and complete within the expected elapsed time at the computers, rah takes a time to detect this and up the shell prompt using long put
- 4 Although rah runs fine when run from the shell command line, if you run rah remotely using rsh, for example,

rsh somewher -1 SUSER db2\_kill

## rah never completes

This is normal. rah starts background monitoring processes, which continue to run after it has exited: Those processes normally persist until all processes associated with the command you ran have themselves terminated. In the case of db2\_kill, this means termination of all database managers. You can terminate the monitoring processes by finding the process whose command is rahwaitfor and kill process\_id&gt;. Do not specify signal number Instead, use the default (15).

- 5. The output from rah is not displayed correctly; or rah incorrectly reports that SRAHBUFNAME does not exist, when multiple commands of rah were issued under the same SRAHUSER:

This is because multiple concurrent executions of rah are trying to use the same buffer file (for example, SRAHBUFDIR o SRAHBUFNAME) for buffering the outputs. To prevent this problem, use different SRAHBUFNAME for each concurrent rah command, for example in the following ksh:

export RAHBUFNAME-rahout rah Scommand 1" &amp; export RAHBUFNAME-rahzout rah Scommand 2" &amp;

or use method that makes the shell choose a unique name automatically such as:

RAHBUFNAME-rahout.$$ db2\_al1

Whatever method you use, you must ensure that you clean up the buffer files at some if disk space is limited. rah does not erase buffer file at the end of execution, although it will erase and then re-use an existing file the next time you specify the same buffer file. point

- 6\_ You entered

rah 'print from ()

and received the message:

ksh: syntax error at Tine 1 (' unexpected

Prerequisites for the substitution of () and ## are:

- Use dbz\_all, not rah:
- Ensure a RAHOSTFILE is used either by exporting RAHOSTFILE or by defaulting Without these prerequisites, rah leaves the () and ## as is. You receive an error because the command from () is not valid. print

For a performance tip when running commands in parallel, use rather than &amp;, and use rather than or unless you truly need the function provided by &amp;. Specifying &amp; requires more remote shell commands and therefore degrades performance:

## Dropping database partitions

You can drop a database partition that is not used by any database and free the computer for other uses\_ being

## Before you begin

Verify that the database partition is not in use by issuing the DROP DBPARTITIONNUM

- If you receive message SQL6034W (Database partition not used in any database), you can drop the database partition:
- If you receive message SQL6O35W (Database partition in use by database), use the REDISTRIBUTE DATABASE PARTITION GROUP command to redistribute the data from the database partition that you are dropping to other database partitions from the database alias.

Also ensure that all transactions for which this database partition was the coordinator have all committed or rolled back successfully: This might require crash recovery on other servers For example, if you the coordinator partition, and another database partition participating in a transaction crashed before the coordinator partition was dropped, the crashed database partition will not be able to query the coordinator partition for the outcome of any indoubt transactions doing drop

## Procedure

To drop database partition using the command line:

Issue the STOP DBM command with the DROP DBPARTITIONNUM parameter to the database partition: drop

After the command completes successfully, the system is stopped. Then start the database manager with the START DBM command:

## Dropping a database partition from an instance (Windows)

On Windows, use the dbzndrop command to a database partition server from instance that has no databases. If you database partition server; its database partition number can be reused for a new database partition server: drop drop an

## About this task

Exercise caution when you drop database partition servers from an instance: If you drop the instance-owning database partition server zero (0) from the instance, the instance becomes unusable: If you want to the instance, use the dbzidrop command drop

Note: Do not use the dbzndrop command if the instance contains databases. Instead, use the STOP DBM DROP DBPARTITIONNUM command: This ensures that the database is correctly removed from the database partition. DO NOT EDIT the dbznodes.cfg file, since changing the file might cause inconsistencies in the partitioned database environment

If you want to database partition that is assigned the logical port 0 from a computer that is running multiple logical database partitions, you must drop all the other database partitions assigned to the other logical ports before you can drop the database partition assigned to logical port 0. Each database partition server must have a database partition assigned to logical port 0. drop

The command has the following parameters:

dbzndrop /n:dbpartitionnum /i instance name

## Indbpartitionnum

The unique database partition number (dbpartitionnum) to identify the database partition server: This is a required parameter: The number can be from zero (0) to 999 in ascending sequence: Recall that database partition zero (0) represents the instance-owning computer:

## liinstance name

The instance name (instance\_name) This is an parameter: If not given, the default is the current instance (set by the DBZINSTANCE registry variable). optional

## Chapter 10. Redistributing data across database partitions

Redistributing data is a task that you might perform in a partitioned database environment after or removing database partitions or when an undesirable proportion of data is appearing on particular partition SO as to rebalance or reconfigure the distribution. adding

## Data redistribution

Data redistribution is a database administration operation that can be performed to primarily move data within a partitioned database environment when partitions The of this operation is typically to balance the usage of storage space, improve database system performance, or satisfy other system requirements. goal

Data redistribution can be performed by one of the following interfaces: using

- REDISTRIBUTE DATABASE PARTITION GROUP command
- ADMIN\_CMD built-in procedure
- STEPWISE\_REDISTRIBUTE\_DBPG built-in procedure
- sqludrdt API

Data redistribution within a partitioned database is done for one of the following reasons:

- To rebalance data whenever a new database partition is added to the database environment or an existing database partition is removed.
- To secure sensitive data by isolating it within particular partition:
- To introduce user-specific data distribution across partitions

Data redistribution is performed by connecting to database at the catalog database partition and beginning a data redistribution operation for a specific partition group by one of the supported interfaces: Data redistribution relies on the existence of distribution definitions for the tables within the partition group. The distribution value for a row of data within the table is used to determine which partition the rOw of data will be stored A distribution is generated automatically when a table is created in multi-partition database partition group. A distribution can also be explicitly defined by using the CREATE TABLE or ALTER TABLE statements By default data redistribution, for each table within a specified database partition grOup, table data is divided and redistributed evenly among the database partitions Other distributions, such as a skewed distribution, can be achieved by specifying an input distribution map which defines how the data is to be distributed. Distribution maps can be generated a data redistribution operation for future use or can be created manually: using key key key on key during during

## Comparison of logged; recoverable redistribution and minimally logged, not roll-forward recoverable redistribution

When performing data redistribution by either the REDISTRIBUTE DATABASE PARTITION GROUP command or the ADMIN\_CMD built-in procedure, you can choose between two methods of data redistribution: logged, recoverable using

redistribution and minimally logged, not roll-forward recoverable redistribution. The latter method is specified by the NOT ROLLFORWARD RECOVERABLE command parameter: using

Data redistribution in capacity growth scenarios, during load balancing, or during performance tuning can require precious maintenance window time, a considerable amount of planning time, as well as space and extra container space that can be expensive. Your choice of redistribution methods depends on whether you prioritize recoverability or speed: log

- When the logged, recoverable redistribution method is used, extensive logging of all row movement is performed such that the database can be recovered in the event of any interruptions, errors, or other business need:
- The not roll-forward recoverable redistribution method offers better performance because data is moved in bulk and records are no longer required for insert and delete operations. log

The latter method is particularly beneficial if, in the past, large active space and storage requirements forced you to break a single data redistribution operation into multiple smaller redistribution tasks, which might have resulted in even more time required to complete the end-to-end data redistribution operation. log

The not roll-forward recoverable redistribution method is the best practice in most situations because the data redistribution takes less time, is less error prone, and consumes fewer system resources. As result, the total cost of performing data redistribution is reduced, which frees up time and resources for other business operations.

## Minimally logged; not roll-forward recoverable redistribution

When the REDISTRIBUTE DATABASE PARTITION GROUP command is issued and the NOT ROLLFORWARD RECOVERABLE parameter is specified, a minimal logging strategy is used that minimizes the of records for each moved row. This type of logging is important for the usability of the redistribute operation Since an approach that fully logs all data movement could, for systems, require an impractical amount of active and permanent space and would generally have poorer performance characteristics. log writing large log

There are also features and optional parameters that are only available when you choose the not roll-forward recoverable redistribution method. For example, by default this method of redistribution quiesces the database and performs a precheck to ensure that prerequisites are met\_ You can also optionally specify to rebuild indexes and collect table statistics as part of the redistribution operation: The combination and automation of these otherwise manual tasks makes them less error prone, faster; and more efficient, while providing you with more control over the operations.

The not roll-forward recoverable redistribution method automatically reorganizes the tables, which can free up disk space: This table reorganization comes at no additional performance cost to the redistribute operation. For tables with clustering indexes, the reorganization does not attempt to maintain clustering: If perfect clustering is desired, it will be necessary to perform a REORG TABLE command on tables with clustering index after data redistribution completes. For multi-dimensional-clustered (MDC) tables, the reorganization maintains the clustering of the table and frees unused blocks for reuse; however the total size of the table after redistribution appears unchanged.

Note: It is critical that you back up each affected table space or the entire database when the redistribute operation is complete because forward through this type of redistribute operation results in all tables that were redistributed being marked invalid. Such tables can only be dropped, which means there is no way to recover the data in these tables. This is for recoverable databases, the REDISTRIBUTE DATABASE PARTITION GROUP utility when issued with the NOT ROLLFORWARD RECOVERABLE all table spaces it touches into the BACKUP PENDING state: This state forces you to back up all redistributed table spaces at the end of a successful redistribute operation. With a backup taken after the redistribution operation, you should not have a need to roll-forward through the redistribute operation itself. rolling why, option puts

There is one important consequence of the lack of roll-forward recoverability: If you choose to allow updates to be made against tables in the database (even tables outside the database partition group redistributed) while the redistribute operation is running, including the period at the end of redistribute where the table spaces touched by redistribute are backed up, such updates can be lost in the event of a serious failure, for example, database container is destroyed. The reason that such updates can be lost is that the redistribute operation is not roll-forward recoverable: If it is necessary to restore the database from backup taken before the redistribution operation, then it will not be possible to roll-forward through the logs in order to replay the that were made the redistribution operation without also forward through the redistribution which, as was described previously, leaves the redistributed tables in the UNAVAILABLE state. Thus, the only thing that can be done in this situation is to restore the database from the backup taken before the redistribution without forward. Then the redistribute operation can be performed again: Unfortunately, all the updates that occurred the original redistribute operation are lost: being being updates during rolling rolling during

The importance of this cannot be overemphasized. In order to be certain that there will be no lost during a redistribution operation, one of the following must be true: point updates

- The redistribution operation is performed with the QUIESCE DATABASE command parameter set to YES. You must still ensure that any applications or users that are allowed to access the quiesced database are not making updates.
- You must avoid making updates the operation of the REDISTRIBUTE DATABASE PARTITION GROUP command, including the period after the command finishes where the affected table spaces are backed up. during being
- Updates that are applied during the redistribute operation come from repeatable source, meaning that can be again at any time: For example, if the source of updates is data that is stored in file and the updates are applied during batch processing, then clearly even in the event of a failure requiring a database restore, the updates would not be lost since could simply be again at any time: applied they they applied

With respect to allowing to the database the redistribution operation, you must decide whether such updates are appropriate or not based on whether the updates can be repeated after database restore, if necessary: updates during

Note: Not every failure during operation of the REDISTRIBUTE DATABASE PARTITION GROUP command results in this problem: In fact, most do not: The REDISTRIBUTE DATABASE PARTITION GROUP command is restartable, meaning that if the utility fails in the middle of its work, it can be easily continued or aborted with the fully

CONTINUE or ABORT options The failures mentioned previously are failures that require the user to restore from the backup taken before the redistribute operation:

## Logged, recoverable redistribution

The original and default version of the REDISTRIBUTE DATABASE PARTITION GROUP command, this method redistributes data by standard SQL inserts and deletes. Extensive logging of all row movement is performed such that the database is recoverable by restoring it using the RESTORE DATABASE command then rolling forward through all changes the ROLLFORWARD DATABASE command\_ using using

After the data redistribution, the source table contains empty spaces because rows were deleted and sent to new database partitions. If you want to free the empty spaces, you must reorganize the tables. To reorganize the tables, you must use separate operation, after the redistribution is complete: To improve performance of this method, the indexes and re-create them after the redistribution is complete drop

## Determining if data redistribution is needed

Determining the current data distribution for a database partition group or table can be helpful in determining if data redistribution is required. Details about the current data distribution can also be used to create a custom distribution map that specifies how to distribute data.

## About this task

If a new database partition is added to a database partition group, Or an existing database partition is dropped from database partition grOup, perform data redistribution to balance data among all the database partitions.

partitions have been added or dropped from a database partition group, then data redistribution is usually only indicated when there is an unequal distribution of data among the database partitions of the database partition group. Note that in some cases an unequal distribution of data can be desirable For example, if some database partitions reside on powerful machine, then it might be beneficial for those database partitions to contain larger volumes of data than other partitions

## Procedure

To determine if data redistribution is needed:

- 1. Get information about the current distribution of data among database partitions in the database partition group.

Run the following query on the largest table (alternatively, a representative table) in the database partition group:

SELECT DBPARTITIONNUM(column\_name) COUNT FROM table GROUP name) ORDER BY DBPARTITIONNUM(column\_name DESC

name

Here, column\_name is the name of the distribution for table table\_name. key

The output of this query shows how many records from table\_name reside on each database partition. If the distribution of data among database partitions is not as desired, then proceed to the next step.

- 2. Get information about the distribution of data across hash partitions.

Run the following query with the same column\_ name and table\_name that were used in the previous step:

SELECT  HASHEDVALUE (column\_name) COUNT ( *) FROM table name GROUP BY  HASHEDVALUE (column name ORDER BY HASHEDVALUE (column\_name DESC

The output of this query can easily be used to construct the distribution file needed when the USING DISTFILE parameter in the REDISTRIBUTE DATABASE PARTITION GROUP command is specified. Refer to the REDISTRIBUTE DATABASE PARTITION GROUP command reference for a description of the format of the distribution file.

- 3\_ Optional: If the data requires redistribution, you can plan to do this operation during a system maintenance opportunity

When the USING DISTFILE parameter is specified, the REDISTRIBUTE DATABASE PARTITION GROUP command uses the information in the file to generate a new partition map for the database partition group. This operation results in uniform distribution of data among database partitions

If a uniform distribution is not desired, you can construct your own target partition map for the redistribution operation: The target partition map can be specified by the USING TARGETMAP parameter in the REDISTRIBUTE DATABASE PARTITION GROUP command. using

## Results

After this investigation, you will know if your data is uniformly distributed or not or if data redistribution is required. doing

## Prerequisites for data redistribution

Before data redistribution can be performed successfully for a set of tables within database partition group, certain prerequisites must be met

The following is a list of mandatory prerequisites:

- Authorization to perform data redistribution from the supported data redistribution interface of choice:
- A significant amount of time period of low activity in which to perform the redistribution operation. during system
- All tables containing data to be redistributed as part of a data redistribution operation must be in example, tables cannot be in LOAD PENDING state or other inaccessible load table states. To check the states of tables, establish a connection to each partition in the database partition group and issue the LOAD QUERY command\_ The output of this command contains information about the state of the table: The documentation of the LOAD QUERY command explains the meaning of each of the table states and how to move one state to another
- All tables within the database partition being redistributed must have been defined with a distribution If a new database partition is added to a single-partition system, data redistribution cannot be performed until all of the tables within the partitions have a distribution For tables that were created the CREATE TABLE statement and have definitions that do not contain a distribution you must alter the table by using the ALTER TABLE statement to add a distribution key before redistributing the data. key: key: using key,

- Replicated materialized query tables contained in a database partition group must be dropped before you redistribute the data. Store a copy of the materialized query table definitions s0 that can be recreated after data redistribution completes. they
- backup of the database must be created by the BACKUP DATABASE command. This backup is not a mandatory prerequisite however it is strongly recommended that it be done. using
- If a non-uniform redistribution is desired a distribution map must be created as target distribution map to be used a parameter to the redistribute interface:
- A connection must be established to the database from the database partition. catalog
- Adequate space must be available to rebuild all indexes either during or after the data redistribution: The INDEXING MODE command parameter affects when the indexes are rebuilt:
- When the NOT ROLLFORWARD RECOVERABLE command parameter is specified, adequate space should be available for writing status information to control files used by IBM Service for problem determination. The control files are generated in the following and should be manually deleted when the data redistribution operation is complete: paths
- On Windows operating systems: diagpath|redist db\_name db tiongroup\_name t imestamp| \_partie
- On Linux and UNIX operating systems: diagpath/redist/db\_ name\_ db\_partitiongroup\_name timestamp/

You can calculate the space requirements in bytes for the control files by the following formula: using

(number of pages for all tables in the database partition group) 64 bytes number of LOB values in the database partition group) 600 bytes

To estimate number of LOB values in the database partition group, add the number of LOB columns in your tables and multiply it by the number of rows in the largest table

- When the NOT ROLLFORWARD RECOVERABLE command parameter is not specified, adequate file space must be available to contain the entries associated with the INSERT and DELETE operations performed during data redistribution otherwise data redistribution will be interrupted or fail: log\_ log

The util\_heap\_sz database configuration parameter is critical to the processing of data movement between database partitions allocate as much memory as possible to util heap\_sz for the duration of the redistribution operation: Sufficient sortheap is also required if indexes are rebuilt as part of the redistribution operation. Increase the value of util\_heap\_ sz and sortheap database configuration parameter; as necessary, to improve redistribution performance: being

## Log space requirements for data redistribution

To successfully perform a data redistribution operation, adequate log file space must be allocated to ensure that data redistribution is not interrupted: space requirements are less of a concern when you specify the NOT ROLLFORWARD RECOVERABLE command parameter; since there is minimal logging during that type of data redistribution Log

The quantity of file space required depends on multiple factors including which options of the REDISTRIBUTE DATABASE PARTITION GROUP command are used. log

When the redistribution is performed from any supported interface where the data redistribution is roll-forward recoverable:

- The must be large enough to accommodate the INSERT and DELETE operations at each database partition where data is being redistributed  The heaviest logging requirements will be either on the database partition that will lose the most data, or on the database partition that will the most data. log gain
- If you are moving to a larger number of database partitions, use the ratio of current database partitions to the new number of database partitions to estimate the number of INSERT and DELETE operations For example, consider redistributing data that is uniformly distributed before redistribution. If you are moving from four to five database partitions, approximately twenty percent of the four original database partitions will move to the new database partition: This means that twenty percent of the DELETE operations will occur on each of the four original database partitions, and all of the INSERT operations will occur on the new database partition:
- Consider a nonuniform distribution of the data, such as the case in which the distribution contains many NULL values. In this case, all rows that contain NULL value in the distribution move from one database partition under the old distribution scheme and to different database partition under the new distribution scheme: As a result, the amount of space required on those two database partitions increases, perhaps well beyond the amount calculated by assuming uniform distribution. key key log
- The redistribution of each table is a single transaction. For this reason, when you estimate space, you multiply the percentage of change, such as twenty might be uniformly distributed but the second largest table, for example, might have one or more inflated database partitions. In such a case, consider the non-uniformly distributed table instead of the largest one\_ log using

Note: After you estimate the maximum amount of data to be inserted and deleted at a database partition, double that estimate to determine the peak size of the active If this estimate is greater than the active limit of 1024 GB, then the data redistribution must be done in steps. For example, use the STEPWISE REDISTRIBUTE\_DBPG procedure with a number of steps proportional to how much the estimate is greater than active limit: You might also set the logsecond database configuration parameter to -1 to avoid most space problems. log: log log log

When the redistribution is performed from any supported interface where the data redistribution is not roll-forward recoverable:

- records are not created when rows are moved as part of data redistribution. This behavior significantly reduces file space requirements; however; when this option is used with database roll-forward recovery, the redistribute operation record cannot be rolled forward, and any tables processed as part of the roll-forward operation remain in UNAVAILABLE state. Log log
- If the database partition group undergoing data redistribution contains tables with long-field (LF) or large-object (LOB) data in the tables, the number of records generated data redistribution will be higher; because a record is created for each row of data. In this case, expect the space requirement per database partition to be roughly one third of the amount of data moving that partition (that is, data sent, received, or both): log during log log on being

## Restrictions on data redistribution

Restrictions on data redistribution are important to note before proceeding with data redistribution or when troubleshooting problems related to data redistribution:

The following restrictions apply to data redistribution:

- Data redistribution on partitions where tables do not have partitioning definitions is restricted: key
- When data redistribution is in progress:
- Starting another redistribution operation the same database partition group is restricted. on
- Dropping the database partition group is restricted.
- Executing an ALTER TABLE statement on any table in the database partition group is restricted:
- Altering the database partition group is restricted.
- Creating new indexes in the table undergoing data redistribution is restricted.
- Dropping indexes defined on the table undergoing data redistribution is restricted.
- Querying data in the table undergoing data redistribution is restricted.
- Updating the table undergoing data redistribution is restricted:
- Updating tables in a database undergoing a data redistribution that was started the REDISTRIBUTE DATABASE PARTITION GROUP command where the NOT ROLLFORWARD RECOVERABLE command parameter was specified is restricted: Although the updates can be made, if data redistribution is interrupted the changes made to the data might be lost and s0 this practice is strongly discouraged: using
- When the REDISTRIBUTE DATABASE PARTITION GROUP command is issued and the NOT ROLLFORWARD RECOVERABLE command parameter is specified:
- Data distribution changes that occur the redistribution are not roll-forward recoverable: during
- If the database is recoverable, the table space is put into the BACKUP PENDING state after accessing the first table within the table space: To remove the table from this state, you must take a of the table space changes when the redistribution operation completes backup
- During data redistribution, the data in the tables in the database partition group redistributed cannot be updated the data is read-only: Tables that are actively redistributed are inaccessible: being being
- For typed (hierarchy) tables, if the REDISTRIBUTE DATABASE PARTITION GROUP command is used and the TABLE parameter is specified with the value ONLY, then the table name is restricted to the name of the root table only: Sub-table names cannot be specified. being
- The partitioned table has an access mode of FULL ACCESS in the SYSTABLES.ACCESS\_MODE catalog table
- Data redistribution is supported for the movement of data between database partitions For partitioned tables, however; movement of data between ranges of data partitioned table is restricted unless both of the following are true:
- The partitioned table does not have any partitions currently being attached or detached:

- For replicated materialized query tables, if the data in a database partition group contains replicated materialized query tables, you must these tables before you redistribute the data: After data is redistributed, YOu can recreate the materialized query tables: drop
- For database partitions that contain multi-dimensional-clustered tables (MDCs) use of the REDISTRIBUTE DATABASE PARTITION GROUP command is restricted and will not proceed successfully if there are any multi-dimensional-clustered tables in the database partition group that contain rolled out blocks that are pending cleanup: These MDC tables must be cleaned up before data redistribution can be resumed or restarted:
- Dropping tables that are currently marked in the Db2 catalog views as in the state 'Redistribute in Progress' is restricted. To a table in this state, first run the REDISTRIBUTE DATABASE PARTITION GROUP command with the ABORT or CONTINUE parameters and an appropriate table list so that redistribution of the table is either completed or aborted. being drop

## Best practices for data redistribution

Data redistribution can be optimally performed when best practices for data redistribution are followed.

Consider the following best practices when planning your data redistribution:

- Ensure that all documented data redistribution prerequisites have been met By default, redistribution operations that are not roll-forward recoverable perform a precheck and proceed only if the verification completes successfully: To verify the prerequisites without launching the redistribution operation, specify the PRECHECK ONLY command parameter:
- Gather information and metrics about your database environment: If performance changes after the redistribution, you can use the information and metrics to identify the reason for the change.
- table is corrupted, you can restore the database from this backup.
- Back up the database before you perform the data redistribution. This is especially important if the redistribution operation is not roll-forward recoverable; if catastrophic failure occurs the redistribution and the database is lost or during
- Perform the redistribution during a planned outage, if possible: The instance does not need to be stopped; quiescing the database is sufficient:
- By default, redistribution operations that are not roll-forward recoverable force all users off the database and the database into a quiesced mode. You must still ensure that any applications or users that are allowed to access the quiesced database are not making updates, for the following reasons: put
- If a disaster occurs, recovering data changes that occurred during the
- Redistribution typically uses lot of resources on the servers. Parallel querying of data might cause both the redistribution and the queries to slow down significantly: Redistributing the data online can also cause lock timeouts or deadlocks:
- Perform a redistribution operation that is not roll-forward recoverable Data is moved in bulk instead of by internal insert and delete operations This reduces the number of times that a table must be scanned and accessed, which
- results in better performance:

- records are not required for each of the insert and delete operations. This means that you do not need to manage large amounts of active space and archiving space in your system when performing data redistribution. Log log log
- A uniform distribution of data might not always result in the best database your own target partition map for the redistribution operation.
- In general if you redistribute data in frequently accessed table such that infrequently accessed data is on few database partitions in the database partition group, and the frequently accessed data is distributed over larger number of database partitions, you can improve data access performance and throughput for the most frequently run applications that access this data.

## Data redistribution mechanism

Data redistribution can be performed by using different methods in different interfaces however internally the mechanism by which the data is moved is the same: It can be helpful to understand this mechanism so that you are aware of automatic changes made within the Db2 database environment\_ being

Data redistribution involves the use of the available source distribution map and target distribution map to identify hash database partitions that have been assigned to new location: The new location is identified by new database partition number: All rows that correspond to database partition that have a new iocation are moved from the database partition specified in the source distribution map to the database partition specified in the target distribution map.

Data redistribution internally invokes a utility that performs the following ordered actions:

- Obtains a new distribution map ID for the target distribution map, and inserts it into the SYSCATPARTITIONMAPS view: catalog
- Updates the REDISTRIBUTE\_PMAP\_ID column in the SYSCATDBPARTITIONGROUPS view for the database partition group with the new distribution map ID. catalog
- 3 Adds any new database partitions to the SYSCATDBPARTITIONGROUPDEF catalog view:
- Commits all catalog updates:
- Sets the IN\_USE column in the SYSCATDBPARTITIONGROUPDEF view to 'D' for any database partition that is to be dropped, if the DROP DBPARTITIONNUM command parameter was specified. catalog
- 6. Creates database files for all new database partitions if the ADD DBPARTITIONNUM command parameter is specified; also might create table spaces in the new database partitions
- Puts the table spaces into the BACKUP PENDING state, if the utility did not them into that state already: put
- 7 Redistributes the data on table-by-table basis for every table in the database partition group, in the following steps:
- b\_ Locks the row for the table in the SYSTABLES table: catalog
- C Invalidates all packages that involve this table: The distribution map ID associated with the table changes because the table rows are redistributed: Because the packages are invalidated, the compiler must obtain the new database partitioning information for the table and generate packages accordingly:
- d. Locks the table in super exclusive mode (with a z-lock).

- e Redistributes data by using bulk data movement operations.
- If the redistribution operation succeeds, the distribution map ID for the table is updated in SYSCATTABLES: The utility issues a COMMIT for the table and continues with the next table in the database partition group. If the operation fails before the table is fully redistributed, the utility fails. partially redistributed tables are left in the REDIST\_IN\_PGRS state and the table is inaccessible until the redistribute operation is either continued Any

Deletes database files and deletes entries in the SYSCATDBPARTITIONGROUPDEF catalog view for database partitions that were previously marked to be dropped.

- 8\_ Updates the database partition group record in the SYSCATDBPARTITIONGROUPS catalog view to set PMAP\_ID to the value of REDISTRIBUTE\_PMAP\_ID and REDISTRIBUTE\_PMAP\_ID to NULL.
- 9 Deletes the old distribution map from the SYSCATPARTITIONMAPS catalog view
- 10 Does a COMMIT for all changes.

When these steps are done data redistribution is complete: For more information about the success or failure status of the data redistribution and each of the individual data redistributions, review the redistribution file. log

## Redistributing data across database partitions by using the REDISTRIBUTE DATABASE PARTITION GROUP command

The REDISTRIBUTE DATABASE PARTITION GROUP command is the recommended interface for performing data redistribution:

## Procedure

To redistribute data across database partitions in a database partition group:

- 1\_ Optional: Perform backup of the database: See the BACKUP DATABASE command.
- It is strongly recommended that you create a backup copy of the database before you perform data redistribution that is not roll-forward recoverable:
- 2 Connect to the database partition that contains the tables. See the CONNECT statement catalog system
- 3\_ Issue the REDISTRIBUTE DATABASE PARTITION GROUP command:

Note: In previous versions of the Db2 database product, this command the NODEGROUP keyword instead of the DATABASE PARTITION GROUP keywords. used

Specify the following arguments:

## database partition group name

You must specify the database partition group within which data is to be redistributed:

## UNIFORM

OPTIONAL: Specifies that data is to be evenly distributed. UNIFORM is the default when no distribution-type is specified, s0 if no other distribution type has been specified, it is valid to omit this option.

## USING DISTFILE distfile-name

OPTIONAL: Specifies that a customized distribution is desired and the

file path name of a distribution file that contains data that defines the desired data skew. The contents of this file is used to generate target distribution map:

## USING TARGETMAP targetmap-name

OPTIONAL: Specifies that a target data redistribution map is to be used and the name of file that contains the target redistribution map.

For details, see the REDISTRIBUTE DATABASE PARTITION GROUP command-line utility information.

- Take a backup of all table spaces in the database partition group that are in the BACKUP PENDING state: Alternatively, a full database backup can be performed.
- 4 Allow the command to run uninterrupted. When the command completes, perform the following actions if the data redistribution proceeded successfully:

Note: Table spaces are only into the BACKUP PENDING state if the database is recoverable and the NOT ROLLFORWARD RECOVERABLE command parameter is used in the REDISTRIBUTE DATABASE PARTITION GROUP command. put

- Recreate any replicated materialized query tables dropped before redistribution.
- Execute the RUNSTATS command if the following conditions are met:
- The STATISTICS NONE command parameter was specified in the REDISTRIBUTE DATABASE PARTITION GROUP command, or the NOT ROLLFORWARD RECOVERABLE command parameter was omitted. Both of these conditions mean that the statistics were not collected data redistribution: during
- There are tables in the database partition group possessing a statistics profile:

The RUNSTATS command collects data distribution statistics for the SQL compiler and optimizer to use when choosing data access plans for queries.

- On Linux and UNIX operating systems: diagpath/redist/db\_name / db\_partitiongroup\_name timestamp/
- If the NOT ROLLFORWARD RECOVERABLE command parameter was specified, delete the control files located in the following paths
- On Windows operating systems: diagpath redist Idb\_name db\_partitiongroup timestamp | \_name

## Results

Data redistribution is complete and information about the data redistribution process is available in the redistribution file: Information about the distribution map that was used can be found in the Db2 explain tables. log

## Redistributing database partition groups using the STEPWISE REDISTRIBUTE DBPG procedure

Data redistribution can be performed built-in procedures. using

## Procedure

To redistribute a database partition group the STEPWISE\_REDISTRIBUTE\_DBPG procedure: using

- 1 \_ Analyze the database partition group regarding space availability and data skew the ANALYZE\_LOG\_SPACE procedure: log using
- The ANALYZE\_LOG\_SPACE procedure returns a result set (an open cursor) of the space analysis results, containing fields for each of the database partitions of the given database partition group. log
- 2 Create a data distribution file for a given table using the GENERATE\_DISTFILE procedure:
- 3\_ Create and report the content of a stepwise redistribution plan for the database partition group using the STEPWISE\_REDISTRIBUTE\_DBPG procedure:
- The GENERATE\_DISTFILE procedure generates a data distribution file for the given table and saves it the provided file name. using
- 4\_ Create a data distribution file for a given table the GET\_SWRD\_SETTINGS and SET\_SWRD\_SETTINGS procedures using
- The SET\_SWRD\_SETTINGS procedure creates or makes changes to the redistribute registry: If the registry does not exist, it creates it and add records into it: If the registry already exists, it uses overwriteSpec to identify which of the field values need to be overwritten\_ The overwriteSpec field enables this function to take NULL inputs for the fields that do not need to be updated:
- The GET\_SWRD\_SETTINGS procedure reads the existing redistribute registry records for the given database partition group.
- 5\_ Redistribute the database partition group according to the plan the STEPWISE\_REDISTRIBUTE\_DBPG procedure. using
- The STEPWISE\_REDISTRIBUTE\_DBPG procedure redistributes part of the database partition group according to the input and the setting file:

## Example

The following is an example of a CLP script on AIXO:

```
# # Set the database you wish to connect to # dbName= SAMPLE" # # Set the target database tion group name # dbpgName=" IBMDEFAULTGROUP" # # Specify the table name and schema # tbSchema= SUSER" tbName="STAFF" # # Specify the name of the data distribution file # distFile-"SHOME/sq]lib/function/SdbName. IBMDEFAULTGROUP_swrdData.dst" export DBZ INSTANCE-SUSER export DBZCOMM-TCPIP # Invoke cal] statements in clp # dbzstart connect to SdbName' parti-
```

```
# Analysing the effect of adding a database partition without applying the changes what if' # hypothetical analysis # # In the fo]lowing case, the hypothesis is adding database partition 40 50 and 60 to the # database partition group, and for database partitions 10,20,30,40,50,60 _ using respective # target ratio of 1:2:1:2:1:2_ # # NOTE: in this example only partitions 10 , 20 and 30 actually exist in the database # partition group # dbz ~V sysproc.analyze_ space( ' SdbpgName StbSchema StbName 2 'A' 40,50,60 ' 10,20,30,40,50,60 1,2,1,2,1,2') # # Analysing the effect of dropping database partition without applying the changes # # In the fol lowing case_ the hypothesis is dropping database partition 30 from the database # partition group, and redistributing the data in database partitions 10 and 20 using # respective target ratio of 1 # # NOTE: In this example database partitions 10_ 20 and 30 should exist in the database # partition group # dbz ~V sysproc.ana yze_log_space( ' SdbpgName StbSchema StbName 2 D 10,20 1,1' ) # # Generate data distribution file to be used by the redistribute process # -V ca]] sysproc.generate_distfilel StbSchema StbName SdistFile' ) # # Write wise redistribution plan into registry # # Setting the 10th parameter to 1, may cause currently running step wise redistribute # stored procedure to complete the current step and until this parameter is reset # to 0 and the redistribute stored procedure is ca] Ied again_ # -V ca]1 sysproc.set_ swrd settingse SdbpgName 255, 0 SdistFile" 1000 _ 12 , 2 , 1, 0 , 10,20,30 ' 50,50,50 ' ) # # Report the content of the step wise redistribution plan for the given database # partition group_ dbz ~V sysproc . swrd_settings SdbpgName 255, 2 , 2 , 2 , # # Redistribute the database partition group "dbpgName' according to the redistribution # plan stored in the regi= by set_ swrd_settings It starting with step 3 and # redistributes the data until 2 steps in the redistribution plan are completed. # dbz cal] SdbpgName 3 2) Jog step stop, get_ stry
```

## Monitoring a data redistribution operation

You can use the LIST UTILITIES command to monitor the progress of data redistribution operations on database.

## Procedure

Issue the LIST UTILITIES command and specify the SHOW DETAIL parameter: Tist utilities show detail

## Results

The following is an example of the output from this command:

ID

Type

REDISTRIBUTE

Database Name

RDST819

Partition Number

11

Description

RDST COMPACT On SPACE REUSE RECORD LEVEL INDEXING MODE INCREMENTAL

Start Time

02-20-2007 23:21:33.785819

State

Executing

Invocation Type

User

Progress Monitoring:

Estimated Percentage Complete 8

Summary

Total Work

1965600

Completed Work

155221

Total Number 0f Tables

15

Tables Completed

Tables In Progress

3

Current Table 1:

Description

NEWTON RDST\_V10\_0154

Total Work

655200 bytes

Completed Work

55001 bytes

Current Table 2:

Description

NEWTON RDST\_V1o\_015B"

Total Work

450200 bytes

Completed Work

54220 bytes

Current Table 3:

Description

NEWTON

Total Work

978901 bytes

Completed Work

46000 bytes

## Redistribution event log files

During data redistribution event logging is performed. Event information is logged to event files which can later be used to perform error recovery: log

When data redistribution is performed, information about each table that is processed is logged in of event files. The event files are named database-name.database-partition-group-name \_ timestamp \_ and database-name.database-partition-group-name \_ timestamp. pair 1og log

The files are located as follows: log

- The dbzinstprofl instancelredist directory on Windows operating systems,
- The homeinst/sq]lib/redist directory on Linux and UNIX operating systems

The following is an example of the event file names: log

SAMPLE. IBMDEFAULTGROUP.2012012620240204 SAMPLE. IBMDEFAULTGROUP.2012012620240204. 1og

These files are for a redistribution operation on a database named SAMPLE with a database partition group named IBMDEFAULTGROUP The files were created on January 26, 2012 at 8.24 PM local time:

The three main uses of the event files are as follows: log

- To provide general information about the redistribute operation, such as the old and new distribution maps.
- Provide users with information that helps them determine which tables have been redistributed so far by the utility
- To provide information about each table that has been redistributed, including the indexing mode being used for the table, an indication of whether the table was successfully redistributed or not, and the starting and ending times for the redistribution operation on the table:

## Recovery from errors related to data redistribution

Recovery from failures and errors that occur during data redistribution generally requires that you consult the redistribution event file: The file contains useful information about data redistribution processing, including information about which table or tables, if any, failed to be processed successfully log log

Possible reasons that a redistribution might fail include:

- A documented prerequisite for successful data redistribution was not met
- documented restriction on data redistribution was encountered that resulted in the interruption of the data redistribution.
- During data redistribution a table to be processed was encountered in a restricted access state, such as LOAD PENDING.
- other problem documented in the event Any

When you have identified and resolved the cause of the failure, perform the recovery by using the same redistribution interfaces that were used when the operation failed: For command was used, once the problem has been addressed you can begin data redistribution again by reissuing the command with one of the following options:

## CONTINUE

This option indicates that the redistribution operation should continue until all tables specified in the original REDISTRIBUTE DATABASE PARTITION GROUP command are redistributed.

ABORT

This indicates that the redistribution operation should be aborted and that all tables that have been redistributed, or partially redistributed, so far should be returned to the state were in before the REDISTRIBUTE DATABASE PARTITION GROUP command was first run on the database partition group. option they

These options cannot be specified unless a previous data redistribution operation failed or completed without redistributing all tables in the database partition group. The latter case can occur if the TABLE command parameter is used and only a subset of tables is specified. In these cases, the value of the REDISTRIBUTE\_PMAP\_ID column in the SYSCATDBPARTITIONGROUPS table will have a value different from -1.

If an interface other than the REDISTRIBUTE DATABASE PARTITION GROUP command was used, continuation or abortion of data redistribution is possible by redistributing data again the appropriate parameter value for the specified interface: See the reference information for the interface for the correct parameter values using

## Examples of redistribute event log file entries

Examples of common redistribute event files entries and descriptions of them provide useful reference that can be consulted when troubleshooting errors or interruptions that occur log during

There are two event files created each time you redistribute a database partition group. The file named database-name .database-partition-groupname timestamp provides a brief summary of the event: For example, SAMPLE. IBMDEFAULTGROUP.2012012622083174 contains: log

```
Data Redistribution Utility The fol lowing options have been specified Database partition group name IBMDEFAULTGROUP Data Redistribution option U Redistribute database partition group uniformly No _ of partitions to be added List of partitions to be added No _ of partitions to be dropped List of partitions to be dropped 2 The execution of the Data Redistribution operation on Begun at Ended at Table (poo] ID;objectID) 22.08.32 "DBZINSTI CL_SCHED" (2;4) 22.08.33 DBZINSTI' "CL_SCHED" (2;4) 22.08.33 DBZINSTI "DEPARTMENT" (2;5) 22.08.35 DBZINSTI DEPARTMENT" (2;5) 22.08.35 "DBZINSTI EMPLOYEE' (2;6) 22.08.36 "DBZINSTI EMPLOYEE' (2;6) 22.09.13 DBZINSTI PRODUCTSUPPLIER" (4;10) 22.09.15 "DBZINSTI PRODUCTSUPPLIER" (4;10)
```

tables have been successfully redistributed.

The file named database-name.database-partition-group-name timestamp \_ provides more detailed entries. The following examples illustrate some common entries is not defined, the examples illustrate the main fields and most common or most important field values. 1og log log

## Example 1: First event entry dumped during a redistribute operation log

2012-01-26-22.08.32.607340-300 I1850E893

LEVEL: Event

```
PID 27700 TID 46912984049984 PROC dbzsysc INSTANCE: dbzinstl NODE 000 DB SAMPLE APPHDL 0-74 APPID: #NO . dbzinstl_ AUTHID DBZINSTI HOSTNAME: EDUID 65 EDUNAME: dbzagent (SAMPLE) FUNCTION: Dbz , relation data serv sqlrdrin, probe:3852 CHANGE DB PART MAP ID IBMDEFAULTGROUP FROM "1" "3" success IMPACT None DATA #1 String, 24 bytes HexDump 01d Map Entries DATA #2 Dumped object of size 65536 bytes at offset 0, 61 bytes /home/dbzinstl/sq]lib/redist/27700.65.000.dump.bin DATA #3 String, 24 bytes HexDump New Map Entries: DATA #4 Dumped object of size 65536 bytes at offset 65672, 61 bytes
```

The first event entry dumped redistribute operation provides information about the distribution map files with which the utility will be working: In this case, the old distribution map for partition group IBMDEFAULTGROUP has an id of 1 and the new distribution map has an id of 3\_ A hexdump of each distribution map file is made to the redist directory in the instance path, and the names of the dump files are included in the In this example, the file named 27700.65.000.dump.bin contains both distribution maps. during log entry:

## Example 2: Event log associated with the start of the redistribute operation

2012-01-26-22.08.32.625956-300  12744E774

LEVEL: Event

PID

27700

TID 46912984049984

PROC dbzsysc

INSTANCE:

dbzinstl

NODE 000

DB

SAMPLE

APPHDL

0-74

APPID: #NO . dbzinstl.

AUTHID

DBZ INSTI

HOSTNAME :

EDUID

65

EDUNAME: dbzagent (SAMPLE)

FUNCTION:

relation data serv sq]rdrInitLogfileInfo, probe:1802

START

REDIST DB PART GROUP

IBMDEFAULTGROUP success

IMPACT

None

DATA #1

String, 28 bytes

Partitioning Option: UNIFORM

DATA #2

String, 23 bytes

Statistics:

USE PROFILE

DATA #3 String, 22 bytes

Indexing Mode: REBUILD

DATA #4 String, 17 bytes

PRECHECK MODE: Y

DATA #5

String,

16 bytes

QUIESCE MODE:

Y

This entry indicates that the start of the redistribute operation has completed successfully and that redistribution of tables is about to begin. The partitioning option, statistics option, indexing mode, precheck mode, and quiesce mode to be used for the redistribution operation are also shown:

In this example, the partitioning option is UNIFORM, which indicates that data will be redistributed uniformly: Other possible values for this option include TARGETMAP, CONTINUE and ABORT.

The statistics is USE PROFILE, which is the default statistics collection mode and means that if the table has a statistics profile, then statistics will be collected according to that profile. Otherwise, statistics will not be collected: If the value of this option is NONE, this indicates that the STATISTICS NONE was specified, which means that no statistics are to be collected for the table, regardless of whether the table has a statistics profile defined or not: option option

In this example, the indexing mode is REBUILD, which is the default indexing mode and means that indexes on each table will be rebuilt during data redistribution: If the value of this is DEFERRED, it means that the user specified the INDEXING MODE DEFERRED option, which results in indexes marked invalid option being during

In this example, the precheck mode is Y, which is the default precheck mode for data redistributions that are NOT ROLLFORWARD RECOVERABLE: This mode indicates that the redistribution operation begins only if the verification completes successfully:

In this example, the quiesce mode is Y, which is the default quiesce mode for data redistributions that are NOT ROLLFORWARD RECOVERABLE: This mode indicates that the

redistribution operation forces all users off the database and puts it into a quiesced mode

## Example 3: Event associated with start of redistributing a table log

LEVEL: Event

PID

27700

TID 46912874998080

PROC dbzsysc 0

INSTANCE: dbzinstl

NODE 000

DB

SAMPLE

APPHDL

0-113

APPID:

#NO . DBZ \_

AUTHID

DBZINSTI

HOSTNAME:

EDUID

181

EDUNAME: dbzagent (SAMPLE) 0

FUNCTION: Dbz , database utilities Redistribute \_ sqlurRedistributeTab]eByID

probe:8743

START

REDIST TABLE "DBZINSTI" SCHED" success "CL\_

IMPACT

None

This entry indicates that the start of redistributing table "CL\_SCHED" was successful:

## Example 4: Event log associated with successful completion of redistribution for a table

2012-01-26-22.08.33.659785-300  14614E541

LEVEL: Event

PID

27700

TID 46912874998080

PROC dbzsysc

INSTANCE: dbzinstl

NODE 000

DB SAMPLE

APPHDL

0-113

APPID: *NO . DBZ .

AUTHID DBZINST1

HOSTNAME:

EDUID

181

EDUNAME: dbzagent  (SAMPLE) 0

FUNCTION: 0bz,

database utilities Redistribute, sqlurRedistributeTableByID

probe:9350

STOP

REDIST TABLE "DBZINSTI' "CL\_SCHED" success

IMPACT None

This entry indicates that table "DBZINSTI" SCHED" has been successfully redistributed. If an error had occurred processing of this table, this entry would indicate failure: "CL\_ during

## Example 5: Event log associated with successful completion of redistribution of a database partition group

LEVEL: Event

PID

27700

TID 46912984049984

PROC dbzsysc

INSTANCE: dbzinstl

NODE 000

DB SAMPLE

APPHDL

0-74

APPID: #NO . dbzinstl\_

AUTHID

DBZINST1

HOSTNAME:

EDUID

65

EDUNAME: dbzagent (SAMPLE)

relation data serv sqlrdrdt, probe:1308

STOP

REDIST

IBMDEFAULTGROUP success

IMPACT

None

This entry indicates that redistribution of database partition group IBMDEFAULTGROUP completed successfully: If the operation had not completed successfully this entry would indicate failure:

These example entries can be a helpful reference when you consult your files to resolve errors that occur data redistribution or to verify that data redistribution complete successfully log during

## Scenario: Redistributing data in new database partitions

This scenario shows how to add new database partitions to a database and redistribute data between the database partitions. The REDISTRIBUTE DATABASE PARTITION GROUP command is demonstrated as part of showing how to redistribute data on different table sets within a database partition group.

## About this task

## Scenario:

A database DBPGI has two database partitions, specified as (0, 1) and a database partition group definition (0, 1).

The following table spaces are defined on database partition group DBPG\_l:

- Table space TS1 this table space has two tables, T1 and T2
- Table space TS2 this table space has three tables defined, T3, T4, and T5

Starting in Version 9.7, you can add database partitions while the database is running and while applications are connected to it: However; the operation can be performed offline in this scenario by changing the default value of the DBZ\_FORCE\_OFFLINE\_ADD\_PARTITION registry variable to TRUE

## Procedure

To redistribute data between the database partitions in DBPGl:

- 1. Identify objects that must be disabled or removed before the redistribution
- a. Replicate MQTs: This type of MQT is not supported as part of the redistribution operation: must be dropped before running the redistribution and recreated afterward. They
- b Write-to-table event monitors: Disable any automatically activated write-to-table event monitors that have table that resides in the database partition group to be redistributed
- C Explain tables: It is recommended to create the tables in a single partition database partition group. If are defined in a database partition group that requires redistribution, however; and the data generated to date does not need to be maintained, consider dropping them. The tables can be redefined once the redistribution is complete: explain they explain
- d. Table access mode and state: Ensure that all tables in the database partition groups to be redistributed are in full access mode and normal table states.

```
SELECT tabschema tabname FROM syscat.tables WHERE partition_mode R
```

```
SELECT distinct evmonname FROM syscat.eventtables E JOIN syscat.tables T on T.tabname E.tabname AND T.tabschema E.tabschema JOIN syscat.tablespaces S on S. tbspace T.tbspace AND S.ngname DBPG_1"
```

```
SELECT DISTINCT TRIM(T . OWNER) TRIM(T. TABNAME) AS NAME_ T.ACCESS_MODE _ A.LOAD_STATUS FROM SYSCAT. TABLES T, SYSCAT. DBPARTITIONGROUPS N, SYSIBMADM.ADMINTABINFO A WHERE T.PMAP ID N . PMAP ID AND A.TABSCHEMA T.OWNER
```

```
AND A. TABNAME T TABNAME AND N. DBPGNAME DBPG_1 AND   (T.ACCESS_MODE F' OR A.LOAD_STATUS IS
```

- e Statistics profiles: If a statistics profile is defined for the table, table statistics can be updated as part of the redistribution process. Having the redistribution utility the statistics for the table reduces I/0, as all the data is scanned for the redistribution and no additional scan of the data is needed for RUNSTATS. update
- 2 Review the database configuration. The util\_heap\_sz is critical to the data movement processing between database partitions allocate as much memory as possible to util\_heap for the duration of the redistribution. Sufficient sortheap is required, if index rebuild is done as part of the redistribution. Increase util\_heap\_sz and sortheap as necessary to improve redistribution performance: ~Sz
- 3\_ Retrieve the database configuration settings to be used for the new database partitions. When database partitions, a default database configuration is used. As a result, it is important to the database configuration on the new database partitions before the REDISTRIBUTE DATABASE PARTITION GROUP command is issued. This sequence of events ensures that the configuration is balanced: adding update
- 4 Back up the database (or the table spaces in the pertinent database partition group), before starting the redistribution process. This action ensures a recent recovery
- 5 Add three new database partitions to the database. Issue the following commands:

```
RUNSTATS on table schema. table USE PROFILE runstats_profile SET PROFILE ONLY
```

```
SELECT name_ CASE WHEN deferred value flags AUTOMATIC THEN deferred value flags ELSE substr(deferred_value,1,20) END AS deferred_value FROM bmadm.dbcfg WHERE dbpartitionnum existing-node AND deferred_va ue != AND name NOT ('hadr Ioca] host hadr Ioca] SVC hadr_peer_window hadr remote host hadr remote inst hadr remote SVC hadr_syncmode' hadr timeout backup_pending codepage codeset co]late info country database consistent database_Tevel hadr dbrole retain_Status Toghead ' multipage_alloc numsegs 'pagesize' release restore_pending " restrict access ro] 1fwd_pending territory user exit status number_compat varchar2_compat database_memory' ) sysi 1og_
```

START DBM DBPARTITIONNUM 3 ADD DBPARTITIONNUM HOSTNAME HOSTNAME3 PORT PORT3 WITHOUT  TABLESPACES; START DBM DBPARTITIONNUM 4 ADD DBPARTITIONNUM HOSTNAME HOSTNAME4 PORT PORT4 WITHOUT  TABLESPACES; START DBM DBPARTITIONNUM 5 ADD DBPARTITIONNUM HOSTNAME HOSTNAMES TABLESPACES;

If the DBZ\_FORCE\_OFFLINE\_ADD\_PARTITION is set to TRUE, new database partitions are not visible to the instance until it has been shut down and restarted: example: For

STOP DBM; START DBM;

- 6 Define temporary table space containers on the newly defined database partitions system
- ALTER TABLESPACE tablespace\_ name ADD container\_information ON dbpartitionnums (3 to 5)
- 7 Add the new database partitions to the database partition groups. The following command changes the DBPG\_1 definition from (0, 1) to (0, 1, 3,4, 5):
- ALTER DATABASE PARTITION GROUP DBPG\_1 ADD dbpartitionnums (3 to 5) WITHOUT TABLESPACES
- Define permanent data table space containers the newly defined database partitions. on

ALTER TABLESPACE tablespace\_ name ADD container\_information ON dbpartitionnums (3 to 5)

- 9 Apply the database configuration settings to the new database partitions (or issue single UPDATE DB CFG command all database partitions). against
- 10. Capture the definition of and then drop any replicated MQTs existing in the database partition groups to be redistributed:

dbzlook -d DBPGl schema -t replicated\_MQT\_table\_ names -0 repMQTs.clp

- 11\_ Disable any write-to-table event monitors that exist in the database partition groups to be redistributed.

SET EVENT MONITOR monitor name STATE

- 12. Run the redistribution utility to redistribute uniformly across all database partitions

REDISTRIBUTE DATABASE PARTITION GROUP DBPG NOT  ROLLFORWARD RECOVERABLE UNIFORM STOP AT 2006-03-10-07.00.00 . 0oo000;

Let us presume that the command ran successfully for tables Tl, T2 and T3, and then stopped due to the specification of the STOP AT option.

To abort the data redistribution for the database partition group and to revert the changes made to tables Tl, T2, and T3, issue the following command: REDISTRIBUTE DATABASE PARTITION GROUP DBPG\_1 NOT  ROLLFORWARD RECOVERABLE ABORT;

You might abort the data redistribution when an error or an interruption occurs and you do not want to continue the redistribute operation. For this scenario, presume that this command was run successfully and that tables Tl and T2 were reverted to their original state.

To redistribute T5 and T4 only with 5000 4K pages as DATA BUFFER:

REDISTRIBUTE DATABASE PARTITION GROUP DBPG 1 NOT   ROLLFORWARD RECOVERABLE UNIFORM TABLE (T5, T4) ONLY DATA BUFFER 5000;

If the command ran successfully, the data in tables T4 and T5 have been redistributed successfully:

To complete the redistribution of data on table Tl, T2, and T3 in a specified order; issue:

REDISTRIBUTE DATABASE PARTITION GROUP DBPG\_1 NOT   ROLLFORWARD RECOVERABLE CONTINUE TABLE (T1) FIRST;

Specifying TABLE (T1) FIRST forces the database manager to process table T1 first s0 that it can return to online (read-only) before other tables. AII other tables are processed in an order determined by the database manager: being

## Note:

- The ADD DBPARTITIONNUM parameter can be specified in the REDISTRIBUTE DATABASE PARTITION GROUP command as an alternative to performing the ALTER DATABASE PARTITION GROUP and ALTER TABLESPACE statements in steps 7 on page 90 and 8 on page 90. When database partition is added by using this command parameter; containers for table spaces are based on the containers of the corresponding table space on the lowest numbered existing partition in the database partition group.
- The REDISTRIBUTE DATABASE PARTITION GROUP command in this example is not roll-forward recoverable
- After the REDISTRIBUTE DATABASE PARTITION GROUP command finishes, all the table spaces it accessed will be left in the BACKUP PENDING state. Such table spaces must be backed up before the tables contain are accessible for write operations. they

more information, refer to the "REDISTRIBUTE DATABASE PARTITION GROUP command"\_ For

Consider also specifying a table list as input to the REDISTRIBUTE DATABASE PARTITION GROUP command to enforce the order that the tables are processed: The redistribution utility will move the data (compressed and compacted) Optionally, indexes will be rebuilt and statistics updated if statistics profiles are defined. Therefore instead of previous command, the following script can be run:

REDISTRIBUTE DATABASE PARTITION GROUP DBPG\_1 NOT   ROLLFORWARD   RECOVERABLE uniform TABLE (t1, t2 FIRST;

## Index

## 3

| best practices      |    |
|---------------------|----|
| data redistribution | 77 |
| BLU                 |    |

capacity

| overview                                   |
|--------------------------------------------|
| database partitions 27 catalog catalog     |
| collocation                                |
| column 13 13 column-organized tables 14,15 |
| Column-organized                           |
| partition configuration                    |
| multiple partitions                        |
| partitioned database 27                    |
| SMS table spaces                           |
| 51                                         |
| adding                                     |
| configuration parameters                   |
| coordinator partitions                     |
| containers                                 |

## D

55

| data                                                                                                                                                                                                                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| distribution partitioned database environments redistribution best practices 77 database partition groups database partitions 69 determining need 72 error recovery 84 event logging 83 file entries 85 log space requirements 74 mechanism 78 methods 70 overview 69, 79 recovery 83 log |
| database configuration file                                                                                                                                                                                                                                                               |
| changing 51                                                                                                                                                                                                                                                                               |

28

| database partition expressions details 52 database partition groups                                                                                                                                                                                                              |                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| data location determination 21 IBMDEFAULTGROUP 45 overview 19 tables 45 database partition servers dropping 67 issuing commands 55 multiple logical partitions 29 specifying 50 database partitions adding overview 37 restrictions running system stopped system (UNIX) catalog | 39 38 39 stopped system (Windows) 41 |
| redistributing data partitions 17 databases crea partitioned database environments 27 data partitioning enabling 27 redistributing data 69 db2_all command overview 56, 57 partitioned database environments 55 ting                                                             | spreading data across multiple       |
| specifying 57 db2_call_stack command 57 db2_kill command 57 db2nchg command                                                                                                                                                                                                      |                                      |
| configurations 54 db2ncrt command db2ndrop command                                                                                                                                                                                                                               |                                      |
| changing database partition server adding database partition servers                                                                                                                                                                                                             |                                      |
| dropping database partition servers 67 db2nlist command 49 declustering                                                                                                                                                                                                          |                                      |
| 1,17 distribution details 22 partial keys                                                                                                                                                                                                                                        |                                      |
| partitioned database                                                                                                                                                                                                                                                             |                                      |
| environments 45                                                                                                                                                                                                                                                                  |                                      |
| distribution maps details 21                                                                                                                                                                                                                                                     |                                      |

## E

| environment variables                      |
|--------------------------------------------|
| SRAHBUFDIR 58                              |
| SRAHBUFNAME 58                             |
| SRAHENV 62                                 |
| rah command 62                             |
| RAHDOTFILES 64                             |
| error messages                             |
| partitioned databases 42 event log file 85 |
| existing partitioned databases 14          |

| FCM                     |
|-------------------------|
| service syntax 47 entry |

| hardware                             | hardware    |
|--------------------------------------|-------------|
| parallelism                          | parallelism |
| partitions                           | partitions  |
| processors                           | processors  |
| hash partitioning hybrid environment | 15          |

| I/0 parallelism overview 2 independent column tables                                                     |
|----------------------------------------------------------------------------------------------------------|
| independent column-organized partitioned environment 15 instances                                        |
| partition servers 28 database partition servers partition servers changing 54 dropping 67 adding listing |
| inter-partition query parallelism 31 interquery parallelism                                              |
| intrapartition parallelism enabling 32 used with inter-partition parallelism intraquery parallelism      |

| keys         |
|--------------|
| distribution |

22

| licenses                          |
|-----------------------------------|
| partitioned database environments |

| logical database partitions database partition servers details        | 29, 50   |
|-----------------------------------------------------------------------|----------|
| logical partitions multiple 29                                        |          |
| redistribute events 85 space requirements data redistribution 74 logs |          |

## M

| monitoring                                                     |
|----------------------------------------------------------------|
| data redistribution 82 rah processes 59                        |
| MPP environments                                               |
| MQTs replicated 25                                             |
| multiple logical partitions configuring 30                     |
| multiple partition configurations multiple-partition databases |
| database partition groups 19                                   |

## P

| parallelism                                                                                                   |
|---------------------------------------------------------------------------------------------------------------|
| backups 2 hardware environments                                                                               |
| I/0                                                                                                           |
| overview                                                                                                      |
| index creation 2 inter-partition 2                                                                            |
| intra-partition enabling 32                                                                                   |
| overview 2                                                                                                    |
| load utility 2                                                                                                |
| overview                                                                                                      |
| partitioned database environments                                                                             |
| partitions processors query declustering partial                                                              |
| overview                                                                                                      |
| partitioned 13                                                                                                |
| partitioned database environment 14, 15 Partitioned database environment 13 partitioned database environments |
| creating 27                                                                                                   |
| data redistribution 88                                                                                        |
| 66                                                                                                            |
| duplicate machine entries 50                                                                                  |
| errors when adding database                                                                                   |
| partitions 42                                                                                                 |
| duplicate elimination 50                                                                                      |
| entry                                                                                                         |
| 50                                                                                                            |
| specifying                                                                                                    |
| 1,17                                                                                                          |
| 24                                                                                                            |
| partition compatibility redistributing data setting up 27                                                     |
| overview                                                                                                      |
| machine list                                                                                                  |
| database partition groups 19                                                                                  |
| dropping partitions                                                                                           |

80

| number ranges defining port   |
|-------------------------------|
| Windows 28                    |
| prefix sequences 60           |
| Prerequisities 14 procedures  |
| STEPWISE REDISTRIBUTE_DBPG    |

queries

## R

| rah command controlling 62 determining problems 65 environment variables 62 monitoring processes 59 overview 56, 57 sequences 60 RAHCHECKBUF environment variable 58 RAHDOTFILES environment variable 64 RAHOSTFILE environment variable 50 RAHOSTLIST environment variable 50 RAHWAITTIME environment variable 59 recursively invoked 60 running commands in parallel 58 setting default environment profile 65 55, prefix   |    |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|
| variable 58 RAHDOTFILES environment variable 64 RAHOSTFILE environment variable                                                                                                                                                                                                                                                                                                                                               | 50 |
| variable 60 RAHWAITTIME environment variable 59 recovery data redistribution errors                                                                                                                                                                                                                                                                                                                                           |    |
| 84 redistribution of data across database partitions 69 database partition groups 55, 80 event file 83 methods 70 necessity 72 log                                                                                                                                                                                                                                                                                            | 25 |
| prerequisites 73 procedures 80                                                                                                                                                                                                                                                                                                                                                                                                |    |
| restrictions 76 redistribution utility monitoring progress 82 replicated materialized query tables                                                                                                                                                                                                                                                                                                                            |    |
| rOW-organized tables 14,15                                                                                                                                                                                                                                                                                                                                                                                                    |    |

## S

scalability

| hardware environments SIGTTIN message 57                                                                |
|---------------------------------------------------------------------------------------------------------|
| single partitions multiple-processor environments single-processor environments SMP cluster environment |
| stdin 57 STEPWISE_REDISTRIBUTE_DBPG procedure redistributing data 80 adding                             |

| tables   |
|----------|
|          |
|          |

| uniprocessor environments utilities   |
|---------------------------------------|
| parallelism 2                         |

## W

| Windows                         |
|---------------------------------|
| database partition additions 41 |

Printed in USA