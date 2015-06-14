# Prodiguer platform developer documentation - Machine Setup

## Overview

Prodiguer is a highly distributed messaging platform upon which are built several applications.  In order to become an active contributor to the platform you will need to setup your machine so that all required dependencies are installed and running.  The required dependencies consist of c libraries, python libraries, 2 database servers, a web server and a message queue server.  Fortunately the machine setup process has been streamlined to allow you to become productive as soon as possible.

## Step 1: Install git

CentOS:  <pre><code>yum install git</pre></code>  

## Step 2: Install prodiguer shell

<pre><code>git clone https://github.com/Prodiguer/prodiguer-shell.git /opt/prodiguer  
echo 'export PRODIGUER_HOME=/opt/prodiguer' >> ~/.bash_profile  
source ~/.bash_profile  
</pre></code>

## Step 3: Activate prodiguer commands  

<pre><code>
echo 'source /opt/prodiguer/aliases.sh' >> ~/.bash_profile  
source ~/.bash_profile  
</pre></code>

Note 1: Type prodiguer- followed by TAB will display set of supported commands

Note 2: Type help-prodiguer- followed by TAB will display supported command help text

## Step 4: Run OS setup command.

CentOS: prodiguer-os-setup centos dev  

This will setup your machine for development.  It will take at least 30 minutes to run and performs the following tasks:

1.	Install common system dependencies;

2.	Installs [PostgreSQL](http://www.postgresql.org) and [MongoDB](https://www.mongodb.org) database servers.  

3.	Installs [RabbitMQ](https://www.rabbitmq.com) message queue server.  

4.	Installs [nginx](http://wiki.nginx.org/Main) web server.




