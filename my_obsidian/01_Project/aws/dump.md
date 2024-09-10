---
id: dump
aliases: []
tags: []
---

# examtopics

### 01

A company collects data for temperature, humidity, and atmospheric pressure in
cities across multiple continents. The average volume of data that the company
collects from each site daily is 500 GB. Each site has a high-speed Internet
connection. The company wants to aggregate the data from all these global sites
as quickly as possible in a single Amazon S3 bucket. The solution must minimize
operational complexity. Which solution meets these requirements?

- A. Turn on **S3 Transfer Acceleration** on the destination S3 bucket. Use
  multipart uploads to directly upload site data to the destination S3 bucket.

- B. Upload the data from each site to an S3 bucket in the closest Region. Use
  **S3 Cross-Region Replication** to copy objects to the destination S3 bucket.
  Then remove the data from the origin S3 bucket.

- C. Schedule **AWS Snowball Edge Storage Optimized** device jobs daily to
  transfer data from each site to the closest Region. Use S3 Cross-Region
  Replication to copy objects to the destination S3 bucket.

- D. Upload the data from each site to an Amazon EC2 instance in the closest
  Region. Store the data in an Amazon Elastic Block Store (Amazon EBS) volume.
  At regular intervals, take an EBS snapshot and copy it to the Region that
  contains the destination S3 bucket. Restore the EBS volume in that Region.

### 02

A company needs the ability to analyze the log files of its proprietary
application. The logs are stored in JSON format in an Amazon S3 bucket. Queries
will be simple and will run on-demand. A solutions architect needs to **perform
the analysis with minimal changes to the existing architecture.** What should
the solutions architect do to meet these requirements with the LEAST amount of
operational overhead?

- A. Use Amazon Redshift to load all the content into one place and run the SQL
  queries as needed.
- B. Use Amazon CloudWatch Logs to store the logs. Run SQL queries as needed
  from the Amazon CloudWatch console.
- C. Use Amazon Athena directly with Amazon S3 to run the queries as needed.
- D. Use AWS Glue to catalog the logs. Use a transient Apache Spark cluster on
  Amazon EMR to run the SQL queries as needed.

### 03

A company uses AWS Organizations to **manage multiple AWS accounts for different
departments.** The management account has an Amazon S3 bucket that contains
project reports. The company wants to limit access to this S3 bucket to only
users of accounts within the organization in AWS Organizations. Which solution
meets these requirements with the LEAST amount of operational overhead?

- A. Add the aws PrincipalOrgID global condition key with a reference to the
  organization ID to the S3 bucket policy.
- B. Create an organizational unit (OU) for each department. Add the
  aws:PrincipalOrgPaths global condition key to the S3 bucket policy.
- C. Use AWS CloudTrail to monitor the CreateAccount,
  InviteAccountToOrganization, LeaveOrganization, and
  RemoveAccountFromOrganization events. Update the S3 bucket policy accordingly.
- D. Tag each user that needs access to the S3 bucket. Add the aws:PrincipalTag
  global condition key to the S3 bucket policy.

### 04

An application runs on an Amazon EC2 instance in a VPC(Virtual Private Cloud).
The application processes logs that are stored in an Amazon S3 bucket. The EC2
instance needs to access the S3 bucket without connectivity to the internet.
Which solution will provide private network connectivity to Amazon S3?

- A. Create a gateway VPC endpoint to the S3 bucket.
- B. Stream the logs to Amazon CloudWatch Logs. Export the logs to the S3
  bucket.
- C. Create an instance profile on Amazon EC2 to allow S3 access.
- D. Create an Amazon API Gateway API with a private link to access the S3
  endpoint.

### 05

A company is hosting a web application on AWS using a single Amazon EC2 instance
that stores user-uploaded documents in an Amazon EBS volume. For better
scalability and availability, the company duplicated the architecture and
created a second EC2 instance and EBS volume in another Availability Zone,
placing both behind an Application Load Balancer. After completing this change,
users reported that, each time they refreshed the website, they could see one
subset of their documents or the other, but never all of the documents at the
same time. What should a solutions architect propose to ensure users see all of
their documents at once?

- A. Copy the data so both EBS volumes contain all the documents
- B. Configure the Application Load Balancer to direct a user to the server with
  the documents
- C. Copy the data from both EBS volumes to Amazon EFS. Modify the application
  to save new documents to Amazon EFS
- D. Configure the Application Load Balancer to send the request to both
  servers. Return each document from the correct server

### 06

A company uses NFS to store large video files in on-premises network attached
storage. Each video file ranges in size from 1 MB to 500 GB. The total storage
is 70 TB and is no longer growing. The company decides to **migrate the video
files** to Amazon S3. The company must migrate the video files as soon as
possible while using the least possible network bandwidth. Which solution will
meet these requirements?

- A. Create an S3 bucket. Create an IAM role that has permissions to write to
  the S3 bucket. Use the AWS CLI to copy all files locally to the S3 bucket.
- B. Create an AWS Snowball Edge job. Receive a Snowball Edge device on
  premises. Use the Snowball Edge client to transfer data to the device. Return
  the device so that AWS can import the data into Amazon S3.
- C. Deploy an S3 File Gateway on premises. Create a public service endpoint to
  connect to the S3 File Gateway. Create an S3 bucket. Create a new NFS file
  share on the S3 File Gateway. Point the new file share to the S3 bucket.
  Transfer the data from the existing NFS file share to the S3 File Gateway.
- D. Set up an AWS Direct Connect connection between the on-premises network and
  AWS. Deploy an S3 File Gateway on premises. Create a public virtual interface
  (VIF) to connect to the S3 File Gateway. Create an S3 bucket. Create a new NFS
  file share on the S3 File Gateway. Point the new file share to the S3 bucket.
  Transfer the data from the existing NFS file share to the S3 File Gateway.

### 07

A company has an application that ingests incoming messages. Dozens of other
applications and microservices then quickly consume these messages. The number
of messages varies drastically and sometimes increases suddenly to 100,000 each
second. **The company wants to decouple the solution and increase scalability.**
Which solution meets these requirements?

- A. Persist the messages to Amazon Kinesis Data Analytics. Configure the
  consumer applications to read and process the messages.
- B. Deploy the ingestion application on Amazon EC2 instances in an Auto Scaling
  group to scale the number of EC2 instances based on CPU metrics.
- C. Write the messages to Amazon Kinesis Data Streams with a single shard. Use
  an AWS Lambda function to preprocess messages and store them in Amazon
  DynamoDB. Configure the consumer applications to read from DynamoDB to process
  the messages.
- D. Publish the messages to an Amazon Simple Notification Service (Amazon SNS)
  topic with multiple Amazon Simple Queue Service (Amazon SOS) subscriptions.
  Configure the consumer applications to process the messages from the queues.

### 08

A company is migrating a distributed application to AWS. The application serves
variable workloads. The legacy platform consists of a primary server that
coordinates jobs across multiple compute nodes. The company wants to modernize
the application with a solution that maximizes resiliency and scalability. How
should a solutions architect design the architecture to meet these requirements?

- A. Configure an Amazon Simple Queue Service (Amazon SQS) queue as a
  destination for the jobs. Implement the compute nodes with Amazon EC2
  instances that are managed in an Auto Scaling group. Configure EC2 Auto
  Scaling to use scheduled scaling.
- B. Configure an Amazon Simple Queue Service (Amazon SQS) queue as a
  destination for the jobs. Implement the compute nodes with Amazon EC2
  instances that are managed in an Auto Scaling group. Configure EC2 Auto
  Scaling based on the size of the queue.
- C. Implement the primary server and the compute nodes with Amazon EC2
  instances that are managed in an Auto Scaling group. Configure AWS CloudTrail
  as a destination for the jobs. Configure EC2 Auto Scaling based on the load on
  the primary server.
- D. Implement the primary server and the compute nodes with Amazon EC2
  instances that are managed in an Auto Scaling group. Configure Amazon
  EventBridge (Amazon CloudWatch Events) as a destination for the jobs.
  Configure EC2 Auto Scaling based on the load on the compute nodes.

### 09

A company is running an SMB file server in its data center. The file server
stores large files that are accessed frequently for the first few days after the
files are created. After 7 days the files are rarely accessed. The total data
size is increasing and is close to the company's total storage capacity. A
solutions architect must increase the company's available storage space without
losing low-latency access to the most recently accessed files. The solutions
architect must also provide file lifecycle management to avoid future storage
issues. Which solution will meet these requirements?

- A. Use AWS DataSync to copy data that is older than 7 days from the SMB file
  server to AWS.
- B. Create an Amazon S3 File Gateway to extend the company's storage space.
  Create an S3 Lifecycle policy to transition the data to S3 Glacier Deep
  Archive after 7 days.
- C. Create an Amazon FSx for Windows File Server file system to extend the
  company's storage space.
- D. Install a utility on each user's computer to access Amazon S3. Create an S3
  Lifecycle policy to transition the data to S3 Glacier Flexible Retrieval after
  7 days.

### 10

A company is building an ecommerce web application on AWS. The application sends
information about new orders to an Amazon API Gateway REST API to process. The
company wants to ensure that orders are processed in the order that they are
received. Which solution will meet these requirements?

- A. Use an API Gateway integration to publish a message to an Amazon Simple
  Notification Service (Amazon SNS) topic when the application receives an
  order. Subscribe an AWS Lambda function to the topic to perform processing.
- B. Use an API Gateway integration to send a message to an Amazon Simple Queue
  Service (Amazon SQS) FIFO queue when the application receives an order.
  Configure the SQS FIFO queue to invoke an AWS Lambda function for processing.
- C. Use an API Gateway authorizer to block any requests while the application
  processes an order.
- D. Use an API Gateway integration to send a message to an Amazon Simple Queue
  Service (Amazon SQS) standard queue when the application receives an order.
  Configure the SQS standard queue to invoke an AWS Lambda function for
  processing.

### 11.

A company has an application that runs on Amazon EC2 instances and uses an
Amazon Aurora database. The EC2 instances connect to the database by using user
names and passwords that are stored locally in a file. The company wants to
minimize the operational overhead of credential management. What should a
solutions architect do to accomplish this goal?

- A. Use AWS Secrets Manager. Turn on automatic rotation. Most Voted
- B. Use AWS Systems Manager Parameter Store. Turn on automatic rotation.
- C. Create an Amazon S3 bucket to store objects that are encrypted with an AWS
  Key Management Service (AWS KMS) encryption key. Migrate the credential file
  to the S3 bucket. Point the application to the S3 bucket.
- D. Create an encrypted Amazon Elastic Block Store (Amazon EBS) volume for each
  EC2 instance. Attach the new EBS volume to each EC2 instance. Migrate the
  credential file to the new EBS volume. Point the application to the new EBS
  volume.

### 12. 중요

A global company hosts its web application on Amazon EC2 instances behind an
Application Load Balancer (ALB). The web application has static data and dynamic
data. The company stores its static data in an Amazon S3 bucket. **The company
wants to improve performance and reduce latency for the static data and dynamic
data.** **The company is using its own domain name registered with Amazon
Route 53.** What should a solutions architect do to meet these requirements?

- A. Create an Amazon CloudFront distribution that has the S3 bucket and the ALB
  as origins. Configure Route 53 to route traffic to the CloudFront
  distribution.
- B. Create an Amazon CloudFront distribution that has the ALB as an origin.
  Create an AWS Global Accelerator standard accelerator that has the S3 bucket
  as an endpoint Configure Route 53 to route traffic to the CloudFront
  distribution.
- C. Create an Amazon CloudFront distribution that has the S3 bucket as an
  origin. Create an AWS Global Accelerator standard accelerator that has the ALB
  and the CloudFront distribution as endpoints. Create a custom domain name that
  points to the accelerator DNS name. Use the custom domain name as an endpoint
  for the web application.
- D. Create an Amazon CloudFront distribution that has the ALB as an origin.
  Create an AWS Global Accelerator standard accelerator that has the S3 bucket
  as an endpoint. Create two domain names. Point one domain name to the
  CloudFront DNS name for dynamic content. Point the other domain name to the
  accelerator DNS name for static content. Use the domain names as endpoints for
  the web application.

### 13.

A company performs monthly maintenance on its AWS infrastructure. During these
maintenance activities, the company needs to rotate the credentials for its
Amazon RDS for MySQL databases across multiple AWS Regions. Which solution will
meet these requirements with the LEAST operational overhead?

- A. Store the credentials as secrets in AWS Secrets Manager. Use multi-Region
  secret replication for the required Regions. Configure Secrets Manager to
  rotate the secrets on a schedule.
- B. Store the credentials as secrets in AWS Systems Manager by creating a
  secure string parameter. Use multi-Region secret replication for the required
  Regions. Configure Systems Manager to rotate the secrets on a schedule.
- C. Store the credentials in an Amazon S3 bucket that has server-side
  encryption (SSE) enabled. Use Amazon EventBridge (Amazon CloudWatch Events) to
  invoke an AWS Lambda function to rotate the credentials.
- D. Encrypt the credentials as secrets by using AWS Key Management Service (AWS
  KMS) multi-Region customer managed keys. Store the secrets in an Amazon
  DynamoDB global table. Use an AWS Lambda function to retrieve the secrets from
  DynamoDB. Use the RDS API to rotate the secrets.

### 14

A company runs an ecommerce application on Amazon EC2 instances behind an
Application Load Balancer. The instances run in an Amazon EC2 Auto Scaling group
across multiple Availability Zones. The Auto Scaling group scales based on CPU
utilization metrics. The ecommerce application stores the transaction data in a
MySQL 8.0 database that is hosted on a large EC2 instance. The database's
performance degrades quickly as application load increases. The application
handles more read requests than write transactions. The company wants a solution
that will automatically scale the database to meet the demand of unpredictable
read workloads while maintaining high availability. Which solution will meet
these requirements?

- A. Use Amazon Redshift with a single node for leader and compute
  functionality.
- B. Use Amazon RDS with a Single-AZ deployment Configure Amazon RDS to add
  reader instances in a different Availability Zone.
- C. Use Amazon Aurora with a Multi-AZ deployment. Configure Aurora Auto Scaling
  with Aurora Replicas.
- D. Use Amazon ElastiCache for Memcached with EC2 Spot Instances.

### 15

A company recently migrated to AWS and wants to implement a solution to protect
the traffic that flows in and out of the production VPC. The company had an
inspection server in its on-premises data center. The inspection server
performed specific operations such as traffic flow inspection and traffic
filtering. The company wants to have the same functionalities in the AWS Cloud.
Which solution will meet these requirements?

- A. Use Amazon GuardDuty for traffic inspection and traffic filtering in the
  production VPC.
- B. Use Traffic Mirroring to mirror traffic from the production VPC for traffic
  inspection and filtering.
- C. Use AWS Network Firewall to create the required rules for traffic
  inspection and traffic filtering for the production VPC.
- D. Use AWS Firewall Manager to create the required rules for traffic
  inspection and traffic filtering for the production VPC.

### 16

A company hosts a data lake on AWS. The data lake consists of data in Amazon S3
and Amazon RDS for PostgreSQL. The company needs a reporting solution that
provides data visualization and includes all the data sources within the data
lake. Only the company's management team should have full access to all the
visualizations. The rest of the company should have only limited access. Which
solution will meet these requirements?

- A. Create an analysis in Amazon QuickSight. Connect all the data sources and
  create new datasets. Publish dashboards to visualize the data. Share the
  dashboards with the appropriate IAM roles.
- B. Create an analysis in Amazon QuickSight. Connect all the data sources and
  create new datasets. Publish dashboards to visualize the data. Share the
  dashboards with the appropriate users and groups.
- C. Create an AWS Glue table and crawler for the data in Amazon S3. Create an
  AWS Glue extract, transform, and load (ETL) job to produce reports. Publish
  the reports to Amazon S3. Use S3 bucket policies to limit access to the
  reports.
- D. Create an AWS Glue table and crawler for the data in Amazon S3. Use Amazon
  Athena Federated Query to access data within Amazon RDS for PostgreSQL.
  Generate reports by using Amazon Athena. Publish the reports to Amazon S3. Use
  S3 bucket policies to limit access to the reports.

### 17

A company is implementing a new business application. The application runs on
two Amazon EC2 instances and uses an Amazon S3 bucket for document storage. A
solutions architect needs to ensure that the EC2 instances can access the S3
bucket. What should the solutions architect do to meet this requirement?

- A. Create an IAM role that grants access to the S3 bucket. Attach the role to
  the EC2 instances.
- B. Create an IAM policy that grants access to the S3 bucket. Attach the policy
  to the EC2 instances.
- C. Create an IAM group that grants access to the S3 bucket. Attach the group
  to the EC2 instances.
- D. Create an IAM user that grants access to the S3 bucket. Attach the user
  account to the EC2 instances.

### 18

An application development team is designing a microservice that will convert
large images to smaller, compressed images. When a user uploads an image through
the web interface, the microservice should store the image in an Amazon S3
bucket, process and compress the image with an AWS Lambda function, and store
the image in its compressed form in a different S3 bucket. A solutions architect
needs to design **a solution that uses durable, stateless components to process
the images automatically.** Which combination of actions will meet these
requirements? (Choose two.)

- A. Create an Amazon Simple Queue Service (Amazon SQS) queue. Configure the S3
  bucket to send a notification to the SQS queue when an image is uploaded to
  the S3 bucket.
- B. Configure the Lambda function to use the Amazon Simple Queue Service
  (Amazon SQS) queue as the invocation source. When the SQS message is
  successfully processed, delete the message in the queue.
- C. Configure the Lambda function to monitor the S3 bucket for new uploads.
  When an uploaded image is detected, write the file name to a text file in
  memory and use the text file to keep track of the images that were processed.
- D. Launch an Amazon EC2 instance to monitor an Amazon Simple Queue Service
  (Amazon SQS) queue. When items are added to the queue, log the file name in a
  text file on the EC2 instance and invoke the Lambda function.
- E. Configure an Amazon EventBridge (Amazon CloudWatch Events) event to monitor
  the S3 bucket. When an image is uploaded, send an alert to an Amazon ample
  Notification Service (Amazon SNS) topic with the application owner's email
  address for further processing.

### 19

A company has a three-tier web application that is deployed on AWS. The web
servers are deployed in a public subnet in a VPC. The application servers and
database servers are deployed in private subnets in the same VPC. The company
has deployed a third-party virtual firewall appliance from AWS Marketplace in an
inspection VPC. The appliance is configured with an IP interface that can accept
IP packets. A solutions architect needs to integrate the web application with
the appliance to inspect all traffic to the application before the traffic
reaches the web server. Which solution will meet these requirements with the
LEAST operational overhead?

- A. Create a Network Load Balancer in the public subnet of the application's
  VPC to route the traffic to the appliance for packet inspection.
- B. Create an Application Load Balancer in the public subnet of the
  application's VPC to route the traffic to the appliance for packet inspection.
- C. Deploy a transit gateway in the inspection VPConfigure route tables to
  route the incoming packets through the transit gateway.
- D. Deploy a Gateway Load Balancer in the inspection VPC. Create a Gateway Load
  Balancer endpoint to receive the incoming packets and forward the packets to
  the appliance.

### 20 다시보기

A company wants to improve its ability to clone large amounts of production data
into a test environment in the same AWS Region. The data is stored in Amazon EC2
instances on Amazon Elastic Block Store (Amazon EBS) volumes. Modifications to
the cloned data must not affect the production environment. The software that
accesses this data requires consistently high I/O performance. A solutions
architect needs to minimize the time that is required to clone the production
data into the test environment. Which solution will meet these requirements?

- A. Take EBS snapshots of the production EBS volumes. Restore the snapshots
  onto EC2 instance store volumes in the test environment.
- B. Configure the production EBS volumes to use the EBS Multi-Attach feature.
  Take EBS snapshots of the production EBS volumes. Attach the production EBS
  volumes to the EC2 instances in the test environment.
- C. Take EBS snapshots of the production EBS volumes. Create and initialize new
  EBS volumes. Attach the new EBS volumes to EC2 instances in the test
  environment before restoring the volumes from the production EBS snapshots.
- D. Take EBS snapshots of the production EBS volumes. Turn on the EBS fast
  snapshot restore feature on the EBS snapshots. Restore the snapshots into new
  EBS volumes. Attach the new EBS volumes to EC2 instances in the test
  environment.

### 21

An ecommerce company wants to launch a one-deal-a-day website on AWS. Each day
will feature exactly one product on sale for a period of 24 hours. **The company
wants to be able to handle millions of requests each hour with millisecond
latency during peak hours.** Which solution will meet these requirements with
the LEAST operational overhead?

- A. Use Amazon S3 to host the full website in different S3 buckets. Add Amazon
  CloudFront distributions. Set the S3 buckets as origins for the distributions.
  Store the order data in Amazon S3.
- B. Deploy the full website on Amazon EC2 instances that run in Auto Scaling
  groups across multiple Availability Zones. Add an Application Load Balancer
  (ALB) to distribute the website traffic. Add another ALB for the backend APIs.
  Store the data in Amazon RDS for MySQL.
- C. Migrate the full application to run in containers. Host the containers on
  Amazon Elastic Kubernetes Service (Amazon EKS). Use the Kubernetes Cluster
  Autoscaler to increase and decrease the number of pods to process bursts in
  traffic. Store the data in Amazon RDS for MySQL.
- D. Use an Amazon S3 bucket to host the website's static content. Deploy an
  Amazon CloudFront distribution. Set the S3 bucket as the origin. Use Amazon
  API Gateway and AWS Lambda functions for the backend APIs. Store the data in
  Amazon DynamoDB.

D because all of the components are infinitely scalable dynamoDB, API Gateway,
Lambda, and of course s3+cloudfront

### 22

A solutions architect is using Amazon S3 to design the storage architecture of a
new digital media application. The media files must be resilient to the loss of
an Availability Zone. Some files are accessed frequently while other files are
rarely accessed in an unpredictable pattern. The solutions architect must
minimize the costs of storing and retrieving the media files. Which storage
option meets these requirements?

- A. S3 Standard
- B. S3 Intelligent-Tiering
- C. S3 Standard-Infrequent Access (S3 Standard-IA)
- D. S3 One Zone-Infrequent Access (S3 One Zone-IA)

"unpredictable pattern" - always go for Intelligent Tiering of S3 It also meets
the resiliency requirement: "S3 Standard, S3 Intelligent-Tiering, S3
Standard-IA, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3
Glacier Deep Archive redundantly store objects on multiple devices across a
minimum of three Availability Zones in an AWS Region"

### 23

A company is storing backup files by using Amazon S3 Standard storage. The files
are accessed frequently for 1 month. However, the files are not accessed after 1
month. The company must keep the files indefinitely. Which storage solution will
meet these requirements MOST cost-effectively?

- A. Configure S3 Intelligent-Tiering to automatically migrate objects.
- B. Create an S3 Lifecycle configuration to transition objects from S3 Standard
  to S3 Glacier Deep Archive after 1 month.
