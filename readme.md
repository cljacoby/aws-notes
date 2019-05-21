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

<!-- ==================================================================================================== -->

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

### CloudFront CDN Examp Tips
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

<!-- ==================================================================================================== -->
 
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
| -------- | ------- | ----------- | ----------- | --------- | -------- | ----------- |
| **General Purpose SSD** | SSD | Medium balance of performance of cost, good for Most workloads | General use | gp2 | 1 GiB - 16 TiB | 16,000 |
| **Provisioned IOPS SSD** | SSD | Highest performance SSD; mission-critical applications | Databases | io1 | 4 GiB - 16 TiB | 64,000 |
| **Throughput Optimized HDD** | HDD | Low cost HDD; frequently-accessed, high throughput workloads  | Big data and data warehouses | st1 | 500 GiB - 16 TiB | 500 |
| **Cold HDD** | HDD | Lowest cost HDD; less frequently accessed, lower throughout workloads | File servers | sc1 | 500 GiB - 16 TIB | 250 |
| **EBS Magnetic** | HDD | Previous generation HDD | Workloads where data is infrequentyl accessed, possibly data archiving | Standard | 1 GIB - TIB  | 40-200 |

* IOPS = Input Output Opeartion per Secon
* Need to know the EBS Types for the Solutions Architect Associate exam
* Know the associated API types, as they are frequent questions

## EBS Lab
* A volume will always be in the same availability zone as the EC2 it is mounted to
* This is done to mitigate lag between EC2 compute actions and getting data from the volume
* Terminating an EC2 will also automatically termiante the root EBS volume
* You can encrypt additional volumes, but not the root volume
* You can tell the root volume by the snapshot column being filled with the EC2 AMI identification string
* Volumes can be modified, such as from gp2 to io1 or whatever, on the fly under `Actions -> Modify Volume` on the fly and don't need to shutdown isntane
* On an EBS volume you can use `Actions -> Create Snapshot` to create a snapshot
* With an EBS Snapshot, you can create an Image, which allows re-launching a new EC2 instance from the snapshotted EBS volume
* This allows launching a new EC2 from a snaphot-to-image in a new availability zone
* Using an Image from an EBS snapshot only allows launching under some EC2 instance types, not all
* When you terminate an EC2, by default the root volume will also be termianted; however, additional attached volumes will persist

## EBS Summary and Exam Tips
* Volumes exist on EBS, and EBS can be thought of as a virtual hard drive
* Snapshots exist on S3
* Think of snapshots as a photograph of the disk
* Snapshots are point-in-time copies of the Volume state
* Snapshots are incremental, meaning only blocks that have been changed from last snapshot will be stored in S3 (only the delta is stored)
* Creating the first snapshot will take longer, as effect of the incremental nature and having no previoous state to build off
* When creating a snapshot, it is best practice to stop the isntance before taking the snapshot, especially for productoin workloads, although you can take a snapshot of a running instance
* You can create AMIs from both Volumes and Snapshots
* You can change EBS volume suze and storage type on the fly
* Volumes will **Always** be in the same availability zone as the EC2 instance
* To migrate an EC2 volume from one AZ to another, take a snapshot of the root volume, create an AMI from the snapshot, and then use the AMI to launch the EC2 in another AZ
* To move an EC2 from on region to another, snapshot the root volume, create an AMI from the snapshot, then copy the AMI from one region to another, then use the copied AMI to launch an EC2 in another region

## AMI Types: EBS vs Instance Store
* You can select your AMI based on:
  * Region
  * Architecture (32-bit or 64-bit architecture)
  * Launch Permissions
  * Storage for the Root Device (a.k.a. Root Device Volume):
    * Instance Store (**Ephemeral Storage**)
    * EBS Backed Volumes
* All AMIs are categorized as either backed by EBS or backed by instance store
* **For EBS Volumes**:  The root device for an instance launched from the AMI is Amazon EBS volumes created from an  EBS snapshot 
* **For Instane Store Volumes**: The root devive for an instance launched from the AMI is an isntance store volumes created from a template stored in S3
* For Instane Store Volumes, all volumes must be added to an EC2 at launch time, and they cannot be added on later. For EBS volumes this is not the case, and these can be added at launch or later on
* Should there be issues with the hyper-visor, an Instance store volume cannot be recovered and is ephermeral

## AMI Types: EBS vs Instance Store Volumes Review and Exam Tips
* Instance Store Volumes are **Ephemeral** storage
* Instance Store Voluems cannot be stopped
* If the underlying host fails for Instance Store Volumes, you lose all your data
* With EBS backed instances can be stopped, and you will not lose your data if the instance is stopped
* You can reboot both, and will not lose your data by doing so
* By default, both Root volumes will be deleted when the EC2 is terminated; however, with EBS volumes, you can tell AWS to keep the root device volume

## Encryption with EBS and Root Volume Encryption
* To encrypt the root volumes:
  * Launch an EC2 instance with a normal, unencrypted root volume
  * Create a snapshot of the EC2 isntance's root volume
  * Copy the EBS snapshot, and select the encrypt option during the copy
  * Create an AMI Image from the encrypted root volume copy
  * Launch an EC2 instance from the encrypted root volume AMI
* Once an EBS root volumes is encrypted during a copy, it cannot be unencypted 
* Launching an EC2 from an AMI built from an encrypted root volume snapshot will limit the types of EC2s you can launch as

## Encryption with EBS and Root Volumes Encrpytion Summary and Exam tips
* Snapshots of encrpyted volumes are encrypted automatically, and cannot be unencrypted
* Volumes restored from encrypted snapshots are encrpyted automatically
* You can share snapshots, but only as unencrypted
* These snapshots can be shared with other AWS accounts or made public on AWS community
* Summary of steps to create encrypted root volume:
  * Create a snapshot of the unencrypted root device volume
  * Create a copy of the snapshot and select the encrypt option
  * Create an AMI from the encrypted snapshot
  * Use than AMI to launch the new encrypted instacne

## CloudWatch
* CLoudWatch is essentially a performance monitoring tool for all other AWS services
* CloudWatch is capable of monitoring:
  * **Compute**:
    * EC2 instances
    * Autoscaling groups
    * Elastic Load Balancer
    * Route53 health checks
  * **Storage and Content Delivery**:
    * EBS Volumes
    * Storage Gateways
    * CloudFront CDN

### Host Level Metrics
* CPU
* Netowrk
* Disk
* Status Check:
  * Underlying hyper-visor
  * Underlying EC2 instance

### CloudWatch vs CloudTrail
* AWS CloudTrail increases visiblity into your user and resource activity by recording AWS Console actions and API calls.
* CloudTrail enables you to identify:
  * Which users and accounts called AWS
  * The source IP address from which calls were made
  * When the calls/actions occured
* Essentially CloudTrail is an audit log whereas CloudWatch is a operational performance monitor

### CloudWatch Summary and Exam Tips
* CloudWatch is used for performance monitoring
* CloudWatch can monitor most of the AWS services, and the applications these services support
* CloudWatch with EC2 will monitor events every 5 minutes by default
* You can have 1 minute intervals by turning on detialed monitoring
* You can create CloudWatch alarms that trigger notifications
* **CloudWatch is all about performance. CloudTrail is all about auditing**

