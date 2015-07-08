# Prodiguer Environment Variables

The Prodiguer platform is distributed across different types of machine.  Code running upon each machine requires access to sensitive information such as passwords & server addresses.  All such information is stored in environment variables details of which are listed below.  

**Note** The list of supported machine types are: db, mq, web & dev.  Some variables are required across all machines (particulary if your machine is setup for development).

# General Variables

**PRODIGUER_HOME**  
* Description:	Path to local prodiguer home directory.  
* Machines:		all  
* Default:		/opt/prodiguer  

**PRODIGUER_DEPLOYMENT_MODE**  
* Description:	Mode of deployment.  
* Machines:		all  
* Default:		test  

**PRODIGUER_CLIENT_WEB_URL**  
* Description:	Web service url from prodiguer client.  
* Machines:		mq, dev  
* Default:		https://prodiguer-test-web.ipsl.fr  

# DB server variables

**PRODIGUER_DB_MONGO_HOST**  
* Description:	Mongo server hostname & port.  
* Machines:		all  
* Default:		localhost:27017  

**PRODIGUER_DB_MONGO_USER_PASSWORD**  
* Description:	Mongo database password for the _prodiguer-db-mongo-user_ account.  
* Machines:		all  

**PRODIGUER_DB_PGRES_HOST**  
* Description:	PostgreSQL server hostname & port.  
* Machines:		all  
* Default:		localhost:5432  

**PRODIGUER_DB_PGRES_USER_PASSWORD** (if .pg_pass **not** used)  
* Description:	PostgreSQL database password for the _prodiguer_db_user_ account.  
* Machines:		all  

# MQ server variables

**PRODIGUER_MQ_RABBIT_HOST**  
* Description:	RabbitMQ server hostname & port.  
* Machines:		mq, dev
* Default:		localhost:5671  

**PRODIGUER_MQ_RABBIT_LIBIGCM_USER_PASSWORD**  
* Description:	RabbitMQ password for the _libigcm-mq-user_ account.  
* Machines:		mq, dev

**PRODIGUER_MQ_RABBIT_USER_PASSWORD**  
* Description:	RabbitMQ password for the _prodiguer-mq-user_ account.  
* Machines:		mq, dev

**PRODIGUER_MQ_RABBIT_SSL_CLIENT_CERT**  (if client ssl cert used)
* Description:	Client ssl cert file path.  
* Machines:		mq, dev
* Default		$PRODIGUER_HOME/ops/certs/rabbitmq/client-cert.pem  

**PRODIGUER_MQ_RABBIT_SSL_CLIENT_KEY**  (if client ssl cert used)
* Description:	Client ssl key file path.  
* Machines:		mq, dev
* Default		$PRODIGUER_HOME/ops/certs/rabbitmq/client-key.pem  

**PRODIGUER_MQ_IMAP_PASSWORD**  
* Description:	IMAP server password for the _superviseur_ account.  
* Machines:		mq, dev  

**PRODIGUER_MQ_SMTP_PASSWORD**  
* Description:	SMTP server password for the _superviseur_ account.  
* Machines:		mq, dev

# Web server variables

**PRODIGUER_WEB_API_COOKIE_SECRET**  
* Description:	Secret cookie key associated with valid web service requests.  
* Machines:		web, dev  
Note - generate using [this site](http://passwordsgenerator.net)

**PRODIGUER_WEB_HOST**  
* Description:	Web server hostname & port.  
* Machines:		web, dev  
* Default:		localhost:8888  

**PRODIGUER_WEB_URL**  
* Description:	Web service url.  
* Machines:		mq, dev  
* Default:		https://prodiguer-test-web.ipsl.fr  