- C. Create an S3 Lifecycle configuration to transition objects from S3 Standard
  to S3 Standard-Infrequent Access (S3 Standard-IA) after 1 month.
- D. Create an S3 Lifecycle configuration to transition objects from S3 Standard
  to S3 One Zone-Infrequent Access (S3 One Zone-IA) after 1 month.

-- The storage solution that will meet these requirements most cost-effectively
is B: Create an S3 Lifecycle configuration to transition objects from S3
Standard to S3 Glacier Deep Archive after 1 month.

Amazon S3 Glacier Deep Archive is a secure, durable, and extremely low-cost
Amazon S3 storage class for long-term retention of data that is rarely accessed
and for which retrieval times of several hours are acceptable. It is the
lowest-cost storage option in Amazon S3, making it a cost-effective choice for
storing backup files that are not accessed after 1 month.

You can use an S3 Lifecycle configuration to automatically transition objects
from S3 Standard to S3 Glacier Deep Archive after 1 month. This will minimize
the storage costs for the backup files that are not accessed frequently.

Option A, configuring S3 Intelligent-Tiering to automatically migrate
objects, is not a good choice because it is not designed for long-term storage
and does not offer the cost benefits of S3 Glacier Deep Archive.

Option C, transitioning objects from S3 Standard to S3 Standard-Infrequent
Access (S3 Standard-IA) after 1 month, is not a good choice because it is not
the lowest-cost storage option and would not provide the cost benefits of S3
Glacier Deep Archive.

Option D, transitioning objects from S3 Standard to S3 One Zone-Infrequent
Access (S3 One Zone-IA) after 1 month, is not a good choice because it is not
the lowest-cost storage option and would not provide the cost benefits of S3
Glacier Deep Archive.

### 24

A company observes an increase in Amazon EC2 costs in its most recent bill. The
billing team notices unwanted vertical scaling of instance types for a couple of
EC2 instances. A solutions architect needs to create a graph comparing the last
2 months of EC2 costs and perform an in-depth analysis to identify the root
cause of the vertical scaling. How should the solutions architect generate the
information with the LEAST operational overhead?

A. Use AWS Budgets to create a budget report and compare EC2 costs based on
instance types. B. Use Cost Explorer's granular filtering feature to perform an
in-depth analysis of EC2 costs based on instance types. C. Use graphs from the
AWS Billing and Cost Management dashboard to compare EC2 costs based on instance
types for the last 2 months. D. Use AWS Cost and Usage Reports to create a
report and send it to an Amazon S3 bucket. Use Amazon QuickSight with Amazon S3
as a source to generate an interactive graph based on instance types.

### 25

A company is designing an application. The application uses an AWS Lambda
function to receive information through Amazon API Gateway and to store the
information in an Amazon Aurora PostgreSQL database. During the proof-of-concept
stage, the company has to increase the Lambda quotas significantly to handle the
high volumes of data that the company needs to load into the database. A
solutions architect must recommend a new design to improve scalability and
minimize the configuration effort. Which solution will meet these requirements?

- A. Refactor the Lambda function code to Apache Tomcat code that runs on Amazon
  EC2 instances. Connect the database by using native Java Database Connectivity
  (JDBC) drivers.
- B. Change the platform from Aurora to Amazon DynamoDProvision a DynamoDB
  Accelerator (DAX) cluster. Use the DAX client SDK to point the existing
  DynamoDB API calls at the DAX cluster.
- C. Set up two Lambda functions. Configure one function to receive the
  information. Configure the other function to load the information into the
  database. Integrate the Lambda functions by using Amazon Simple Notification
  Service (Amazon SNS).
- D. Set up two Lambda functions. Configure one function to receive the
  information. Configure the other function to load the information into the
  database. Integrate the Lambda functions by using an Amazon Simple Queue
  Service (Amazon SQS) queue.

**answer**

A - refactoring can be a solution, BUT requires a LOT of effort - not the answer
B - DynamoDB is NoSQL and Aurora is SQL, so it requires a DB migration... again
a LOT of effort, so no the answer C and D are similar in structure, but... C
uses SNS, which would notify the 2nd Lambda function... provoking the same
bottleneck... not the solution D uses SQS, so the 2nd lambda function can go to
the queue when responsive to keep with the DB load process. Usually the app
decoupling helps with the performance improvement by distributing load. In this
case, the bottleneck is solved by uses queues... so D is the answer.

### 26

A company needs to review its AWS Cloud deployment to ensure that its Amazon S3
buckets do not have unauthorized configuration changes. What should a solutions
architect do to accomplish this goal?

A. Turn on AWS Config with the appropriate rules. B. Turn on AWS Trusted Advisor
with the appropriate checks. C. Turn on Amazon Inspector with the appropriate
assessment template. D. Turn on Amazon S3 server access logging. Configure
Amazon EventBridge (Amazon Cloud Watch Events).

### 27

A company is launching a new application and will display application metrics on
an Amazon CloudWatch dashboard. The company's product manager needs to access
this dashboard periodically. The product manager does not have an AWS account. A
solutions architect must provide access to the product manager by following the
principle of least privilege. Which solution will meet these requirements?

- A. Share the dashboard from the CloudWatch console. Enter the product
  manager's email address, and complete the sharing steps. Provide a shareable
  link for the dashboard to the product manager.
- B. Create an IAM user specifically for the product manager. Attach the
  CloudWatchReadOnlyAccess AWS managed policy to the user. Share the new login
  credentials with the product manager. Share the browser URL of the correct
  dashboard with the product manager.
- C. Create an IAM user for the company's employees. Attach the ViewOnlyAccess
  AWS managed policy to the IAM user. Share the new login credentials with the
  product manager. Ask the product manager to navigate to the CloudWatch console
  and locate the dashboard by name in the Dashboards section.
- D. Deploy a bastion server in a public subnet. When the product manager
  requires access to the dashboard, start the server and share the RDP
  credentials. On the bastion server, ensure that the browser is configured to
  open the dashboard URL with cached AWS credentials that have appropriate
  permissions to view the dashboard.

---

Share a single dashboard and designate specific email addresses of the people
who can view the dashboard. Each of these users creates their own password that
they must enter to view the dashboard.

### 28 다시보기

A company is migrating applications to AWS. The applications are deployed in
different accounts. The company manages the accounts centrally by using AWS
Organizations. The company's security team needs a single sign-on (SSO) solution
across all the company's accounts. The company must continue managing the users
and groups in its on-premises self-managed Microsoft Active Directory. Which
solution will meet these requirements?

- A. Enable AWS Single Sign-On (AWS SSO) from the AWS SSO console. Create a
  one-way forest trust or a one-way domain trust to connect the company's
  self-managed Microsoft Active Directory with AWS SSO by using AWS Directory
  Service for Microsoft Active Directory.
- B. Enable AWS Single Sign-On (AWS SSO) from the AWS SSO console. Create a
  two-way forest trust to connect the company's self-managed Microsoft Active
  Directory with AWS SSO by using AWS Directory Service for Microsoft Active
  Directory.
- C. Use AWS Directory Service. Create a two-way trust relationship with the
  company's self-managed Microsoft Active Directory.
- D. Deploy an identity provider (IdP) on premises. Enable AWS Single Sign-On
  (AWS SSO) from the AWS SSO console.

### 29

A company provides a Voice over Internet Protocol (VoIP) service that uses UDP
connections. The service consists of Amazon EC2 instances that run in an Auto
Scaling group. The company has deployments across multiple AWS Regions. The
company needs to route users to the Region with the lowest latency. The company
also needs automated failover between Regions. Which solution will meet these
requirements?

- A. Deploy a Network Load Balancer (NLB) and an associated target group.
  Associate the target group with the Auto Scaling group. Use the NLB as an AWS
  Global Accelerator endpoint in each Region.
- B. Deploy an Application Load Balancer (ALB) and an associated target group.
  Associate the target group with the Auto Scaling group. Use the ALB as an AWS
  Global Accelerator endpoint in each Region.
- C. Deploy a Network Load Balancer (NLB) and an associated target group.
  Associate the target group with the Auto Scaling group. Create an Amazon Route
  53 latency record that points to aliases for each NLB. Create an Amazon
  CloudFront distribution that uses the latency record as an origin.
- D. Deploy an Application Load Balancer (ALB) and an associated target group.
  Associate the target group with the Auto Scaling group. Create an Amazon Route
  53 weighted record that points to aliases for each ALB. Deploy an Amazon
  CloudFront distribution that uses the weighted record as an origin.

### 30

A development team runs monthly resource-intensive tests on its general purpose
Amazon RDS for MySQL DB instance with Performance Insights enabled. The testing
lasts for 48 hours once a month and is the only process that uses the database.
**The team wants to reduce the cost of running the tests without reducing the
compute and memory attributes of the DB instance.** Which solution meets these
requirements MOST cost-effectively?

- A. Stop the DB instance when tests are completed. Restart the DB instance when
  required.
- B. Use an Auto Scaling policy with the DB instance to automatically scale when
  tests are completed.
- C. Create a snapshot when tests are completed. Terminate the DB instance and
  restore the snapshot when required.
- D. Modify the DB instance to a low-capacity instance when tests are completed.
  Modify the DB instance again when required.

#### 30 해설

C - Create a manual Snapshot of DB and shift to S3- Standard and Restore form
Manual Snapshot when required.

Not A - By stopping the DB although you are not paying for DB hours you are
still paying for Provisioned IOPs , the storage for Stopped DB is more than
Snapshot of underlying EBS vol. and Automated Back ups . Not D - Is possible but
not MOST cost effective, no need to run the RDS when not needed.

### 31

A company that hosts its web application on AWS wants to ensure all Amazon EC2
instances. Amazon RDS DB instances. and Amazon Redshift clusters are configured
with tags. **The company wants to minimize the effort of configuring and
operating this check.** -> 설정과 운영의 노력을 최소화하고 싶다. -> AWS Config
What should a solutions architect do to accomplish this?

- A. Use AWS Config rules to define and detect resources that are not properly
  tagged.
- B. Use Cost Explorer to display resources that are not properly tagged. Tag
  those resources manually.
- C. Write API calls to check all resources for proper tag allocation.
  Periodically run the code on an EC2 instance.
- D. Write API calls to check all resources for proper tag allocation. Schedule
  an AWS Lambda function through Amazon CloudWatch to periodically run the code.

### 32

A development team needs to host a website that will be accessed by other teams.
The **website contents consist of HTML, CSS, client-side JavaScript, and
images.** -> 정적 웹사이트 -> S3 Which method is the MOST cost-effective for
hosting the website?

- A. Containerize the website and host it in AWS Fargate.
- B. Create an Amazon S3 bucket and host the website there.
- C. Deploy a web server on an Amazon EC2 instance to host the website.
- D. Configure an Application Load Balancer with an AWS Lambda target that uses
  the Express.js framework.

### 33

A company runs an online marketplace web application on AWS. The application
serves hundreds of thousands of users during peak hours. The company needs a
scalable, near-real-time solution to share the details of millions of financial
transactions with several other internal applications. **Transactions also need
to be processed to remove sensitive data before being stored in a document
database for low-latency retrieval.** What should a solutions architect
recommend to meet these requirements?

- A. Store the transactions data into Amazon DynamoDB. Set up a rule in DynamoDB
  to remove sensitive data from every transaction upon write. Use DynamoDB
  Streams to share the transactions data with other applications.
- B. Stream the transactions data into Amazon Kinesis Data Firehose to store
  data in Amazon DynamoDB and Amazon S3. Use AWS Lambda integration with Kinesis
  Data Firehose to remove sensitive data. Other applications can consume the
  data stored in Amazon S3.
- C. Stream the transactions data into Amazon Kinesis Data Streams. Use AWS
  Lambda integration to remove sensitive data from every transaction and then
  store the transactions data in Amazon DynamoDB. Other applications can consume
  the transactions data off the Kinesis data stream.
- D. Store the batched transactions data in Amazon S3 as files. Use AWS Lambda
  to process every file and remove sensitive data before updating the files in
  Amazon S3. The Lambda function then stores the data in Amazon DynamoDB. Other
  applications can consume transaction files stored in Amazon S3.

#### 33 해설

- **Amazon Kinensis Data Firehose** is a fully managed service for delivering
  real-time streaming data to destinations such as Amazon Simple Storage Service
  (Amazon S3), Amazon Redshift, Amazon Elasticsearch Service (Amazon ES), and
  Splunk. -> DynamoDB를 지원하지 않음

- **Amazon Kinensis Data Streams** is a massively scalable and durable real-time
  data streaming service. You can continuously collect gigabytes of data per
  second from hundreds of thousands of sources such as website clickstreams,
  database event streams, financial transactions, social media feeds, IT logs,
  and location-tracking events.

### 34

A company hosts its **multi-tier applications on AWS.** For compliance,
governance, auditing, and security, **the company must track configuration
changes on its AWS resources and record a history of API calls made to these
resources.** What should a solutions architect do to meet these requirements?

- A. Use AWS CloudTrail to track configuration changes and AWS Config to record
  API calls.
- B. Use AWS Config to track configuration changes and AWS CloudTrail to record
  API calls.
- C. Use AWS Config to track configuration changes and Amazon CloudWatch to
  record API calls.
- D. Use AWS CloudTrail to track configuration changes and Amazon CloudWatch to
  record API calls.

### 35

A company is preparing to launch a public-facing web application in the AWS
Cloud. The architecture consists of Amazon EC2 instances within a VPC behind an
Elastic Load Balancer (ELB). A third-party service is used for the DNS. The
company's solutions architect must recommend a solution to detect and protect
against large-scale DDoS attacks. Which solution meets these requirements?

- A. Enable Amazon GuardDuty on the account.
- B. Enable Amazon Inspector on the EC2 instances.
- C. Enable AWS Shield and assign Amazon Route 53 to it.
- D. Enable AWS Shield Advanced and assign the ELB to it.

### 36

A company is building an application in the AWS Cloud. The application will
store data in Amazon S3 buckets in two AWS Regions. The company must use an AWS
Key Management Service (AWS KMS) customer managed key to encrypt all data that
is stored in the S3 buckets. The data in both S3 buckets must be encrypted and
decrypted with the same KMS key. The data and the key must be stored in each of
the two Regions. Which solution will meet these requirements with the LEAST
operational overhead?

- A. Create an S3 bucket in each Region. Configure the S3 buckets to use
  server-side encryption with Amazon S3 managed encryption keys (SSE-S3).
  Configure replication between the S3 buckets.
- B. Create a customer managed multi-Region KMS key. Create an S3 bucket in each
  Region. Configure replication between the S3 buckets. Configure the
  application to use the KMS key with client-side encryption.
- C. Create a customer managed KMS key and an S3 bucket in each Region.
  Configure the S3 buckets to use server-side encryption with Amazon S3 managed
  encryption keys (SSE-S3). Configure replication between the S3 buckets.
- D. Create a customer managed KMS key and an S3 bucket in each Region.
  Configure the S3 buckets to use server-side encryption with AWS KMS keys
  (SSE-KMS). Configure replication between the S3 buckets.

### 37

A company recently launched a variety of new workloads on Amazon EC2 instances
in its AWS account. The company needs **to create a strategy to access and
administer the instances remotely and securely.** The company needs to implement
a repeatable process that works with native AWS services and follows the AWS
Well-Architected Framework. Which solution will meet these requirements with the
LEAST operational overhead?

- A. Use the EC2 serial console to directly access the terminal interface of
  each instance for administration.
- B. Attach the appropriate IAM role to each existing instance and new instance.
  Use AWS Systems Manager Session Manager to establish a remote SSH session.
- C. Create an administrative SSH key pair. Load the public key into each EC2
  instance. Deploy a bastion host in a public subnet to provide a tunnel for
  administration of each instance.
- D. Establish an AWS Site-to-Site VPN connection. Instruct administrators to
  use their local on-premises machines to connect directly to the instances by
  using SSH keys across the VPN tunnel.

#### 37 해설

B - AWS Systems Manager Session Manager is a fully managed AWS Systems Manager
capability that lets you manage your Amazon EC2 instances through an interactive
one-click browser-based shell or through the AWS CLI. Session Manager provides
secure and auditable instance management without the need to open inbound ports,
maintain bastion hosts, or manage SSH keys.

### 38

A company is hosting a static website on Amazon S3 and is using Amazon Route 53
for DNS. The website is experiencing increased demand from around the world. The
company must decrease latency for users who access the website. Which solution
meets these requirements MOST cost-effectively?

- A. Replicate the S3 bucket that contains the website to all AWS Regions. Add
  Route 53 geolocation routing entries.
- B. Provision accelerators in AWS Global Accelerator. Associate the supplied IP
  addresses with the S3 bucket. Edit the Route 53 entries to point to the IP
  addresses of the accelerators.
- C. Add an Amazon CloudFront distribution in front of the S3 bucket. Edit the
  Route 53 entries to point to the CloudFront distribution. D. Enable S3
  Transfer Acceleration on the bucket. Edit the Route 53 entries to point to the
  new endpoint.

#### 38 해설

C - Amazon CloudFront is a fast content delivery network (CDN) service that
securely delivers data, videos, applications, and APIs to customers globally
with low latency, high transfer speeds, all within a developer-friendly
environment. CloudFront is integrated with AWS – both physical locations that
are directly connected to the AWS global infrastructure, as well as other AWS
services. CloudFront works seamlessly with services including AWS Shield for
DDoS mitigation, Amazon S3, Elastic Load Balancing or Amazon EC2 as origins for
your applications, and Lambda@Edge to run custom code closer to customers’ users
and to customize the user experience. Lastly, if you use AWS origins such as
Amazon S3, Amazon EC2 or Elastic Load Balancing, you don’t pay for any data
transferred between these services and CloudFront.

### 39

A company maintains a searchable repository of items on its website. The data is
stored in an Amazon RDS for MySQL database table that contains more than 10
million rows. The database has 2 TB of General Purpose SSD storage. There are
millions of updates against this data every day through the company's website.
The company has noticed that some insert operations are taking 10 seconds or
longer. The company has determined **that the database storage performance is
the problem.** Which solution addresses this performance issue?

- A. Change the storage type to Provisioned IOPS SSD.
- B. Change the DB instance to a memory optimized instance class.
- C. Change the DB instance to a burstable performance instance class.
- D. Enable Multi-AZ RDS read replicas with MySQL native asynchronous
  replication.

A: Made for high levels of I/O opps for consistent, predictable performance. B:
Can improve performance of insert opps, but it's a storage performance rather
than processing power problem C: for moderate CPU usage D: for scale read-only
replicas and doesn't improve performance of insert opps on the primary DB
instance

#### 39 해설

provisioned IOPS SSD volumes are designed to meet the needs of I/O-intensive
workloads, particularly database workloads, **that are sensitive to storage
performance and consistency in random access I/O throughput.** Provisioned IOPS
SSD volumes are designed to deliver within 10% of the provisioned IOPS
performance 99.9% of the time. Provisioned IOPS SSD volumes are also designed to
support bursts of I/O activity. This means that most database workloads, which
are typically bursty, can use provisioned IOPS SSD volumes effectively.

### 40

A company has thousands of edge devices that collectively generate 1 TB of
status alerts each day. Each alert is approximately 2 KB in size. A solutions
architect needs to implement a solution to ingest and store the alerts for
future analysis. The company wants a highly available solution. However, the
company needs to minimize costs and does not want to manage additional
infrastructure. Additionally, the company wants to keep 14 days of data
available for immediate analysis and archive any data older than 14 days. What
is the MOST operationally efficient solution that meets these requirements?

- A. Create an Amazon Kinesis Data Firehose delivery stream to ingest the
  alerts. Configure the Kinesis Data Firehose stream to deliver the alerts to an
  Amazon S3 bucket. Set up an S3 Lifecycle configuration to transition data to
  Amazon S3 Glacier after 14 days.
- B. Launch Amazon EC2 instances across two Availability Zones and place them
  behind an Elastic Load Balancer to ingest the alerts. Create a script on the
  EC2 instances that will store the alerts in an Amazon S3 bucket. Set up an S3
  Lifecycle configuration to transition data to Amazon S3 Glacier after 14 days.
- C. Create an Amazon Kinesis Data Firehose delivery stream to ingest the
  alerts. Configure the Kinesis Data Firehose stream to deliver the alerts to an
  Amazon OpenSearch Service (Amazon Elasticsearch Service) cluster. Set up the
  Amazon OpenSearch Service (Amazon Elasticsearch Service) cluster to take
  manual snapshots every day and delete data from the cluster that is older than
  14 days.
- D. Create an Amazon Simple Queue Service (Amazon SQS) standard queue to ingest
  the alerts, and set the message retention period to 14 days. Configure
  consumers to poll the SQS queue, check the age of the message, and analyze the
  message data as needed. If the message is 14 days old, the consumer should
  copy the message to an Amazon S3 bucket and delete the message from the SQS
  queue.

#### 40 해설

Amazon Kinesis Data Firehose is the easiest way to reliably load streaming data
into data lakes, data stores, and analytics services. It can capture, transform,
and load streaming data into Amazon S3, Amazon Redshift, Amazon Elasticsearch
Service, and Splunk, enabling near real-time analytics with existing business
intelligence tools and dashboards you’re already using today. It is a fully
managed service that automatically scales to match the throughput of your data
and requires no ongoing administration. It can also batch, compress, and encrypt
the data before loading it, minimizing the amount of storage used at the
destination and increasing security.

### 41

**A company's application integrates with multiple software-as-a-service (SaaS)
sources for data collection. The company runs Amazon EC2 instances to receive
the data and to upload the data to an Amazon S3 bucket for analysis.** **The
same EC2 instance that receives and uploads the data also sends a notification
to the user when an upload is complete. The company has noticed slow application
performance and wants to improve the performance as much as possible.** Which
solution will meet these requirements with the LEAST operational overhead?

- A. Create an Auto Scaling group so that EC2 instances can scale out. Configure
  an S3 event notification to send events to an Amazon Simple Notification
  Service (Amazon SNS) topic when the upload to the S3 bucket is complete.
- B. Create an Amazon AppFlow flow to transfer data between each SaaS source and
  the S3 bucket. Configure an S3 event notification to send events to an Amazon
  Simple Notification Service (Amazon SNS) topic when the upload to the S3
  bucket is complete.
- C. Create an Amazon EventBridge (Amazon CloudWatch Events) rule for each SaaS
  source to send output data. Configure the S3 bucket as the rule's target.
  Create a second EventBridge (Cloud Watch Events) rule to send events when the
  upload to the S3 bucket is complete. Configure an Amazon Simple Notification
  Service (Amazon SNS) topic as the second rule's target.
- D. Create a Docker container to use instead of an EC2 instance. Host the
  containerized application on Amazon Elastic Container Service (Amazon ECS).
  Configure Amazon CloudWatch Container Insights to send events to an Amazon
  Simple Notification Service (Amazon SNS) topic when the upload to the S3
  bucket is complete.

#### 41 해설