## CloudWatch Lab
* Enabling CloudWatch detailed monitoring gives 1 minute monitoring interval, but is not eligible for free tier EC2
* You can use CloudWatch create dashboards for custom monitoring setups  
* You can create regional or global monitoring dashboards
* You can use CloudWatch to create logs

## CloudWatch Lab Summary and Exam Tips
* Standard Monitoring is 5 miunute interval, detailed monitoring is 1 minute interval
* CloudWatch enables creating dashboards to visualize system performance metrics
* CloudWatch enables creating alarms that notify you when certain thresholds are reached (email)
* CloudWatch enables you to create Events, which allow you to respond to state changes in AWS resources
* CloudWatch enables you to setup and maintain logs
* CloudWatch monitors performance, versus CloudTrail monitors API calls

## AWS Command Line Tool 
* Security Groups are region specific (I think)
* You can use the AWS CLI to interact with AWS from anywhere in the world
* You will need to set up access via IAM
* Commands themselves are not in the exam, but some basic commands will be useful to know
* You will need to execute `chmod 400 myKey.pem` on a new private key file when SSHing to the EC2 for the first time

## Using IAM Roles with EC2
* Roles are more secure than storing access key and secret access key credentials in an EC2 instance
* Roles are also easier to manage
* Roles can be assigned to any EC2 instance after it is created using either the console or the CLI
* Roles are universal; you can use them from every region 

## Bootstrap Scripts
* Bootstrap scripts are a way to automate EC2 deployment
* A boostrap script is a script that runs when an EC2 is first deployed
* Comman actions:
  * Run updates
  * Install dependencies
  * Initialize logging info
* To add a bootstrap script, use  `Advanced Data -> User Data -> As Text`
* Begin a bootstrap script with a shebang line, normally `#!/bin/bash`
* Honestly this is a really ugly way to add a bash startup script


## EC2 Instance Metadata
* Meta-data for an instane can be accessed via `curl http://169.254.169.254/meta-data/`
* The bootstrap script passed at launch time can be accessed via `curl http://169.254.169.254/user-data/`

## Elastic File System (EFS)
* Elastic File System (EFS) is the file storage system for EC2 instances
* You cannot mount two EC2 instance two one EBS volume; however, you can have two EC2 instances sharing an EFS volume
* Storage is elastic, and grows and shrinks as needed similair to compute power with EC2
* You do not need to pre-provision storage maximum limit the way you do with EBS
* A great method to share files between EC2 isntances

## EFS Exam Tips
* Supports the Netowrk File System version 4 (NFSv4) protocol
* You only pay for the storage you use (no pre-provisioning required)
* Can scale up to petabytes
* Can support thousands of concurrent NFS connections
* Data is stored across multiple AS's within a region
* Read after write consistency

## EC2 Placement Groups
* Two Types:
  * **Clustered Placement Groups**
  * **Spread Placement Groups**
* The two types are complete opposites
* The name of a placement group must be unique withibn your AWS account
* Only certain types of EC2 isntanes can be launched in a placement group, such as:
  * Compute Optimized
  * GPU
  * Memory Optimized
  * Storage Optimized

### Clustered Placement Group
* A **Clustered Placement Group** is a grouping of instances within a single AZ
* Clustered placement groups are recommended for applications with low network latency, or high network throughput, or both
* Basically the idea of having the phyiscal machines running the EC2s to be as close together as possible
* Only certain instances can be launched in a Clustered Placement Group 
* Clustered groups cannot span multiple AZs, as thats kind of exactly the opposite of their point

### Spread Placement Group
* A **Spread Placement Group** is a group of EC2 instanes placed on distinct underlyging hardware
* Basically, the intentionally run on different machines
* Spread Placement Groups are for appliations that have a small number of critical instances that should be kept seperate from each other
* Maybe to facilitate a business risk consideration/mitigation in relation to failing machines
* Spread placement groups can span mulitple AZs

### EC2 Placement Groups Summary and Exam Tips
* The name of a placement group must be unique withibn your AWS account
* Only certain types of EC2 isntanes can be launched in a placement group, such as:
  * Compute Optimized
  * GPU
  * Memory Optimized
  * Storage Optimized
* AWS recommends homogenous EC2 instance types within a placement group (doesnt elaborate why)
* Clustered Placement Group can't span multiple AZs, while Spread Placement Group can
* You can't merge placement groups
* You can't move a running EC2 instance into a placement group; hwoever, you can generate an AMI from an isntance an launch that in a placement group

## EC2 Summary and Exam Tips

### EC2 Overview
* Elastic Cloud Compute (EC2) is a web service that provides resizable compute capaity in the cloud
* EC2 reduces the time to obtain and boot a server instance, allowing you to have a host in miniutes 
* Allows you to easily scale up and scale down your compute power as your requirements change
* The four types of EC2 pricing:
  * **On Demand**: Allows you to pay a fixed rate by the hour (or by second) with no commitment 
  * **Reserved**: Provides you with a capacity reservastion (either 1 or 3 years) and offers a significant discount in hourly rate compared to On-Demand
  * **Spot**: Enables you to set a bid price on compute power which is supplied when a surplus in compute resources causes the spot price to dip. You get and relinquish compute power as the priced dips below your threshold.
  * **Dedicated Hosts**: Physical EC2 servers dedicated for your use, normally to facilitate license-bound software agreements or cannot use multi-tennant virtualization
* If a Spot instance is terminated by AWS you will not be charged for the partial hour of use; however, if you termiante the Spot instance, you will be charged for the partial hour of use 
* **TODO:** Write down the EC2 types pneomonic
* Says that you do not need to memorize EC2 instance types for Assocaite level Solutions Architect (but will for professional)
* Termination protection is turned **off** by default, and must be turned on to use

