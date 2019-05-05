# IAM

## What is IAM
* IAM allows managing users level of access in the AWS consol
* Grants permission to different aspects of AWS
* Granular permission control
* Identity Federation supporting Active Directory, Facebook, LinkedIn, etc.
* Requires MFA
* Provides temporary access to services when neccessary
* Allows setting password rotation timeframe
* Supports PCI DSS Compliance
* **IAM is incredibly important, as it defines the rules by which all other AWS resources will interact/operate**

## Terminology

## 1. Users
* End users such as people, employees of a company, etc.

## 2. Groups
* Groups of people. Each user in group inherits permission in group.

## 1. Policies
* Policies are made up of documents called Policy Documents. These docuemntsare in JSON format and defined what a User/Group/Role is able to do

## 1. Roles
* A role describes ways different resources in AWS may interact with each other.
* For example, a role might specify that an EC2 isntance is privelaged to right to an S3 bucket1

## Summary of IAM Fundamentals
* IAM is universal, and not specific to a region (at this time)
* The root account is the account created when you create your AWS account, and it has complete Admin access
* New users by default have **NO** permissions when first created
* New users are assigned an Access Key ID and Secret Access Key for programatic access to AWS
* Programmatic and Console (UI) access are different, and are enabled for a user independantly
* Access Key ID and Secret Access Key **ONLY** allow programmatic access, not console accesss
* Your Access Key ID and Secrey Access Key will only be visible once, so save the CSV file of the keys somewhere secure
* Use MFA to protect access to the root account. MFA uses Google Authenticator app
* Can customize password rules (such as minimum length and inclusion of special characters) and rotation timefram

## IAM Exam Review
* IAM consists of the following:
  * User
    * Users are the individual end users of the AWS resources
    * Organized into Groups
  * Group
    * Groups of Users
    * Organizations of users with different permission settings
  * Roles
    * Define access of AWS resrouces to other AWS resoures
    * For example, the ability of an EC2 to read/write to S3
    * This might be named an 'S3-Admin' role
  * Policies
    * Policies define the permissions that make up Users, Groups, and Roles
    * Are individual JSON files that define an indidual permission
    * Can use wildcards to grant general/wide access when needed
    * Policies are explored more in the *Certified Security Speciality* AWS Certificatio
* IAM is universal, not regional
* The "root account", which is created when the account is created, has full Admin access across the AWS console
* New users by defaule have **NO** permissions, anc can therefore do nothing
* New users by default will have an Access Key ID and Access Secret Key created for their account by default
* Access Key ID and Secret Access Key are only visible once, so make sure to save
* IAM allows defining password strength rules, and password rotation policy rules

# S3

## What is S3?
* Simple Storage Service
* Provides developers securable, durable, 1highly scalable, object storage
* Simply put, a way to store files
* Able to store any size files, and accessable anywhere on the web

## S3 Basics
* Allows you to upload files
* Files may be between 0 Bytes and 5 TB
* For large file uploads to an S3 bucket, design your API to use the Multipart Upload API for all objects
* AWS charges by the GB for file uploads
* S3 is organized into "buckets", which are interactable like directories on a file system
* Individual files are stored inside a bucket
* S3 is a universal namespace, so must be universally unique
* Example bucket URL:
  * `https://s3-eu-west-1.amazonaws.com/acloudguru`
  * `acloudguru` is the bucket name
  * `s3-eu-west-1` is the regio
* Uploading a file to a bucket returns an HTTP 200 response status on succesful ulpload

## Data Consistency Model for S3
* Read after write consistency for PUTS of new objects
* Eventual consistency for overwrite PUTS and DELTES (can take some time to propogate)
* Basically, after writing a new file (a.k.a. a new upload), the file will be immediately readable and its state will be accurate
* In contrast, if reading a file after a PUT or DELETE which modified an existing file, the file's state upon reading may or may not reflect the new changes
* Eventually, the modification will become consistent and reflect the changes
* acloudguru says after about a minute, the data consistency of modified files will be accurate

## S3 as a Simple Key-Value Storage
* S3 is a object based, which means it works for storing files of all varieties, but is not capable of installing an operating system or database
* S3 stores files via a key-value storage
* The key is the file name, and the value is the actual file contents
* There is also a version ID and metadata attached to every stored files
* Metadata includes customizable tags
* There are also subresources in S3:
  * Access Control Limits control access of Users/Groups to certain files in a bucket
  * Torrents (not covered in detail in this course)