B Amazon AppFlow is a fully managed integration service that enables you to
securely transfer data between Software-as-a-Service (SaaS) applications like
Salesforce, Marketo, Slack, and ServiceNow, and AWS services like Amazon S3 and
Amazon Redshift, in just a few clicks. With AppFlow, you can use pre-built
connectors to third-party applications to create integrations called flows.
These flows can transfer data bi-directionally between applications, without
writing custom integration code.

### 42

A company runs a highly available image-processing application on Amazon EC2
instances in a single VPC. The EC2 instances run inside several subnets across
multiple Availability Zones. The EC2 instances do not communicate with each
other. However, the EC2 instances download images from Amazon S3 and upload
images to Amazon S3 through a single NAT gateway. The company is concerned about
data transfer charges. What is the MOST cost-effective way for the company to
avoid Regional data transfer charges?

- A. Launch the NAT gateway in each Availability Zone.
- B. Replace the NAT gateway with a NAT instance.
- C. Deploy a gateway VPC endpoint for Amazon S3.
- D. Provision an EC2 Dedicated Host to run the EC2 instance

#### 42 해설

C - **A gateway VPC endpoint is a gateway that you specify as a target for a
route in your route table for traffic destined to a supported AWS service.
Gateway endpoints support services such as Amazon S3 and DynamoDB. Gateway
endpoints are available in all AWS Regions.**

### 43

A company has an on-premises application that generates a large amount of
time-sensitive data that is backed up to Amazon S3. The application has grown
and there are user complaints about internet bandwidth limitations. A solutions
architect needs to design a long-term solution that allows for both timely
backups to Amazon S3 and with minimal impact on internet connectivity for
internal users. Which solution meets these requirements?

- A. Establish AWS VPN connections and proxy all traffic through a VPC gateway
  endpoint.
- B. Establish a new AWS Direct Connect connection and direct backup traffic
  through this new connection.
- C. Order daily AWS Snowball devices. Load the data onto the Snowball devices
  and return the devices to AWS each day.
- D. Submit a support ticket through the AWS Management Console. Request the
  removal of S3 service limits from the account.

### 44

A company has an Amazon S3 bucket that contains critical data. The company must
protect the data from accidental deletion. Which combination of steps should a
solutions architect take to meet these requirements? (Choose two.)

- A. Enable versioning on the S3 bucket.
- B. Enable MFA Delete on the S3 bucket.
- C. Create a bucket policy on the S3 bucket.
- D. Enable default encryption on the S3 bucket.
- E. Create a lifecycle policy for the objects in the S3 bucket.

### 45

A company has a data ingestion workflow that consists of the following: • An
Amazon Simple Notification Service (Amazon SNS) topic for notifications about
new data deliveries • An AWS Lambda function to process the data and record
metadata The company observes that the ingestion workflow fails occasionally
because of network connectivity issues. When such a failure occurs, the Lambda
function does not ingest the corresponding data unless the company manually
reruns the job. Which combination of actions should a solutions architect take
to ensure that the Lambda function ingests all data in the future? (Choose two.)

- A. Deploy the Lambda function in multiple Availability Zones.
- B. Create an Amazon Simple Queue Service (Amazon SQS) queue, and subscribe it
  to the SNS topic. Most Voted
- C. Increase the CPU and memory that are allocated to the Lambda function.
- D. Increase provisioned throughput for the Lambda function.
- E. Modify the Lambda function to read from an Amazon Simple Queue Service
  (Amazon SQS) queue. Most Voted

### 46

A company has an application that provides marketing services to stores. The
services are based on previous purchases by store customers. The stores upload
transaction data to the company through SFTP, and the data is processed and
analyzed to generate new marketing offers. Some of the files can exceed 200 GB
in size. Recently, the company discovered that some of the stores have uploaded
files that contain personally identifiable information (PII) that should not
have been included. The company wants administrators to be alerted if PII is
shared again. The company also wants to automate remediation. What should a
solutions architect do to meet these requirements with the LEAST development
effort?

- A. Use an Amazon S3 bucket as a secure transfer point. Use Amazon Inspector to
  scan the objects in the bucket. If objects contain PII, trigger an S3
  Lifecycle policy to remove the objects that contain PII.
- B. Use an Amazon S3 bucket as a secure transfer point. Use Amazon Macie to
  scan the objects in the bucket. If objects contain PII, use Amazon Simple
  Notification Service (Amazon SNS) to trigger a notification to the
  administrators to remove the objects that contain PII.
- C. Implement custom scanning algorithms in an AWS Lambda function. Trigger the
  function when objects are loaded into the bucket. If objects contain PII, use
  Amazon Simple Notification Service (Amazon SNS) to trigger a notification to
  the administrators to remove the objects that contain PII.
- D. Implement custom scanning algorithms in an AWS Lambda function. Trigger the
  function when objects are loaded into the bucket. If objects contain PII, use
  Amazon Simple Email Service (Amazon SES) to trigger a notification to the
  administrators and trigger an S3 Lifecycle policy to remove the meats that
  contain PI

### 47

A company needs guaranteed Amazon EC2 capacity in three specific Availability
Zones in a specific AWS Region for an upcoming event that will last 1 week. What
should the company do to **guarantee the EC2 capacity?**

A. Purchase Reserved Instances that specify the Region needed. B. Create an
On-Demand Capacity Reservation that specifies the Region needed. C. Purchase
Reserved Instances that specify the Region and three Availability Zones needed.
D. Create an On-Demand Capacity Reservation that specifies the Region and three
Availability Zones needed.

### 48

A company's website uses an **Amazon EC2 instance store** for its catalog of
items. The company wants to make sure that the catalog is highly available and
that the catalog is stored in a durable location. What should a solutions
architect do to meet these requirements?

- A. Move the catalog to Amazon ElastiCache for Redis.
- B. Deploy a larger EC2 instance with a larger instance store.
- C. Move the catalog from the instance store to Amazon S3 Glacier Deep Archive.
- D. Move the catalog to an Amazon Elastic File System (Amazon EFS) file system.

### 49

A company stores call transcript files on a monthly basis. Users access the
files randomly within 1 year of the call, but users access the files
infrequently after 1 year. The company wants to optimize its solution by giving
users the ability to query and retrieve files that are less than 1-year-old as
quickly as possible. A delay in retrieving older files is acceptable. Which
solution will meet these requirements MOST cost-effectively?

- A. Store individual files with tags in Amazon S3 Glacier Instant Retrieval.
  Query the tags to retrieve the files from S3 Glacier Instant Retrieval.
- B. Store individual files in Amazon S3 Intelligent-Tiering. Use S3 Lifecycle policies to
  move the files to S3 Glacier Flexible Retrieval after 1 year. Query and retrieve
  the files that are in Amazon S3 by using Amazon Athena. Query and retrieve the
  files that are in S3 Glacier by using S3 Glacier Select.
- C. Store individual files with tags in Amazon S3 Standard storage. Store search metadata for each
  archive in Amazon S3 Standard storage. Use S3 Lifecycle policies to move the
  files to S3 Glacier Instant Retrieval after 1 year. Query and retrieve the files
  by searching for metadata from Amazon S3.
- D. Store individual files in Amazon S3 Standard storage. Use S3 Lifecycle policies to move the files to S3 Glacier Deep
  Archive after 1 year. Store search metadata in Amazon RDS. Query the files from
  Amazon RDS. Retrieve the files from S3 Glacier Deep Archive.

### 50

A company has a production workload that runs on 1,000 Amazon EC2 Linux
instances. The workload is powered by third-party software. The company needs to
patch the third-party software on all EC2 instances as quickly as possible to
remediate a critical security vulnerability. What should a solutions architect
do to meet these requirements?

- A. Create an AWS Lambda function to apply the patch to all EC2 instances.
- B.Configure AWS Systems Manager Patch Manager to apply the patch to all EC2
  instances.
- C. Schedule an AWS Systems Manager maintenance window to apply the
  patch to all EC2 instances.
- D. Use AWS Systems Manager Run Command to run a
  custom command that applies the patch to all EC2 instances.

### 51

A company is developing an application that provides order shipping statistics
for retrieval by a REST API. The company wants to extract the shipping
statistics, organize the data into an easy-to-read HTML format, and send the
report to several email addresses at the same time every morning. Which
combination of steps should a solutions architect take to meet these
requirements? (Choose two.)

- A. Configure the application to send the data to Amazon Kinesis Data Firehose.
- B. Use Amazon Simple Email Service (Amazon SES) to format the data and to send
  the report by email.
- C. Create an Amazon EventBridge (Amazon CloudWatch Events)
  scheduled event that invokes an AWS Glue job to query the application's API for
  the data.
- D. Create an Amazon EventBridge (Amazon CloudWatch Events) scheduled
  event that invokes an AWS Lambda function to query the application's API for the
  data.
- E. Store the application data in Amazon S3. Create an Amazon Simple
  Notification Service (Amazon SNS) topic as an S3 event destination to send the
  report by email.

### 52

A company wants to migrate its on-premises application to AWS. The application
produces output files that vary in size from tens of gigabytes to hundreds of
terabytes. The application data must be stored in a standard file system
structure. The company wants a solution that scales automatically. is highly
available, and requires minimum operational overhead. Which solution will meet
these requirements?

- A. Migrate the application to run as containers on Amazon Elastic Container
  Service (Amazon ECS). Use Amazon S3 for storage.
- B. Migrate the application to run as containers on Amazon Elastic Kubernetes Service (Amazon EKS). Use Amazon Elastic Block Store (Amazon EBS) for storage.
- C. Migrate the application to Amazon EC2 instances in a Multi-AZ Auto Scaling group. Use Amazon Elastic File
  System (Amazon EFS) for storage.
- D. Migrate the application to Amazon EC2 instances in a Multi-AZ Auto Scaling group. Use Amazon Elastic Block Store
  (Amazon EBS) for storage.

### 53

A company needs to store its accounting records in Amazon S3. The records must
be immediately accessible for 1 year and then must be archived for an additional
9 years. No one at the company, including administrative users and root users,
can be able to delete the records during the entire 10-year period. The records
must be stored with maximum resiliency. Which solution will meet these
requirements?

- A. Store the records in S3 Glacier for the entire 10-year period. Use an access
  control policy to deny deletion of the records for a period of 10 years.
- B.Store the records by using S3 Intelligent-Tiering. Use an IAM policy to deny
  deletion of the records. After 10 years, change the IAM policy to allow
  deletion.
- C. Use an S3 Lifecycle policy to transition the records from S3 Standard to S3 Glacier Deep Archive after 1 year. Use S3 Object Lock in
  compliance mode for a period of 10 years.
- D. Use an S3 Lifecycle policy to transition the records from S3 Standard to S3 One Zone-Infrequent Access (S3 One
  Zone-IA) after 1 year. Use S3 Object Lock in governance mode for a period of 10
  years.

### 54

A company runs multiple Windows workloads on AWS. The company's employees use
Windows file shares that are hosted on two Amazon EC2 instances. The file shares
synchronize data between themselves and maintain duplicate copies. The company
wants a highly available and durable storage solution that preserves how users
currently access the files. What should a solutions architect do to meet these
requirements?

- A. Migrate all the data to Amazon S3. Set up IAM authentication for users to
  access files.
- B. Set up an Amazon S3 File Gateway. Mount the S3 File Gateway on the existing EC2 instances.
- C. Extend the file share environment to Amazon FSx for Windows File Server with a Multi-AZ configuration. Migrate all the data to
  FSx for Windows File Server.
- D. Extend the file share environment to Amazon Elastic File System (Amazon EFS) with a Multi-AZ configuration. Migrate all the
  data to Amazon EFS.

### 55

A solutions architect is developing a VPC architecture that includes multiple
subnets. The architecture will host applications that use Amazon EC2 instances
and Amazon RDS DB instances. The architecture consists of six subnets in two
Availability Zones. Each Availability Zone includes a public subnet, a private
subnet, and a dedicated subnet for databases. **Only EC2 instances that run in
the private subnets can have access to the RDS databases.** Which solution will
meet these requirements?

- A. Create a new route table that excludes the route to the public subnets' CIDR
  blocks. Associate the route table with the database subnets.
- B. Create a security group that denies inbound traffic from the security group that is
  assigned to instances in the public subnets. Attach the security group to the DB
  instances.
- C. Create a security group that allows inbound traffic from the
  security group that is assigned to instances in the private subnets. Attach the
  security group to the DB instances.
- D. Create a new peering connection between the public subnets and the private subnets. Create a different peering
  connection between the private subnets and the database subnets.

### 56

A company has registered its domain name with Amazon Route 53. The company uses
Amazon API Gateway in the ca-central-1 Region as a public interface for its
backend microservice APIs. Third-party services consume the APIs securely. The
company wants to design its API Gateway URL with the company's domain name and
corresponding certificate so that the third-party services can use HTTPS. Which
solution will meet these requirements?

- A. Create stage variables in API Gateway with Name="Endpoint-URL" and Value="Company Domain Name" to overwrite the default URL. Import the public certificate associated with the company's domain name into AWS Certificate Manager (ACM).

- B. Create Route 53 DNS records with the company's domain name. Point the alias record to the Regional API Gateway stage endpoint. Import the public certificate associated with the company's domain name into AWS Certificate Manager (ACM) in the us-east-1 Region.
- C. Create a Regional API Gateway endpoint. Associate the API Gateway endpoint with the company's domain name. Import the public certificate associated with the company's domain name into AWS Certificate Manager (ACM) in the same Region. Attach the certificate to the API Gateway endpoint. Configure Route 53 to route traffic to the API Gateway endpoint.
- D. Create a Regional API Gateway endpoint. Associate the API Gateway endpoint with the company's domain name. Import the public certificate associated with the company's domain name into AWS Certificate Manager (ACM) in the us-east-1 Region. Attach the certificate to the API Gateway APIs. Create Route 53 DNS records with the company's domain name. Point an A record to the company's domain name.

#### 56 해설

The correct solution to meet these requirements is option C.

To design the API Gateway URL with the company's domain name and corresponding
certificate, the company needs to do the following:

1. Create a Regional API Gateway endpoint: This will allow the company to create
   an endpoint that is specific to a region.

2. Associate the API Gateway endpoint with the company's domain name: This will
   allow the company to use its own domain name for the API Gateway URL.

3. Import the public certificate associated with the company's domain name into
   AWS Certificate Manager (ACM) in the same Region: This will allow the company
   to use HTTPS for secure communication with its APIs.

4. Attach the certificate to the API Gateway endpoint: This will allow the
   company to use the certificate for securing the API Gateway URL.

5. Configure Route 53 to route traffic to the API Gateway endpoint: This will
   allow the company to use Route 53 to route traffic to the API Gateway URL
   using the company's domain name.

### 57

A company is running a popular social media website. The website gives users the
ability to upload images to share with other users. The company wants to make
sure that the images do not contain inappropriate content. The company needs a
solution that minimizes development effort. What should a solutions architect do
to meet these requirements?

- A. Use Amazon Comprehend to detect inappropriate content. Use human review for
  low-confidence predictions.
- B. Use Amazon Rekognition to detect inappropriate content. Use human review for low-confidence predictions.
- C. Use Amazon SageMaker to detect inappropriate content. Use ground truth to label
  low-confidence predictions.
- D. Use AWS Fargate to deploy a custom machine learning model to detect inappropriate content. Use ground truth to label
  low-confidence predictions.

### 58

A company wants to run its critical applications in containers to meet
requirements for scalability and availability. The company prefers to focus on
maintenance of the critical applications. The company does not want to be
responsible for provisioning and managing the underlying infrastructure that
runs the containerized workload. What should a solutions architect do to meet
these requirements?

- A. Use Amazon EC2 instances, and install Docker on the instances.
- B. Use Amazon Elastic Container Service (Amazon ECS) on Amazon EC2 worker nodes.
- C. Use Amazon Elastic Container Service (Amazon ECS) on AWS Fargate.
- D. Use Amazon EC2 instances from an Amazon Elastic Container Service (Amazon ECS)-optimized Amazon
  Machine Image (AMI).

### 59

A company hosts more than 300 global websites and applications. The company
requires a platform to analyze more than 30 TB of clickstream data each day.
What should a solutions architect do to transmit and process the clickstream
data?

- A. Design an AWS Data Pipeline to archive the data to an Amazon S3 bucket and
  run an Amazon EMR cluster with the data to generate analytics.
- B. Create an Auto Scaling group of Amazon EC2 instances to process the data and send it to an
  Amazon S3 data lake for Amazon Redshift to use for analysis.
- C. Cache the data to Amazon CloudFront. Store the data in an Amazon S3 bucket. When an object is
  added to the S3 bucket. run an AWS Lambda function to process the data for analysis.
- D. Collect the data from Amazon Kinesis Data Streams. Use Amazon
  Kinesis Data Firehose to transmit the data to an Amazon S3 data lake. Load the
  data in Amazon Redshift for analysis.

#### 59 해설

Option D is the most appropriate solution for transmitting and processing the
clickstream data in this scenario.

Amazon Kinesis Data Streams is a highly scalable and durable service that
enables real-time processing of streaming data at a high volume and high rate.
You can use Kinesis Data Streams to collect and process the clickstream data in
real-time.

Amazon Kinesis Data Firehose is a fully managed service that loads streaming
data into data stores and analytics tools. You can use Kinesis Data Firehose to
transmit the data from Kinesis Data Streams to an Amazon S3 data lake.

Once the data is in the data lake, you can use Amazon Redshift to load the data
and perform analysis on it. Amazon Redshift is a fully managed, petabyte-scale
data warehouse service that allows you to quickly and efficiently analyze data
using SQL and your existing business intelligence tools.

### 60

A company has a website hosted on AWS. The website is behind an Application Load
Balancer (ALB) that is configured to handle HTTP and HTTPS separately. The
company wants to forward all requests to the website so that the requests will
use HTTPS. What should a solutions architect do to meet this requirement?

- A. Update the ALB's network ACL to accept only HTTPS traffic.
- B. Create a rule that replaces the HTTP in the URL with HTTPS.
- C. Create a listener rule on the ALB to redirect HTTP traffic to HTTPS.
- D. Replace the ALB with a Network Load Balancer configured to use Server Name Indication (SNI).

#### 60 해설

-> Create a listener rule on the ALB to redirect HTTP traffic to HTTPS.

### 61

A company is developing a two-tier web application on AWS. The company's
developers have deployed the application on an Amazon EC2 instance that connects
directly to a backend Amazon RDS database. The company must not hardcode
database credentials in the application. The company must also implement a
solution to automatically rotate the database credentials on a regular basis.
Which solution will meet these requirements with the LEAST operational overhead?

- A. Store the database credentials in the instance metadata. Use Amazon
  EventBridge (Amazon CloudWatch Events) rules to run a scheduled AWS Lambda
  function that updates the RDS credentials and instance metadata at the same
  time.
- B. Store the database credentials in a configuration file in an encrypted
  Amazon S3 bucket. Use Amazon EventBridge (Amazon CloudWatch Events) rules to run
  a scheduled AWS Lambda function that updates the RDS credentials and the
  credentials in the configuration file at the same time. Use S3 Versioning to
  ensure the ability to fall back to previous values.
- C. Store the database credentials as a secret in AWS Secrets Manager. Turn on automatic rotation for
  the secret. Attach the required permission to the EC2 role to grant access to
  the secret.
- D. Store the database credentials as encrypted parameters in AWS
  Systems Manager Parameter Store. Turn on automatic rotation for the encrypted
  parameters. Attach the required permission to the EC2 role to grant access to
  the encrypted parameters.

### 62

A company is deploying a new public web application to AWS. The application will
run behind an Application Load Balancer (ALB). The application needs to be
encrypted at the edge with an SSL/TLS certificate that is issued by an external
certificate authority (CA). The certificate must be rotated each year before the
certificate expires. What should a solutions architect do to meet these
requirements?

- A. Use AWS Certificate Manager (ACM) to issue an SSL/TLS certificate. Apply the
  certificate to the ALB. Use the managed renewal feature to automatically rotate
  the certificate.
- B. Use AWS Certificate Manager (ACM) to issue an SSL/TLS
  certificate. Import the key material from the certificate. Apply the certificate
  to the ALUse the managed renewal feature to automatically rotate the
  certificate.
- C. Use AWS Certificate Manager (ACM) Private Certificate Authority
  to issue an SSL/TLS certificate from the root CA. Apply the certificate to the
  ALB. Use the managed renewal feature to automatically rotate the certificate.
- D.Use AWS Certificate Manager (ACM) to import an SSL/TLS certificate. Apply the
  certificate to the ALB. Use Amazon EventBridge (Amazon CloudWatch Events) to
  send a notification when the certificate is nearing expiration. Rotate the
  certificate manually.

#### 62 해설

It is D, because **ACM does not manage the renewal process for imported
certificates.** You are responsible for monitoring the expiration date of your
imported certificates and for renewing them before they expire. Check this
question on the link below: Q: What types of certificates can I create and
manage with ACM?
https://www.amazonaws.cn/en/certificate-manager/faqs/#Managed_renewal_and_deployment

### 63

A company runs its infrastructure on AWS and has a registered base of 700,000
users for its document management application. The company intends to create a
product that converts large .pdf files to .jpg image files. The .pdf files
average 5 MB in size. The company needs to store the original files and the
converted files. A solutions architect must design a scalable solution to
accommodate demand that will grow rapidly over time. Which solution meets these
requirements MOST cost-effectively?

- A. Save the .pdf files to Amazon S3. Configure an S3 PUT event to invoke an AWS
  Lambda function to convert the files to .jpg format and store them back in
  Amazon S3.
- B. Save the .pdf files to Amazon DynamoDUse the DynamoDB Streams feature to invoke an AWS Lambda function to convert the files to .jpg format and
  store them back in DynamoDB.
- C. Upload the .pdf files to an AWS Elastic Beanstalk application that includes Amazon EC2 instances, Amazon Elastic Block
  Store (Amazon EBS) storage, and an Auto Scaling group. Use a program in the EC2
  instances to convert the files to .jpg format. Save the .pdf files and the .jpg
  files in the EBS store.
- D. Upload the .pdf files to an AWS Elastic Beanstalk application that includes Amazon EC2 instances, Amazon Elastic File System
  (Amazon EFS) storage, and an Auto Scaling group. Use a program in the EC2
  instances to convert the file to .jpg format. Save the .pdf files and the .jpg
  files in the EBS store.

### 64 다시보기

A company has more than 5 TB of file data on Windows file servers that run on
premises. Users and applications interact with the data each day. The company is
moving its Windows workloads to AWS. As the company continues this process, the
company requires access to AWS and on-premises file storage with minimum
latency. The company needs a solution that minimizes operational overhead and
requires no significant changes to the existing file access patterns. The
company uses an AWS Site-to-Site VPN connection for connectivity to AWS. What
should a solutions architect do to meet these requirements?

- A. Deploy and configure Amazon FSx for Windows File Server on AWS. Move the
  on-premises file data to FSx for Windows File Server. Reconfigure the workloads
  to use FSx for Windows File Server on AWS.