### EC2 Storage: EBS Volumes
* On an EBS-backed instance, the default action for the root EBS volumes is to be deleted when the instance is terminated
* Any additional EBS volumes mounted to an EC2 will persist after termination of the EC2
* EBS root volumes of your **DEFAULLT AMI**s cannot be encrypted.
* To encrypt the root volume, You can use a third party tool like bitlocker, or you can create an AMI with an encrypted root volume
* Additional EBS volumes can be encrypted from start (don't need to create an AMI)

### EC2 Security
* All Inbound traffic is blocked by default
* All Outbound traffic is allowed by default
* Changes to Security Groups take effect immediately
* You can have any number of EC2 isntances assinged to a Security Group
* You can assign any number of Security Groups to an EC2
* Security groups are **STATEFUL**, meaning when you open up a port, it will be opened for inbound and outbound traffic
* **NACL**s are **STATELESS** and you must manually specifiy a port is open for inbound and outbound traffic
* If you create an inbound traffic rule allowing inbound traffic, the corresponding outbound traffic is automatically allowed back out
* You cannot block certain IP Addresses with a Security Group, isntead you would use a Network Access Control List
* You can specify allow rules with Security Groups, but not deny rules
* Know the types of EBS volumes, described in the table in the main EBS section

### EC2 Snapshots and AMIs
* Voluems exist on EBS, and EBS can be thought of as a virtual hard disk drive in the cloud
* Snapshots exist on S3, and snapshots can be thought of as an image of a hard disk drive at a state in time
* Sanpshots are point in time copies of a volume
* Snapshots are incremental, and only store changes since the last snapshot
* The first snapshot can take longer to generate as it has not previous state to build incremental changes off
* To create a snapshot of a root EBS volumes, it is recommended to stop the EC2 instance before taking the snapshot (but you can do on running)
* You can create AMIs from both volumes and snapshots
* You can change EBS volume sizes on the fly, including changing the storage size and storage type
* Volumes will **always** be in the same availability zone as the EC2 instance
* A.k.a. you cannot have an EC2 instance and an EBS volume in different AZs
* To move an EC2 volumes from one **AZ** to another:
  * Take a snapshot of it
  * Create an AMI from the snapshot
  * Use the AMI to launch the EC2 instance in a new AZ
* To move an EC2 from one **region** to another:
  * Take a snapshot ofit
  * Create an AMI from the snapshot
  * Copy the AMI from region to another
  * Laucnh an EC2 from the copied AMI

### EBS vs Instance Store
* Instance store volumes are sometimes called **Ephemeral** storage
* Instance store volumes cannot be stopped, and if the underlying instance or hypervisor fails you will lose your data
* EBS backed instances can be stopped, and you will not lose data if the isntance is stopped
* You can reboot either the EBS isntane or EC2 isntnace and not lose your data
* By defualt, both an Instance Store and EBS root volumes will be deleted upon EC2 termination; however, with EBS you can tell AWS to keep the root volume

### EBS Encryption
* Snapshots of encrypted volumes are encrypted automatically
* Snapshots of encrypted volumes cannot be unencrypted, and will always stay encrypted
* Volumes restored from encrypted snapshots are encrypted automatically
* You can share snapshots with other accounts or make them public, but only if they are unecrypted
* The root volume cannot be launched as encrypted the way additional valumes can
* However, an EC2 with an encrypyted root volume can be achieved by:
  * Launch an EC2 with an unencrypted root volume (just a normal EC2)
  * Create a snapthos of the unencrypted root volume
  * Create a copy of the snapshot and select encryption option during copy
  * Create an AMI from the snapshot
  * Launch the AMI with the encrypted root volumes
* Alternatively you can use a third party tool like bitlocker to en encrypt the root volume

### CloudWatch
* CloudWatch is used to monitor performance
* Can monitor performance of EC2, but also performance of most AWS services
* CloudWatch will monitor EC2 events every 5 minutes by default
* Can turn on detailed monitoring to get 1 minute interval monitoring (but this isnt free)
* You can create CloudWatch Alarms which trigger notifications
* **CloudWatch** -> **Performance**; **CloudTrail** -> **Auditing**
* **CloudWatch Dashboard**: Customize your view of  performance metrics
* **CloudWatch Alarms**: Allows you to set Alarms that notify you when a threshold is reached
* **CloudWatch Events**: Help you respond to state changes on your AWS resources
* **CloudWatch Logs**: Create logs of your running instances to review/debug

### AWS CLI
* You can interact with AWS from anywhere in the world with the CLI
* You will need to set up access in IAM for the CLI

### EC2 Roles
* Key infromation can be stored in the `~/.aws` directory; however, this is a bad way to do identity authentication
* Instead create a role
* Roles are easier to manage
* Roles can be assigned to an EC2 after launch
* Roles are universal, and can be used in any region in the world
* Roles can be applies using either the console or the CLI

### Bootstrap Scripts and Instace User and Meta Data
* Bootstrap scripts run when an EC2 first boots (a.k.a. launch)
* Normally used to automate updating and installing software
* Meta-data provides information about an EC2 isntance such as the public IP
* Meta-data can be accessed using this curl command in any EC2 instance:
  * `curl http://169.254.269.254/lastest/meta-data/`
* User data is literally the bootstrap script
* User data can be accessed via the following curl command in any EC2 isntance:
  * `curl http://169.254.269.254/lastest/user-data/`

### EFS
* Supports Netowrk File System version 4 (NFSv4) protocol
* You only pay for the storage you use; no pre-provisioning required
* Can scale up to petabytes
* Can support thousand of concurrent NFS connections
* Data is stored across multiple AZ's within a region
* Read after write consistency
* You cannot share EBS with multiple instances, but you can create an EFS mount which multiple EC2 can connect to

### EC2 Placement Groups
* Two types:
  * **Clustered Placement Groups**: Used for very high network throughput, low latency, or both. EC2's are ran on machines physically located very close (or the same machine altogether)
  * **Spread Placement Group**: Used for critical EC2 instances that need to be on seperate machines for risk mitigation
* Clustered placement groups cannot span multiple AZs, whereas spread placement groups can
* The name you specify for a placement group must be unique in your AWS account
* Only certain types of EC2 instances can be launched in a placmeent group:
  * Compute Optimized
  * GPU
  * Memory Optimized
  * Storage Optimized
* AWS highly recommends using homogengous instance types within a placement group, although you can not if you want
* You cannot merge placement groups
* You cannot move an exisitng EC2 instance into a placement group; however, you can create an AMI and launch a new instance from the AMI in the placement group

<!-- ==================================================================================================== -->

# Databases on AWS

## Relational Databases
* Relational Database Service (RDS) is the Relational Database service on AWS
* 6 Database flavors on of RDS:
  * **Microsoft SQL Server**
  * **Oracle**
  * **MySQL**
  * **PostgeSQL**
  * **Amazon Aurora**
  * **MariaDB**
* RDS has two key features:
  * **Multi-AZ** - For disaster Recovery
  * **Read Replicas** - For performance
* MySQL installations default to using port 3306

### Multi-AZ Overview
* With Multi-AZ, there are multiple stored copies of the database on AWS
* There is a single public URL for an EC2 that is pointed to the primary database instance
* If the primary database goes down, the public EC2 is automatically switched over to the secodary database instance
* The change is orchestrated by AWS, with no user interaction
* Useful if you have a critical database that you want fail over prevention for

### Read Replicas Overview
* There is a database instance, with a public EC2 URL that directs to the database instance
* When writes are made to the database, the writes are made to the primary database isntance, and also propogated to a seconrary database instance
* The secondary database instance is always a perfect replica of the primary database
* The read replica solution is useful when you have a large request volume increase, and you need to scale up performance:
* For read opearations, users can be split to read between different read replices of the primary database instance, therefore splitting the overall load
* Can have up to **five** copies for read replices

## Non-Relational Databases
* Consist of Collections, Documents, Key-Value Pairs which can be construed as analogs to Tables, Rows, and Fields in an RDB
* Very similar to JSON structure organization
* Non-Relational databases do not need a rigid schema the way RDBs do
* Amazon's solution for NoSQL databases is **DynamoDB**

### Case Analysis: OTLP vs OLAP
* **OTLP**: Online Transaction Processing
* **OLAP**: Online Analytics Processing
* OTLP Example:
  * Query on online transaction
  * Order Number: 2120121
  * Pulls up a row of data such as Name, Date, Deliery Address, and Delivery Status
* OLAP Example:
  * Net profit for EMEA and Pacific for the Digital Radio Product
  * Pulls in a large number of recrods
  * Sum all radios sold in EMEA, sum all radios sold in pacific, calculate unit cost ratio of each region, calculate net profit
* Data Warehousing databases use different type of architecture both from a database perspective and an infrastructural perspective
* Amazon's solution to data warehousing is called **Redshift**

## RDS Backups
* Two Types:
  * **Automated Backups**
  * **Database Snapshots**
* When you restore an RDS from a backup (either type), the restored version will be a new RDS instance with a new DNS endpoint

### Automated Backups
* Automated backups allow you to recover your database to any point in time within a **retention period**
* Retention period can be between 1 - 35 days
* Automated backups take a full daily snapshot and also store transaction logs throughout the day
* WHen you do a recovery, AWS starts with the most recent daily backup, and applies transactions from the log up until the relevant time
* This allows recovery down to a second-in-time accuracy
* Enabled by defualt
* Backup data stored in S3
* Your amount of free storage is equal to the size of your database
* Backups are taken within a refined window, during which I/0 may be suspended while data is being backed up. This can induce latency
* If RDS database instance is deleted, the automated backup data is also deleted

### Database Snapshots
* Snapshots are taken manually; user initiated
* The snapshot is retained even after the original RDS is deleted

### Encryption at Rest
* Encryption supported for:
  * PostgreSQL
  * MariaDB
  * Aurora
  * Oracle
  * SQL Server
  * MySQL
* Encryption is done via Amazon KMS
* Once encryption is on, all automated backups, read replicas, and snapshots are also encrypted

### Multi-AZ Database
* Allows you to have another copy of your production DB in another AZ in case of failure of an AZ
* AWS handles the replication for you, and all write will automatically be synchronized to the backup
* In the event of planned maitenance, DB instance failure, or AZ failure, Amazon RDS will automatically fail over to the standby copy so that DB operations can resume as normal
* Multi-AZ is designed for fail over prevention, not for performance optimization, which would use read replicas instead
* Multi-AZ databases are available for:
  * SQL Server
  * Oracel
  * MySQL Server
  * PostgreSQL
  * MariaDB

### RDS Backups, Multi-AZ, and Read Replicas Lab
* Can migrate MySQL database to Aurora by
  * Creatng an Aurora read replica from MySQL DB
  * Promoting to primary database
* When adding Multi-AZ configuration to a previously single AZ DB, it can significantly decrease database performance, especially for write intensive workloads
* You can add Multi-AZ to a previously single AZ DB during a schedule maitenance window
* The status when Multi-AZ is applied will change from `Available` to `Modifying`
* You can force an AZ change by rebooting DB instance with failover option selected
* Backups need to be turned on in order to enable read replicas
* Maximum retention period for backups is 35 days
* Turning backups on when they were off can cause downtime and slow performance. Status will change to `Modifying`
* Read replicas can be in a different region than primary instance
* Read replicas can be set to publicly accessible
* Read replicas can be set to encrypted
* Read replicas can be set to Multi-AZ deployment
* Read replicas require a DB instane identifier, which is basically just a name

### Read Replicas
* All EC2s write to a single primary RDS databse, and the writes are syncornized to replica databases
* The EC2s then read from multiple database copy to distribute the worload out and improve performance
* Read replicas will boost performance with read heavy workloads
* Propogation of the primary RDS write to the read replica instance is Asnychronous
* In general the two ways to improve DB performance are:
  * **Read Replices**
  * **ElastiCache**
* Read replicas are available for the following databases:
  * MySQL Server
  * PostgreSQL
  * MariaDB
  * Aurora
* Read replicas are used for scaling performance, not for disaster recovery
* Must have automatic backups turned on in order to deploy read replicas
* You can have 5 read replicas of any database
* You can have read replias of read replicas, but increased chaining can induce latency
* Each read replica will have its own DNS endpoint
* You can have read replicas that have Multi-AZ
* You can create read replicas of Multi-AZ source databases
* Read replicas can be promoted to their own databases. This breaks the replication
* You can have a read replica in a secon region

## DynamoDB
* Amazon's NoSQL database solution
* Fast/performant, and offsers single-digit millisecond latency at any scale
* Supports document and key-value data models
* Performance makes it suiable for:
  * Mobile
  * Web
  * Gaming
  * Ad-tech
  * IoT
  * More
* Many mobile developers use DyanomoDB
* Basics of DyanamoDB are:
  * Stored on SSD storage (part of the performance is this)
  * SPread across 3 geographically distinct data centers
  * Two types of read models:
    * **Eventual Consistency Reads (Default)** 
    * **Strongly consistent Reads**
  * Choosing between read models is done with the rule of thumb **1 Second Rule**
  * **1 Second Rule**: If your application needs to write, and read the updates within 1 second or less, you will need Strongly Consistent Reads. Otherwise Eventual Consistency Reads will suffice. 

### Eventual Consistency Reads
* Consitency of writesacross all copies of data is usually reached within a second
* Repeating a read after a short time should return the updated data
* This model offers the best read perfomrance
* Default behaviour

### Strongly Consistent Reads
* IF you're application needs to write data, and read with the gaurentee of the update being reflected, you should use Strongly Consistent Reads
* Strongly Consistent Reads will return all updates for reads for writes that have returned a succesful response

### DyanoDB Summary and Exam Tips
* DynamoDB is stored on SSD
* Spread across 3 geographically distinct data centers
* Most applications can use the Eventual Consisteny Reads, which is the default read model
* If reads need to be accurate to the most recent writes within 1 second or less, you will need the Strongly Consistent Reads read model


## Redshift
* Redshift is a way of doing business intelligence or data warehousing in the cloud
* Petabyte-scale capacity
* Can start small at $0.25/hour with no commitments or uprfront costs
* Can scale up to petabytes at a cost of $1000/year/terabyte
* Datawarehousing use different architecure compared to database or infrastructure layer

## Redshift Configurationl
* You can have a single node or a multi-node
* A single node is 160GB in size
* A multi-node has one leader node, which manages client connections and recieves queries
* A multi-node then has many compute nodes, which store data and perform queries
* Can have up to 128 compute nodes behind a leader node
* Redshift uses **Advanced Compression**

### Redshift Advanced Compression
* Columnar data can be compressed much more than row-based data
* Because columns are consistent in their types, data is easier to compress because all data is the same
* Compression is better compared to normal RDS
* Redshift will use less space on disk compared to an RDS

### Redshift Massively Parellel Processing (MPP):
* Redshift automatically distriburtes data and query load across all nodes
* Redshift makes it easy to add additional nodes to your data warehous
* Enables easy scaling yo growth, as simply adding more nodes is a viable scaling technique

### Redshift Backups
* Enabled by default with a 1 day retention
* Maximum retention period of 35 days
* Redshift always attempts to maintain at leasy 3 copies of your data:
  * The original
  * The replica on the compute nodes
  * A backup on S3
* Redshift can asynchronsouly replicate your snapshots to S3 in another region for disaster recovery
  
### Redshift Pricing
* Priced by **Compute Node Hours**, which is the total number of hours of process timing across all your compute nodes during a billing period
* You are billed for 1 unit per node per hour
* A 3-node data warehouse cluster running persisently for a month would incur **2160** hours, which is 24hrs/day * 30 days/month * 3 nodes
* You are not charged for leader node hours, only compute node hours

### Redshift Security
* Encrypted in transit using SSL
* Encrypted at rest using AES-256 encryption
* By default, Redshift manages the keys internally
* You can manage your own keys via:
  * HSM (Hardware Service Manager)
  * KSM (Key Management Service)

### Redshift Availability
* Currently only available in 1 As; no multi-AZ option
* Can restore snapshots to another AZ in the event of an outage


### Redshift Summary and Exam Tips
* Redshift is used for business intelligence
* Availability is only 1 AZ
* Backups enabled by default for 1 day retention period
* Maximum retention period of 35 days
* Redshift will always attempt to maintain at least 3 copies of your data:
  * The original
  * The replica on the compute node
  * A backup in S3
* Redshift can asynchounously replicated your snapshots in S3 to another region for disaster recovery

## Aurora
* Aurora is a MySQL/PostgreSQL compatible database engine on the AWS cloud
* Combines speed/performance of commercial database engines with cheapness of open-source databases
* 5x better performance compared to MySQL and 10% the cost of a commercial database
* Propietary Amazon DB engine
* You start with a 10GB database, and can scale incrementally 10GB at a time up to maximum 64TB
* Storage autoscales
* Compute resources can scale up to 32vCPUs and 244GB of memory
* 2 copies of your data is contained in each Availability Zone, with minimum of 3 availability zone
* This creates 6 total copies of your data of 3 AZs
* Designed to handle loss of up to two copies of your data without affecting DB write availability, and up to 3 opies withou affecting read availiablity
* The handling is automatic on AWS, and will be transparent to users and developers
* Aurora storage is self-healing and data blocks and disks are routinely scanned for errors and repaired automatically

### Aurora Read Replices
* Aurora Read Replices (15 available)
* Also can have MySQL read replicas (5 available)
* You can have AWS automatically fail over from one Aurora DB to another, but cannot automatically fail over to a MySQL relica
* Failing over to a MySQL DB will be manual and handled by the developers
* Automated backups are always enables on Aurora DB isntances
* Backups do not inhibit performance
* You can also take snapshots of Aurora DBs, which also does not inhibit performance
* You can share Aurora DB snapshots with other AWS accounts
* Promoting a read replica of a MySQL backup of an Aurora database creates a new Aurora database that is primary, no longer a read replica

### Aurora Summary and Exam Tips
* Aurora is a MySQL/PostgreSQL compatible RDS database engine on the AWS cloud
* Aurora is a propietary technology created by amazon
* 2 copies of your data is contained in each AZ, with minimum of 3 AZs, to create 6 total copies
* 2 types of replicas:
  * Aurora replicas
  * MySQL replices
* Automated fail over is only available with Aurora replicas, manual fail over can be used with MySQL replicas
* You can migrate MySQL replicas to Aurora DB by promoting the replica, or by creating a snapshot and launching an Aurora DB from the snapshot
* Aurora has automated backups turned on by default, with default 1 day retention period
* You can share Aurora snapshots with other AWS accounts


## ElastiCache
* ElastiCache is a web service that makes it easy to deploy, operate, and scale in-memory caching in the cloud
* ElastiCache improves the performance of web applications by retrieving resources from in memory caches rather than slower disk-based reads
* Can also reduce loads on over loaded DBs (somewhat synonymous with performance improvment)
* Two types of caching systems:
  * **Memcached**
  * **Redis**

### Comparison of ElastiCache Models: Memcached and Redis

| Requirement | Memcached | Redis |
| ----------- | --------- | ----- |
| Simple Cache to offload DB | Yes | Yes |
| Ability to scale horiztonally  | Yes | No |
| Multi-Threaded performance | Yes | No |
| Advanced data types | No | Yes |
| Ranking/Sorting data sets | No | Yes |
| Pub/Sub capabilities | No | Yes |
| Persistance | No | Yes |
| Multi-AZ | No | Yes |
| Backup and Restore capabilities | No | Yes |

* Memcached is in general a simple memory cache to setup and get basic features easy
* Redis should be used when your use case demands more complex features like complex data types, backups and restores, etc.

### ElastiCache
* Use ElastiCache to increase database and web appliation performance
* Use ElastiCache to decrease load on overloaded DBs
* The two steps to ease load on overloaded DBs are:
  * Add read replicas
  * Add ElastiCache
* Reddis is Multi-AZ; memcached is not
* Can do backups and restores with Reddis; memcached can not

## Databases Summary and Exam Tips
* RDS is the relational database service on AWS
* RDS associated with Online Transaction Processing (OLTP)
* RDS (OLTP) types:
  * SQL
  * MySQL
  * PostgreSQL
  * Oracle
  * Aurora
  * MariaDB
* DyanmoDB is Amazon's NoSQL database
* RedShift is Amazon's Online Analytics Processing (OLAP), Online Business Intelligence, and data warehousing
* ElastiCache is Amazon's memory caching service, with two types: Memcached and Redis
* Memcached is easier to setup and will give memory caching, but Redis will provide advanced features like backups/restores, complex data types, and Multi-AZ
* RDS runs on virtual machines, and you **cannot** SSH into these operating system
* Patching of the RDS operating system and DB is Amazon's resposibility
* RDS is not serverless, with exception begin Aurora Serverless
* DynamoDB is serverless
* RDS has two types of backups:
  * Automated backups
  * Database snapshots
* **Read Replicas**:
  * Used to increase performance and deload overloaded DBs (along with ElastiCache)
  * Not used for disaster recovery
  * Can be Multi-AZ
  * Must have backups turned on
  * Can be in different regions
  * Can be in Aurora or MySQL
  * Can be promoted to a master DB instance, but this breaks replication from the original master DB instacne
* **Multi-AZ**:
  * Used for disaster recovery
  * **Not** used for performance increases
  * You can force a failover from one RDS instance to another by rebooting the instance
* Encryption at rest is supported for:
  * **MySQL**
  * **Oracle**
  * **SQL Server**
  * **PostgreSQL**
  * **MariaDB**
  * **Aurora**
* Encryption is done using the AWS KMS service
* Once your date is encrypted, the data stored at rest in the underlying storage is encrypted, and all automated backups, read replicas, and snapshots will also be encrypted
* **DynamoDB**:
  * Stored on SSD storage
  * Spread across 3 geographicall distinct data centers
  * Two consistency models:
    * Eventual Consistent Reads (Default)
    * Strongly Consistent Reads
  * Use Eventual Consistent Reads for all use cases that dont need writes reflected in less than 1 second
* **Redshift**:
  * Redshift is used for business intelligence
  * Currently limited to 1 AZ only
  * Automated backups are endabled by default and have 1 day retention period
  * Maximum retention period of 35 days
  * Redshift will always attempt to maintain 3 copies of your data:
  * The original one on the compute node
  * The replica one on the compute node
  * A backup in Amazon S3
  * Redshift can asyncrhonosuly replicate your snapshots to S3 in another region
* **Aurora**:
  * Alwqays have 2 copies of your data in each AZ, with minimum of 3 AZs
  * Minimum of 6 copies of your data
  * You can share your Aurora DB with other AWS accounts as a snapshot
  * 2 types of replicas:
    * Aurora replica
    * MySQL replica
  * Can only do automated fail over with Aurora replicas, and manual failover with MySQL replic
  * Aurora has automated backups turned on by default
  * You can also take snapshots with Aurora, and share these snapshots
* **ElastiCache**:
  * Along with read replica, ElastiCache is used to increase web application performance by caching
  * If you need Multi-AZ, you need to use Redis
  * If you need backups and restores, you need to use Redis
  * If you need complex data types, you need Redis
  * If you need to scale horizonally, you need Memcached
  * If you just need memory caching and prefer simplicity, you should use Memcached

<!-- ==================================================================================================== -->

# DNS 101
* Amazon's DNS service is called Route 53
* The name Route 53 comes from the port Route 53 is on, which is port 53

## What is DNS
* DNS can be analagously thought of as a phone book
* DNS is used to convert human friendly domain names into compute IPv4 and IPv6 IP address
* IP addresses are used to identify individual machines on a Network
* The IPv4 space is a 32 bit field and has over 4 billion different possible adresses (4,294,967,296)
* The IPv6 has an address space of 128bits which in theory is 340 undecillion addresses (340,282,366,920,938,463,374,607,431,768,211,456)
* The **Top Level** domain is the last string section after the last period in a URL.
* For example with `http://www.google.com` the top level domaion is `.com`
* There is **Second Level Domain** which is an optional string just before the top level domain
* An example of a URL with a second level domain would be URLs ending in `.co.uk`
* The top level domain names are controlled by the Internet Assigned Numbers Authority (IANA) in a root zone database
* This database is essentially a database of all available top level domains
* This database is viewable at `http://www.iana.org/domains/root/db`
* Because all the names in a domain must be unqiue, there needs to be a way to organize this so domain names aren't duplicated
* This is performed by domain registrars
* A registrar is an authority that can assiogn domain names directly under one or more top-level domains
* These domains are registered woith InterNIC, a service of ICANN, which enforce uniquesness of domain names
* Each domain name becomes registered in a central database known as the WholS database
* Popular domain registers are:
  * Amazon
  * GoDaddy
  * 123-reg.co.uk



#### RDS Backups, Multi-AZ, and Read Replicas Lab Summary and Exam Tips
* There are two types of RDS DB backups:
  * Automated backups
  * Database snapshots
* Automated backups are done during a scheduled maitenance window
* Dtabase snapshots are triggered manually
* **Read Replicas**:
  * Can be Multi-AZ
  * Used to increase performance
  * Not used for disaster recovery
  * Must have automated backups turned on to use
  * Can be in different regions that primary DB instance
  * Can be Aurora or MySQL read replica, regardless of primary DB type
  * Can be promoted to a primary DB instance, however, this breaks the previous read replication to the old master
* **Multi-AZ**:
  * Used for disaster recovery
  * Not used for performance boosting
  * You can force a failover from one AZ to another by rebooting the primary RDS instnace and selecting force failover
  * Encryption is supported for the following RDS DB engines:
    * MySQL
    * Oracle
    * SQL Server
    * PostgreSQL
    * MariaDB
    * Aurora
  * Encryption is done using the AWS KMS service
  * Once a database is encrypted, the underyling data stored is encrypted, and therefore all future automated backups, read replicas, and snapshots will also be encrypted




<!-- Database stuff =========================================================================-->

### Register a Domain Name Lab
* Registering a domain name is not free
* You must include personal contact information when you register a domain name
* Normally domain names will be ready in 1-2 hours, but can take up to 3 days

#### Register a Domain Name Lab Summary and Exam Tips
* You can buy domain names directly through AWS
* Can take up to 3 days for a domain name to register

### Route53 Routing Policies Available on AWS
* The **Routing Types** on AWS are:
  * **Simple Routing**
  * **Weighted Routing**
  * **Latency-based Routing**
  * **Failover Routing**
  * **Geolocation Routing**
  * **Geoproximity Routing**
  * **Geoproxmitiy Routing (Traffic Flow Only)**
  * **Multivalue Answer Routing**

#### Route53 Simple Routing
* **Simple Routing Policy**: You can only have one record with multiple IP addresses
* If you specify multiple values in a record, Route53 returns all values to the user in a random order
* Basically, users can randomly directed to one of the IP addressed assocaited with the record
* **Naked Domain Name** and **Zone Apex** are synonymous
* Your browser will cache the actual IP address it got, so you wont actually be getting random IPs every time. TTL also plays into this
* You can flush DNS to achieve random effects of the Simple Routing Policy, and in relation to the TTL

#### Summary and Exam Tips
* **Simple Routing Polcy** is the simplest routing policy you can use
* It consists of a single record, with multiple IP addresses attached to the record
* Route53 will direct users to one of the IP addreses at random
* You can use one IP address as well

### Route53 Weighted Routing Policy
* **Weighted Routing Policy** allows you to split your traffic based on different weights assigned
* For example, you can weight it to send 90% of traffic to an EC2 in us-east-1, and 10% of traffic to go to us-west-1
* The EC2 any user will end up at is still somewhat random, its just that the odds have been weighted to specific instances
* Weighted Routing Policy allows you to set a health check, and then omit EC2 servers from the DNS listings which are failing health checks
* The health check requires you to specifiy a protocol, and IP address, a host name, a port, and a path, and Route53 will then routinely attempt to establish TCP connection to assess health
* You can use advanced health check options to change failure threshold, retry interval, etc.
* You can setup health check failure notifications

#### Summary and Exam Tips
* **Weighted Routing Policy** splits traffic between EC2 instances based upon configured weightings
* You can set health checks on individual recrod sets
* Should a record set fail a health check, it will be removed from Route53 until it passes health check again
* Record set is the IP addres of a single EC2 instance
* You can setup SNS notifications for health check failure

### Route53 Latency-Based Routing Policy
* Allows you to route your traffic based upon the lowest network latency for your end user
* A.k.a., route the user to the region which will give them the fastest response time
* To use latency-based routing, you create a latency resource record set for the resource (EC2 or ELB) in each region that hosts your website
* When Route53 recieves a request, it selects the user with the latency resource record set for the region that fives the user the lowest latency
* Route53 then responds with the value associated with that recrod set

#### Exam Tips
* Connects users to a record set based on the loweset latency for the user
* Can be verified with a VPN connection in differnt locations across the world

### Route53 Failover Routing Policy
* Failover routing policies are used when you want to create an active/passive setup
* For examply, you may setup your primary site to be in eu-west-2, and a secondary site in ap-southeast-2 in the event of disaster recovery
* Route53 will monitor the health of your endpoints using a health check, and fail to secondary path on failure

#### Summary and Exam Tips
* There is an active and passive site
* All traffic is directed to active site, unless Route53 detects a failure in the primary site via a health check fail
* In this event, traffic is redirected to the secondary site

### Route53 Geolocation Routing Policy
* **Geolocation Routing Policy** lets you choose which traffic a user is routed to based on the geographic location of the user
* Determined by the location associated with the DNS query origin
* For example, all queries from Europe could be directed to a set of EC2s running with specific EU features, such as Euro priced items rathern than dollar priced items
* This is contrasted with Latency Based Routing, which is based off latency metrics rather than strictly on locations
* Latency based routing is better for performance concerns, whereas Geolocation routing is better when the content returned is specific to different locations, or there are other strictly location based concerns

#### Summary and Exam Tips
* Send users from specific geographic regions to specific web servers, normally for some geographic/cultural differences in the content served on different web servers
* Not to be confused with latency based routing, which routes strictly based on which web server will have the lowest netowrk latency for a user
  
### Route53 Geoproximity Routing (Traffic Flow Only) Policy
* **Geoproximity Routing**: lets Route53 route traffic to resources based on the geographic location of the users **AND** the location of the resources
* You can optionally chose to route more/less traffic to a specific resource by setting a bias value
* A bias expands/shriknks the size of the geographic region from with the traffic resource is routed
* Route53 allows you to create extremely complicated traffic routing maps which network engineers would handle
* To use Geoproximity Routing, you **must** use **Route53 Traffic Flow**

### Route53 Multivalue Answer Routing Policy
* **Multivalue Answer Routing Policy** lets you configure Route53 to return multiple values, such as IP addresses for your web servers, in response to DNS queries
* Basically the same as Simple Routing, with the only difference being Multivalue Answer Routing also allows you to incorporate health checks
* In the event a resource fails a healh check, that record set will not be returned in a DNS query
* Otherwise, the behaviour is the same as Simple Routing
* It seems like there's no reason to use Simple Routing if this exists

#### Summary and Exam Tips
* Users are directed to record sets at random, unless the corresponding resrouce for a record set fails the health check

## DNS Summary and Exam Tips
* ELB (Elastic Load Balancer) do not have predefined IPv4 addresses; you resolve them using a DNS name
* Difference between an Alias Record (A-Record) and a CNAME:
  * The analogy is to a telephone book
  * An A-Record is a name connected to a phone number 
  * A CNAME is a name that directs to another name, which then directs to a phone number
  * In this analogy the phone number is the actual IP address
* Common DNS types:
  * SOA Records
  * NS Records
  * A Recrods
  * CNAMEs
  * MX Records
  * PTR Records
* The following are the types of Route53 routing:
  * **Simple Routing**:
    * Simple routing policy you an only have one record with multiple IP addresses  
    * Route53 randomly directs all users to the different records in a random order  
  * **Weighted Routing**:
    * Can have multiple records
    * Users are directed to different records based on weights assigned to each recrod
  * **Latency-Based Routing**:
    * Based on users location and the latency on the network to their location
    * Route53 directs users to records based on which record produces the minimum network latency
    * While location will impact latency heavily, the decision is based upon latency metric (a.k.a. milliseconds) not actual geograpghic distances or locations
  * **Failover Routing**:
    * There is an active record, and a passive
    * Traffic is directed to the active record, unless failure is detected on the active record
    * This is determined via a health check
    * At this point, traffic is automatically redirected to the passive route
  * **Geolocation Routing**:
    * Users are directed to specific records (and corresponding web servers) based on their geographic location
    * Geographic location is determined by the origin of the DNS lookup query
    * Based upon location users are directed to specific resources dedicated to specific regions
    * Not based on latency, and theoretically users could be directed to slower resources (although this would be due to a bad implemented configuration)
    * This is to direct users to specific web servers based upon their location, such as to render a site with euroes attached to list prices rather than dollars
  * **Geoproximity Routing (Traffic Flow Only)**:
    * Advanced networking feature that allows you to route traffic of users to resources based on both the location of the users and the location of the resources
    * You must Route53 traffic flow to do Geaoproximity Routing
    * You can set bias values, which effectively expand/shrink the size of a geographic region associated with a specific resource and will effect the overall traffic to that resource
  * **Multivalue Answer Routing**:
    * Essentially the same as Simple Routing, except with health checks
    * Can have multiple values in your record sets, and health checks associated with each record
    * If a health check fails for a record, traffic will automatically stop being routed to this resource until it passes the health checks again
* Health checks can be set up with respect to invidual record sets against a resource (EC2 or ELB)
* You can setup SNS notifcations upon health check failure

# VPC

## VPC Overview
* Recomneds being able to build out your own VPC as a knowledge check for the Exam
* VPC can be thought of as a personal, private data center in the cloud
* VPC lets you provision a logically isolated section of the AWS cloud where you can launch AWS resouces in a virtual network that you define
* In your VPC, you can select your own IP address range, create subnets, and configure route tables and network gateways
* A use of a VPC might be setting up web servers that are exposed to the internet, but containing database servers on an isolated private network that only the web servers can reach
* You can also create a Hardware Virtual Private Network (VPN) connection between your corporate datacenter and your VPC to leverage the AWS ckoud as an extension of a corporate data center
* A bastion host is an EC2 in a public subnet that can be used to SSH to an EC2 in a private subnet
* Private IP Address rates of note:
  * **10.0.0.0 - 10.255.255.255 (10/8 prefix)**
    * Amazon does not actually allow /8 prefix, and the largest subnet you can have is /16
  * **172.16.0.0 - 172.31.225.255 (172.16/12 prefix)**
  * **192.168.0.0 - 192.168.255.255 (192.168/16 prefix)**
    * This is for your home network 
* These IP Address ranges are defined by the Internet Signed Mumbers Authority as being reserver
* These ranges are only available on private networks, not public networks

### What can be done with a VPC:
* Launch instanes into a subnet of your choosing
* Assign custom IP address ranges in each subnet
* Configure route tables between subnets
* Create internet gateway and attach it to our VPC
* Much better security control over AWS resources
* Instance Secuirty Group
* Subnet netowrk access control lists (ACLS)

### Default VPC vs Custom VPC
* Default VPC is user friendly and allows you to deploy instances immediately
* All subnets in defualt VPC has a route out to the internet
* Each EC2 instance has both a public and private IP address
* You can recover the default VPC, but dont delete it

### VPC Peering
* Allows you to connect one VPC with another via a direct network route using private IP Addresses
* Instances behave as if they were on the same private network
* You can peer VPCs with other AWS accounts as well as with other VPCs in the same account
* VPC peering is done in a **star configuration**, meaning there is 1 central VPC and more can peer to it, but there is not transitive peering
* You can peer between VPCs in different regions

### VPC Overview Summary and Exam Tips
* Think of a VPC as a logical data center on the cloud
* Consists of IGWs (or virtual private gateways), route tables, network access control lists, subnets, and security groups
* 1 subnet always will be in 1 Availability zone, and a subnet cannot span multiple AZs
* Security Groups are stateful, Network Access Control Lists are stateless
* Basically means that Network Access Control Lists can have allow and deny rules, whereas security groups only have explicit allow rules
* There is no transistive peering

### Create youw own Custom VPC Lab Part 1
* A subnet under a VPC cannot span multiple AZs.
* Auto-assign public IP address is turned off by default, and will need to be enabled to create a public subnet
* Amazon automatically reserves the first four and last four IP Addresses in each subnet CIDR block, and these cannot be assigned to an EC2 instance
* For example, for the CIDR block `10.0.0.0/24` the following five IP addresses are reserved:
  * `10.0.0.0`: Network Address
  * `10.0.0.1`: Reserved by AWS for the VPC router
  * `10.0.0.2`: Reserved by AWS. The IP Address of the DNS server is always the base of the VPC network range plus two;l however, AWS also reserves the base of each subnet range plus two. For VPCs with multiple CIDR blocks, the IP address of the DNS server is located in the primary CIDR.
  * `10.0.0.3`: Reserved by AWS for future use
  * `10.0.0.255`: Network broadcast address. AWS does not support broadcast in a VPC, therefore they reserve this address
* Using `10.0.1.0` is conventionally used as the public subnet (I think this is what he said)
* To enable auto assign public IP address used the related actions on a subnet and use `Modify auto assign IP settings`
* This will make it so when EC2s are launched into this subnet they automatically recieve a public IP address
* Even with a public subnet, you will need an internet gateway in order to allow incoming connections to the EC2s in the public subnet
* Creating an interet gateway can be done with a button in the console when viewing the VPC
* When a VPC is created, it must also be attached to the VPC it is intended to act on
* You cannot attach multiple internet gateways to a single VPC. **One internet gateway per VPC**
* After creating an internet gateway, you will need to create a main route that will be the route out to the internet
* By defualt in the route table, all subnets in a VPC wil have routes added to allows the subnets to communicate with each other over IPv4 and IPv6
* If you create a route out to the internet in your main route table, every subnet you create by default would be public to the internet
* This is a security concern, so to improve this, you normally make your main route table private and then use seperate route tables for the public subnets
* To create a route out to the internet, in a route table add a route for `0.0.0.0/0` as the Destianation, and Internet Gateway as the Target, and select your Internet Gateway instance
* To add a route out to the internet using IPv6, add a route with `;;/0` as the destination, and Internet Gateway as the Taret, and select your Internet Gateway instance
* After creating a public subnet and a private subnet with the corresponding route tables and internet gateways configured, the next step is to provision EC2s within the VPC
* To launch EC2s within the VPC use the **Network** select dropdown, and select the VPC instnace
* Security groups do not span VPCs, and will be specific to the VPC they were created with respect to

#### Create your own Custom VPC Lab Part 1 Sumamry and Exam Tips
* When you create a VPC, automatically created with it are:
  * A default route table
  * A network access control list
  * A default security group
* When you create a VPC, it will **NOT** automatically create:
  * Any subnets
  * Any internet gateway
* The AZs listed in your account are consistent for you, but specific to you. Across AWS accounts the AZs are randomzied and the AZ one account lists as `us-east-1a` might be different than another AWS account's `us-east-1a`
* Amazon always reserves at least **5** IP addressed in your subnet, at the beginning and end of the CIDR block
* You can only have 1 internet gateway per VPC
* Security groups cannot span VPCs

### Create your own Custom VPC Lab Part 2
* By default, EC2s in different security groups will not have access to each other
* To allowing pinging of a server, use allow `All ICMP`
* Conventianally, it is a good practice to create a seperate security group for your private subnet where you explicitly allows connections only from the public subnet, not the entire internet
* You can SSH to the private subnet by placing your private key on a public EC2 and SSHing from the public EC2 to the private EC2; however, this is a bad idea and should be done using a bastion host
* Unless you create a internet route out from a private subnet, it will not be able to use commands like `yum` or `curl`

### NAT Instances and NAT Gateways Lab
* 9/10 you will use a NAT Gateway over a NAT Instance
* NAT Instances are an  individual EC2 isntance that allows private subnets to communicate out to internet without being exposed as public
* A NAT Gateway is a highly avaialable gateway that allows private subnets to communicate out to internet without being exposed as public
* You can launch a NAT Instnace by searching ***NAT*** in the AMI search bar when laucnhing an EC2
* You should notice that a NAT instance has a public IP address
* Each EC2 automatically runs a **Source/Destination Check** by default
* This means the EC2 must be the source or destination of any traffic it recieves
* A NAT instance must be able to sned/recieve traffic when the source or destination is not itself
* Therefore, for NAT instances you must disable source/destination checks
* The NAT instance is like a bridge between the private subnet and the internet gateway
* You will also need to create a route in your default route table for the VPC
* Do this by creating a route to the internet, using `0.0.0.0/0` as the destination and the instance ID of the NAT instnace for the Target
* Using a NAT instance is unfavourable because:
  * It is a single instance that all traffic is directed through, creating a bottleneck
  * It has a single point of failure, if the NAT instance ever fails
* For a more highly scalable solution, use a NAT Gateway
* You should create your NAT Gateway in your public subnet
* You then edit your route table and add a route in the main root table to allow route out to internet and use the NAT Gateway as the target
* NAT Gateways can take some time to provision

#### NAT Instances and NAT Gateways Lab Summary and Exam Tips
* NAT Instances are out of date and you should almost always use NAT Gateways
* **NAT Isntances**:
  * Have to manually disable source/destination checks
  * NAT instnaces must be in a public subnet
  * There must be a route out of the private subnet to the NAT instance in order to access internet from private subnet
  * The amount of traffic that a NAT instance can support depends on the instance, and the size can be increased/decreased depending on bottlenecking
  * You can create high availability with a NAT instance using auto-scaling groups, multiple subnets in different AZs, and a script to automate failover 
  * This is a pain though
  * NAT Instances are assigned to a security group just like other EC2s
* **NAT Gateways**:
  * Redundant with respect to the availability zone they exist in
  * You can only have a NAT Gateway in one AZ; they cannot span AZs
  * They are recommended by AWS over NAT instnace
  * They start at throughout of 5gps and scale up to 45Gps
  * No need to patch the OS of NAT Gateways, which you do have to do with NAT instacnes
  * Not assigned to a securiy group, which a NAT instance is
  * Automatically assigned a public IP address
  * No need to disable source/destination checks
  * If you have resources (EC2s, ELBs) in mmultiple AZs and they share once NAT gateway, in the event the NAT gateway's AZ is down, resoures in the other AZs will also lose internet
  * In order to prevent this single point of failure, create a NAT gateway in each AZ and configure your routing table to use the NAT gateway which is in the same AZ
  * This a more AZ independant architecture

### Network Access Contol Lists vs Secrutiy Groups Lab
* When you create a VPC, there will be a default NACL with two rules of **Rule Number** `100` and `101`. These rules **ALLOW**  all traffic using IPv4 addresses (`0.0.0.0/0`) and IPv6 addresses (`;;/0`)
* When you create new rules, AWS recomneds the best practice of incrementing the rule number up by 100 from the last IPv4 rule or IPv6 rule depending on which IP version your rule is for
* When you create a new custom, NACL there will be two rules by defualt which **DENY** all traffic by default
* To use a custom NACL, you use the `Subnet Associateions` on the NACL instance view
* NACLs are not stateful, so you must manually allow the outbound rule in addition to the inboud rule. In comparison, Security Groups would automatically allow the corresponding outbound rule
* When you allow outbound rules with a NACL, you will use an **Ephemeral Port** as the port
* **Ephemeral Port**:
  * Are short lived transport protocol ports for Intrenet Protocol (IP) communications
  * Ephemeral ports are automatically allocated from the predefined range by the IP stack software
  * On web servers, ephemeral ports may be used on the server end for communication. This is to continue communication with a client that connected initially on a well known port, like 80/443 for HTTP/HTTPS
  * The ephemeral port allocation is only valid for the duration of the communication session, and after completion or timeout the port becomes reavailable for more use
  * NAT Gateways use **1024 - 65535** as the ephemeral port range





<!-- ==================================================================================================== -->

# Conventional Port-Protocol Association
| Protocol | Port |
|  ------- | ---- |
| HTTP | 80 |
| HTTPS | 443 |
| SSH | 22 |
| SFTP | 22 |
| MySQL |  |

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
| IOPS |  |
| Amazon Machine Image (AMI) |  |
| Snapshot |  |
| Elastic File System (EFS) |  |
| Clustered Placement Group |  | 
|  Diaster Recovery (DR) |  |
| Multi-AZ |  |
| Hardware Service Manager (HSM) |  |
| Key Management Service (KSM) |  |
| Online Transaction Processing | OLTP |
| Online Analytics Processing (OLAP)  |  |
| DyanamoDB |  |
| Internet Gateway |  |
| Virtual Private Cloud (VPC) |  |
| Route Table |  |
| Main Route |  |
| Subnet |  |
| Domain Name System (DNS) |  |
| NAT Gateway |  |
| NAT Instance |  |
|  |  |
|  |  |