## S3 Availability
* S3 is built for 99% availability
* Amazon guarentees 99.9% availability in the Service Level Agreement
* Amazon garuentees 99.999999999% durability for S3 information, meaning this percentage of files uploaded to S3 will not be lost
* Tiered Storage is available
* There is Lifecycle Managemnt, which manages files between storage services depending on time
* There is file versioning and version control within S3
* There is encryption service for uploaded files
* Control is managed by Control Lists and Bucket Policies
* Bucket policies define access policies for the entire bucket, whereas Access Control Lists control access with respect to files

## S3 Tiered Storage
* **S3 Standard**
  * Provides 99.99% availability and 99.999999999% durability for files, and is stored reduntantly across multiple facilities
  * Designed to sustain loss of 2 concurrent facilities
* **S3 IA**
  * Infrequent Access
  * Intendee for data that is accessed less often, but requires rapid access when needed
  * Lower fee for storage than S3, but charged a retrieval fee
* **S3 One Zone - IA**
  * Lower cost version of normal IA, but is only stored in one Availability Zone
* **Glacier**
  * Cheapest storage option
  * Intended for data archiving
  * Available in Expedited, Stanard, and Bulk varieties
    * **Expediated** 
    * **Standard** 
    * **Bulk**

## S3 Charges
Charged for:
* Storage of files
* Requests, a.k.a. downloading stored files
* Storage Management Pricing, a.k.a. limiting access to S3 items via tagging
* Data Transfer Pricing, a.k.a. transferring data from one region to another
* S3 Transfer Acceleration

## S3 Transfer Acceleration
* Enables fast, easy, and secure transfer of files between end users and an S3 bucket
* Uses CloudFront, which is a network globally distributed edge locations
* Basically data is routed over an optimized network path

## S3 Exam Tips
* S3 is object based storage
* Object based storage allows uploading files but not installing an operating system which would be blolock based storage
* Files can be 0 Bytes to 5 TB
* Files are stored in buckets, which are like directories on a file system
* S3 is a universal namespace, so bucket names must be universally unique
* Example of S3 bucket URL:
  * `https://s3-eu-west-1.amazonaws.com/acloudguru`
* Read-after-Write consistency for PUTS of new objects
* Eventual consistency for overwrite PUTS and DELETES (can take time to propogate across regions)
* S3 is available in the following tiers:
  * S3 (or S3 standard)
		* Durable, immediately available, frequently accessed
  * S3 - IA (Infreqently Accessed)
		* Durable, immediately avaialable, infrequently accessed
    * Cheaper flat rate than S3, but charged per retrieval
  * S3 One Zone IA
		* Even cheaper version of S3 IA, but only available in one availability zone
  * Glacier
		* Data archival service
		* Standard retrieval time is 3-5 hours, although different pricing models are avaialbe for this
* Fundamentals of an S3 object:
	* Key (file name)
  * Value (file contents)
  * Version ID
  * Subresources
    * ACL (Access Control Lists)
    * Torrent info
* Uplpoading to S3 will return an HTTP 200 response status code on succesful upload
* Default limit of 100 buckets per account in S3

## S3 Create an S3 Bucket Exam Tips
* Buckets are a universal namespace
* Uploading an object to an S3 bucket succesfully produces an HTTP 200 response status code
* Supports encryption:
	* Client side encryption
	* Server side encrpytion with Amazon S3 Managed Keys (SSE-S3)
  * Server Side encrpytion with customer provided keys (KMS)
	* Control access to buckets using either a bucket ACL or Bucket policies
* By default buckets are private and all objects uploaded to a bucket are private


## S3 Versioning Lab Exam Tips
* By defualt versioning is disabled, and must be enabled
* Once versioning is enabled, versioning cannot be disabled, only suspended
* When a new version of a file is uploaded to a bucket, overriding an existing version that was set to public, the object will be private and must be reset to public
* There is support to restrict deletes to MFA only
* Versioning stores all versions of an object
* Versioning integrates with lifecycle rules

