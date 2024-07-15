

### 라우팅 정책

- 단순 라우팅 정책


### DNS records


### S3 Transfer Acceleration

- S3 Transfer Acceleration is designed to maximize transfer speeds when you need to move data over long distances, for instance across countries or continents, to your Amazon S3 bucket. **Transfer Acceleration takes advantage of Amazon CloudFront’s globally distributed edge locations.** As the data arrives at an edge location, data is routed to Amazon S3 over an optimized network path.

### Amazon CloudFront

- Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with **low latency, high transfer speeds, all within a developer-friendly environment.**
- Configure a CloudFront distribution to deliver your entire website, including dynamic, static, streaming, and interactive content using a global network of edge locations. Requests for your content are automatically routed to the nearest edge location, so content is delivered with the best possible performance.


### Amazon Athena


- S3 에 있는 데이터를 Standard SQL 로 쿼리할 수 있게 해주는 서비스
- Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. Athena is serverless, so there is no infrastructure to manage, and you pay only for the queries that you run.

### AWS PrincipalOrgID

- 특정 조직에 속한 user, role 명시
- AWS PrincipalOrgId is a global condition context key that is used in an IAM policy to specify the organization ID of the principal entity (user or role) making the request. You can use this key to help secure your organization's data by requiring that the request comes from only specified accounts in your organization.

### bandwidth

- 대역폭
- 대역폭은 단위 시간당 전송되는 데이터의 양을 의미한다. 대역폭이 높을수록 많은 데이터를 빠르게 전송할 수 있다.

### AWS Snowball Edge

- AWS Snowball Edge is a 100TB data transfer device with **on-board storage** and compute capabilities. You can use Snowball Edge to move large amounts of data into and out of AWS, as a temporary storage tier for large local datasets, or to support local workloads in remote or offline locations.

### VPC Endpoint

- VPC endpoint allows you to connect to AWS services using a private network instead of using the public Internet(Without connecting to the Internet Gateway). This is a more secure and efficient way to access AWS services.

### Amazon EFS(Elastic File System)

- ELB 를 통해 EC2 인스턴스에 접근하는 경우, EC2 인스턴스가 여러개인 경우, 각 인스턴스에 동일한 파일을 저장해야 하는 경우, EFS 를 사용하면 편리하다.
- Amazon EFS provides a simple, scalable, fully managed elastic NFS file system for use with AWS Cloud services and on-premises resources. It is built to scale on demand to petabytes without disrupting applications, growing and shrinking automatically as you add and remove files, eliminating the need to provision and manage capacity to accommodate growth.


### Amazon Simple Queue Service(SQS)

- Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to **decouple and scale microservices**, distributed systems, and serverless applications. SQS eliminates the complexity and overhead associated with managing and operating message oriented middleware, and empowers developers to focus on differentiating work. **Using SQS, you can send, store, and receive messages between software components at any volume, without losing messages or requiring other services to be available**.

### Amazon Simple Notification Service(SNS)

- Amzon SNS is a fully managed messaging service for both application-to-application (A2A) and application-to-person (A2P) communication. Using Amazon SNS, you can **pub/sub (publish/subscribe) to topics** of interest, with configurable delivery options and **endpoints** in the form of **SMS, email, and mobile push notifications**.


### Auto Scaling Group

- an Auto Scaling group contains a collection of Amazon EC2 instances that are treated as a logical grouping for the purposes of automatic scaling and management. An Auto Scaling group also enables you to use Amazon EC2 Auto Scaling features such as health check replacements and scaling policies.
- increase or decrease scale automatically based on the conditions you define. You can use scaling policies to accomplish the following tasks:

    - Maintain performance by proactively adding instances to accommodate increasing load.
    - Automatically remove instances when load decreases, to minimize costs.
    - Ensure that your application always has the right amount of capacity to handle the current traffic demands.


### S3 Glacier Deep Archive


- S3 Glacier Deep Archive is a new Amazon S3 storage class that provides secure, durable object storage for **long-term retention** of data that is rarely accessed. S3 Glacier Deep Archive offers the lowest cost storage in AWS, at prices significantly lower than storing and maintaining data in on-premises magnetic tape libraries or archiving data off-site. S3 Glacier Deep Archive can also be used as a **“digital landfill”** for petabyte-scale data sets that are growing exponentially and are rarely accessed, but still need to be retained for future reference and compliance reasons.


