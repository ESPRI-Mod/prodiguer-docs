# Prodiguer Machine Setup

Prodiguer is a highly distributed messaging platform upon which are built several applications.  The platform runs across several types of machine and each one has to be setup accordingly so that all required dependencies are installed and running.  

The setup process takes upto 30 minutes and installs some or all of the following (depending upon machine type):  

1.	Common system dependencies;

2.	[PostgreSQL](http://www.postgresql.org) and [MongoDB](https://www.mongodb.org) database servers.  

3.	[RabbitMQ](https://www.rabbitmq.com) message queue server.  

4.	[nginx](http://wiki.nginx.org/Main) web server.  

Once the process has ran you can proceed to [install the prodiguer stack](https://github.com/Prodiguer/prodiguer-docs/blob/master/devops/stack_management.md).  

## Supported Machine types  

db = database server  

dev = development workstation  

mq = message queue server  

web = web server  

## Supported OS types  

centos = CentOS 6.5+

## Assumptions

You are running linux OS upon a suitably powerful machine.  

## Step 1: Install git

**CentOS:**  <pre><code>yum install git</pre></code>  

## Step 2: Install prodiguer shell

<pre><code>git clone https://github.com/Prodiguer/prodiguer-shell.git /opt/prodiguer  
</pre></code>

## Step 3: Run machine setup

<pre><code>/opt/prodiguer/exec.sh os-setup OS-TYPE MACHINE-TYPE</pre></code>  