## Cross Region Replication Lab
* Cross region replication requires versioning to be enabled in source and destination bucket
* Regions must be unique
* Files in an existing bucket are not replicated automatically. All subsequent updated files will be replicated automatically.
* You cannot replicate to multiple buckets or use daisy chaining (at this time)
* Delete markers are not replicated
* Deleting individual versions or delte markers will not be replicated

## S3 Lifecycle Managemenet Exam Tips
* Can be used in conjunction with versioning
* Can be applied to current versions, and previous versions
* Following actions can be set up on time basis:
  * Transition to S3 IA, such as 30 days after upload
  * Archive to Glacier, such as 30 days after adding to S3 IA
  * Permanently Delete


## CloudFront CDN
* **Content Delivery Network (CDN)** is a system of distributed servers (a network) that deliver web pages and other content to a user based on the geographic locations of the user, the origin of the webpage, and the content deliviring server
* Basically, rather than distributing web content from a single central location, the contnet is cached on edge locations closer to the end users
* Key components of CDN:
  * **Edge Location**: This is the location where content will be cached. Different than an AWS Region/AZ
  * **Origin**: The origin of all the web resource files the CDN will distrubut. Can be an EC2, an ELB, or Route53
  * **Distribution**: THe name given to the CDN which consists of a collection of edge locations  
* Process Overview:
  1. User makes a request to a URL. This URL is a distribution URL.
  2. The request is routed to the closest edge location to the user
  3. The edge location server determines if the requested resource is already cached
  4. If the file is cached, the edge location server serves the content back to the use
  5. If the content is not already cached, the edge location server requests the resource from the origin server
  6. When the resource is served from the origin, the edge server cahces the resource, and serves it back to the end user
* The performance advantage from the CDN is only effectual after the content is cached, a.k.a. after an end user has reqeusted a specific resource
* The file is cached on the edge location for the duration of the **Time to Live (TTL)**
* The TTL is an important design consideration, as a poorly chosen TTL such as one longer than the average update time will induce lots of manual cache emptying, which costs mone
* CloudFront offers a Web Access Firewall (WAF), which is an application level firewall, mainly used to prevent SQL injections
* Creating and updates of CloudFront distrubutions often take 15-20 minutes for changes to propogate out to the edges
* Cloudfrount allows Whitelisting and Blacklisting geographic regions by the **Edit Geo-Locations** feature
* CloudFront allows **Invalidations**, which stops files from being cached on edge locations, but must be manually triggered and costs money
* Invalidations are used when you accidnelty push a change you wihs to stop from propogating to the edge locations


### Key Terminology:
* **Web Distribution**: Typically used for static websites
* **RTMP**: Used for media streaming

### Examp Tips
* An **Edge Location** is the location (server) where the content will be cached. Seperate from the AWS Region and AZ
* An **Origin** is the origin of all the files the CDN will distribute. This can be an S3 Bucket, EC2 isntance, Elastic Load Balancer, or Route53
* Considering TTL at design time, mainly in reference to rate of updates
* Use presigned URLs or presigned cookeis to secure content behind an authentication
* CloudFront allows **Invalidations**, which stop a pushed change from propogating to all the edge locations, but costs a fee
* In addition to reading files, CloudFront also allows writing changes to the edge locations, which are then propogated back to the origin


## S3 Security and Encryption
* By default, all newly created buckets are private
* You can setup access to your buckets using:
  * Bucket Policies
  * Access Control Lists
* S3 buckets can be configured to create access logs, which log all requests made to the S3 bucket

### Encryption
* There are two types of encryption, **In Transit**, and **At Rest**.
* **In Transit**:
  * Data in the process of being sent to/from a computer to the S3 bucket
  * Secured using SSL/TLS
* **At Rest**:
  * Data existing in the bucket
  * There are 4 methods for securing data at rest:
    * **SSE-S3**
    * **SSE-KMS**
    * **SSE-C**
    * **Client Side Encryption**

#### Encryption of Data at Rest

##### Server Side Encrpytion
* **Server Side Encryption**
  * **S3 Manage Keys - (SSE-S3)**
    * Each object is encrypted by a unique key
    * Each key itself is encrypted itself with a master key, and the master keys are regularly rotated
    * Amazon handles all keys for the users
    * AES256 Encryption of data
    * User simply uses **Encrypt** option on object
