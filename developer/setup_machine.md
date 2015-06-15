# Prodiguer Machine Setup

Prodiguer is a highly distributed messaging platform upon which are built several applications.  In order to become an active contributor to the platform you will need to setup your machine so that all required dependencies are installed and running.  The required dependencies consist of c libraries, python libraries, 2 database servers, a web server and a message queue server.  Fortunately the machine setup process has been streamlined to allow you to become productive as soon as possible.

The install process will take upto 30 minutes and will isntall the following:  

1.	Common system dependencies;

2.	[PostgreSQL](http://www.postgresql.org) and [MongoDB](https://www.mongodb.org) database servers.  

3.	[RabbitMQ](https://www.rabbitmq.com) message queue server.  

4.	[nginx](http://wiki.nginx.org/Main) web server.

## Assumptions

You are running linux OS upon a suitably powerful machine.  

## Step 1: Install git

**CentOS:**  <pre><code>yum install git</pre></code>  

## Step 2: Install prodiguer shell

<pre><code>git clone https://github.com/Prodiguer/prodiguer-shell.git /opt/prodiguer  
</pre></code>

## Step 3: Run OS setup

**CentOS:**  <pre><code>/opt/prodiguer/exec.sh os-setup centos dev</pre></code>  