- B. Deploy and configure an Amazon S3 File Gateway on premises. Move the on-premises file data to the S3 File Gateway.
  Reconfigure the on-premises workloads and the cloud workloads to use the S3 File
  Gateway.
- C. Deploy and configure an Amazon S3 File Gateway on premises. Move the
  on-premises file data to Amazon S3. Reconfigure the workloads to use either
  Amazon S3 directly or the S3 File Gateway. depending on each workload's
  location.
- D. Deploy and configure Amazon FSx for Windows File Server on AWS.
  Deploy and configure an Amazon FSx File Gateway on premises. Move the
  on-premises file data to the FSx File Gateway. Configure the cloud workloads to
  use FSx for Windows File Server on AWS. Configure the on-premises workloads to
  use the FSx File Gateway.

### 65

A hospital recently deployed a RESTful API with Amazon API Gateway and AWS
Lambda. The hospital uses API Gateway and Lambda to upload reports that are in
PDF format and JPEG format. The hospital needs to modify the Lambda code to
identify protected health information (PHI) in the reports. Which solution will
meet these requirements with the LEAST operational overhead?

- A. Use existing Python libraries to extract the text from the reports and to
  identify the PHI from the extracted text.
- B. Use Amazon Textract to extract the text from the reports. Use Amazon SageMaker to identify the PHI from the
  extracted text.
- C. Use Amazon Textract to extract the text from the reports. Use Amazon Comprehend Medical to identify the PHI from the extracted text.
- D. Use Amazon Rekognition to extract the text from the reports. Use Amazon Comprehend
  Medical to identify the PHI from the extracted text.

### 66

A company has an application that generates a large number of files, each
approximately 5 MB in size. The files are stored in Amazon S3. Company policy
requires the files to be stored for 4 years before they can be deleted.
**Immediate accessibility is always required as the files contain critical
business data that is not easy to reproduce**. The files are frequently accessed
in the first 30 days of the object creation but are rarely accessed after the
first 30 days. Which storage solution is MOST cost-effective?

- A. Create an S3 bucket lifecycle policy to move files from S3 Standard to S3
  Glacier 30 days from object creation. Delete the files 4 years after object
  creation.
- B. Create an S3 bucket lifecycle policy to move files from S3 Standard
  to S3 One Zone-Infrequent Access (S3 One Zone-IA) 30 days from object creation.
  Delete the files 4 years after object creation.
- C. Create an S3 bucket lifecycle policy to move files from S3 Standard to S3 Standard-Infrequent Access (S3
  Standard-IA) 30 days from object creation. Delete the files 4 years after object
  creation.
- D. Create an S3 bucket lifecycle policy to move files from S3 Standard
  to S3 Standard-Infrequent Access (S3 Standard-IA) 30 days from object creation.
  Move the files to S3 Glacier 4 years after object creation.

### 67

A company hosts an application on multiple Amazon EC2 instances. The application
processes messages from an Amazon SQS queue, writes to an Amazon RDS table, and
deletes the message from the queue. Occasional duplicate records are found in
the RDS table. The SQS queue does not contain any duplicate messages. What
should a solutions architect do to ensure messages are being processed once
only?

- A. Use the CreateQueue API call to create a new queue.
- B. Use the AddPermission API call to add appropriate permissions.
- C. Use the ReceiveMessage API call to set an appropriate wait time.
- D. Use the ChangeMessageVisibility API call to increase the visibility timeout.

### 68

A solutions architect is designing a new hybrid architecture to extend a
company's on-premises infrastructure to AWS. The company requires a highly
available connection with consistent low latency to an AWS Region. The company
needs to minimize costs and is willing to accept slower traffic if the primary
connection fails. What should the solutions architect do to meet these
requirements?

- A. Provision an AWS Direct Connect connection to a Region. Provision a VPN
  connection as a backup if the primary Direct Connect connection fails. Most
  Voted

- B. Provision a VPN tunnel connection to a Region for private connectivity.
  Provision a second VPN tunnel for private connectivity and as a backup if the
  primary VPN connection fails.
- C. Provision an AWS Direct Connect connection to a Region. Provision a second Direct Connect connection to the same Region as a
  backup if the primary Direct Connect connection fails.
- D. Provision an AWS Direct Connect connection to a Region. Use the Direct Connect failover attribute
  from the AWS CLI to automatically create a backup connection if the primary
  Direct Connect connection fails.

#### 68 해설

Direct Connect is a dedicated network connection from your premises to AWS. It
can be used to establish a private virtual interface from your on-premises
network directly to your VPC. It can also be used to establish a private virtual
interface from your on-premises network to your public resources in AWS. Direct
Connect is a good choice if you have a large amount of traffic that you need to
send to AWS, or if you need a stable and reliable connection. It is also a good
choice if you need to transfer large amounts of data to AWS, such as in a
migration scenario.

### 69

A company is running a business-critical web application on Amazon EC2 instances
behind an Application Load Balancer. The EC2 instances are in an Auto Scaling
group. The application uses an Amazon Aurora PostgreSQL database that is
deployed in a single Availability Zone. **The company wants the application to
be highly available with minimum downtime and minimum loss of data.** Which
solution will meet these requirements with the LEAST operational effort?

A. Place the EC2 instances in different AWS Regions. Use Amazon Route 53 health
checks to redirect traffic. Use Aurora PostgreSQL Cross-Region Replication. B.
Configure the Auto Scaling group to use multiple Availability Zones. Configure
the database as Multi-AZ. Configure an Amazon RDS Proxy instance for the
database. C. Configure the Auto Scaling group to use one Availability Zone.
Generate hourly snapshots of the database. Recover the database from the
snapshots in the event of a failure. D. Configure the Auto Scaling group to use
multiple AWS Regions. Write the data from the application to Amazon S3. Use S3
Event Notifications to launch an AWS Lambda function to write the data to the
database.

### 70

A company's HTTP application is behind a Network Load Balancer (NLB). The NLB's
target group is configured to use an Amazon EC2 Auto Scaling group with multiple
EC2 instances that run the web service. The company notices that the NLB is not
detecting HTTP errors for the application. These errors require a manual restart
of the EC2 instances that run the web service. The company needs to improve the
application's availability without writing custom scripts or code. What should a
solutions architect do to meet these requirements?

A. Enable HTTP health checks on the NLB, supplying the URL of the company's
application. B. Add a cron job to the EC2 instances to check the local
application's logs once each minute. If HTTP errors are detected. the
application will restart. C. Replace the NLB with an Application Load Balancer.
Enable HTTP health checks by supplying the URL of the company's application.
Configure an Auto Scaling action to replace unhealthy instances. Most Voted D.
Create an Amazon Cloud Watch alarm that monitors the UnhealthyHostCount metric
for the NLB. Configure an Auto Scaling action to replace unhealthy instances
when the alarm is in the ALARM state.

NLBs support HTTP, HTTPS and TCP health checks:
https://docs.aws.amazon.com/elasticloadbalancing/latest/network/target-group-health-checks.html
(check HealthCheckProtocol)

But NLBs only accept either selecting EC2 instances or IP addresses directly as
targets. You can't provide a URL to your endpoints, only a health check path (if
you're using HTTP or HTTPS health checks)

### 71

A company runs a shopping application that uses Amazon DynamoDB to store
customer information. In case of data corruption, a solutions architect needs to
design a solution that meets a recovery point objective (RPO) of 15 minutes and
a recovery time objective (RTO) of 1 hour. What should the solutions architect
recommend to meet these requirements?

A. Configure DynamoDB global tables. For RPO recovery, point the application to
a different AWS Region. B. Configure DynamoDB point-in-time recovery. For RPO
recovery, restore to the desired point in time. Most Voted C. Export the
DynamoDB data to Amazon S3 Glacier on a daily basis. For RPO recovery, import
the data from S3 Glacier to DynamoDB. D. Schedule Amazon Elastic Block Store
(Amazon EBS) snapshots for the DynamoDB table every 15 minutes. For RPO
recovery, restore the DynamoDB table by using the EBS snapshot.

### 72

A company runs a photo processing application that needs to frequently upload
and download pictures from Amazon S3 buckets that are located in the same AWS
Region. A solutions architect has noticed an increased cost in data transfer
fees and needs to implement a solution to reduce these costs. How can the
solutions architect meet this requirement?

A. Deploy Amazon API Gateway into a public subnet and adjust the route table to
route S3 calls through it. B. Deploy a NAT gateway into a public subnet and
attach an endpoint policy that allows access to the S3 buckets. C. Deploy the
application into a public subnet and allow it to route through an internet
gateway to access the S3 buckets. D. Deploy an S3 VPC gateway endpoint into the
VPC and attach an endpoint policy that allows access to the S3 buckets

#### 72 해설

By deploying an S3 VPC gateway endpoint, the application can access the S3
buckets over a private network connection within the VPC, eliminating the need
for data transfer over the internet. This can help reduce data transfer fees as
well as improve the performance of the application. The endpoint policy can be
used to specify which S3 buckets the application has access to.

### 73

A company recently launched Linux-based application instances on Amazon EC2 in a
private subnet and launched a Linux-based bastion host on an Amazon EC2 instance
in a public subnet of a VPC. A solutions architect needs to connect from the
on-premises network, through the company's internet connection, to the bastion
host, and to the application servers. The solutions architect must make sure
that the security groups of all the EC2 instances will allow that access. Which
combination of steps should the solutions architect take to meet these
requirements? (Choose two.)

A. Replace the current security group of the bastion host with one that only
allows inbound access from the application instances. B. Replace the current
security group of the bastion host with one that only allows inbound access from
the internal IP range for the company. C. Replace the current security group of
the bastion host with one that only allows inbound access from the external IP
range for the company. D. Replace the current security group of the application
instances with one that allows inbound SSH access from only the private IP
address of the bastion host. E. Replace the current security group of the
application instances with one that allows inbound SSH access from only the
public IP address of the bastion host

#### 73 해설