* **AWS Key Management Service, Managed Keys (SSE-KMS)**
  * Similar to SSE-S3, but with additional benefits and additional charges
  * Seperate permissions for use of envelope key
  * An **Envelope Key** is a key that protects the data encryption keys
  * Adds another level of additional protection
  * **SSE-KMS** also provides an Audit Trail feautre, which shows who is decrpypting objects and when
  * **SSE-KMS** also has options of creating/managing keys yourself, as well as using the default key
* **Server Side Encryption with Customer Provided Keys (SSE-C)** 
  * Allows user to provide their own keys, and amazon uses the customer's provided keys to encrpyt/decrpyt files when reading/writing to disk

##### Client Side Encryption
* Client encrypts their own objects, and upload the encrpyted objects to S3
* Client decrpyts object when the pull manully encrypted files from S3 
 

### Storage Gateway
* AWS Storage Gateway is a services that connects an on-premises software appliance with cloud-based storage
* Provides seamless and secure connection between data center processesing with AWS S3 cloud based storage
* Storage Gateway's software appliance is available for download as a virutal machine image that you install in the data center
* Supports both VMware ESXi and Microsoft Hyper-V
* Storage Gateway is basically a virtual machine

#### Types of Storage Gateways
* **File Gateway (NFS)**
  * Store flat files in S3
* **Volumes Gateway (iSCSI)**
  * Store files in block based storage
  * Can store flat files, but also save virtual hard disk with a virtual machine or database installed on
  * Two Types:
    * **Stored Volumes**
    * **Cached Volumes** 
* **Tape Gateway (VTL)**

### File Gateway
* Files are stored in S3 buckets and accessed through an NFS mount point
* Ownership, permissions, and timestamps are durably stored in S3 in the user-metadata of the object associated with the file
* Once objects are transferred to S3, they can be manipulated as regular S3 objects

### Stored Volumes
* An interface that presents an application with disk volumes
* Volumes use iSCSI block based storage
* Acts as a virtual hard drive service
* Volumes can be snapshotted and stored as backups using **Elastic Block Store (EBS)**
* Snapshots are incremental, meaning only the changes from the last snapshot are stored
* Snapshots are also compressed when stored to minimize storage costs
* Snapshots are flat files, and can (and are) stored in S3

### Stored Volumes Highlights
* Stored volumes act as a virtual hard-dirk
* There is a complete copy of all data  on premesise at any given time, and this acts as the data source for the application server
* Over time, backups of the volume are incrementally stored to S3
* Allows volume size of 16TB (double check this)

### Volume Storage Architecture Diagram
![Volume Storage Architecture Diagram](/images/stored_volumes_architecture.png) 

### Cached Volumes
* Cached Volumes let you use S3 as your primary data source
* Only the frequently accessed data is kept on premise, measured by most recenrtly read
* The rest of the data is stored on S3
* Allows storing volumes of up to 32TB

### Cached Volumes Architecture Diagram
![Cached Volumes Architecture Diagram](/images/cached_volumes_architecture.png) 

### Tape Gateway
* Tape gateway offers a durable, cost-effective way to archive data in the cloud
* Supported by NetBackup, Backup Exec, Veeam
* Basically creates an archive file, and stores the archive in S3
* Can also setup lifecycle rules in the S3 bucket to also backup archives to glacier

### Storage Gateway Exam Tips
* File Gateway is for flat files and stored them directly in S3
* No block based storage or installed OS, databases, etc.
* **Volume Gateway**:
  * **Stored Volumes**: Entire dataset is stored on site and is asynchronsouly backup up to S3
  * **Cached Volumes**: Entire dataset is stored on S3 and the most frequently accessed files are cached on site
* **Gateway Virtual Tape Library (VTL)**
  * Used for backup and uses popular backup applications like NetBackup, Backup Exec, and Veeam
* Exam questions will likely be scenario based, and ask the testee to evaluate which service is best for a given use case

## Snowball
* Snowball came from an older service called **Import/Export Disc**
* This service allowed mailing physical hard drives to upload/download data directly from disk at an Amazon location
* Normally for large amounts of data (i.e. >1TB), possibly combined with an otherwise slow internet connection
* To fix this, Amazon expanded the service by offering three options:
  * **Snowball**
  * **Snow Edge**
  * **Snowmobile**

