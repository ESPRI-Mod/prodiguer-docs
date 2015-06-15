# Prodiguer Environment Variables

The Prodiguer platform is distributed across 3 servers: db, mq & web.  Code running upon each server requires access to sensitive information such as passwords & server addresses.  All such information is stored in environment variables details of which are listed below.  

**Note** The list of supported machine types are: db, mq, web & dev.  Some variables are required across all machines (particulary if your machine is setup for development).

## Variables  

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

**PRODIGUER_DB_PGRES_USER_PASSWORD**  
* Description:	PostgreSQL database password for the _prodiguer_db_user_ account.  
* Machines:		all  

**PRODIGUER_HOME**  
* Description:	Path to local prodiguer home directory.  
* Machines:		all  
* Default:		/opt/prodiguer  

**PRODIGUER_MQ_IMAP_PASSWORD**  
* Description:	IMAP server password for the _superviseur_ account.  
* Machines:		mq, dev  

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

**PRODIGUER_MQ_SMTP_PASSWORD**  
* Description:	SMTP server password for the _superviseur_ account.  
* Machines:		mq, dev

**PRODIGUER_WEB_API_COOKIE_SECRET**  
* Description:	Secret cookie key associated with valid web service requests.  
* Machines:		web, dev  

**PRODIGUER_WEB_HOST**  
* Description:	Web server hostname & port.  
* Machines:		web, dev  
* Default:		localhost:8888  
