# AWS Overview

## Regions

> a cluster of data centers

- Most AWS services are region-scoped
- Compliance is region-scoped
- proximity to customers : lower latency
- Available servicess within a region may vary
- Pricing may vary across regions

## Availability Zones

> a data center

- Each region has many AZ (>= 2)
- Each AZ is one or more discrete data centers with redundant power, networking and connectivity : isolated from failures
- 높은 대역폭, 매우 낮은 지연 시간 네트워킹으로 연결되어 있음

## AWS Global Infrastructure 

### AWS Regional Services 

# IAM & AWS CLI

- 참고 : https://docs.aws.amazon.com/iam/

- IAM : Identity and Access Management. Global service
- Root account : should never be used or shared
- Users : people within your organization and can be grouped

## IAM Policies

- JSON documents that define permissions
- These Policies can be attached to
  - Users
  - Groups
  - Roles

- In AWS you apply the **least privilege principle**
  - Always give the minimum level of access required
  - IAM policies are applied **by default deny all**

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListAllMyBuckets",
                "s3:GetBucketLocation"
            ],
            "Resource": "*"
        }
    ]
}
```

## IAM Users & Groups

### IAM Users

- IAM users are **physical persons** (employees, admins, etc...)
- They can have a **password** to login
- They can have **access keys** (access key ID & secret access key) to access AWS via the APIs & CLI
- They can have tags (key-value pairs).

## IAM Policies

- IAM policies are **JSON documents** that give permissions to perform actions

### IAM Policies - inheritance

- Group Level Policies 적용 
  - 그룹 내에 있는 모든 사용자에게 적용

### IAM Policies - structure

- Version Number
- Id (optional)
- Statement
  - Sid (optional) : identifier for the statement . statement ID 
  - Effect : whether the statement allows or denies access
    - Effect 는 access를 허용할지 거부할지 결정
  - Principal : account/user/role to apply the policy to
  - Action : list of actions this policy allows or denies
  - Resource : list of resources to apply the action to
  - Condition (optional) : conditions for when this policy is in effect.

중요 : A statement must have an effect, action, and resource
sid and condition are optional

### IAM Policies - MFA

IAM Policies는 크게 2 종류의 defense mechanism을 가지고 있다.

- Password Policy
- MFA

**Password Policy**
- password policy은 IAM user가 사용할 수 있는 password의 조건을 정의한다.
- 90일마다 password를 변경하도록 강제할 수 있다.
- password 생성 시, 대문자, 소문자, 숫자, 특수문자를 포함하도록 강제할 수 있다.

**MFA( Multi-Factor Authentication )**

- combination of password you know + security device you own
- virtural or hardware MFA device
  - virtual : google authenticator, authy, auth0, etc...
  - hardware : Yubikey device

### AWS CLI, Access Keys & SDK

SDK : Software Development Kit

- a set of libraries and tools to interact with AWS services
- language specific apis (java, python, .net, etc...)s
- embedded in your code/ application
- ex) AWS cli is built on aws sdk for python (boto3)

### AWS CLI Configuration

- use access key and secret access key to configure aws cli

### AWS CLI Commands

```bash
aws iam list-users # list all users
```

### AWS CloudShell

- 일종의 repository로 파일을 생성하고 저장할 수 있다.
- AWS CLI를 사용할 수 있다.
- Download, Upload, Edit, Preview, Delete 등의 기능을 제공한다.

## IAM Roles

- IAM roles are **a secure way to grant permissions to entities that you trust**
- 기본적으로 IAM role은 AWS service에게 권한을 부여하는데 사용된다.
- 물리적인 사람에게는 IAM user를 사용하고, AWS service에게는 IAM role을 사용한다.
- 기본적으로 어떤 사용할 수있는 권한이 있는 역할이다.
- 커스텀 생성할 수 있다.
- **Role** 은 단지 사람에게 만 부여되는게 아니라 EC2 instance, Lambda function 등의 AWS service에게도 부여할 수 있다.


계정에서 생성할 수 있는 특정 권한을 가진 IAM 자격 증명입니다. IAM 역할은 IAM 사용자와 몇 가지 점에서 유사합니다. 역할과 사용자 모두 AWS에서 자격 증명으로 할 수 있는 것과 할 수 없는 것을 결정하는 권한 정책을 포함하는 AWS 자격 증명입니다. 그러나 역할은 한 사람과만 연관되지 않고 해당 역할이 필요한 사람이라면 누구든지 맡을 수 있어야 합니다. 또한 역할에는 그와 연관된 암호 또는 액세스 키와 같은 표준 장기 자격 증명이 없습니다. 대신에 역할을 맡은 사람에게는 해당 역할 세션을 위한 임시 보안 자격 증명이 제공됩니다.

역할은 다음의 주체들이 사용할 수 있습니다.

- 역할과 동일한 AWS 계정의 IAM 사용자
- 역할과 다른 AWS 계정의 IAM 사용자
- AWS에서 제공하는 웹 서비스(예: Amazon Elastic Compute Cloud(Amazon EC2))
- SAML 2.0, OpenID Connect 또는 사용자 지정 구축 자격 증명 브로커와 호환되는 외부 자격 증명 공급자(IdP) 서비스에 의해 인증된 외부 사용자

### Common roles

- EC2 Instance Roles
- Lambda Function Roles
- Roles for CloudFormation

## IAM Security Tools

### IAM Credentials Report

- account level report
- a report that lists all your account's users and the status of their various credentials

### IAM Access Advisor

- user level
- shows the service permissions granted to a user
- and when those services were last accessed
- 유저가 어떤 서비스에 접근했는지, 언제 접근했는지를 보여준다.
- user policy를 수정할 때, 이 정보를 참고하여 권한을 수정할 수 있다.

## IAM Best Practices

- Don't use root account except for AWS account setup
- one physical user = one AWS user
- Assign users to groups and assign permissions to groups
- Create a strong password policy
- use and enforce the use of MFA(Multi-Factor Authentication)
- Create and use roles for giving permissions to AWS services
- Use Access Keys for programmatic access (CLI/SDK)
- Audit permissions of your account with
  - IAM Credentials Report(account level)
  - IAM Access Advisor(user level)

## IAM Summary

- Users : mapped to a physical user, has a password for AWS Console
- Groups : contains users only
- Policies : JSON document that outlines permissions for users or groups
- Roles : for EC2 instances or AWS services
- Security : MFA + Password Policy
- AWS CLI : manage your AWS services using commandline
- AWS SDK : manage your AWS services using a programming language(Java, Python, etc...)
- Audit
  - IAM Credentials Report : account level
  - IAM Access Advisor : user level

# EC2 Fundamentals

## EC2 Overview

- Elastic Compute Cloud = Infrastructure as a Service(IaaS)
- It mainly consists of
  - Renting virtual machines(EC2)
  - Storage data on virtual drives (EBS & EFS)
  - Distribute load across machines (ELB)
  - Scaiing the services using an auto-scaling group(ASG)

### Sizing & Configuration Options

- OS : Linux, Windows, Mac
- CPU
- RAM
- Storage
  - network-attached (EBS, EFS)
  - hardware (EC2 Instance Store)
- Network Card
  - speed (10Gbps)
  - IPv4 & IPv6
  - DNS name
- Firewall rules : security groups
- Bootstrap script : launch commands(configure at first launch) -> EC2 User Data

### EC2 User Data

- bootstrapping : process of starting up a machine and loading the initial set of instructions
- the script is **only run once** at the instance first start
- EC2 User Data is used to automate boot tasks such as
  - installing updates
  - installing software
  - download common files from the internet
  - anything you can think of
- 기본적으로 instance가 처음 시작될 때, 한 번만 실행된다.
ec2 user data script에 이것저것 추가할 수록 부팅 시간이 보다 길어진다.

## EC2 Instance Types

- https://aws.amazon.com/ec2/instance-types/


### General Purpose

- Great for diversity of workloads such as web servers, code repositories, dev/test environments, etc...
- Balance Between
  - Compute
  - Memory
  - Networking

### Compute Optimized

- Great for compute-intensive tasks that require high performance processors
- Ideal for
  - Batch processing workloads
  - Media transcoding
  - High performance web servers
  - High performance computing (HPC)
  - **Scientific modeling & machine learning**

### Memory Optimized

- Fast performance for workloads that process **large data sets in memory**
- Use Cases
  - High performance, relational/non-relational databases
  - Distributed web scale cache stores
  - In-memory databases optimized for BI
  - **Applications performing real-time processing of big unstructured data**

### Storage Optimized

대량의 데이터셋을 로컬 스토리지에 저장하고 처리할 때 사용한다.

- Great for storage-intensive tasks that require high, sequential read and write access to large data sets on local storage
- Use Cases
  - **High frequency online transaction processing (OLTP) systems**
  - Relational & NoSQL databases
  - Cache for in-memory databases (Redis, Memcached)
  - Data warehousing applications
  - Distributed file systems

### EC2 Instance Types : example

ex) m5.2 xlarge

- m : instance class
- 5 : generation of intance
- 2xlarge : size within the instance class

- ec2 instances info : https://aws.amazon.com/ec2/instance-types/

### Security Groups

- 기본적으로 EC2 의 Firewall 역할을 한다.
- They control how traffic is allowed into or out of our EC2 Machines
- Security groups only contain **allow rules**
- Security groups rules can reference by IP or by security group

- inbound traffic : traffic coming in
- outbound traffic : traffic going out

- They Regulate
  - Access to ports
  - Authorised IP ranges - IPv4 and IPv6
  - Control of inbound network (from other to the instance)
  - Control of outbound network (from the instance to other)

**Good to know**

- 여러 instance에 같은 security group을 적용할 수 있다.
- locked down to a region / VPC combination 
- Does live "outside" the EC2 - if traffic is blocked the EC2 instance won't see it
- **It's good to maintain one separate security group for SSH access**
- If your application is not accessible (time out), then it's a security group issue -> 기본적으로 방화벽 역할 하기 때문에
- If your application gives a "connection refused" error, then it's an application error or it's not launched
- **All inbound traffic is blocked by default**
- **All outbound traffic is authorised by default**

referencing other security groups

- EC2 instance can belong to multiple security groups
- good practice : give each instance only the permissions it needs
- **이미 만들어진 security group을 다른 instance의 security group으로 연결될 수 있다.**
- 로드밸런서를 사용할 때, 로드밸런서의 security group을 EC2 instance의 security group으로 참조할 수 있다.

### Classic Ports to Know

- 22 : SSH (Secure Shell) - log into a Linux instance
- 21 : FTP (File Transfer Protocol) - upload files into a file share
- 22 : SFTP (Secure File Transfer Protocol) - upload files using SSH
- 80 : HTTP - access unsecured websites
- 443 : HTTPS - access secured websites
- 3389 : RDP (Remote Desktop Protocol) - log into a Windows instance // 윈도우 서버에 접속할 때 사용

## SSH Overview


## EC2 Instance Purchase Options

- On Demand Instances : short workload, predictable pricing, pay per second
- Reserved : (min 1 year) : 
  - Reserved instances : long workloads 
  - Convertible Reserved Instance : long workloads with flexible instances
- Savings Plans : (1 to 3 years) : commitment 
- Spot Instances : short workloads, for cheap, can lose instances (ex : bidding price)
- Dedicated Instances : no other customers will share your hardware
- Dedicated Hosts : book an entire physical server, control instance placement
- Capacity Reservations : reserve capacity in a specific AZ for any duration

### EC2 On Demand

- Pay for what you use
  - linux or windows : billed per second after the first minute
  - other OS : billed per hour 
- No long term commitment
- has the highest cost but no upfront payment

- 단기간에 방해없이 사용하고 싶을 때 사용한다.
- 어플리케이션이 어떻게 작동할지 모를 때

### EC2 Reserved Instances

- 72% discount compared to On-Demand
- 특정한 instance attribute를 예약할 수 있다.
  - instance type
  - Region
  - Tenacy
  - OS 
- 기간 : 1년, 3년
- 결제옵셔 : All Upfront, Partial Upfront, No Upfront
- Scope : Regional or Availability Zone Reserved Instance
- **Recommended for steady state usage applications (think database)**
- Market Place에서 사고팔고가 가능하다.

- **Convertible Reserved Instance**
  - can change the EC2 instance type, instance family, OS, scope , tenancy
  - 유연성을 보다 가져가기 때문에 할인율이 66% 까지 떨어진다.

### EC2 Savings Plans

- 장기사용을 전제로 할인율을 제공한다.
- 1년 또는 3년 기간으로 구매할 수 있다. ($10 / hour for 1 year)
- EC2 Saving을 넘어서는 사용량은 On-Demand로 청구된다.

### EC2 Spot Instances

- **Can get a discount of up to 90% compared to On-Demand**
- Instacnes that you can "lose" at any point of time if your max price is less than the current spot price
- The most cost-efficient instances in AWS
- Useful for workloads that are resilient to failure
  - batch jobs 
  - data analysis
  - image processing
  - any distributed workloads

### EC2 Dedicated Hosts

- Actual physical dedicated EC2 server for your use
- Allows you address compliance requirements and use your existing server-bound software licenses(per socket, per core, or pe VM software licenses)

purchasing options

- On-Demand
- reservation : 1 year or 3 year
- The Most Expensive Option
- Useful for software that have complicated licensing model
- Or for companies that have strong regulatory or compliance needs

### EC2 Dedicated Instances

- Instances running on hardware that's dedicated to you
- May share hardware with other instances in the same account
- No control over instance placement (can move hardware after stop/start)

### EC2 Capacity Reservations
- EC2 Instance를 위한 Capacity를 예약할 수 있다.
- Instance를 예약하는 것이 아니라, Capacity를 예약하는 것이다.
- 기본적으로 인스탄스 실행여부에 상관없이 고정요금이 청구된다.


### EC2 Instance What to Choose

Hotel Room Analogy

- On-Demand : coming and staying in resort whenever we like, we pay the full price
- Reserved : (min 1 year) : like planning ahead and if plan to stay for a long time, we get a discount
- Savings Plans : pay a certain amount per hour for certain period and stay in any room type
- Spot instances : the Hotel allows people to bid for the empty rooms and the highest bidder keeps the room. you can get kicked out at any time
- Dedicated Hosts : We book an entire building of the resort
- Capacity Reservations : you book a room for period with full price even if you don't use it

## Spot Instances Deep Dive

- Can get a discount of up to 90% compared to On-Demand
- Define a max price and get the instance while current spot price < max price
- The hourly spot price varies based on offer and capacity
- If the current spot price > your max price, you can choose to stop or terminate the instance with a 2 min grace period

Other Strategy : Spot Blocks
- Spot Block 은 일정 시간동한 Spot Instance를 Block해 AWS가 instance를 차단하는걸 막는다.

**How to terminate Spot Instances**

- You can only cancel Spot Instance requests that are open, active, or disabled
- Canceling a Spot Request does not terminate running Spot Instances
- You must first cancel a Spot Request , and then terminate the associated Spot Instances

### Spot Fleets

- **Spot Fleets : set of Spot Instances + (optional) On-Demand Instances**
- Spot Fleet will try to meet the target capacity with Spot Instances first

- Strategy
  - lowestPrice : the Spot Instances with the lowest price are launched first
  - diversified : the Spot Instances are launched across all the Spot pools (Great for availability , long workloads)
  - capacityOptimized : pools with highest capacity available , then select the pool with the lowest price (Great for short workloads that are urgent or for big data jobs)

- **Spot Fleets allow us to automatically request Spot Instances with the lowest price**

# EC2 Advanced



## Private vs Public vs Elastic IP

### Private IP

- private network 내에서만 식별할 수 있다.
- private network 안에서 unique하다.
- 일정한 범위의 IP만 private IP로 사용할 수 있다.
- Machines connect to WWW using a NAT + Internet Gateway(proxy)

### Public IP

- 인터넷 게이트웨이
- the machine can be identified on the whole internet
- 전체 웹상에서 식별할 수 있는 유일한 값이다.
- Can be geo-located

### Elastic IP

- 기본적으로 EC2 instance는 instance를 중지하고 재실행할 때 Public IP가 변경된다.
- Elastic IP는 instance를 중지하고 재실행해도 Public IP가 변경되지 않는다.
- Elastic IP는 개인 계정에 귀속된 IP주소이다.
- 계정당 5개의 Elastic IP를 생성할 수 있다.
- 별로 권장되지 않는다.
- 대신 Random Public IP에 대한 DNS를 사용하는 것이 좋다.
- 아니면 Load Balancer 사용하고 Public IP를 아예 사용하지 않는 것이 좋다.

## EC2 Placement Groups

### Cluster

- Same AZ
- pros
  - Great network

### Spread

- Different AZ
- 실패 위험을 최소화
- pros
  - Can span across AZ
  - EC2 instances are on different hardware
  - Can span across multiple AZ
- cons
  - limited to 7 instances per AZ
- use cases
  - critical applications
  - small number of instances
  - instances that should be kept separate from each other
  - 고가용성 : 가용성은 높지만, 네트워크 성능은 상대적으로 떨어진다.
  - 가용성 뜻 : 어떤 서비스가 항상 사용가능한 상태를 유지하는 것

### Partition

- spread instances across may different partitions within an AZ
- up to 7 instances per partition per AZ
- catn span across multiple AZ
- use cases : HDFS, HBase, Cassandra, Kafka, etc...

##  Elastic Network Interfaces (ENI)

**ENI**
- VPC의 가상 네트워크 카드를 나타내는 논리적인 네트워킹 구성요소
- logical component in a VPC that represents a **virtual network card**
- [VPC(Virtual Private Network) 개념] (https://medium.com/harrythegreat/aws-%EA%B0%80%EC%9E%A5%EC%89%BD%EA%B2%8C-vpc-%EA%B0%9C%EB%85%90%EC%9E%A1%EA%B8%B0-71eef95a7098)
- failover 관리 : instance에서 instance로 ENI를 붙여서 failover를 관리할 수 있다.
- ENI 컨셉 관련 참고
  - https://aws.amazon.com/ko/blogs/aws/new-elastic-network-interfaces-in-the-virtual-private-cloud/

------------------------ 여기서부터 정리
- bound to specific availability zone

## EC2 Hibernate

- Hibernate : in-memory(RAM) state is preserved
- Root EBS volume 이 충분히 커야 한다.

# EC2 Instance Storage

## EBS Volumes

**EBS volume**

- EBS : Elastic Block Store
- 기본적으로 Network USB stick 같은 역할을 한다. -> Network drive
- Locked to an AZ
- Have a provisioned capacity (size in GBs, and IOPS)
- EBS 볼륨은 인스턴스 중지 및 종료 시에도 데이터를 보존합니다.
- EBS 스냅샷으로 EBS 볼륨을 백업할 수 있습니다.
- 한 인스턴스에서 EBS 볼륨을 제거하고 다른 인스턴스에 다시 연결할 수 있습니다.
- EBS 볼륨은 전체 볼륨 암호화를 지원합니다.

- Delete on Termination attribute
  - By default, the root EBS volume is deleted when the EC2 instance is terminated
  - But, by default, any other attached EBS volume is not deleted
  - EBS volume can be detached from an EC2 instance and attached to another one quickly

### EBS Snapshots

- 특정시점의 Snapshot을 만들 수 있다.
- EBS Snapshot Archive
- Recycle Bin for EBS Snapshots
- Fast Snapshot Restore(FSR) : EBS Snapshot을 빠르게 복원할 수 있다.

## Amazon Machine Image (AMI)

- AMI is a customization of an EC2 instance

## EC2 Instance Store

- if you need a high-performance hardware disk, us an EC2 Instance Store
- Better I/O performance
- 하지만 Data loss의 위험이 있다.
- EC2 Instance Store lose their storage if they're stopped (ephemeral)
- ephemeral : 일시적인, 덧붙여진

## EBS Volume Types

- EBS Volume Type
  - GP2/GP3 : General Purpose SSD
  - IO1/IO2 : 
    - Highest performance SSD
    - Mission Critical Low Latency
    - High Throughput Workloads
  - ST1 : Low Cost HDD
    - can't be a boot volume
    - Low Cost HDD
    - Frequently Accessed, Throughput Intensive Workloads
  - SC1 : Lowest Cost HDD
    - can't be a boot volume
    - Lowest Cost HDD
    - cold hdd
    - Less Frequently Accessed

IOPS(in/out operations per second)

## Multi Attach EBS Volumes

## EBS Encryption

- EBS 볼륨은 전체 볼륨 암호화를 지원합니다.

## EFS (Elastic File System)

- Managed NFS(Network File System) that can be mounted on many EC2
- works with Linux EC2 instances in multi-AZ
- Highly available, scalable, expensive (3x gp2), pay per use, no capacity planning
- Compatible with only linux based AMI

### EFS - Performance & Storage Classes

- EFS Scale
- Performance Mode
  - General Purpose (default)
  - Max I/O
- Throughput Mode
  - Bursting (default) : burstable up to 100MB/s
  - Provisioned : set throughput regardless of storage size. storage size를 늘려도 throughput은 변하지 않는다.
  - Elastic : 사용량에 따라 throughput이 자동으로 조정된다.

## EBS vs EFS

# High Availability & Scalability : ELB & ASG

## Application Load Balancer(ALB)

## Network Load Balancer(NLB)

- Layer 4 Load Balancer(lower level)
- TCP, TLS, UDP
- handle millions of request per second
- less latency ~100ms
- one static IP per AZ, supports assigning Elastic IP(EIP) to NLB
- Health checks support TCP, HTTP, HTTPS

## Gateway Load Balancer(GLB)

- Deploy , Scale and Manage a fleet of third-party virtual appliances
- Ex) firewalls, intrusion detection and prevention systems, deep packet inspection, etc...

- All users traffic is routed through the gateway load balancer before reaching the virtual appliances

- Combines the following funtionalities
  - Transparent Network Gateway
  - Load Balancer

## Sticky Sessions(Sessions Affinity)

- cookie-based
  - application based cookie
  - duration based cookie : expires after a specified duration
- enable stickiness on ALB or NLB
- 클라이언트를 같은 인스턴스로 유지한다.


## Cross Zone Load Balancing

> Each load balancer instance distributes evenly across all registered instances in all AZs

## SSL/TLS Certificates

## Connection Draining(Deregistration Delay)

> Time to complete "in-flight requests" while the instance is de-registering or unhealthy

## Auto Scaling Group(ASG)

- The goal of ASG is to :
  - Scale out (add EC2 instances) to match an increased load
  - Scale in (remove EC2 instances) to match a decreased load
  - Ensure we have a minimum and a maximum number of machines running
  - Automatically register new instances to a load balancer
  - Replace unhealthy instances
  - ASG makes sure we have a desired capacity of EC2 instances running all the time

- **A Launch Template is Needed**

# AWS fundamentals: RDS + Aurora + ElastiCache

## RDS

### EC2 인스턴스에 자체 DB 서비스를 배포하지 않고 RDS를 사용하는 이유

- RDS는 관리형 서비스이다.
- 데이터베이스 프로비저닝, 기본 운영체제 패치가 완전 자동화되어 있다.
- 지속적으로 백업이 생성되므로 특정 타임 스탬프, 즉 특정 시점으로 복원할 수 있다.
- 데이터베이스의 성능을 대시보드에서 모니터링할 수 있다.
- 읽기 전용 복제본을 활용해 읽기 성능을 개선할 수 있다.
- 재해 복구 목적으로 다중 AZ를 설정할 수 있다.
- 유지 관리 기간에 업그레이드를 할 수 있다.
- 인스턴스 유형을 늘려 수직 확장하거나 읽기 전용 복제본을 추가하여 수평 확장할 수 있다.
- 파일 스토리지는 EBS에 구성된다.
- 한 가지 단점은 RDS 인스턴스에 SSH 액세스할 수 없다는 점이다.

### RDS - Storage Auto Scaling

- RDS 데이터베이스를 만들 때 RDS 스토리지 오토 스케일링 기능이 활성화되어 있으면 RDS가 이를 감지해서 자동으로 스토리지를 확장해 준다.
- 스토리지를 확장하기 위해 DB를 다운시키는 등의 작업을 할 필요가 없다.
- 데이터베이스 스토리지를 수동으로 확장하는 작업을 피할 수 있게 해준다.
- 이를 위해 최대 스토리지 임곗값을 설정해야 한다. 이는 스토리지를 확장할 최대치를 정하는 것이다.
- 할당된 용량에서 남은 공간이 10% 미만이 되면 스토리지를 자동으로 수정한다.
- 스토리지 부족 상태가 5분 이상 지속되거나 지난 수정으로부터 6시간이 지났을 경우 오토 - 스케일링이 활성화되어 있다면 스토리지가 자동 확장된다.(스토리지 최적화가 최대 6시간 동안 소요되기 때문에 지난 수정으로부터 6시간 이후에 스토리지 오토 스케일링을 수행하는 것 같음)
- 워크로드를 예측할 수 없는 애플리케이션에서 굉장히 유용하다.
- 모든 RDS 데이터베이스 엔진에서 지원되는 기능이다


### RDS Read Replicas for read scalability

- 읽기 전용 복제본은 최대 5개까지 생성할 수 있다.
- 이들은 동일한 AZ 또는 AZ나 리전을 걸쳐서 생성될 수 있다.

#### Async Replication

- Master RDS 데이터베이스 인스턴스와 두 읽기 전용 복제본 사이에 비동기식 복제가 발생한다.
- 비동기식이란 결국 읽기가 일관적으로 유지된다는 것을 의미한다. 가령 애플리케이션에서 데이터를 복제하기 - 전 읽기 전용 복제본을 읽어들이면 모든 데이터를 얻을 수 있다. 이것이 바로 일관적인 비동기식 복제의 의미이다.
- 복제본 중 하나를 데이터베이스로도 승격시켜 이용할 수 있다. 즉 이들 복제본 중 하나를 데이터베이스로 사용하고자 하며 그에 대한 권한을 획득하면 이를 데이터베이스로 승격시킬 수 있다. 그 후에 이 복제본은 - 복제 메커니즘을 완저히 탈피한다. 대신 자체적인 생애 주기를 갖게 된다.
- 읽기 전용 복제본을 사용하려는 경우에는 화면 상단의 주요 애플리케이션에 있는 모든 연결을 업데이터해야 하며 이를 통해서 RDS 클러스터 상의 읽기 전용 복제본 전체 목록을 활용할 수 있다.
- 읽기 전용 복제본은 SELECT문만 필요한 경우에 사용된다.

### RDS Read Replicas - Network Cost

- AWS에서는 하나의 AZ에서 다른 AZ로 데이터가 이동할 때에 비용이 발생한다. 하지만 예외가 존재하며 이 예외는 보통 관리형 서비스에서 나타난다.
- RDS 읽기 전용 복제본은 관리형 서비스이기 때문에 예외이다.
- 읽기 전용 복제본이 다른 AZ 상에 위치하지만 동일한 리전 내에 있을 때는 비용이 발생하지 않는다.
- 하지만 서로 다른 리전에 복제본이 존재하는 경우 여러 리전을 넘나들어야 하기 때문에 네트워크에 대한 복제 비용이 발생한다.


## ElastiCache

Amazon ElastiCache는 클라우드에서 분산된 인 메모리 데이터 스토어 또는 캐시 환경을 손쉽게 설정, 관리 및 확장할 수 있는 웹 서비스

- Redis와 Memcached을 지원
- 캐시 노드 실패에서 자동 감지 및 복구
- 사용 예시 : 캐싱 / 세션 스토어 / AI/ML모델 / 실시간성이 높은 작업들

# Route53

## Route53

# Classic Solutions Architecture Discussions

# Amazon S3

# Amazon S3 Advanced

# Amazon S3 Security 

# CloudFront & AWS Global Accelerator

# AWS Storage Extras

# Decoupling Applications: SQS, SNS, Kinesis, Active MQ

## SQS

## SNS

## Kinesis

# Containers: ECS, ECR, Fargate

# Serverless Overview

# Databases in AWS

# Data & Analytics in AWS

# Machine Learning in AWS

# AWS Monitoring & Audit: CloudWatch, X-Ray, CloudTrail

# IAM advanced

# AWS Security & Encryption: KMS, SSM Parameter Store, IAM Policies

# Networking in AWS: VPC, Direct Connect, VPN, Transit Gateway

# Disaster Recovery & Migrations

# More Solutions Architectures

# Other AWS Services