### Snowball
* A physical device mailed by Amazon, roughly the size of a suitcase, which allows petebyte-scale storage
* Basically, you load a large amount of data on to the Snowball and mail it back to Amazon and they load it into AWS of the drive
* Normally used due to network speed, network costs, or securuty concerns
* Available in 80TB size (possibly other size)
* Only has onboard storage capacity, not compute capacity
* Data is encrypted on the device using 256-bit encryption
* Amazon ensures software erasure of data from Snowball device after use is done

### Snowball Edge
* Similar to Snowball, but with 100TB size and onboard compute capacity
* Somewhat like a miniture AWS data center
* Can run AWS Lambda functions from Snowball Edge
* Example use: A running airplane uses a Snowball Edge to collect data during flight. Lambda functions execute and store metrics appropriately during flight, and data is offloaded after flight

### Snowmobile
* A 100PB (petabyte) storage and data transfer solution
* Literally a shipping container of data storage on an 18-wheeler truck
* Only used by large companies to move massive amounts of data

### Exam Tips for Snowball
* Know what Snowball is
* Know that Import/Export drive was the original service Snowball came from
* Know Snowball can:
  * Import from Snowball to S3
  * Export from S3 to Snowball

## S3 Transfer Acceleration
* S3 Transfer Acceleration uses CloudFront to accelerate uploads to S3
* You upload data directly to an Edge Location of the CloudFront CDN, which then transfer the file to S3
* Since buckets are created with respect to a region, users far from that region would otherwise have slow speeds uploading/downloading to the bucket

## S3 Final Overview & Summary
* S3 is object based storage, and allows storage of flat files, not installation of OS, database, application, etc.
* To do OS or database, you would need block based storage, which would normally be an EBS
* Files can be 0 Bytes to 5TB
* There is unlimited storage
* Files are stored in buckets
* S3 is a universal namespace, so names must be globally unique and must be all lowercase
* S3 bucket name format is `http[s]://region.amazonaws.com/bucketname`
* **Consistency Model**:
  * Read after Write immediate consistency for PUTS of new objects. When a new file is uploaded, it will immediately be readable
  * Eventual consistency for overwrite PUTS and DELETS of existing objects. Can take time to propogate changes. Should be ~15 mins for consistency
* **Tiers**:
  * **S3 Standard**:
    * 99.99% availability
    * 99.999999999% durability
    * Stored reduntantly across multiple devices in multiple data centers
    * Designed to sustain loss of 2 facilities concurrently
  * **S3 - IA**:
    * 99.99% Availability
    * Infrequently Accessed
    * For data that is accessed less frequently, but requried rapid access when needed
    * Lower storage fee, but charged for retirevals
  * **S3 One Zone - IA**:
    * An even lower cost verison of S3 - IA that is only stored in one data center
    * Replaces Reduced **Redundany Store (RRS)**
  * **Glacier**:
    * Intended for data archival
    * Split into three sub-tiers: **Expediated**,  **Standard**, and **Bulk**, which deliver retrieval rates
    * The slower the retrieval time, the cheaper the pricing
    * **Standard** retrieval time is 3-5 hours

## S3 Other
* Until 2018 there was a hard limit of 100 PUTS per second
* To achieve this limit, care needed to be taken with the object's Key
* In 2018, amazon raised the limit to 3500, which essentially eliminates the problem
* Amazon doesnt recomend needed action with Key naming for performance
* More:
  * https://aws.amazon.com/about-aws/whats-new/2018/07/amazon-s3-announces-increased-request-rate-performance/
  * https://docs.aws.amazon.com/AmazonS3/latest/dev/request-rate-perf-considerations.html
  * https://aws.amazon.com/s3/storage-classes/
 
# Elastic Cloud Compute (EC2)

## EC2 Overview