### Amazon SQS FIFO queues

- Amazon SQS FIFO (first-in-first-out) queues are designed to **guarantee that messages are processed exactly once, in the exact order that they are sent**. FIFO queues are available in the US East (Ohio), US East (N. Virginia), US West (Oregon), and EU (Ireland) regions. FIFO queues are limited to 300 transactions per second (TPS).


### AWS Secrets Manager

- AWS Secrets Manager enables you to easily create and manage the secrets that you use in your customer-facing apps. Instead of embedding credentials into your source code, **you can dynamically query Secrets Manager from your app whenever you need credentials.** You can automatically and frequently rotate your secrets without having to deploy updates to your apps. All secret values are encrypted when they're at rest with AWS KMS, and while they're in transit with HTTPS.


### Amazon Aurora

- Amazon Aurora is a MySQL and PostgreSQL-compatible relational database built for the cloud, that combines the performance and availability of traditional enterprise databases with the simplicity and cost-effectiveness of open source databases. Amazon Aurora is up to five times faster than standard MySQL databases and three times faster than standard PostgreSQL databases. It provides the security, availability, and reliability of commercial databases at 1/10th the cost.
- Multi AZ deployment 를 통해 failover 를 자동으로 수행한다.


### Durable, Stateless Components

To design a solution that uses durable, stateless components to process images automatically, a solutions architect could consider the following actions:

Option A involves creating an SQS queue and configuring the S3 bucket to send a notification to the queue when an image is uploaded. This allows the application to decouple the image upload process from the image processing process and ensures that the image processing process is triggered automatically when a new image is uploaded.

Option B involves configuring the Lambda function to use the SQS queue as the invocation source. When the SQS message is successfully processed, the message is deleted from the queue. This ensures that the Lambda function is invoked only once per image and that the image is not processed multiple times.


### Gateway Load Balancer

- Gateway Load Balancer is a new type of load balancer that allows you to deploy, scale, and manage third-party virtual appliances such as firewalls, intrusion detection and prevention systems, analytics, and other virtual appliances that are required for in-line network inspection.


### 20번 다시보기

### AWS Cost Explorer

- AWS Cost Explorer is a free tool that you can use to view your historical AWS costs and forecasts. You can also use Cost Explorer to create reports and analyze your costs.


### AWS Config

- AWS Config is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources. 
- **Config continuously monitors and records your AWS resource configurations and allows you to automate the evaluation of recorded configurations against desired configurations.**
- automatically tag resoruces


- To create tags for your resources using AWS Config, you will need to create an AWS Config rule that specifies the tag key and value you want to use and the resources you want to apply the tag to. You can then enable the rule and AWS Config will automatically apply the tag to the specified resources when they are created or when their configurations change.

### Amazon CloudWatch

- Amazon CloudWatch is a monitoring and observability service built for DevOps engineers, developers, site reliability engineers (SREs), and IT managers. CloudWatch provides you with data and actionable insights to monitor your applications, respond to system-wide performance changes, optimize resource utilization, and get a unified view of operational health. CloudWatch collects monitoring and operational data in the form of logs, metrics, and events, providing you with a unified view of AWS resources, applications, and services that run on AWS and on-premises servers.


### 28 다시보기


### AWS Organizations

- AWS Organizations is an account management service that enables you to consolidate multiple AWS accounts into an organization that you create and centrally manage. AWS Organizations includes account management and consolidated billing capabilities that enable you to better meet the budgetary, security, and compliance needs of your business. As an administrator of an organization, you can create accounts in your organization and invite existing accounts to join the organization.
- Single Sign-On (SSO) is an AWS Organizations feature that enables you to centrally manage SSO access to multiple AWS accounts and business applications. With SSO, you can easily manage access and user permissions to all of your accounts in AWS Organizations centrally.


### Amazon Kinesis Data Streams

- Amazon Kinesis Data Streams is a scalable and durable real-time data streaming service that can **continuously capture gigabytes of data per second from hundreds of thousands of sources.** The data collected is available in milliseconds to enable real-time analytics use cases such as real-time dashboards, real-time anomaly detection, dynamic pricing, and more.

