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
  * There are 4 methods for securing data at rest

#### Encryption of Data at Rest
* **One**
  * one
* **One**
  * one
* **One**
  * one
* **One**
  * one

##### Server Side Encrpytion:
1. one
2. two
3. three

##### another section
4. four    


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
<!--
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  |
-->