* Elastic Cloud Compute (EC2) is a web services that provides resizable compute capacity in the cloud
* Reduces time to boot a new server instance to minutes, allowing users to quickly scale up and dlown as needed
* Also mitigates huge capital investment of server racks for companies
* Pricing Models:
  * **On Demand**:
    * You pay a fixed rate by the hour (or second) with no commitments
    * Great for development and testing, where you can start and stop as needed
  * **Reserved**:
    * Provides you with a capacity reservation, and offers a significatn discout compared to hourly charge
    * Contract terms are 1 - 3 years
  * **Spot**:
    * Occurs when amazon has abundance of compute due to momentary dip in overall consumption
    * Amazon lowers prices to encourage people to buy the surplus
    * You bid at a price, by setting a price you're willing to pay for, and when the price drops that low, you get computer
    * When the price raises above your threshold, you lose compute again within minutes 
  * **Dedicated Hosts**:
    * Physical EC2 servers dedicated for your use
    * Allow to use your existing server-bound software licenses, such as Oralce products

## EC2: On Demand
* Users who want the lost cost and flexibility of EC2, without up front payments or long term comittments
* Useful for applications with short term or spiky, unpredictable workloads that cannot be interupted
* Useful for applications in development/testing, or applications being ported to AWS for the first time

## EC2: Reserved Pricing
* Applications with steady state, predictable usage
* Applications that have a required reserved capacity
* Users get lower cost per compute resource, but make upfront payment and have payment commitments
* Reserved pricing options:
  * **Standard Reserved Instanes**:
    * Offer up to 75% off on demand pricing options. 75% is the maximum discount, not base level
    * The more you pay up front, and the longer the contract, the larger discount you get
  * **Convertible Reserved Instanes**:
    * Offer up to 54% off on demand pricing options. 75% is the maximum discount, not base level\
    * EC2's are like virtual machines, and certain EC2 have different RAM and CPU specifications
    * Standard EC2 instances don't allow flexibile conversion of EC2 isntance types
    * With convertible you can, which is useful for meeting variable demands such as high memory spikes
  * **Scheduled Reserved Instances**:
    * These are instnaces which launch on a time schedule
    * This allows scaling up and scaling down based on a predictable time schedule

## EC2: Spot Pricing
* Useful for applications that have flexible start and end times
* Useful for applications that are only feasible at very cheap compute pricing
* Users with computing needs for large amounts amount of additional capacity