### Amazon Kinesis Data Firehose

- **Amazon Kinesis Data Firehose** is the easiest way to **load streaming data into data stores and analytics tools.** It can capture, transform, and load streaming data into Amazon S3, Amazon Redshift, Amazon Elasticsearch Service, and Splunk, enabling near real-time analytics with existing business intelligence tools and dashboards you’re already using today. It is a fully managed service that automatically scales to match the throughput of your data and requires no ongoing administration. It can also batch, compress, and encrypt the data before loading it, minimizing the amount of storage used at the destination and increasing security.
- fully managed service
- load streaming data into data stores and analytics tools
- Kinesis Data Streams focuses on ingesting and storing data streams. Kinesis Data Firehose focuses on delivering data streams to select destinations


### AWS Fargate

- AWS Fargate is a **serverless compute engine for containers that works with both Amazon Elastic Container Service (ECS)** and Amazon Elastic Kubernetes Service (EKS). Fargate makes it easy for you to focus on building your applications. Fargate removes the need to provision and manage servers, lets you specify and pay for resources per application, and improves security through application isolation by design.


### AWS CloudTrail

- AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. **With CloudTrail, you can log, continuously monitor, and retain account activity related to actions across your AWS infrastructure.** CloudTrail provides event history of your AWS account activity, including actions taken through the AWS Management Console, AWS SDKs, command line tools, and other AWS services. This event history simplifies security analysis, resource change tracking, and troubleshooting.
- record API calls

### AWS GuardDuty

- AWS GuardDuty is a threat detection service that continuously monitors for malicious activity and unauthorized behavior to protect your AWS accounts and workloads. With the cloud, the collection and aggregation of account and network activities is simplified, but it can be time consuming for security teams to continuously analyze event log data for potential threats. **With GuardDuty, you now have an intelligent and cost-effective option for continuous threat detection in the AWS Cloud. GuardDuty analyzes tens of billions of events across multiple AWS data sources, such as AWS CloudTrail, Amazon VPC Flow Logs, and DNS logs.** With a few clicks in the AWS Management Console, GuardDuty can be enabled with no software or hardware to deploy or maintain. By integrating with AWS CloudWatch Events, GuardDuty alerts are actionable, easy to aggregate across multiple accounts, and straightforward to push into existing event management and workflow systems.

### AWS Inspector

- Amazon Inspector is an automated security assessment service that helps improve the security and compliance of applications deployed on AWS. Amazon Inspector automatically assesses applications for vulnerabilities or deviations from best practices. After performing an assessment, **Amazon Inspector produces a detailed list of security findings prioritized by level of severity. These findings can be reviewed directly or as part of detailed assessment reports which are available via the Amazon Inspector console or API.**

### AWS Shield

- AWS Shield is a managed Distributed Denial of Service (DDoS) protection service that safeguards applications running on AWS. AWS Shield provides always-on detection and automatic inline mitigations that minimize application downtime and latency, so there is no need to engage AWS Support to benefit from DDoS protection.
- provides protection against DDoS attacks


### Amazon AppFlow

- Amazon AppFlow is a fully managed integration service that enables you to securely transfer data between AWS services and software-as-a-service (SaaS) applications like Salesforce, Marketo, Slack, Snowflake, and ServiceNow, in just a few clicks. With AppFlow, you can use pre-built connectors to third-party applications to create integrations called flows. These flows can transfer data bi-directionally between applications, securely and at scale.
- transfer data between AWS services(S3, exc..) and software-as-a-service (SaaS) applications


### Gateway VPC Endpoint

Deploying a gateway VPC endpoint for Amazon S3 is the most cost-effective way for the company to avoid Regional data transfer charges. A gateway VPC endpoint is a network gateway that allows communication between instances in a VPC and a service, such as Amazon S3, without requiring an Internet gateway or a NAT device. Data transfer between the VPC and the service through a gateway VPC endpoint is free of charge, while data transfer between the VPC and the Internet through an Internet gateway or NAT device is subject to data transfer charges. By using a gateway VPC endpoint, the company can reduce its data transfer costs by eliminating the need to transfer data through the NAT gateway to access Amazon S3. This option would provide the required connectivity to Amazon S3 and minimize data transfer charges.