C because from on-prem network to bastion through internet (using on-prem
resource's public IP), D because bastion and ec2 is in same VPC, meaning bastion
can communicate to EC2 via it's private IP address

### 74 다시보기

A solutions architect is designing a two-tier web application. The application
consists of a public-facing web tier hosted on Amazon EC2 in public subnets. The
database tier consists of Microsoft SQL Server running on Amazon EC2 in a
private subnet. Security is a high priority for the company. How should security
groups be configured in this situation? (Choose two.)

A. Configure the security group for the web tier to allow inbound traffic on
port 443 from 0.0.0.0/0. B. Configure the security group for the web tier to
allow outbound traffic on port 443 from 0.0.0.0/0. C. Configure the security
group for the database tier to allow inbound traffic on port 1433 from the
security group for the web tier. D. Configure the security group for the
database tier to allow outbound traffic on ports 443 and 1433 to the security
group for the web tier. E. Configure the security group for the database tier to
allow inbound traffic on ports 443 and 1433 from the security group for the web
tier.

### 75 다시보기

A company wants to move a multi-tiered application from on premises to the AWS
Cloud to improve the application's performance. The application consists of
application tiers that communicate with each other by way of RESTful services.
**Transactions are dropped when one tier becomes overloaded.** A solutions
architect must design a solution that resolves these issues and **modernizes the
application.** Which solution meets these requirements and is the MOST
operationally efficient?

A. Use Amazon API Gateway and direct transactions to the AWS Lambda functions as
the application layer. Use Amazon Simple Queue Service (Amazon SQS) as the
communication layer between application services. B. Use Amazon CloudWatch
metrics to analyze the application performance history to determine the servers'
peak utilization during the performance failures. Increase the size of the
application server's Amazon EC2 instances to meet the peak requirements. C. Use
Amazon Simple Notification Service (Amazon SNS) to handle the messaging between
application servers running on Amazon EC2 in an Auto Scaling group. Use Amazon
CloudWatch to monitor the SNS queue length and scale up and down as required. D.
Use Amazon Simple Queue Service (Amazon SQS) to handle the messaging between
application servers running on Amazon EC2 in an Auto Scaling group. Use Amazon
CloudWatch to monitor the SQS queue length and scale up when communication
failures are detected.

#### 75 해설

Lambda = serverless + auto scaling SQS = queue + decouple()

### 76

A company receives 10 TB of instrumentation data each day from several machines
located at a single factory. The data consists of JSON files stored on a storage
area network (SAN) in an on-premises data center located within the factory. The
company wants to send this data to Amazon S3 where it can be accessed by several
additional systems that provide critical near-real-time analytics. A secure
transfer is important because the data is considered sensitive. Which solution
offers the MOST reliable data transfer?

A. AWS DataSync over public internet B. AWS DataSync over AWS Direct Connect C.
AWS Database Migration Service (AWS DMS) over public internet D. AWS Database
Migration Service (AWS DMS) over AWS Direct Connect

### 77

A company needs to configure a real-time data ingestion architecture for its
application. The company needs an API, a process that transforms data as the
data is streamed, and a storage solution for the data. Which solution will meet
these requirements with the LEAST operational overhead?

A. Deploy an Amazon EC2 instance to host an API that sends data to an Amazon
Kinesis data stream. Create an Amazon Kinesis Data Firehose delivery stream that
uses the Kinesis data stream as a data source. Use AWS Lambda functions to
transform the data. Use the Kinesis Data Firehose delivery stream to send the
data to Amazon S3. B. Deploy an Amazon EC2 instance to host an API that sends
data to AWS Glue. Stop source/destination checking on the EC2 instance. Use AWS
Glue to transform the data and to send the data to Amazon S3. C. Configure an
Amazon API Gateway API to send data to an Amazon Kinesis data stream. Create an
Amazon Kinesis Data Firehose delivery stream that uses the Kinesis data stream
as a data source. Use AWS Lambda functions to transform the data. Use the
Kinesis Data Firehose delivery stream to send the data to Amazon S3. D.
Configure an Amazon API Gateway API to send data to AWS Glue. Use AWS Lambda
functions to transform the data. Use AWS Glue to send the data to Amazon S3.

#### 77 해설

EC2보다 API Gateway가 더 적은 operational overhead를 가진다. 그리고 API
Gateway는 Kinesis Data Stream을 사용할 수 있다. 그리고 Kinesis Data Firehose는
Lambda를 사용할 수 있다. 그리고 Kinesis Data Firehose는 S3로 데이터를 보낼 수
있다.

### 78

A company needs to keep user transaction data in an Amazon DynamoDB table. The
company must retain the data for 7 years. 2What is the MOST operationally
efficient solution that meets these requirements?

A. Use DynamoDB point-in-time recovery to back up the table continuously. B. Use
AWS Backup to create backup schedules and retention policies for the table. C.
Create an on-demand backup of the table by using the DynamoDB console. Store the
backup in an Amazon S3 bucket. Set an S3 Lifecycle configuration for the S3
bucket. D. Create an Amazon EventBridge (Amazon CloudWatch Events) rule to
invoke an AWS Lambda function. Configure the Lambda function to back up the
table and to store the backup in an Amazon S3 bucket. Set an S3 Lifecycle
configuration for the S3 bucket.

### 79

A company is planning to use an Amazon DynamoDB table for data storage. The
company is concerned about cost optimization. The table will not be used on most
mornings. **In the evenings, the read and write traffic will often be
unpredictable.** When traffic spikes occur, they will happen very quickly. What
should a solutions architect recommend?

A. Create a DynamoDB table in on-demand capacity mode. B. Create a DynamoDB
table with a global secondary index. C. Create a DynamoDB table with provisioned
capacity and auto scaling. D. Create a DynamoDB table in provisioned capacity
mode, and configure it as a global table.

#### 79 해설

On-demand mode is a good option if any of the following are true:

- You create new tables with unknown workloads.
- You have unpredictable application traffic.
- You prefer the ease of paying for only what you use.

### 80 다시보기

A company recently signed a contract with an AWS Managed Service Provider (MSP)
Partner for help with an application migration initiative. A solutions architect
needs ta share an Amazon Machine Image (AMI) from an existing AWS account with
the MSP Partner's AWS account. The AMI is backed by Amazon Elastic Block Store
(Amazon EBS) and uses an AWS Key Management Service (AWS KMS) customer managed
key to encrypt EBS volume snapshots. What is the MOST secure way for the
solutions architect to share the AMI with the MSP Partner's AWS account?

A. Make the encrypted AMI and snapshots publicly available. Modify the key
policy to allow the MSP Partner's AWS account to use the key. B. Modify the
launchPermission property of the AMI. Share the AMI with the MSP Partner's AWS
account only. Modify the key policy to allow the MSP Partner's AWS account to
use the key. Most Voted C. Modify the launchPermission property of the AMI.
Share the AMI with the MSP Partner's AWS account only. Modify the key policy to
trust a new KMS key that is owned by the MSP Partner for encryption. D. Export
the AMI from the source account to an Amazon S3 bucket in the MSP Partner's AWS
account, Encrypt the S3 bucket with a new KMS key that is owned by the MSP
Partner. Copy and launch the AMI in the MSP Partner's AWS account.

#### 80 다시보기

Share the existing KMS key with the MSP external account because it has already
been used to encrypt the AMI snapshot.

If EBS snapshots are encrypted, then we need to share the same KMS key to
partners to be able to access it. Read the note section in the link
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharingamis-explicit.html

### 81

A solutions architect is designing the cloud architecture for a new application
being deployed on AWS. The process should run in parallel while adding and
removing application nodes as needed based on the number of jobs to be
processed. The processor application is stateless. The solutions architect must
ensure that the application is loosely coupled and the job items are durably
stored. Which design should the solutions architect use?

A. Create an Amazon SNS topic to send the jobs that need to be processed. Create
an Amazon Machine Image (AMI) that consists of the processor application. Create
a launch configuration that uses the AMI. Create an Auto Scaling group using the
launch configuration. Set the scaling policy for the Auto Scaling group to add
and remove nodes based on CPU usage. B. Create an Amazon SQS queue to hold the
jobs that need to be processed. Create an Amazon Machine Image (AMI) that
consists of the processor application. Create a launch configuration that uses
the AMI. Create an Auto Scaling group using the launch configuration. Set the
scaling policy for the Auto Scaling group to add and remove nodes based on
network usage. C. Create an Amazon SQS queue to hold the jobs that need to be
processed. Create an Amazon Machine Image (AMI) that consists of the processor
application. Create a launch template that uses the AMI. Create an Auto Scaling
group using the launch template. Set the scaling policy for the Auto Scaling
group to add and remove nodes based on the number of items in the SQS queue. D.
Create an Amazon SNS topic to send the jobs that need to be processed. Create an
Amazon Machine Image (AMI) that consists of the processor application. Create a
launch template that uses the AMI. Create an Auto Scaling group using the launch
template. Set the scaling policy for the Auto Scaling group to add and remove
nodes based on the number of messages published to the SNS topic.

### 82

A company hosts its web applications in the AWS Cloud. The company configures
Elastic Load Balancers to use certificates that are imported into AWS
Certificate Manager (ACM). **The company's security team must be notified 30
days before the expiration of each certificate.** What should a solutions
architect recommend to meet this requirement?

A. Add a rule in ACM to publish a custom message to an Amazon Simple
Notification Service (Amazon SNS) topic every day, beginning 30 days before any
certificate will expire.

B. Create an AWS Config rule that checks for certificates that will expire
within 30 days. Configure Amazon EventBridge (Amazon CloudWatch Events) to
invoke a custom alert by way of Amazon Simple Notification Service (Amazon SNS)
when AWS Config reports a noncompliant resource.

C. Use AWS Trusted Advisor to check for certificates that will expire within 30
days. Create an Amazon CloudWatch alarm that is based on Trusted Advisor metrics
for check status changes. Configure the alarm to send a custom alert by way of
Amazon Simple Notification Service (Amazon SNS).

D. Create an Amazon EventBridge (Amazon CloudWatch Events) rule to detect any
certificates that will expire within 30 days. Configure the rule to invoke an
AWS Lambda function. Configure the Lambda function to send a custom alert by way
of Amazon Simple Notification Service (Amazon SNS).

### 83

A company's dynamic website is hosted using on-premises servers in the United
States. The company is launching its product in Europe, and it wants to optimize
site loading times for new European users. The site's backend must remain in the
United States. The product is being launched in a few days, and an immediate
solution is needed. What should the solutions architect recommend?

A. Launch an Amazon EC2 instance in us-east-1 and migrate the site to it. B.
Move the website to Amazon S3. Use Cross-Region Replication between Regions. C.
Use Amazon CloudFront with a custom origin pointing to the on-premises servers.
Most Voted D. Use an Amazon Route 53 geoproximity routing policy pointing to
on-premises servers.

### 84

A company wants to reduce the cost of its existing three-tier web architecture.
The web, application, and database servers are running on Amazon EC2 instances
for the development, test, and production environments. The EC2 instances
average 30% CPU utilization during peak hours and 10% CPU utilization during
non-peak hours. The production EC2 instances run 24 hours a day. The development
and test EC2 instances run for at least 8 hours each day. The company plans to
implement automation to stop the development and test EC2 instances when they
are not in use. Which EC2 instance purchasing solution will meet the company's
requirements MOST cost-effectively?

A. Use Spot Instances for the production EC2 instances. Use Reserved Instances
for the development and test EC2 instances. B. Use Reserved Instances for the
production EC2 instances. Use On-Demand Instances for the development and test
EC2 instances. Most Voted C. Use Spot blocks for the production EC2 instances.
Use Reserved Instances for the development and test EC2 instances. D. Use
On-Demand Instances for the production EC2 instances. Use Spot blocks for the
development and test EC2 instances.

### 85 다시보기

A company has a production web application in which users upload documents
through a web interface or a mobile app. According to a new regulatory
requirement. new documents cannot be modified or deleted after they are stored.
**What should a solutions architect do to meet this requirement?**

A. Store the uploaded documents in an Amazon S3 bucket with S3 Versioning and S3
Object Lock enabled. B. Store the uploaded documents in an Amazon S3 bucket.
Configure an S3 Lifecycle policy to archive the documents periodically. C. Store
the uploaded documents in an Amazon S3 bucket with S3 Versioning enabled.
Configure an ACL to restrict all access to read-only. D. Store the uploaded
documents on an Amazon Elastic File System (Amazon EFS) volume. Access the data
by mounting the volume in read-only mode.

#### 85 해설

_**CORRECT**_ A. Store the uploaded documents in an Amazon S3 bucket with S3
Versioning and S3 Object Lock enabled.

S3 Versioning allows multiple versions of an object to be stored in the same
bucket. This means that when an object is modified or deleted, the previous
version is preserved. S3 Object Lock adds additional protection by allowing
objects to be placed under a legal hold or retention period, during which they
cannot be deleted or modified. Together, S3 Versioning and S3 Object Lock can be
used to meet the requirement of not allowing documents to be modified or deleted
after they are stored.

Option C, storing the documents in an S3 bucket with S3 Versioning enabled and
configuring an ACL to restrict all access to read-only, would also not prevent
the documents from being modified or deleted, **since an ACL only controls
access to the object and does not prevent it from being modified or deleted.**

### 86

A company has several web servers that need to frequently access a common
**Amazon RDS MySQL Multi-AZ DB instance.** The company wants a secure method for
the web servers to connect to the database **while meeting a security
requirement to rotate user credentials frequently.** Which solution meets these
requirements?

A. Store the database user credentials in AWS Secrets Manager. Grant the
necessary IAM permissions to allow the web servers to access AWS Secrets
Manager. B. Store the database user credentials in AWS Systems Manager
OpsCenter. Grant \*the necessary IAM permissions to allow the web servers to
access OpsCenter. C. Store the database user credentials in a secure Amazon S3
bucket. Grant the necessary IAM permissions to allow the web servers to retrieve
credentials and access the database. D. Store the database user credentials in
files encrypted with AWS Key Management Service (AWS KMS) on the web server file
system. The web server should be able to decrypt the files and access the
database.

### 87

A company hosts an application on AWS Lambda functions that are invoked by an
Amazon API Gateway API. The Lambda functions save customer data to an Amazon
Aurora MySQL database. Whenever the company upgrades the database, the Lambda
functions fail to establish database connections until the upgrade is complete.
The result is that customer data is not recorded for some of the event. A
solutions architect needs to design a solution that stores customer data that is
created during database upgrades. Which solution will meet these requirements?

- A. Provision an Amazon RDS proxy to sit between the Lambda functions and the
  database. Configure the Lambda functions to connect to the RDS proxy.
- B. Increase the run time of the Lambda functions to the maximum. Create a
  retry mechanism in the code that stores the customer data in the database.
- C. Persist the customer data to Lambda local storage. Configure new Lambda
  functions to scan the local storage to save the customer data to the database.
- D. Store the customer data in an Amazon Simple Queue Service (Amazon SQS) FIFO
  queue. Create a new Lambda function that polls the queue and stores the
  customer data in the database.

### 88

A survey company has gathered data for several years from areas in the United
States. The company hosts the data in an Amazon S3 bucket that is 3 TB in size
and growing. The company has started to share the data with a European marketing
firm that has S3 buckets. The company wants to ensure that its data transfer
costs remain as low as possible. Which solution will meet these requirements?

A. Configure the Requester Pays feature on the company's S3 bucket. B. Configure
S3 Cross-Region Replication from the company's S3 bucket to one of the marketing
firm's S3 buckets. C. Configure cross-account access for the marketing firm so
that the marketing firm has access to the company's S3 bucket. D . Configure the
company's S3 bucket to use S3 Intelligent-Tiering. Sync the S3 bucket to one of
the marketing firm's S3 buckets.

### 89

A company uses Amazon S3 to store its confidential audit documents. The S3
bucket uses bucket policies to restrict access to audit team IAM user
credentials according to the principle of least privilege. Company managers are
worried about accidental deletion of documents in the S3 bucket and want a more
secure solution. What should a solutions architect do to secure the audit
documents?

A. Enable the versioning and MFA Delete features on the S3 bucket. B. Enable
multi-factor authentication (MFA) on the IAM user credentials for each audit
team IAM user account. C. Add an S3 Lifecycle policy to the audit team's IAM
user accounts to deny the s3:DeleteObject action during audit dates. D. Use AWS
Key Management Service (AWS KMS) to encrypt the S3 bucket and restrict audit
team IAM user accounts from accessing the KMS key.

### 90

A company is using a SQL database to store movie data that is publicly
accessible. The database runs on an Amazon RDS Single-AZ DB instance. A script
runs queries at random intervals each day to record the number of new movies
that have been added to the database. The script must report a final total
during business hours. **The company's development team notices that the
database performance is inadequate for development tasks when the script is
running. A solutions architect must recommend a solution to resolve this
issue.** Which solution will meet this requirement with the LEAST operational
overhead?

A. Modify the DB instance to be a Multi-AZ deployment. B. Create a read replica
of the database. Configure the script to query only the read replica. C.
Instruct the development team to manually export the entries in the database at
the end of each day. D. Use Amazon ElastiCache to cache the common queries that
the script runs against the database.

### 91

A company has applications that run on Amazon EC2 instances in a VPC. One of the
applications needs to call the Amazon S3 API to store and read objects.
According to the company's security regulations, no traffic from the
applications is allowed to travel across the internet. Which solution will meet
these requirements?

- A. Configure an S3 gateway endpoint.
- B. Create an S3 bucket in a private subnet.
- C. Create an S3 bucket in the same AWS Region as the EC2 instances.
- D. Configure a NAT gateway in the same subnet as the EC2 instances.

### 92

A company is storing sensitive user information in an Amazon S3 bucket. The company wants to provide secure access to this bucket from the application tier running on Amazon EC2 instances inside a VPC.
Which combination of steps should a solutions architect take to accomplish this? (Choose two.)

- A. Configure a VPC gateway endpoint for Amazon S3 within the VPC.
- B. Create a bucket policy to make the objects in the S3 bucket public.
- C. Create a bucket policy that limits access to only the application tier running in the VPC.
- D. Create an IAM user with an S3 access policy and copy the IAM credentials to the EC2 instance.
- E. Create a NAT instance and have the EC2 instances use the NAT instance to access the S3 bucket.

### 93

A company runs an on-premises application that is powered by a MySQL database. The company is migrating the application to AWS to increase the application's elasticity and availability.
The current architecture shows heavy read activity on the database during times of normal operation. Every 4 hours, the company's development team pulls a full export of the production database to populate a database in the staging environment. During this period, users experience unacceptable application latency. The development team is unable to use the staging environment until the procedure completes.
A solutions architect must recommend replacement architecture that alleviates the application latency issue. The replacement architecture also must give the development team the ability to continue using the staging environment without delay.
Which solution meets these requirements?

- A. Use Amazon Aurora MySQL with Multi-AZ Aurora Replicas for production. Populate the staging database by implementing a backup and restore process that uses the mysqldump utility.
- B. Use Amazon Aurora MySQL with Multi-AZ Aurora Replicas for production. Use database cloning to create the staging database on-demand.
- C. Use Amazon RDS for MySQL with a Multi-AZ deployment and read replicas for production. Use the standby instance for the staging database.
- D. Use Amazon RDS for MySQL with a Multi-AZ deployment and read replicas for production. Populate the staging database by implementing a backup and restore process that uses the mysqldump utility.

#### 93 해설

Option C: Use Amazon RDS for MySQL with a Multi-AZ deployment and read replicas for production. Using the standby instance for the staging database is not the recommended solution because it does not give the development team the ability to continue using the staging environment without delay. The standby instance is used for failover in case of a production instance failure, and it is not intended for use as a staging environment.

### 94

A company is designing an application where users upload small files into Amazon S3. After a user uploads a file, the file requires one-time simple processing to transform the data and save the data in JSON format for later analysis.
Each file must be processed as quickly as possible after it is uploaded. Demand will vary. On some days, users will upload a high number of files. On other days, users will upload a few files or no files.
Which solution meets these requirements with the LEAST operational overhead?

- A. Configure Amazon EMR to read text files from Amazon S3. Run processing scripts to transform the data. Store the resulting JSON file in an Amazon Aurora DB cluster.
- B. Configure Amazon S3 to send an event notification to an Amazon Simple Queue Service (Amazon SQS) queue. Use Amazon EC2 instances to read from the queue and process the data. Store the resulting JSON file in Amazon DynamoDB.
- C. Configure Amazon S3 to send an event notification to an Amazon Simple Queue Service (Amazon SQS) queue. Use an AWS Lambda function to read from the queue and process the data. Store the resulting JSON file in Amazon DynamoDB.
- D. Configure Amazon EventBridge (Amazon CloudWatch Events) to send an event to Amazon Kinesis Data Streams when a new file is uploaded. Use an AWS Lambda function to consume the event from the stream and process the data. Store the resulting JSON file in an Amazon Aurora DB cluster.

### 95

An application allows users at a company's headquarters to access product data. The product data is stored in an Amazon RDS MySQL DB instance. The operations team has isolated an application performance slowdown and wants to separate read traffic from write traffic. A solutions architect needs to optimize the application's performance quickly.
What should the solutions architect recommend?

- A. Change the existing database to a Multi-AZ deployment. Serve the read requests from the primary Availability Zone.
- B. Change the existing database to a Multi-AZ deployment. Serve the read requests from the secondary Availability Zone.
- C. Create read replicas for the database. Configure the read replicas with half of the compute and storage resources as the source database.
- D. Create read replicas for the database. Configure the read replicas with the same compute and storage resources as the source database.

### 96 다시보기

#### 96

- allow termination of any instance if user's source ip address is 100.100.254
- Deny termination of instances that are not in the us-east-1

### 97

A company has a large Microsoft SharePoint deployment running on-premises that requires Microsoft Windows shared file storage. The company wants to migrate this workload to the AWS Cloud and is considering various storage options. The storage solution must be highly available and integrated with Active Directory for access control.
Which solution will satisfy these requirements?

- A. Configure Amazon EFS storage and set the Active Directory domain for authentication.
- B. Create an SMB file share on an AWS Storage Gateway file gateway in two Availability Zones.
- C. Create an Amazon S3 bucket and configure Microsoft Windows Server to mount it as a volume.
- D. Create an Amazon FSx for Windows File Server file system on AWS and set the Active Directory domain for authentication

### 98

An image-processing company has a web application that users use to upload images. The application uploads the images into an Amazon S3 bucket. The company has set up S3 event notifications to publish the object creation events to an Amazon Simple Queue Service (Amazon SQS) standard queue. The SQS queue serves as the event source for an AWS Lambda function that processes the images and sends the results to users through email.
Users report that they are receiving multiple email messages for every uploaded image. A solutions architect determines that SQS messages are invoking the Lambda function more than once, resulting in multiple email messages.
What should the solutions architect do to resolve this issue with the LEAST operational overhead?

- A. Set up long polling in the SQS queue by increasing the ReceiveMessage wait time to 30 seconds.
- B. Change the SQS standard queue to an SQS FIFO queue. Use the message deduplication ID to discard duplicate messages.
- C. Increase the visibility timeout in the SQS queue to a value that is greater than the total of the function timeout and the batch window timeout.
- D. Modify the Lambda function to delete each message from the SQS queue immediately after the message is read before processing.

#### 98 해설

https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html

this is important part:
Immediately after a message is received, it remains in the queue. To prevent other consumers from processing the message again, Amazon SQS sets a visibility timeout, a period of time during which Amazon SQS prevents other consumers from receiving and processing the message. The default visibility timeout for a message is 30 seconds. The minimum is 0 seconds. The maximum is 12 hours

### 99

A company is implementing a shared storage solution for a gaming application that is hosted in an on-premises data center. The company needs the ability to use Lustre clients to access data. The solution must be fully managed.
Which solution meets these requirements?

- A. Create an AWS Storage Gateway file gateway. Create a file share that uses the required client protocol. Connect the application server to the file share.
- B. Create an Amazon EC2 Windows instance. Install and configure a Windows file share role on the instance. Connect the application server to the file share.
- C. Create an Amazon Elastic File System (Amazon EFS) file system, and configure it to support Lustre. Attach the file system to the origin server. Connect the application server to the file system.
- D. Create an Amazon FSx for Lustre file system. Attach the file system to the origin server. Connect the application server to the file system.

### 100

A company's containerized application runs on an Amazon EC2 instance. The application needs to download security certificates before it can communicate with other business applications. The company wants a highly secure solution to encrypt and decrypt the certificates in near real time. The solution also needs to store data in highly available storage after the data is encrypted.
Which solution will meet these requirements with the LEAST operational overhead?

A. Create AWS Secrets Manager secrets for encrypted certificates. Manually update the certificates as needed. Control access to the data by using fine-grained IAM access.
B. Create an AWS Lambda function that uses the Python cryptography library to receive and perform encryption operations. Store the function in an Amazon S3 bucket.
C. Create an AWS Key Management Service (AWS KMS) customer managed key. Allow the EC2 role to use the KMS key for encryption operations. Store the encrypted data on Amazon S3.
D. Create an AWS Key Management Service (AWS KMS) customer managed key. Allow the EC2 role to use the KMS key for encryption operations. Store the encrypted data on Amazon Elastic Block Store (Amazon EBS) volumes.

### 101

A solutions architect is designing a VPC with public and private subnets. The VPC and subnets use IPv4 CIDR blocks. There is one public subnet and one private subnet in each of three Availability Zones (AZs) for high availability. An internet gateway is used to provide internet access for the public subnets. The private subnets require access to the internet to allow Amazon EC2 instances to download software updates.
What should the solutions architect do to enable Internet access for the private subnets?

- A. Create three NAT gateways, one for each public subnet in each AZ. Create a private route table for each AZ that forwards non-VPC traffic to the NAT gateway in its AZ.
- B. Create three NAT instances, one for each private subnet in each AZ. Create a private route table for each AZ that forwards non-VPC traffic to the NAT instance in its AZ.
- C. Create a second internet gateway on one of the private subnets. Update the route table for the private subnets that forward non-VPC traffic to the private internet gateway.
- D. Create an egress-only internet gateway on one of the public subnets. Update the route table for the private subnets that forward non-VPC traffic to the egress-only Internet gateway.

### 102

A company wants to migrate an on-premises data center to AWS. The data center hosts an SFTP server that stores its data on an NFS-based file system. The server holds 200 GB of data that needs to be transferred. The server must be hosted on an Amazon EC2 instance that uses an Amazon Elastic File System (Amazon EFS) file system.
Which combination of steps should a solutions architect take to automate this task? (Choose two.)

A. Launch the EC2 instance into the same Availability Zone as the EFS file system.
B. Install an AWS DataSync agent in the on-premises data center.
C. Create a secondary Amazon Elastic Block Store (Amazon EBS) volume on the EC2 instance for the data.
D. Manually use an operating system copy command to push the data to the EC2 instance.
E. Use AWS DataSync to create a suitable location configuration for the on-premises SFTP server.

### 103

A company has an AWS Glue extract, transform, and load (ETL) job that runs every day at the same time. The job processes XML data that is in an Amazon S3 bucket. New data is added to the S3 bucket every day. A solutions architect notices that AWS Glue is processing all the data during each run.
What should the solutions architect do to prevent AWS Glue from reprocessing old data?

A. Edit the job to use job bookmarks.
B. Edit the job to delete data after the data is processed.
C. Edit the job by setting the NumberOfWorkers field to 1.
D. Use a FindMatches machine learning (ML) transform.

### 104

A solutions architect must design a highly available infrastructure for a website. The website is powered by Windows web servers that run on Amazon EC2 instances. The solutions architect must implement a solution that can mitigate a large-scale DDoS attack that originates from thousands of IP addresses. Downtime is not acceptable for the website.
Which actions should the solutions architect take to protect the website from such an attack? (Choose two.)

A. Use AWS Shield Advanced to stop the DDoS attack.
B. Configure Amazon GuardDuty to automatically block the attackers.
C. Configure the website to use Amazon CloudFront for both static and dynamic content.
D. Use an AWS Lambda function to automatically add attacker IP addresses to VPC network ACLs.
E. Use EC2 Spot Instances in an Auto Scaling group with a target tracking scaling policy that is set to 80% CPU utilization.

#### 104 해설

CloudFront is a content delivery network (CDN) that integrates with other Amazon Web Services products, such as Amazon S3 and Amazon EC2, to deliver content to users with low latency and high data transfer speeds. **By using CloudFront, the solutions architect can distribute the website's content across multiple edge locations, which can help absorb the impact of a DDoS attack and reduce the risk of downtime for the website.**

### 105 다시보기

A company is preparing to deploy a new serverless workload. A solutions architect must use the principle of least privilege to configure permissions that will be used to run an AWS Lambda function. An Amazon EventBridge (Amazon CloudWatch Events) rule will invoke the function.
Which solution meets these requirements?

- A. Add an execution role to the function with lambda:InvokeFunction as the action and \* as the principal.
- B. Add an execution role to the function with lambda:InvokeFunction as the action and Service: lambda.amazonaws.com as the principal.
- C. Add a resource-based policy to the function with lambda:\* as the action and Service: events.amazonaws.com as the principal.
- D. Add a resource-based policy to the function with lambda:InvokeFunction as the action and Service: events.amazonaws.com as the principal.

### 106

A company is preparing to store confidential data in Amazon S3. For compliance reasons, the data must be encrypted at rest.
Encryption key usage must be logged for auditing purposes. Keys must be rotated every year.
Which solution meets these requirements and is the MOST operationally efficient?

- A. Server-side encryption with customer-provided keys (SSE-C)
- B. Server-side encryption with Amazon S3 managed keys (SSE-S3)
- C. Server-side encryption with AWS KMS keys (SSE-KMS) with manual rotation
- D. Server-side encryption with AWS KMS keys (SSE-KMS) with automatic rotation

### 107

A bicycle sharing company is developing a multi-tier architecture to track the location of its bicycles during peak operating hours. The company wants to use these data points in its existing analytics platform. A solutions architect must determine the most viable multi-tier option to support this architecture. The data points must be accessible from the REST API.
Which action meets these requirements for storing and retrieving location data?

- A. Use Amazon Athena with Amazon S3.
- B. Use Amazon API Gateway with AWS Lambda.
- C. Use Amazon QuickSight with Amazon Redshift.
- D. Use Amazon API Gateway with Amazon Kinesis Data Analytics.

### 108 다시보기

A company has an automobile sales website that stores its listings in a database on Amazon RDS. When an automobile is sold, the listing needs to be removed from the website and the data must be sent to multiple target systems.
Which design should a solutions architect recommend?

- A. Create an AWS Lambda function triggered when the database on Amazon RDS is updated to send the information to an Amazon Simple Queue Service (Amazon SQS) queue for the targets to consume.
- B. Create an AWS Lambda function triggered when the database on Amazon RDS is updated to send the information to an Amazon Simple Queue Service (Amazon SQS) FIFO queue for the targets to consume.
- C. Subscribe to an RDS event notification and send an Amazon Simple Queue Service (Amazon SQS) queue fanned out to multiple Amazon Simple Notification Service (Amazon SNS) topics. Use AWS Lambda functions to update the targets.
- D. Subscribe to an RDS event notification and send an Amazon Simple Notification Service (Amazon SNS) topic fanned out to multiple Amazon Simple Queue Service (Amazon SQS) queues. Use AWS Lambda functions to update the targets.

### 109 다시보기

A company needs to store data in Amazon S3 and must prevent the data from being changed. The company wants new objects that are uploaded to Amazon S3 to remain unchangeable for a nonspecific amount of time until the company decides to modify the objects. Only specific users in the company's AWS account can have the ability 10 delete the objects.
What should a solutions architect do to meet these requirements?

- A. Create an S3 Glacier vault. Apply a write-once, read-many (WORM) vault lock policy to the objects.
- B. Create an S3 bucket with S3 Object Lock enabled. Enable versioning. Set a retention period of 100 years. Use governance mode as the S3 bucket’s default retention mode for new objects.
- C. Create an S3 bucket. Use AWS CloudTrail to track any S3 API events that modify the objects. Upon notification, restore the modified objects from any backup versions that the company has.
- D. Create an S3 bucket with S3 Object Lock enabled. Enable versioning. Add a legal hold to the objects. Add the s3:PutObjectLegalHold permission to the IAM policies of users who need to delete the objects.

### 110

A social media company allows users to upload images to its website. The website runs on Amazon EC2 instances. During upload requests, the website resizes the images to a standard size and stores the resized images in Amazon S3. Users are experiencing slow upload requests to the website.
The company needs to reduce coupling within the application and improve website performance. A solutions architect must design the most operationally efficient process for image uploads.
Which combination of actions should the solutions architect take to meet these requirements? (Choose two.)

- A. Configure the application to upload images to S3 Glacier.
- B. Configure the web server to upload the original images to Amazon S3.
- C. Configure the application to upload images directly from each user's browser to Amazon S3 through the use of a presigned URL
- D. Configure S3 Event Notifications to invoke an AWS Lambda function when an image is uploaded. Use the function to resize the image.
- E. Create an Amazon EventBridge (Amazon CloudWatch Events) rule that invokes an AWS Lambda function on a schedule to resize uploaded images.

#### 110 해설

C. Configure the application to upload images directly from each user's browser to Amazon S3 through the use of a pre-signed URL. This will allow the application to upload images directly to S3 without having to go through the web server, which can reduce the load on the web server and improve performance.

D. Configure S3 Event Notifications to invoke an AWS Lambda function when an image is uploaded. Use the function to resize the image. This will allow the application to resize images asynchronously, rather than having to do it synchronously during the upload request, which can improve performance.

Why other options are wrong
Option A, Configuring the application to upload images to S3 Glacier, is not relevant to improving the performance of image uploads.

Option B, Configuring the webserver to upload the original images to Amazon S3, is not a recommended solution as it would not reduce coupling within the application or improve performance.

Option E, Creating an Amazon EventBridge (Amazon CloudWatch Events) rule that invokes an AWS Lambda function on a schedule to resize uploaded images, is not a recommended solution as it would not be able to resize images in a timely manner and would not improve performance.

### 111

A company recently migrated a message processing system to AWS. The system receives messages into an ActiveMQ queue running on an Amazon EC2 instance. Messages are processed by a consumer application running on Amazon EC2. The consumer application processes the messages and writes results to a MySQL database running on Amazon EC2. The company wants this application to be highly available with low operational complexity.
Which architecture offers the HIGHEST availability?

- A. Add a second ActiveMQ server to another Availability Zone. Add an additional consumer EC2 instance in another Availability Zone. Replicate the MySQL database to another Availability Zone.
- B. Use Amazon MQ with active/standby brokers configured across two Availability Zones. Add an additional consumer EC2 instance in another Availability Zone. Replicate the MySQL database to another Availability Zone.
- C. Use Amazon MQ with active/standby brokers configured across two Availability Zones. Add an additional consumer EC2 instance in another Availability Zone. Use Amazon RDS for MySQL with Multi-AZ enabled.
- D. Use Amazon MQ with active/standby brokers configured across two Availability Zones. Add an Auto Scaling group for the consumer EC2 instances across two Availability Zones. Use Amazon RDS for MySQL with Multi-AZ enabled.

### 112

A company hosts a containerized web application on a fleet of on-premises servers that process incoming requests. The number of requests is growing quickly. The on-premises servers cannot handle the increased number of requests. The company wants to move the application to AWS with minimum code changes and minimum development effort.
Which solution will meet these requirements with the LEAST operational overhead?

- A. Use AWS Fargate on Amazon Elastic Container Service (Amazon ECS) to run the containerized web application with Service Auto Scaling. Use an Application Load Balancer to distribute the incoming requests.
- B. Use two Amazon EC2 instances to host the containerized web application. Use an Application Load Balancer to distribute the incoming requests.
- C. Use AWS Lambda with a new code that uses one of the supported languages. Create multiple Lambda functions to support the load. Use Amazon API Gateway as an entry point to the Lambda functions.
- D. Use a high performance computing (HPC) solution such as AWS ParallelCluster to establish an HPC cluster that can process the incoming requests at the appropriate scale.

### 113

A company uses 50 TB of data for reporting. The company wants to move this data from on premises to AWS. A custom application in the company’s data center runs a weekly data transformation job. The company plans to pause the application until the data transfer is complete and needs to begin the transfer process as soon as possible.
The data center does not have any available network bandwidth for additional workloads. A solutions architect must transfer the data and must configure the transformation job to continue to run in the AWS Cloud.
Which solution will meet these requirements with the LEAST operational overhead?

- A. Use AWS DataSync to move the data. Create a custom transformation job by using AWS Glue.
- B. Order an AWS Snowcone device to move the data. Deploy the transformation application to the device.
- C. Order an AWS Snowball Edge Storage Optimized device. Copy the data to the device. Create a custom transformation job by using AWS Glue.
- D. Order an AWS Snowball Edge Storage Optimized device that includes Amazon EC2 compute. Copy the data to the device. Create a new EC2 instance on AWS to run the transformation application.

### 114

A company has created an image analysis application in which users can upload photos and add photo frames to their images. The users upload images and metadata to indicate which photo frames they want to add to their images. The application uses a single Amazon EC2 instance and Amazon DynamoDB to store the metadata.
The application is becoming more popular, and the number of users is increasing. The company expects the number of concurrent users to vary significantly depending on the time of day and day of week. The company must ensure that the application can scale to meet the needs of the growing user base.
Which solution meats these requirements?

- A. Use AWS Lambda to process the photos. Store the photos and metadata in DynamoDB.
- B. Use Amazon Kinesis Data Firehose to process the photos and to store the photos and metadata.
- C. Use AWS Lambda to process the photos. Store the photos in Amazon S3. Retain DynamoDB to store the metadata.
- D. Increase the number of EC2 instances to three. Use Provisioned IOPS SSD (io2) Amazon Elastic Block Store (Amazon EBS) volumes to store the photos and metadata.

### 115

A medical records company is hosting an application on Amazon EC2 instances. The application processes customer data files that are stored on Amazon S3. The EC2 instances are hosted in public subnets. The EC2 instances access Amazon S3 over the internet, but they do not require any other network access.
A new requirement mandates that the network traffic for file transfers take a private route and not be sent over the internet.
Which change to the network architecture should a solutions architect recommend to meet this requirement?

- A. Create a NAT gateway. Configure the route table for the public subnets to send traffic to Amazon S3 through the NAT gateway.
- B. Configure the security group for the EC2 instances to restrict outbound traffic so that only traffic to the S3 prefix list is permitted.
- C. Move the EC2 instances to private subnets. Create a VPC endpoint for Amazon S3, and link the endpoint to the route table for the private subnets.
- D. Remove the internet gateway from the VPC. Set up an AWS Direct Connect connection, and route traffic to Amazon S3 over the Direct Connect connection.

### 116

A company uses a popular content management system (CMS) for its corporate website. However, the required patching and maintenance are burdensome. The company is redesigning its website and wants anew solution. The website will be updated four times a year and does not need to have any dynamic content available. The solution must provide high scalability and enhanced security.
Which combination of changes will meet these requirements with the LEAST operational overhead? (Choose two.)

- A. Configure Amazon CloudFront in front of the website to use HTTPS functionality.
- B. Deploy an AWS WAF web ACL in front of the website to provide HTTPS functionality.
- C. Create and deploy an AWS Lambda function to manage and serve the website content.
- D. Create the new website and an Amazon S3 bucket. Deploy the website on the S3 bucket with static website hosting enabled.
- E. Create the new website. Deploy the website by using an Auto Scaling group of Amazon EC2 instances behind an Application Load Balancer.

### 117

A company stores its application logs in an Amazon CloudWatch Logs log group. A new policy requires the company to store all application logs in Amazon OpenSearch Service (Amazon Elasticsearch Service) in near-real time.
Which solution will meet this requirement with the LEAST operational overhead?

- A. Configure a CloudWatch Logs subscription to stream the logs to Amazon OpenSearch Service (Amazon Elasticsearch Service).
- B. Create an AWS Lambda function. Use the log group to invoke the function to write the logs to Amazon OpenSearch Service (Amazon Elasticsearch Service).
- C. Create an Amazon Kinesis Data Firehose delivery stream. Configure the log group as the delivery streams sources. Configure Amazon OpenSearch Service (Amazon Elasticsearch Service) as the delivery stream's destination.
- D. Install and configure Amazon Kinesis Agent on each application server to deliver the logs to Amazon Kinesis Data Streams. Configure Kinesis Data Streams to deliver the logs to Amazon OpenSearch Service (Amazon Elasticsearch Service).

#### 117 해설

answer is A
https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_OpenSearch_Stream.html

> You can configure a CloudWatch Logs log group to stream data it receives to your Amazon OpenSearch Service cluster in NEAR REAL-TIME through a CloudWatch Logs subscription

least overhead compared to kinesis

### 118

A company is building a web-based application running on Amazon EC2 instances in multiple Availability Zones. The web application will provide access to a repository of text documents totaling about 900 TB in size. The company anticipates that the web application will experience periods of high demand. A solutions architect must ensure that the storage component for the text documents can scale to meet the demand of the application at all times. The company is concerned about the overall cost of the solution.
Which storage solution meets these requirements MOST cost-effectively?

- A. Amazon Elastic Block Store (Amazon EBS)
- B. Amazon Elastic File System (Amazon EFS)
- C. Amazon OpenSearch Service (Amazon Elasticsearch Service)
- D. Amazon S3

### 119

A global company is using Amazon API Gateway to design REST APIs for its loyalty club users in the us-east-1 Region and the ap-southeast-2 Region. A solutions architect must design a solution to protect these API Gateway managed REST APIs across multiple accounts from SQL injection and cross-site scripting attacks.
Which solution will meet these requirements with the LEAST amount of administrative effort?

- A. Set up AWS WAF in both Regions. Associate Regional web ACLs with an API stage.
- B. Set up AWS Firewall Manager in both Regions. Centrally configure AWS WAF rules.
- C. Set up AWS Shield in bath Regions. Associate Regional web ACLs with an API stage.
- D. Set up AWS Shield in one of the Regions. Associate Regional web ACLs with an API stage.

#### 119 해설

B

Using AWS WAF has several benefits. Additional protection against web attacks using criteria that you specify. You can define criteria using characteristics of web requests such as the following:
Presence of SQL code that is likely to be malicious (known as SQL injection).
Presence of a script that is likely to be malicious (known as cross-site scripting).

**AWS Firewall Manager simplifies your administration and maintenance tasks across multiple accounts and resources for a variety of protections.**

https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html

### 120 다시보기

A company has implemented a self-managed DNS solution on three Amazon EC2 instances behind a Network Load Balancer (NLB) in the us-west-2 Region. Most of the company's users are located in the United States and Europe. The company wants to improve the performance and availability of the solution. The company launches and configures three EC2 instances in the eu-west-1 Region and adds the EC2 instances as targets for a new NLB.
Which solution can the company use to route traffic to all the EC2 instances?

- A. Create an Amazon Route 53 geolocation routing policy to route requests to one of the two NLBs. Create an Amazon CloudFront distribution. Use the Route 53 record as the distribution’s origin.
- B. Create a standard accelerator in AWS Global Accelerator. Create endpoint groups in us-west-2 and eu-west-1. Add the two NLBs as endpoints for the endpoint groups.
- C. Attach Elastic IP addresses to the six EC2 instances. Create an Amazon Route 53 geolocation routing policy to route requests to one of the six EC2 instances. Create an Amazon CloudFront distribution. Use the Route 53 record as the distribution's origin.
- D. Replace the two NLBs with two Application Load Balancers (ALBs). Create an Amazon Route 53 latency routing policy to route requests to one of the two ALBs. Create an Amazon CloudFront distribution. Use the Route 53 record as the distribution’s origin.

#### 120 해설

B. Create a standard accelerator in AWS Global Accelerator. Create endpoint groups in us-west-2 and eu-west-1. Add the two NLBs as endpoints for the endpoint groups.

Here's why this option is the most suitable:

Global Accelerator: AWS Global Accelerator is designed to improve the availability and performance of applications by using static IP addresses (Anycast IPs) and routing traffic over the AWS global network infrastructure.

Endpoint Groups: By creating endpoint groups in both the us-west-2 and eu-west-1 Regions, the company can effectively distribute traffic to the NLBs in both Regions. This improves availability and allows traffic to be directed to the closest Region based on latency.

e two ALBs. Create an Amazon CloudFront distribution. Use the Route 53 record as the distribution’s origin.

### 121

A company is running an online transaction processing (OLTP) workload on AWS. This workload uses an unencrypted Amazon RDS DB instance in a Multi-AZ deployment. Daily database snapshots are taken from this instance.
What should a solutions architect do to ensure the database and snapshots are always encrypted moving forward?

- A. Encrypt a copy of the latest DB snapshot. Replace existing DB instance by restoring the encrypted snapshot.
- B. Create a new encrypted Amazon Elastic Block Store (Amazon EBS) volume and copy the snapshots to it. Enable encryption on the DB instance.
- C. Copy the snapshots and enable encryption using AWS Key Management Service (AWS KMS) Restore encrypted snapshot to an existing DB instance.
- D. Copy the snapshots to an Amazon S3 bucket that is encrypted using server-side encryption with AWS Key Management Service (AWS KMS) managed keys (SSE-KMS).

### 122

A company wants to build a scalable key management infrastructure to support developers who need to encrypt data in their applications.
What should a solutions architect do to reduce the operational burden?

- A. Use multi-factor authentication (MFA) to protect the encryption keys.
- B. Use AWS Key Management Service (AWS KMS) to protect the encryption keys.
- C. Use AWS Certificate Manager (ACM) to create, store, and assign the encryption keys.
- D. Use an IAM policy to limit the scope of users who have access permissions to protect the encryption keys.

### 123

A company has a dynamic web application hosted on two Amazon EC2 instances. The company has its own SSL certificate, which is on each instance to perform SSL termination.
There has been an increase in traffic recently, and the operations team determined that SSL encryption and decryption is causing the compute capacity of the web servers to reach their maximum limit.
What should a solutions architect do to increase the application's performance?

- A. Create a new SSL certificate using AWS Certificate Manager (ACM). Install the ACM certificate on each instance.
- B. Create an Amazon S3 bucket Migrate the SSL certificate to the S3 bucket. Configure the EC2 instances to reference the bucket for SSL termination.
- C. Create another EC2 instance as a proxy server. Migrate the SSL certificate to the new instance and configure it to direct connections to the existing EC2 instances.
- D. Import the SSL certificate into AWS Certificate Manager (ACM). Create an Application Load Balancer with an HTTPS listener that uses the SSL certificate from ACM.

### 124

A company has a highly dynamic batch processing job that uses many Amazon EC2 instances to complete it. The job is stateless in nature, can be started and stopped at any given time with no negative impact, and typically takes upwards of 60 minutes total to complete. The company has asked a solutions architect to design a scalable and cost-effective solution that meets the requirements of the job.
What should the solutions architect recommend?

- A. Implement EC2 Spot Instances.
- B. Purchase EC2 Reserved Instances.
- C. Implement EC2 On-Demand Instances.
- D. Implement the processing on AWS Lambda.

### 125

A company runs its two-tier ecommerce website on AWS. The web tier consists of a load balancer that sends traffic to Amazon EC2 instances. The database tier uses an Amazon RDS DB instance. The EC2 instances and the RDS DB instance should not be exposed to the public internet. The EC2 instances require internet access to complete payment processing of orders through a third-party web service. The application must be highly available.
Which combination of configuration options will meet these requirements? (Choose two.)

- A. Use an Auto Scaling group to launch the EC2 instances in private subnets. Deploy an RDS Multi-AZ DB instance in private subnets.
- B. Configure a VPC with two private subnets and two NAT gateways across two Availability Zones. Deploy an Application Load Balancer in the private subnets.
- C. Use an Auto Scaling group to launch the EC2 instances in public subnets across two Availability Zones. Deploy an RDS Multi-AZ DB instance in private subnets.
- D. Configure a VPC with one public subnet, one private subnet, and two NAT gateways across two Availability Zones. Deploy an Application Load Balancer in the public subnet.
- E. Configure a VPC with two public subnets, two private subnets, and two NAT gateways across two Availability Zones. Deploy an Application Load Balancer in the public subnets.

Answer A for: The EC2 instances and the RDS DB instance should not be exposed to the public internet. Answer D for: The EC2 instances require internet access to complete payment processing of orders through a third-party web service. Answer A for: The application must be highly available.

### 126

A solutions architect needs to implement a solution to reduce a company's storage costs. All the company's data is in the Amazon S3 Standard storage class. The company must keep all data for at least 25 years. Data from the most recent 2 years must be highly available and immediately retrievable.
Which solution will meet these requirements?

- A. Set up an S3 Lifecycle policy to transition objects to S3 Glacier Deep Archive immediately.
- B. Set up an S3 Lifecycle policy to transition objects to S3 Glacier Deep Archive after 2 years.
- C. Use S3 Intelligent-Tiering. Activate the archiving option to ensure that data is archived in S3 Glacier Deep Archive.
- D. Set up an S3 Lifecycle policy to transition objects to S3 One Zone-Infrequent Access (S3 One Zone-IA) immediately and to S3 Glacier Deep Archive after 2 years.

### 127

A media company is evaluating the possibility of moving its systems to the AWS Cloud. The company needs at least 10 TB of storage with the maximum possible I/O performance for video processing, 300 TB of very durable storage for storing media content, and 900 TB of storage to meet requirements for archival media that is not in use anymore.
Which set of services should a solutions architect recommend to meet these requirements?

- A. Amazon EBS for maximum performance, Amazon S3 for durable data storage, and Amazon S3 Glacier for archival storage
- B. Amazon EBS for maximum performance, Amazon EFS for durable data storage, and Amazon S3 Glacier for archival storage
- C. Amazon EC2 instance store for maximum performance, Amazon EFS for durable data storage, and Amazon S3 for archival storage
- D. Amazon EC2 instance store for maximum performance, Amazon S3 for durable data storage, and Amazon S3 Glacier for archival storage

### 128

A company wants to run applications in containers in the AWS Cloud. These applications are stateless and can tolerate disruptions within the underlying infrastructure. The company needs a solution that minimizes cost and operational overhead.
What should a solutions architect do to meet these requirements?

- A. Use Spot Instances in an Amazon EC2 Auto Scaling group to run the application containers.
- B. Use Spot Instances in an Amazon Elastic Kubernetes Service (Amazon EKS) managed node group.
- C. Use On-Demand Instances in an Amazon EC2 Auto Scaling group to run the application containers.
- D. Use On-Demand Instances in an Amazon Elastic Kubernetes Service (Amazon EKS) managed node group.

### 129

A company is running a multi-tier web application on premises. The web application is containerized and runs on a number of Linux hosts connected to a PostgreSQL database that contains user records. The operational overhead of maintaining the infrastructure and capacity planning is limiting the company's growth. A solutions architect must improve the application's infrastructure.
Which combination of actions should the solutions architect take to accomplish this? (Choose two.)

- A. Migrate the PostgreSQL database to Amazon Aurora.
- B. Migrate the web application to be hosted on Amazon EC2 instances.
- C. Set up an Amazon CloudFront distribution for the web application content.
- D. Set up Amazon ElastiCache between the web application and the PostgreSQL database.
- E. Migrate the web application to be hosted on AWS Fargate with Amazon Elastic Container Service (Amazon ECS).

#### 129 해설

Aurora and Fargate are fully managed services, so they will reduce the operational overhead of maintaining the infrastructure and capacity planning.

### 130

An application runs on Amazon EC2 instances across multiple Availability Zonas. The instances run in an Amazon EC2 Auto Scaling group behind an Application Load Balancer. The application performs best when the CPU utilization of the EC2 instances is at or near 40%.
What should a solutions architect do to maintain the desired performance across all instances in the group?

- A. Use a simple scaling policy to dynamically scale the Auto Scaling group.
- B. Use a target tracking policy to dynamically scale the Auto Scaling group.
- C. Use an AWS Lambda function ta update the desired Auto Scaling group capacity.
- D. Use scheduled scaling actions to scale up and scale down the Auto Scaling group.

### 131

A company is developing a file-sharing application that will use an Amazon S3 bucket for storage. The company wants to serve all the files through an Amazon CloudFront distribution. The company does not want the files to be accessible through direct navigation to the S3 URL.
What should a solutions architect do to meet these requirements?

- A. Write individual policies for each S3 bucket to grant read permission for only CloudFront access.
- B. Create an IAM user. Grant the user read permission to objects in the S3 bucket. Assign the user to CloudFront.
- C. Write an S3 bucket policy that assigns the CloudFront distribution ID as the Principal and assigns the target S3 bucket as the Amazon Resource Name (ARN).
- D. Create an origin access identity (OAI). Assign the OAI to the CloudFront distribution. Configure the S3 bucket permissions so that only the OAI has read permission.

### 132

A company’s website provides users with downloadable historical performance reports. The website needs a solution that will scale to meet the company’s website demands globally. The solution should be cost-effective, limit the provisioning of infrastructure resources, and provide the fastest possible response time.
Which combination should a solutions architect recommend to meet these requirements?

- A. Amazon CloudFront and Amazon S3
- B. AWS Lambda and Amazon DynamoDB
- C. Application Load Balancer with Amazon EC2 Auto Scaling
- D. Amazon Route 53 with internal Application Load Balancers

### 133

A company runs an Oracle database on premises. As part of the company’s migration to AWS, the company wants to upgrade the database to the most recent available version. The company also wants to set up disaster recovery (DR) for the database. The company needs to minimize the operational overhead for normal operations and DR setup. The company also needs to maintain access to the database's underlying operating system.
Which solution will meet these requirements?

- A. Migrate the Oracle database to an Amazon EC2 instance. Set up database replication to a different AWS Region.
- B. Migrate the Oracle database to Amazon RDS for Oracle. Activate Cross-Region automated backups to replicate the snapshots to another AWS Region.
- C. Migrate the Oracle database to Amazon RDS Custom for Oracle. Create a read replica for the database in another AWS Region.
- D. Migrate the Oracle database to Amazon RDS for Oracle. Create a standby database in another Availability Zone.

#### 133 해설

Option C since RDS Custom has access to the underlying OS and it provides less operational overhead. Also, a read replica in another Region can be used for DR activities.

https://aws.amazon.com/blogs/database/implementing-a-disaster-recovery-strategy-with-amazon-rds/

### 134 다시보기

A company wants to move its application to a serverless solution. The serverless solution needs to analyze existing and new data by using SL. The company stores the data in an Amazon S3 bucket. The data requires encryption and must be replicated to a different AWS Region.
Which solution will meet these requirements with the LEAST operational overhead?

- A. Create a new S3 bucket. Load the data into the new S3 bucket. Use S3 Cross-Region Replication (CRR) to replicate encrypted objects to an S3 bucket in another Region. Use server-side encryption with AWS KMS multi-Region kays (SSE-KMS). Use Amazon Athena to query the data.
- B. Create a new S3 bucket. Load the data into the new S3 bucket. Use S3 Cross-Region Replication (CRR) to replicate encrypted objects to an S3 bucket in another Region. Use server-side encryption with AWS KMS multi-Region keys (SSE-KMS). Use Amazon RDS to query the data.
- C. Load the data into the existing S3 bucket. Use S3 Cross-Region Replication (CRR) to replicate encrypted objects to an S3 bucket in another Region. Use server-side encryption with Amazon S3 managed encryption keys (SSE-S3). Use Amazon Athena to query the data.
- D. Load the data into the existing S3 bucket. Use S3 Cross-Region Replication (CRR) to replicate encrypted objects to an S3 bucket in another Region. Use server-side encryption with Amazon S3 managed encryption keys (SSE-S3). Use Amazon RDS to query the data.

#### 134 해설

Amazon S3 Bucket Keys reduce the cost of Amazon S3 server-side encryption using AWS Key Management Service (SSE-KMS). This new bucket-level key for SSE can reduce AWS KMS request costs by up to 99 percent by decreasing the request traffic from Amazon S3 to AWS KMS. With a few clicks in the AWS Management Console, and without any changes to your client applications, you can configure your bucket to use an S3 Bucket Key for AWS KMS-based encryption on new objects.
The Existing S3 bucket might have uncrypted data - encryption will apply new data received after the applying of encryption on the new bucket.

### 135 다시보기

A company runs workloads on AWS. The company needs to connect to a service from an external provider. The service is hosted in the provider's VPC. According to the company’s security team, the connectivity must be private and must be restricted to the target service. The connection must be initiated only from the company’s VPC.
Which solution will mast these requirements?

- A. Create a VPC peering connection between the company's VPC and the provider's VPC. Update the route table to connect to the target service.
- B. Ask the provider to create a virtual private gateway in its VPC. Use AWS PrivateLink to connect to the target service.
- C. Create a NAT gateway in a public subnet of the company’s VPUpdate the route table to connect to the target service.
- D. Ask the provider to create a VPC endpoint for the target service. Use AWS PrivateLink to connect to the target service.

### 136

A company is migrating its on-premises PostgreSQL database to Amazon Aurora PostgreSQL. The on-premises database must remain online and accessible during the migration. The Aurora database must remain synchronized with the on-premises database.
Which combination of actions must a solutions architect take to meet these requirements? (Choose two.)

- A. Create an ongoing replication task.
- B. Create a database backup of the on-premises database.
- C. Create an AWS Database Migration Service (AWS DMS) replication server.
- D. Convert the database schema by using the AWS Schema Conversion Tool (AWS SCT).
- E. Create an Amazon EventBridge (Amazon CloudWatch Events) rule to monitor the database synchronization.

### 137 다시보기\_완전모르는 개념

A company uses AWS Organizations to create dedicated AWS accounts for each business unit to manage each business unit's account independently upon request. The root email recipient missed a notification that was sent to the root user email address of one account. The company wants to ensure that all future notifications are not missed. Future notifications must be limited to account administrators.
Which solution will meet these requirements?

A. Configure the company’s email server to forward notification email messages that are sent to the AWS account root user email address to all users in the organization.
B. Configure all AWS account root user email addresses as distribution lists that go to a few administrators who can respond to alerts. Configure AWS account alternate contacts in the AWS Organizations console or programmatically.
C. Configure all AWS account root user email messages to be sent to one administrator who is responsible for monitoring alerts and forwarding those alerts to the appropriate groups.
D. Configure all existing AWS accounts and all newly created accounts to use the same root user email address. Configure AWS account alternate contacts in the AWS Organizations console or programmatically.

### 138 다시보기

A company runs its ecommerce application on AWS. Every new order is published as a massage in a RabbitMQ queue that runs on an Amazon EC2 instance in a single Availability Zone. These messages are processed by a different application that runs on a separate EC2 instance. This application stores the details in a PostgreSQL database on another EC2 instance. All the EC2 instances are in the same Availability Zone.
The company needs to redesign its architecture to provide the highest availability with the least operational overhead.
What should a solutions architect do to meet these requirements?

- A. Migrate the queue to a redundant pair (active/standby) of RabbitMQ instances on Amazon MQ. Create a Multi-AZ Auto Scaling group for EC2 instances that host the application. Create another Multi-AZ Auto Scaling group for EC2 instances that host the PostgreSQL database.
- B. Migrate the queue to a redundant pair (active/standby) of RabbitMQ instances on Amazon MQ. Create a Multi-AZ Auto Scaling group for EC2 instances that host the application. Migrate the database to run on a Multi-AZ deployment of Amazon RDS for PostgreSQL.
  C. Create a Multi-AZ Auto Scaling group for EC2 instances that host the RabbitMQ queue. Create another Multi-AZ Auto Scaling group for EC2 instances that host the application. Migrate the database to run on a Multi-AZ deployment of Amazon RDS for PostgreSQL.
  D. Create a Multi-AZ Auto Scaling group for EC2 instances that host the RabbitMQ queue. Create another Multi-AZ Auto Scaling group for EC2 instances that host the application. Create a third Multi-AZ Auto Scaling group for EC2 instances that host the PostgreSQL database

#### 138 해설

Migrating to Amazon MQ reduces the overhead on the queue management. C and D are dismissed.
Deciding between A and B means deciding to go for an AutoScaling group for EC2 or an RDS for Postgress (both multi- AZ). The RDS option has less operational impact, as provide as a service the tools and software required. Consider for instance, the effort to add an additional node like a read replica, to the DB.
https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/active-standby-broker-deployment.html
https://aws.amazon.com/rds/postgresql/

### 139

A reporting team receives files each day in an Amazon S3 bucket. The reporting team manually reviews and copies the files from this initial S3 bucket to an analysis S3 bucket each day at the same time to use with Amazon QuickSight. Additional teams are starting to send more files in larger sizes to the initial S3 bucket.
The reporting team wants to move the files automatically analysis S3 bucket as the files enter the initial S3 bucket. The reporting team also wants to use AWS Lambda functions to run pattern-matching code on the copied data. In addition, the reporting team wants to send the data files to a pipeline in Amazon SageMaker Pipelines.
What should a solutions architect do to meet these requirements with the LEAST operational overhead?

- A. Create a Lambda function to copy the files to the analysis S3 bucket. Create an S3 event notification for the analysis S3 bucket. Configure Lambda and SageMaker Pipelines as destinations of the event notification. Configure s3:ObjectCreated:Put as the event type.
- B. Create a Lambda function to copy the files to the analysis S3 bucket. Configure the analysis S3 bucket to send event notifications to Amazon EventBridge (Amazon CloudWatch Events). Configure an ObjectCreated rule in EventBridge (CloudWatch Events). Configure Lambda and SageMaker Pipelines as targets for the rule.
- C. Configure S3 replication between the S3 buckets. Create an S3 event notification for the analysis S3 bucket. Configure Lambda and SageMaker Pipelines as destinations of the event notification. Configure s3:ObjectCreated:Put as the event type.
- D. Configure S3 replication between the S3 buckets. Configure the analysis S3 bucket to send event notifications to Amazon EventBridge (Amazon CloudWatch Events). Configure an ObjectCreated rule in EventBridge (CloudWatch Events). Configure Lambda and SageMaker Pipelines as targets for the rule.

### 140

A solutions architect needs to help a company optimize the cost of running an application on AWS. The application will use Amazon EC2 instances, AWS Fargate, and AWS Lambda for compute within the architecture.
The EC2 instances will run the data ingestion layer of the application. EC2 usage will be sporadic and unpredictable. Workloads that run on EC2 instances can be interrupted at any time. The application front end will run on Fargate, and Lambda will serve the API layer. The front-end utilization and API layer utilization will be predictable over the course of the next year.
Which combination of purchasing options will provide the MOST cost-effective solution for hosting this application? (Choose two.)

- A. Use Spot Instances for the data ingestion layer
- B. Use On-Demand Instances for the data ingestion layer
- C. Purchase a 1-year Compute Savings Plan for the front end and API layer.
- D. Purchase 1-year All Upfront Reserved instances for the data ingestion layer.
- E. Purchase a 1-year EC2 instance Savings Plan for the front end and API layer.

#### 140

EC2 instance Savings Plan saves 72% while Compute Savings Plans saves 66%. But according to link, it says "Compute Savings Plans provide the most flexibility and help to reduce your costs by up to 66%. These plans automatically apply to EC2 instance usage regardless of instance family, size, AZ, region, OS or tenancy, and also apply to Fargate and Lambda usage." EC2 instance Savings Plans are not applied to Fargate or Lambda

### 141 다시보기 cloudfront

A company runs a web-based portal that provides users with global breaking news, local alerts, and weather updates. The portal delivers each user a personalized view by using mixture of static and dynamic content. Content is served over HTTPS through an API server running on an Amazon EC2 instance behind an Application Load Balancer (ALB). The company wants the portal to provide this content to its users across the world as quickly as possible.
How should a solutions architect design the application to ensure the LEAST amount of latency for all users?

- A. Deploy the application stack in a single AWS Region. Use Amazon CloudFront to serve all static and dynamic content by specifying the ALB as an origin.
- B. Deploy the application stack in two AWS Regions. Use an Amazon Route 53 latency routing policy to serve all content from the ALB in the closest Region.
- C. Deploy the application stack in a single AWS Region. Use Amazon CloudFront to serve the static content. Serve the dynamic content directly from the ALB.
- D. Deploy the application stack in two AWS Regions. Use an Amazon Route 53 geolocation routing policy to serve all content from the ALB in the closest Region.

### 142

A gaming company is designing a highly available architecture. The application runs on a modified Linux kernel and supports only UDP-based traffic. The company needs the front-end tier to provide the best possible user experience. That tier must have low latency, route traffic to the nearest edge location, and provide static IP addresses for entry into the application endpoints.
What should a solutions architect do to meet these requirements?

- A. Configure Amazon Route 53 to forward requests to an Application Load Balancer. Use AWS Lambda for the application in AWS Application Auto Scaling.
- B. Configure Amazon CloudFront to forward requests to a Network Load Balancer. Use AWS Lambda for the application in an AWS Application Auto Scaling group.
- C. Configure AWS Global Accelerator to forward requests to a Network Load Balancer. Use Amazon EC2 instances for the application in an EC2 Auto Scaling group.
- D. Configure Amazon API Gateway to forward requests to an Application Load Balancer. Use Amazon EC2 instances for the application in an EC2 Auto Scaling group.

### 143

A company wants to migrate its existing on-premises monolithic application to AWS. The company wants to keep as much of the front-end code and the backend code as possible. **However, the company wants to break the application into smaller applications.** A different team will manage each application. The company needs a highly scalable solution that minimizes operational overhead.
Which solution will meet these requirements?

- A. Host the application on AWS Lambda. Integrate the application with Amazon API Gateway.
- B. Host the application with AWS Amplify. Connect the application to an Amazon API Gateway API that is integrated with AWS Lambda.
- C. Host the application on Amazon EC2 instances. Set up an Application Load Balancer with EC2 instances in an Auto Scaling group as targets.
- D. Host the application on Amazon Elastic Container Service (Amazon ECS). Set up an Application Load Balancer with Amazon ECS as the target.

### 144

A company recently started using Amazon Aurora as the data store for its global ecommerce application. When large reports are run, developers report that the ecommerce application is performing poorly. After reviewing metrics in Amazon CloudWatch, a solutions architect finds that the ReadIOPS and CPUUtilizalion metrics are spiking when monthly reports run.
What is the MOST cost-effective solution?

- A. Migrate the monthly reporting to Amazon Redshift.
- B. Migrate the monthly reporting to an Aurora Replica.
- C. Migrate the Aurora database to a larger instance class.
- D. Increase the Provisioned IOPS on the Aurora instance.

#### 144 해설

**Aurora Replicas** utilize the same storage as the primary instance so there is no additional storage cost.
Replicas can be created and destroyed easily to match reporting needs.
The primary Aurora instance size does not need to be changed, avoiding additional cost.
Workload is offloaded from the primary instance, improving its performance.
No major software/configuration changes needed compared to options like Redshift.

### 145

A company hosts a website analytics application on a single Amazon EC2 On-Demand Instance. The analytics software is written in PHP and uses a MySQL database. The analytics software, the web server that provides PHP, and the database server are all hosted on the EC2 instance. The application is showing signs of performance degradation during busy times and is presenting 5xx errors. The company needs to make the application scale seamlessly.
Which solution will meet these requirements MOST cost-effectively?

- A. Migrate the database to an Amazon RDS for MySQL DB instance. Create an AMI of the web application. Use the AMI to launch a second EC2 On-Demand Instance. Use an Application Load Balancer to distribute the load to each EC2 instance.
- B. Migrate the database to an Amazon RDS for MySQL DB instance. Create an AMI of the web application. Use the AMI to launch a second EC2 On-Demand Instance. Use Amazon Route 53 weighted routing to distribute the load across the two EC2 instances.
- C. Migrate the database to an Amazon Aurora MySQL DB instance. Create an AWS Lambda function to stop the EC2 instance and change the instance type. Create an Amazon CloudWatch alarm to invoke the Lambda function when CPU utilization surpasses 75%.
- D. Migrate the database to an Amazon Aurora MySQL DB instance. Create an AMI of the web application. Apply the AMI to a launch template. Create an Auto Scaling group with the launch template Configure the launch template to use a Spot Fleet. Attach an Application Load Balancer to the Auto Scaling group.

#### 145 해설

I was tempted to pick A but then I realized there are two key requirements:

- scale seamlessly
- cost-effectively

None of A-C give seamless scalability. A and B are about adding second instance (which I assume does not match to "scale seamlessly"). C is about changing instance type.

Therefore D is only workable solution to the scalability requirement

### 146

A company runs a stateless web application in production on a group of Amazon EC2 On-Demand Instances behind an Application Load Balancer. The application experiences heavy usage during an 8-hour period each business day. Application usage is moderate and steady overnight. Application usage is low during weekends.
The company wants to minimize its EC2 costs without affecting the availability of the application.
Which solution will meet these requirements?

- A. Use Spot Instances for the entire workload.
- B. Use Reserved Instances for the baseline level of usage. Use Spot instances for any additional capacity that the application needs.
- C. Use On-Demand Instances for the baseline level of usage. Use Spot Instances for any additional capacity that the application needs.
- D. Use Dedicated Instances for the baseline level of usage. Use On-Demand Instances for any additional capacity that the application needs.

### 147

A company needs to retain application log files for a critical application for 10 years. The application team regularly accesses logs from the past month for troubleshooting, but logs older than 1 month are rarely accessed. The application generates more than 10 TB of logs per month.
Which storage option meets these requirements MOST cost-effectively?

- A. Store the logs in Amazon S3. Use AWS Backup to move logs more than 1 month old to S3 Glacier Deep Archive.
- B. Store the logs in Amazon S3. Use S3 Lifecycle policies to move logs more than 1 month old to S3 Glacier Deep Archive.
- C. Store the logs in Amazon CloudWatch Logs. Use AWS Backup to move logs more than 1 month old to S3 Glacier Deep Archive.
- D. Store the logs in Amazon CloudWatch Logs. Use Amazon S3 Lifecycle policies to move logs more than 1 month old to S3 Glacier Deep Archive.

### 148

A company has a data ingestion workflow that includes the following components:
An Amazon Simple Notification Service (Amazon SNS) topic that receives notifications about new data deliveries
An AWS Lambda function that processes and stores the data
The ingestion workflow occasionally fails because of network connectivity issues. When failure occurs, the corresponding data is not ingested unless the company manually reruns the job.
What should a solutions architect do to ensure that all notifications are eventually processed?

- A. Configure the Lambda function for deployment across multiple Availability Zones.
- B. Modify the Lambda function's configuration to increase the CPU and memory allocations for the function.
- C. Configure the SNS topic’s retry strategy to increase both the number of retries and the wait time between retries.
- D. Configure an Amazon Simple Queue Service (Amazon SQS) queue as the on-failure destination. Modify the Lambda function to process messages in the queue.

### 149

A company has a service that produces event data. The company wants to use AWS to process the event data as it is received. The data is written in a specific order that must be maintained throughout processing. The company wants to implement a solution that minimizes operational overhead.
How should a solutions architect accomplish this?

- A. Create an Amazon Simple Queue Service (Amazon SQS) FIFO queue to hold messages. Set up an AWS Lambda function to process messages from the queue.
- B. Create an Amazon Simple Notification Service (Amazon SNS) topic to deliver notifications containing payloads to process. Configure an AWS Lambda function as a subscriber.
- C. Create an Amazon Simple Queue Service (Amazon SQS) standard queue to hold messages. Set up an AWS Lambda function to process messages from the queue independently.
- D. Create an Amazon Simple Notification Service (Amazon SNS) topic to deliver notifications containing payloads to process. Configure an Amazon Simple Queue Service (Amazon SQS) queue as a subscriber.

### 150

A company is migrating an application from on-premises servers to Amazon EC2 instances. As part of the migration design requirements, a solutions architect must implement infrastructure metric alarms. The company does not need to take action if CPU utilization increases to more than 50% for a short burst of time. However, if the CPU utilization increases to more than 50% and read IOPS on the disk are high at the same time, the company needs to act as soon as possible. The solutions architect also must reduce false alarms.
What should the solutions architect do to meet these requirements?

- A. Create Amazon CloudWatch composite alarms where possible.
- B. Create Amazon CloudWatch dashboards to visualize the metrics and react to issues quickly.
- C. Create Amazon CloudWatch Synthetics canaries to monitor the application and raise an alarm.
- D. Create single Amazon CloudWatch metric alarms with multiple metric thresholds where possible.

#### 150 해설

Composite alarms determine their states by monitoring the states of other alarms. You can **use composite alarms to reduce alarm noise**. For example, you can create a composite alarm where the underlying metric alarms go into ALARM when they meet specific conditions. You then can set up your composite alarm to go into ALARM and send you notifications when the underlying metric alarms go into ALARM by configuring the underlying metric alarms never to take actions. Currently, composite alarms can take the following actions:
https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Composite_Alarm.html

### 151

A company wants to migrate its on-premises data center to AWS. According to the company's compliance requirements, the company can use only the ap-northeast-3 Region. Company administrators are not permitted to connect VPCs to the internet.
Which solutions will meet these requirements? (Choose two.)

- A. Use AWS Control Tower to implement data residency guardrails to deny internet access and deny access to all AWS Regions except ap-northeast-3.
- B. Use rules in AWS WAF to prevent internet access. Deny access to all AWS Regions except ap-northeast-3 in the AWS account settings.
- C. Use AWS Organizations to configure service control policies (SCPS) that prevent VPCs from gaining internet access. Deny access to all AWS Regions except ap-northeast-3.
- D. Create an outbound rule for the network ACL in each VPC to deny all traffic from 0.0.0.0/0. Create an IAM policy for each user to prevent the use of any AWS Region other than ap-northeast-3.
- E. Use AWS Config to activate managed rules to detect and alert for internet gateways and to detect and alert for new resources deployed outside of ap-northeast-3.

### 152

A company uses a three-tier web application to provide training to new employees. The application is accessed for only 12 hours every day. The company is using an Amazon RDS for MySQL DB instance to store information and wants to minimize costs.
What should a solutions architect do to meet these requirements?

- A. Configure an IAM policy for AWS Systems Manager Session Manager. Create an IAM role for the policy. Update the trust relationship of the role. Set up automatic start and stop for the DB instance.
- B. Create an Amazon ElastiCache for Redis cache cluster that gives users the ability to access the data from the cache when the DB instance is stopped. Invalidate the cache after the DB instance is started.
- C. Launch an Amazon EC2 instance. Create an IAM role that grants access to Amazon RDS. Attach the role to the EC2 instance. Configure a cron job to start and stop the EC2 instance on the desired schedule.
- D. Create AWS Lambda functions to start and stop the DB instance. Create Amazon EventBridge (Amazon CloudWatch Events) scheduled rules to invoke the Lambda functions. Configure the Lambda functions as event targets for the rules.

#### 152 해설

https://aws.amazon.com/blogs/database/schedule-amazon-rds-stop-and-start-using-aws-lambda/

It is option D. Option A could have been applicable had it been AWS Systems Manager State Manager & not AWS Systems Manager Session Manager

### 153

A company sells ringtones created from clips of popular songs. The files containing the ringtones are stored in Amazon S3 Standard and are at least 128 KB in size. The company has millions of files, but downloads are infrequent for ringtones older than 90 days. The company needs to save money on storage while keeping the most accessed files readily available for its users.
Which action should the company take to meet these requirements MOST cost-effectively?

- A. Configure S3 Standard-Infrequent Access (S3 Standard-IA) storage for the initial storage tier of the objects.
- B. Move the files to S3 Intelligent-Tiering and configure it to move objects to a less expensive storage tier after 90 days.
- C. Configure S3 inventory to manage objects and move them to S3 Standard-Infrequent Access (S3 Standard-1A) after 90 days.
- D. Implement an S3 Lifecycle policy that moves the objects from S3 Standard to S3 Standard-Infrequent Access (S3 Standard-1A) after 90 days.

#### 153 해설

Intelligent-Tiering은 unknown pattern이 나타날 경우 사용. 이 문제는 D가 보다 적합할듯

### 154

A company needs to save the results from a medical trial to an Amazon S3 repository. The repository must allow a few scientists to add new files and must restrict all other users to read-only access. No users can have the ability to modify or delete any files in the repository. The company must keep every file in the repository for a minimum of 1 year after its creation date.
Which solution will meet these requirements?

- A. Use S3 Object Lock in governance mode with a legal hold of 1 year.
- B. Use S3 Object Lock in compliance mode with a retention period of 365 days.
- C. Use an IAM role to restrict all users from deleting or changing objects in the S3 bucket. Use an S3 bucket policy to only allow the IAM role.
- D. Configure the S3 bucket to invoke an AWS Lambda function every time an object is added. Configure the function to track the hash of the saved object so that modified objects can be marked accordingly.

### 155

A large media company hosts a web application on AWS. The company wants to start caching confidential media files so that users around the world will have reliable access to the files. The content is stored in Amazon S3 buckets. The company must deliver the content quickly, regardless of where the requests originate geographically.
Which solution will meet these requirements?

- A. Use AWS DataSync to connect the S3 buckets to the web application.
- B. Deploy AWS Global Accelerator to connect the S3 buckets to the web application.
- C. Deploy Amazon CloudFront to connect the S3 buckets to CloudFront edge servers.
- D. Use Amazon Simple Queue Service (Amazon SQS) to connect the S3 buckets to the web application.

#### 155 해설

Amazon CloudFront is a content delivery network (CDN) that caches content at edge locations around the world.
Connecting the S3 buckets containing the media files to CloudFront will cache the content at global edge locations.
This provides fast reliable access to users everywhere by serving content from the nearest edge location.
CloudFront integrates tightly with S3 for secure, durable storage.
Global Accelerator improves availability and performance for TCP/UDP traffic, not HTTP-based content delivery.
DataSync and SQS are not technologies for a global CDN like CloudFront.

### 156 다시보기

A company produces batch data that comes from different databases. The company also produces live stream data from network sensors and application APIs. The company needs to consolidate all the data into one place for business analytics. The company needs to process the incoming data and then stage the data in different Amazon S3 buckets. Teams will later run one-time queries and import the data into a business intelligence tool to show key performance indicators (KPIs).
Which combination of steps will meet these requirements with the LEAST operational overhead? (Choose two.)

- A. Use Amazon Athena for one-time queries. Use Amazon QuickSight to create dashboards for KPIs.
- B. Use Amazon Kinesis Data Analytics for one-time queries. Use Amazon QuickSight to create dashboards for KPIs.
- C. Create custom AWS Lambda functions to move the individual records from the databases to an Amazon Redshift cluster.
- D. Use an AWS Glue extract, transform, and load (ETL) job to convert the data into JSON format. Load the data into multiple Amazon OpenSearch Service (Amazon Elasticsearch Service) clusters.
- E. Use blueprints in AWS Lake Formation to identify the data that can be ingested into a data lake. Use AWS Glue to crawl the source, extract the data, and load the data into Amazon S3 in Apache Parquet format.

#### 156 해설

A - Manual task that can be automated, so why make life difficult?
B - The maximum retention period is 35 days, so would not help
C - The maximum retention period is 35 days, so would not help
D - Only option that deals with logs, so makes sense
E - Partially manual but only option that achieves the 5 year goal

### 157

A company stores data in an Amazon Aurora PostgreSQL DB cluster. The company must store all the data for 5 years and must delete all the data after 5 years. The company also must indefinitely keep audit logs of actions that are performed within the database. Currently, the company has automated backups configured for Aurora.

Which combination of steps should a solutions architect take to meet these requirements? (Choose two.)

- A. Take a manual snapshot of the DB cluster.
- B. Create a lifecycle policy for the automated backups.
- C. Configure automated backup retention for 5 years.
- D. Configure an Amazon CloudWatch Logs export for the DB cluster.
- E. Use AWS Backup to take the backups and to keep the backups for 5 years.

### 158 다시보기

A solutions architect is optimizing a website for an upcoming musical event. Videos of the performances will be streamed in real time and then will be available on demand. The event is expected to attract a global online audience.

Which service will improve the performance of both the real-time and on-demand streaming?

- A. Amazon CloudFront
- B. AWS Global Accelerator
- C. Amazon Route 53
- D. Amazon S3 Transfer Acceleration

### 159

A company is running a publicly accessible serverless application that uses Amazon API Gateway and AWS Lambda. The application’s traffic recently spiked due to fraudulent requests from botnets.

Which steps should a solutions architect take to block requests from unauthorized users? (Choose two.)

- A. Create a usage plan with an API key that is shared with genuine users only.
- B. Integrate logic within the Lambda function to ignore the requests from fraudulent IP addresses.
- C. Implement an AWS WAF rule to target malicious requests and trigger actions to filter them out.
- D. Convert the existing public API to a private API. Update the DNS records to redirect users to the new API endpoint.
- E. Create an IAM role for each user attempting to access the API. A user will assume the role when making the API call.

### 160

An ecommerce company hosts its analytics application in the AWS Cloud. The application generates about 300 MB of data each month. The data is stored in JSON format. The company is evaluating a disaster recovery solution to back up the data. The data must be accessible in milliseconds if it is needed, and the data must be kept for 30 days.

Which solution meets these requirements MOST cost-effectively?

- A. Amazon OpenSearch Service (Amazon Elasticsearch Service)
- B. Amazon S3 Glacier
- C. Amazon S3 Standard
- D. Amazon RDS for PostgreSQL

### 161

A company has a small Python application that processes JSON documents and outputs the results to an on-premises SQL database. The application runs thousands of times each day. The company wants to move the application to the AWS Cloud. The company needs a highly available solution that maximizes scalability and minimizes operational overhead.

Which solution will meet these requirements?

- A. Place the JSON documents in an Amazon S3 bucket. Run the Python code on multiple Amazon EC2 instances to process the documents. Store the results in an Amazon Aurora DB cluster.
- B. Place the JSON documents in an Amazon S3 bucket. Create an AWS Lambda function that runs the Python code to process the documents as they arrive in the S3 bucket. Store the results in an Amazon Aurora DB cluster.
- C. Place the JSON documents in an Amazon Elastic Block Store (Amazon EBS) volume. Use the EBS Multi-Attach feature to attach the volume to multiple Amazon EC2 instances. Run the Python code on the EC2 instances to process the documents. Store the results on an Amazon RDS DB instance.
- D. Place the JSON documents in an Amazon Simple Queue Service (Amazon SQS) queue as messages. Deploy the Python code as a container on an Amazon Elastic Container Service (Amazon ECS) cluster that is configured with the Amazon EC2 launch type. Use the container to process the SQS messages. Store the results on an Amazon RDS DB instance

### 162

A company wants to use high performance computing (HPC) infrastructure on AWS for financial risk modeling. The company’s HPC workloads run on Linux. Each HPC workflow runs on hundreds of Amazon EC2 Spot Instances, is short-lived, and generates thousands of output files that are ultimately stored in persistent storage for analytics and long-term future use.

The company seeks a cloud storage solution that permits the copying of on-premises data to long-term persistent storage to make data available for processing by all EC2 instances. The solution should also be a high performance file system that is integrated with persistent storage to read and write datasets and output files.

Which combination of AWS services meets these requirements?

- A. Amazon FSx for Lustre integrated with Amazon S3
- B. Amazon FSx for Windows File Server integrated with Amazon S3
- C. Amazon S3 Glacier integrated with Amazon Elastic Block Store (Amazon EBS)
- D. Amazon S3 bucket with a VPC endpoint integrated with an Amazon Elastic Block Store (Amazon EBS) General Purpose SSD (gp2) volume

### 163

A company is building a containerized application on premises and decides to move the application to AWS. The application will have thousands of users soon after it is deployed. The company is unsure how to manage the deployment of containers at scale. The company needs to deploy the containerized application in a highly available architecture that minimizes operational overhead.

Which solution will meet these requirements?

- A. Store container images in an Amazon Elastic Container Registry (Amazon ECR) repository. Use an Amazon Elastic Container Service (Amazon ECS) cluster with the AWS Fargate launch type to run the containers. Use target tracking to scale automatically based on demand.
- B. Store container images in an Amazon Elastic Container Registry (Amazon ECR) repository. Use an Amazon Elastic Container Service (Amazon ECS) cluster with the Amazon EC2 launch type to run the containers. Use target tracking to scale automatically based on demand.
- C. Store container images in a repository that runs on an Amazon EC2 instance. Run the containers on EC2 instances that are spread across multiple Availability Zones. Monitor the average CPU utilization in Amazon CloudWatch. Launch new EC2 instances as needed.
- D. Create an Amazon EC2 Amazon Machine Image (AMI) that contains the container image. Launch EC2 instances in an Auto Scaling group across multiple Availability Zones. Use an Amazon CloudWatch alarm to scale out EC2 instances when the average CPU utilization threshold is breached.

### 164

A company has two applications: a sender application that sends messages with payloads to be processed and a processing application intended to receive the messages with payloads. The company wants to implement an AWS service to handle messages between the two applications. The sender application can send about 1,000 messages each hour. The messages may take up to 2 days to be processed: If the messages fail to process, they must be retained so that they do not impact the processing of any remaining messages.

Which solution meets these requirements and is the MOST operationally efficient?

- A. Set up an Amazon EC2 instance running a Redis database. Configure both applications to use the instance. Store, process, and delete the messages, respectively.
- B. Use an Amazon Kinesis data stream to receive the messages from the sender application. Integrate the processing application with the Kinesis Client Library (KCL).
- C. Integrate the sender and processor applications with an Amazon Simple Queue Service (Amazon SQS) queue. Configure a dead-letter queue to collect the messages that failed to process.
- D. Subscribe the processing application to an Amazon Simple Notification Service (Amazon SNS) topic to receive notifications to process. Integrate the sender application to write to the SNS topic.

### 165

A solutions architect must design a solution that uses Amazon CloudFront with an Amazon S3 origin to store a static website. The company’s security policy requires that all website traffic be inspected by AWS WAF.

How should the solutions architect comply with these requirements?

A. Configure an S3 bucket policy to accept requests coming from the AWS WAF Amazon Resource Name (ARN) only.
B. Configure Amazon CloudFront to forward all incoming requests to AWS WAF before requesting content from the S3 origin.
C. Configure a security group that allows Amazon CloudFront IP addresses to access Amazon S3 only. Associate AWS WAF to CloudFront.
D. Configure Amazon CloudFront and Amazon S3 to use an origin access identity (OAI) to restrict access to the S3 bucket. Enable AWS WAF on the distribution.

### 166

Organizers for a global event want to put daily reports online as static HTML pages. The pages are expected to generate millions of views from users around the world. The files are stored in an Amazon S3 bucket. A solutions architect has been asked to design an efficient and effective solution.

Which action should the solutions architect take to accomplish this?

- A. Generate presigned URLs for the files.
- B. Use cross-Region replication to all Regions.
- C. Use the geoproximity feature of Amazon Route 53.
- D. Use Amazon CloudFront with the S3 bucket as its origin.

### 167

A company runs a production application on a fleet of Amazon EC2 instances. The application reads the data from an Amazon SQS queue and processes the messages in parallel. The message volume is unpredictable and often has intermittent traffic. This application should continually process messages without any downtime.

Which solution meets these requirements MOST cost-effectively?

- A. Use Spot Instances exclusively to handle the maximum capacity required.
- B. Use Reserved Instances exclusively to handle the maximum capacity required.
- C. Use Reserved Instances for the baseline capacity and use Spot Instances to handle additional capacity.
- D. Use Reserved Instances for the baseline capacity and use On-Demand Instances to handle additional capacity.

### 168

A security team wants to limit access to specific services or actions in all of the team’s AWS accounts. All accounts belong to a large organization in AWS Organizations. The solution must be scalable and there must be a single point where permissions can be maintained.

What should a solutions architect do to accomplish this?

- A. Create an ACL to provide access to the services or actions.
- B. Create a security group to allow accounts and attach it to user groups.
- C. Create cross-account roles in each account to deny access to the services or actions.
- D. Create a service control policy in the root organizational unit to deny access to the services or actions.

### 169

A company is concerned about the security of its public web application due to recent web attacks. The application uses an Application Load Balancer (ALB). A solutions architect must reduce the risk of DDoS attacks against the application.

What should the solutions architect do to meet this requirement?

- A. Add an Amazon Inspector agent to the ALB.
- B. Configure Amazon Macie to prevent attacks.
- C. Enable AWS Shield Advanced to prevent attacks.
- D. Configure Amazon GuardDuty to monitor the ALB.

### 170

A company’s web application is running on Amazon EC2 instances behind an Application Load Balancer. The company recently changed its policy, which now requires the application to be accessed from one specific country only.

Which configuration will meet this requirement?

- A. Configure the security group for the EC2 instances.
- B. Configure the security group on the Application Load Balancer.
- C. Configure AWS WAF on the Application Load Balancer in a VPC.
- D. Configure the network ACL for the subnet that contains the EC2 instances.

### 171

A company provides an API to its users that automates inquiries for tax computations based on item prices. The company experiences a larger number of inquiries during the holiday season only that cause slower response times. A solutions architect needs to design a solution that is scalable and elastic.

What should the solutions architect do to accomplish this?

- A. Provide an API hosted on an Amazon EC2 instance. The EC2 instance performs the required computations when the API request is made.
- B. Design a REST API using Amazon API Gateway that accepts the item names. API Gateway passes item names to AWS Lambda for tax computations.
- C. Create an Application Load Balancer that has two Amazon EC2 instances behind it. The EC2 instances will compute the tax on the received item names.
- D. Design a REST API using Amazon API Gateway that connects with an API hosted on an Amazon EC2 instance. API Gateway accepts and passes the item names to the EC2 instance for tax computations.

### 172

A solutions architect is creating a new Amazon CloudFront distribution for an application. Some of the information submitted by users is sensitive. The application uses HTTPS but needs another layer of security. The sensitive information should.be protected throughout the entire application stack, and access to the information should be restricted to certain applications.

Which action should the solutions architect take?

- A. Configure a CloudFront signed URL.
- B. Configure a CloudFront signed cookie.
- C. Configure a CloudFront field-level encryption profile.
- D. Configure CloudFront and set the Origin Protocol Policy setting to HTTPS Only for the Viewer Protocol Policy.

### 173

A gaming company hosts a browser-based application on AWS. The users of the application consume a large number of videos and images that are stored in Amazon S3. This content is the same for all users.

The application has increased in popularity, and millions of users worldwide accessing these media files. The company wants to provide the files to the users while reducing the load on the origin.

Which solution meets these requirements MOST cost-effectively?

- A. Deploy an AWS Global Accelerator accelerator in front of the web servers.
- B. Deploy an Amazon CloudFront web distribution in front of the S3 bucket.
- C. Deploy an Amazon ElastiCache for Redis instance in front of the web servers.
- D. Deploy an Amazon ElastiCache for Memcached instance in front of the web servers.

### 174

A company has a multi-tier application that runs six front-end web servers in an Amazon EC2 Auto Scaling group in a single Availability Zone behind an Application Load Balancer (ALB). A solutions architect needs to modify the infrastructure to be highly available without modifying the application.

Which architecture should the solutions architect choose that provides high availability?

- A. Create an Auto Scaling group that uses three instances across each of two Regions.
- B. Modify the Auto Scaling group to use three instances across each of two Availability Zones.
- C. Create an Auto Scaling template that can be used to quickly create more instances in another Region.
- D. Change the ALB in front of the Amazon EC2 instances in a round-robin configuration to balance traffic to the web tier.

### 175

An ecommerce company has an order-processing application that uses Amazon API Gateway and an AWS Lambda function. The application stores data in an Amazon Aurora PostgreSQL database. During a recent sales event, a sudden surge in customer orders occurred. Some customers experienced timeouts, and the application did not process the orders of those customers.

A solutions architect determined that the CPU utilization and memory utilization were high on the database because of a large number of open connections. The solutions architect needs to prevent the timeout errors while making the least possible changes to the application.

Which solution will meet these requirements?

- A. Configure provisioned concurrency for the Lambda function. Modify the database to be a global database in multiple AWS Regions.
- B. Use Amazon RDS Proxy to create a proxy for the database. Modify the Lambda function to use the RDS Proxy endpoint instead of the database endpoint.
- C. Create a read replica for the database in a different AWS Region. Use query string parameters in API Gateway to route traffic to the read replica.
- D. Migrate the data from Aurora PostgreSQL to Amazon DynamoDB by using AWS Database Migration Service (AWS DMS). Modify the Lambda function to use the DynamoDB table.

### 176

An application runs on Amazon EC2 instances in private subnets. The application needs to access an Amazon DynamoDB table.

What is the MOST secure way to access the table while ensuring that the traffic does not leave the AWS network?

- A. Use a VPC endpoint for DynamoDB.
- B. Use a NAT gateway in a public subnet.
- C. Use a NAT instance in a private subnet.
- D. Use the internet gateway attached to the VPC.

### 177

An entertainment company is using Amazon DynamoDB to store media metadata. The application is read intensive and experiencing delays. The company does not have staff to handle additional operational overhead and needs to improve the performance efficiency of DynamoDB without reconfiguring the application.

What should a solutions architect recommend to meet this requirement?

- A. Use Amazon ElastiCache for Redis.
- B. Use Amazon DynamoDB Accelerator (DAX).
- C. Replicate data by using DynamoDB global tables.
- D. Use Amazon ElastiCache for Memcached with Auto Discovery enabled.

### 178

A company’s infrastructure consists of Amazon EC2 instances and an Amazon RDS DB instance in a single AWS Region. The company wants to back up its data in a separate Region.

Which solution will meet these requirements with the LEAST operational overhead?

- A. Use AWS Backup to copy EC2 backups and RDS backups to the separate Region.
- B. Use Amazon Data Lifecycle Manager (Amazon DLM) to copy EC2 backups and RDS backups to the separate Region.
- C. Create Amazon Machine Images (AMIs) of the EC2 instances. Copy the AMIs to the separate Region. Create a read replica for the RDS DB instance in the separate Region.
- D. Create Amazon Elastic Block Store (Amazon EBS) snapshots. Copy the EBS snapshots to the separate Region. Create RDS snapshots. Export the RDS snapshots to Amazon S3. Configure S3 Cross-Region Replication (CRR) to the separate Region.

### 179

A solutions architect needs to securely store a database user name and password that an application uses to access an Amazon RDS DB instance. The application that accesses the database runs on an Amazon EC2 instance. The solutions architect wants to create a secure parameter in AWS Systems Manager Parameter Store.

What should the solutions architect do to meet this requirement?

- A. Create an IAM role that has read access to the Parameter Store parameter. Allow Decrypt access to an AWS Key Management Service (AWS KMS) key that is used to encrypt the parameter. Assign this IAM role to the EC2 instance.
- B. Create an IAM policy that allows read access to the Parameter Store parameter. Allow Decrypt access to an AWS Key Management Service (AWS KMS) key that is used to encrypt the parameter. Assign this IAM policy to the EC2 instance.
- C. Create an IAM trust relationship between the Parameter Store parameter and the EC2 instance. Specify Amazon RDS as a principal in the trust policy.
- D. Create an IAM trust relationship between the DB instance and the EC2 instance. Specify Systems Manager as a principal in the trust policy.

### 180

A company is designing a cloud communications platform that is driven by APIs. The application is hosted on Amazon EC2 instances behind a Network Load Balancer (NLB). The company uses Amazon API Gateway to provide external users with access to the application through APIs. The company wants to protect the platform against web exploits like SQL injection and also wants to detect and mitigate large, sophisticated DDoS attacks.

Which combination of solutions provides the MOST protection? (Choose two.)

- A. Use AWS WAF to protect the NLB.
- B. Use AWS Shield Advanced with the NLB.
- C. Use AWS WAF to protect Amazon API Gateway.
- D. Use Amazon GuardDuty with AWS Shield Standard
- E. Use AWS Shield Standard with Amazon API Gateway.

### 181

A company has a legacy data processing application that runs on Amazon EC2 instances. Data is processed sequentially, but the order of results does not matter. The application uses a monolithic architecture. The only way that the company can scale the application to meet increased demand is to increase the size of the instances.

The company’s developers have decided to rewrite the application to use a microservices architecture on Amazon Elastic Container Service (Amazon ECS).

What should a solutions architect recommend for communication between the microservices?

- A. Create an Amazon Simple Queue Service (Amazon SQS) queue. Add code to the data producers, and send data to the queue. Add code to the data consumers to process data from the queue.
- B. Create an Amazon Simple Notification Service (Amazon SNS) topic. Add code to the data producers, and publish notifications to the topic. Add code to the data consumers to subscribe to the topic.
- C. Create an AWS Lambda function to pass messages. Add code to the data producers to call the Lambda function with a data object. Add code to the data consumers to receive a data object that is passed from the Lambda function.
- D. Create an Amazon DynamoDB table. Enable DynamoDB Streams. Add code to the data producers to insert data into the table. Add code to the data consumers to use the DynamoDB Streams API to detect new table entries and retrieve the data.

### 182

A company wants to migrate its MySQL database from on premises to AWS. The company recently experienced a database outage that significantly impacted the business. To ensure this does not happen again, the company wants a reliable database solution on AWS that minimizes data loss and stores every transaction on at least two nodes.

Which solution meets these requirements?

- A. Create an Amazon RDS DB instance with synchronous replication to three nodes in three Availability Zones.
- B. Create an Amazon RDS MySQL DB instance with Multi-AZ functionality enabled to synchronously replicate the data.
- C. Create an Amazon RDS MySQL DB instance and then create a read replica in a separate AWS Region that synchronously replicates the data.
- D. Create an Amazon EC2 instance with a MySQL engine installed that triggers an AWS Lambda function to synchronously replicate the data to an Amazon RDS MySQL DB instance.

### 183

A company is building a new dynamic ordering website. The company wants to minimize server maintenance and patching. The website must be highly available and must scale read and write capacity as quickly as possible to meet changes in user demand.

Which solution will meet these requirements?

- A. Host static content in Amazon S3. Host dynamic content by using Amazon API Gateway and AWS Lambda. Use Amazon DynamoDB with on-demand capacity for the database. Configure Amazon CloudFront to deliver the website content.
- B. Host static content in Amazon S3. Host dynamic content by using Amazon API Gateway and AWS Lambda. Use Amazon Aurora with Aurora Auto Scaling for the database. Configure Amazon CloudFront to deliver the website content.
- C. Host all the website content on Amazon EC2 instances. Create an Auto Scaling group to scale the EC2 instances. Use an Application Load Balancer to distribute traffic. Use Amazon DynamoDB with provisioned write capacity for the database.
- D. Host all the website content on Amazon EC2 instances. Create an Auto Scaling group to scale the EC2 instances. Use an Application Load Balancer to distribute traffic. Use Amazon Aurora with Aurora Auto Scaling for the database.

### 184

A company has an AWS account used for software engineering. The AWS account has access to the company’s on-premises data center through a pair of AWS Direct Connect connections. All non-VPC traffic routes to the virtual private gateway.

A development team recently created an AWS Lambda function through the console. The development team needs to allow the function to access a database that runs in a private subnet in the company’s data center.

Which solution will meet these requirements?

- A. Configure the Lambda function to run in the VPC with the appropriate security group.
- B. Set up a VPN connection from AWS to the data center. Route the traffic from the Lambda function through the VPN.
- C. Update the route tables in the VPC to allow the Lambda function to access the on-premises data center through Direct Connect.
- D. Create an Elastic IP address. Configure the Lambda function to send traffic through the Elastic IP address without an elastic network interface.

### 185

A company runs an application using Amazon ECS. The application creates resized versions of an original image and then makes Amazon S3 API calls to store the resized images in Amazon S3.

How can a solutions architect ensure that the application has permission to access Amazon S3?

- A. Update the S3 role in AWS IAM to allow read/write access from Amazon ECS, and then relaunch the container.
- B. Create an IAM role with S3 permissions, and then specify that role as the taskRoleArn in the task definition.
- C. Create a security group that allows access from Amazon ECS to Amazon S3, and update the launch configuration used by the ECS cluster.
- D. Create an IAM user with S3 permissions, and then relaunch the Amazon EC2 instances for the ECS cluster while logged in as this account.

### 186

A company has a Windows-based application that must be migrated to AWS. The application requires the use of a shared Windows file system attached to multiple Amazon EC2 Windows instances that are deployed across multiple Availability Zone:

What should a solutions architect do to meet this requirement?

- A. Configure AWS Storage Gateway in volume gateway mode. Mount the volume to each Windows instance.
- B. Configure Amazon FSx for Windows File Server. Mount the Amazon FSx file system to each Windows instance.
- C. Configure a file system by using Amazon Elastic File System (Amazon EFS). Mount the EFS file system to each Windows instance.
- D. Configure an Amazon Elastic Block Store (Amazon EBS) volume with the required size. Attach each EC2 instance to the volume. Mount the file system within the volume to each Windows instance.

### 187

A company is developing an ecommerce application that will consist of a load-balanced front end, a container-based application, and a relational database. A solutions architect needs to create a highly available solution that operates with as little manual intervention as possible.

Which solutions meet these requirements? (Choose two.)

- A. Create an Amazon RDS DB instance in Multi-AZ mode.
- B. Create an Amazon RDS DB instance and one or more replicas in another Availability Zone.
- C. Create an Amazon EC2 instance-based Docker cluster to handle the dynamic application load.
- D. Create an Amazon Elastic Container Service (Amazon ECS) cluster with a Fargate launch type to handle the dynamic application load.
- E. Create an Amazon Elastic Container Service (Amazon ECS) cluster with an Amazon EC2 launch type to handle the dynamic application load.

### 188

A company uses Amazon S3 as its data lake. The company has a new partner that must use SFTP to upload data files. A solutions architect needs to implement a highly available SFTP solution that minimizes operational overhead.

Which solution will meet these requirements?

- A. Use AWS Transfer Family to configure an SFTP-enabled server with a publicly accessible endpoint. Choose the S3 data lake as the destination.
- B. Use Amazon S3 File Gateway as an SFTP server. Expose the S3 File Gateway endpoint URL to the new partner. Share the S3 File Gateway endpoint with the new partner.
- C. Launch an Amazon EC2 instance in a private subnet in a VPInstruct the new partner to upload files to the EC2 instance by using a VPN. Run a cron job script, on the EC2 instance to upload files to the S3 data lake.
- D. Launch Amazon EC2 instances in a private subnet in a VPC. Place a Network Load Balancer (NLB) in front of the EC2 instances. Create an SFTP listener port for the NLB. Share the NLB hostname with the new partner. Run a cron job script on the EC2 instances to upload files to the S3 data lake.

### 189

A company needs to store contract documents. A contract lasts for 5 years. During the 5-year period, the company must ensure that the documents cannot be overwritten or deleted. The company needs to encrypt the documents at rest and rotate the encryption keys automatically every year.

Which combination of steps should a solutions architect take to meet these requirements with the LEAST operational overhead? (Choose two.)

- A. Store the documents in Amazon S3. Use S3 Object Lock in governance mode.
- B. Store the documents in Amazon S3. Use S3 Object Lock in compliance mode.
- C. Use server-side encryption with Amazon S3 managed encryption keys (SSE-S3). Configure key rotation.
- D. Use server-side encryption with AWS Key Management Service (AWS KMS) customer managed keys. Configure key rotation.
- E. Use server-side encryption with AWS Key Management Service (AWS KMS) customer provided (imported) keys. Configure key rotation.

### 190

A company has a web application that is based on Java and PHP. The company plans to move the application from on premises to AWS. The company needs the ability to test new site features frequently. The company also needs a highly available and managed solution that requires minimum operational overhead.

Which solution will meet these requirements?

- A. Create an Amazon S3 bucket. Enable static web hosting on the S3 bucket. Upload the static content to the S3 bucket. Use AWS Lambda to process all dynamic content.
- B. Deploy the web application to an AWS Elastic Beanstalk environment. Use URL swapping to switch between multiple Elastic Beanstalk environments for feature testing.
- C. Deploy the web application to Amazon EC2 instances that are configured with Java and PHP. Use Auto Scaling groups and an Application Load Balancer to manage the website’s availability.
- D. Containerize the web application. Deploy the web application to Amazon EC2 instances. Use the AWS Load Balancer Controller to dynamically route traffic between containers that contain the new site features for testing.