## EC2: Dedicated Hosts Pricing
* Useful for regulatory requirements that may not support multi-tennant virtualization
* Useful for licencsing that does not allow multi-tenant virtualization, or cloud deploymnents (such as Orcale's licenses)
* Can be purchased as either Reserved or On-Demand
* Similar to standard EC2, Reserved dedicated hosts are cheaper than On-Demand

## EC2 Instance Types:
| Family | Speciality | Use Cases |
| ------ | ---------- | --------- |
| F1 | Field Programmable Gate Array | Genomics research, financial anlytics, real-time video processing, big data |
| I3 | High Speed Storage | NoSQL DBs, Data Warehousing |
| G3 | Graphics Intensive | Video Encoding, 3D Application Streaming |
| H1 | High Disk Throughput | MapReduce workloads, distrubuted file systems, HDFS, MapR-FS |
| T3 | Loweest Cost, General Purpose | Web Servers, Small DBs |
| D2 | Dense Storage | File Servers, Data Warehousing, Hadoop |
| R5 | Memory Optimized | Memory Intensive Apps, DBs |
| M5 | General Purpose | Applicaiton Servers |
| C5 | Compute Optimized | CPU Intensive Apps, DBs |
| P3 | Graphics/General Purpose GPU  | Machine Learning, Bit Coin Mining |
| X1 | Memory Optimized | SAP HANA, Apache Spark |
| Z1D | High compute capactiy and high memory | Electronic Design Automation (EDA), certain RDBMS sysyems with high per-core licesnsing costs |
| A1 | Arm-based workloads | Scale-out workloads like web servers |
| U-6b1 | Bare Metal | Bare metal applications that eliminate virtualization overhead |

* Note that the numbers like `F1` can change, as they indicate generation
* Memorizing EC2 instnace type isnt neccessary for Solutions Architect Associate, but is for higher level course

## EC2 Overview Summary
* Amazon Elastic Cloud Compute (EC2) is a web service that provides resizable compute capacity in the cloud
* Allows you to provision server computing in minutes rather than weeks/months by buying/building your own racks
* Allows easy scaling up and scaling down
* Different price tiering: **On-Demand**, **Reserved**, **Spot**, **Dedicated Hosts**
* Different sub-tiers of Reserved EC2: **Standard**, **Convertible**, **Scheduled**

## EC2 Lab
* Availability zone names are different between accounts (this was uncklear)
* Adding an additional volume allows addition of more volume types
* Security Group is a virtual firewall
* Tags allow keeping track via labeling
* SSH goes across port 22
* HTTP goes accros port 80

## EC2 Lab 2
* Termination Protection blocks shutting down the EC2 so you dont accidently stop it. To actually shut down, you go back in and turn Termination Protection off then shut down the EC2
* Termination Protection is turned off by defualt and must be enabled
* On an EBS-backed instance, the default action is for the root EBS volume to be deleted when the instance is termianted
* The defualt EBS root device volumes of your defualt AMI's cannot be encrypted
* The root device volumes is essentially the volume where the OS is installed
* Additional volumes can be encrypted

## EC2 Lab 3
* Security Group edits on EC2 instnace take effect immediately
* Allowing a protocol to provide Inbound communication will automatically allow the same protocol Outbound
* Security Groups are stateful, whereas Network Access Control Lists are stateless
* Security Groups do not allow blocking specific IP addresses or ranges, and do not allow blocking specific ports. This can be done with a Network Access Control List
* All Inbound traffic is blocked by default, you will need to open ports 80 for HTTP, 22 for SSH, etc. if you want this
* All Outbound traffic is allowed
* Changes to security groups take effect immiediately
* You can add multiple EC2 instances into a secuirty group
* You can have multiple security groups attached to a single EC2 instance 
* Security groups are **stateful**
* If you create an inbound rule allowing traffic in, the corresponding outobund rule is automatically allowed
* You cannot block IP addressed using Security Groups, instead use NACLs
* You can set allow rules, but you cannot set deny rules. All non-allowed rules are denied

## Elastic Block Store (EBS)
* Essentially a virtual hard disk in the cloud
* Provides persistent block storage volumes for use within EC2 instances
* 5 different types:
  * **General Purpose (SSD)**
  * **Provisioned IOPS**
  * **Throughput Optimised Hard Disk Drive**
  * **Cold Hard Disk Drive**
  * **Magnetic**

## EBS Types
| EBS Volume Type | SSD/HDD | Description | Use Cases | API Name | Volume Size | Max IOPS/Volume |
| -------- | ------- | ----------- | ----------- | --------- | -------- | ----------- | --------------- |
<!--| **General Purpose SSD** | General purpose SSD volume that balances price and performance for a wide variety of workloads | Highest performance SSD volumes designed for mission-critical applications | Low cost HDD volume designed for frequently accessed, throughput-intensive workloads | Lower cost HDD volumes designed for less frequently accessed workloads | Previous generation HDD |  |  |-->
| **General Purpose SSD** | SSD | Most workloads; general use |  |  |  |  |  |
| **Provisioned IOPS SSD** | SSD | Highest performance SSD; mission-critical applications |  |  |  |  |
| **Throughput Optimized HDD** | HDD | Low cost HDD; frequently-accessed, high throughput workloads  |  |  |  |  |
| **Cold HDD** | HDD | Lowest cost HDD; less frequently accessed, lower throughout workloads |  |  |  |  |
| **EBS Magnetic** | HDD | Previous generation HDD |  |  |  |  |


# Glossary
| Term | Definition |
| ---- | ---------- |
| Availability Zone | |
| Region | |
| S3 | |
| Glacier | |
| Infrequent Access (IA) | |
| Identity Access Managenet (IAM) | |
| Content Delivery Network (CDN) | |
| KMS | |
| End Use | |
| Edge Location | |
| Route 53 | |
| Elastic Cloud Compute (EC2) | |
| Elastic Load Balancer (ELB) ||
| Time to Live (TTL) | |
| Invalidation  |   | 
| Storage Gateway |  | 
| SSE-SSE  |  | 
| SSE-KMS  |  | 
| SSE-C  |  | 
| Elastic Block Store (EBS) |  | 
| Redundany Store (RRS) |  |
| Network Access Control List (NACL) |  |
| Security Group (SG) |  |

<!--
|  |  | 
-->
