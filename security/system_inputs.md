# Prodiguer system inputs  

Prodiguer system inputs vary widely in nature: source code, config files, messages, HTTP requests ...etc.  An input validation failure may indicate a security related event.  Input validation enforces constraints upon input encoding & content.  Inputs are validated at both external & internal system boundaries (i..e defense in depth).  Input validation errors are logged in such a way that sysem operators can be notified of any suspicious errors.  

An example system input validation scenario is as follows.  A Prodiguer web-service endpoint exposes a POST action that results in POST data being passed to a Prodiguer data access object (DAO) which subsequently updates a database.  The web-service endpoint is at an external boundary and validate the raw POST data.  The DAO is at an internal boundary validates the paraemters to be passed to the database for updating.

This document lists the set of Prodiguer platform external system boundary inputs.  For each type of input a security threat level is defined.  

# Message Queue messages (HIGH)

libIGCM publishes data to the Message Queue (MQ) platform via email.  Each email consists of a subject, a body and optional attachments.  The email subject is simple text.  The email body is base64 encoded JSON text.  The email attachments are either .ini or .json files.  

These messages can be sent by anyone with knowledge of the email account to which all messages are sent.  There is also the possibilty that the email server is itself compromised.   Thus this attack vector is wide.  

# Stack configuration files (MEDIUM)  

The Prodiguer platform loads several configuration files either at start up or in response to invocation of a prodiguer command.  These files can be tampered with if a Prodiguer server is compromised.  The list of such files is as follows:  

* PRODIGUER_HOME/ops/config/prodiguer.json  

* PRODIGUER_HOME/ops/config/prodiguer.sh  

* PRODIGUER_HOME/ops/config/mq-supervisord.conf  

* PRODIGUER_HOME/ops/config/web-supervisord.conf  

# Stack environment variables (MEDIUM)  

The Prodiguer platform uses environment variables to store sensitive configuration information.  Any or all of these variables can be tampered with if a Prodiguer server is compromised.  The set of variables is as follows:

* PRODIGUER_CLIENT_WEB_URL   
* PRODIGUER_DB_MONGO_HOST   
* PRODIGUER_DB_MONGO_USER_PASSWORD  
* PRODIGUER_DB_PGRES_HOST  
* PRODIGUER_DB_PGRES_USER_PASSWORD  
* PRODIGUER_HOME  
* PRODIGUER_MQ_IMAP_PASSWORD  
* PRODIGUER_MQ_RABBIT_HOST  
* PRODIGUER_MQ_RABBIT_LIBIGCM_USER_PASSWORD  
* PRODIGUER_MQ_RABBIT_USER_PASSWORD  
* PRODIGUER_MQ_SMTP_PASSWORD  
* PRODIGUER_WEB_API_COOKIE_SECRET  
* PRODIGUER_WEB_HOST  

# Stack template files (MEDIUM)  

The Prodiguer platform uses a few template files when a stack update is performed.  These files can be tampered with if either a Prodiguer GitHub account or Prodiguer server is compromised.  The list of such files is as follows:  

* PRODIGUER_HOME/shell/templates/config/mq-rabbit.json  

* PRODIGUER_HOME/shell/templates/venv/requirement-server.txt  

# Service configuration files (MEDIUM)  

The Prodiguer platform leverages several 3rd party services each of which loads configuration file(s) at start up.  Any or all of these files can be tampered with if a Prodiguer server is compromised.  The list of such services are as follows:  

* RabbitMQ

* NGinx  

* PostgreSQL  

* MongoDB  

# Web service endpoints (HIGH)

The Prodiguer web-service exposes a set of HTTP(S) endpoints.  HTTP requests made to these endpoints are processed by Prodiguer web handlers.  Request processing can alter system state, e.g. by updating a database.  These endpoints can be compromised simply by sending mal-formed HTTP requests.  They can also be compromised via "man-in-the-middle" attacks in which well-formed requests are substituted for mal-formed ones.  Denial of service attacks may bring down the web-server.  Thus this attack vector is wide.   

* /api/1/monitoring/fe/cv  (GET)
* /api/1/monitoring/fe/setup/all  (GET)
* /api/1/monitoring/fe/setup/one  (GET)
* /api/1/monitoring/fe/ws/all
* /api/1/monitoring/event  (POST)
* /api/1/metric/add  (POST)
* /api/1/metric/delete  (POST)
* /api/1/metric/fetch  (GET)
* /api/1/metric/fetch_count  (GET)
* /api/1/metric/fetch_columns  (GET)
* /api/1/metric/fetch_list  (GET)
* /api/1/metric/fetch_setup  (GET)
* /api/1/metric/rename  (POST)
* /api/1/metric/set_hashes  (POST)
* /api/1/ops/heartbeat  (GET)
* /api/1/ops/list_endpoints  (GET)

# Controlled vocabularies (MEDIUM)  

The Prodiguer platform uses controlled vocabularies (CV's) for various purposes including whitelist validatation of data flowing through the system.  CV validation is in some cases 'soft', i.e. new terms are accepted by the system.  

All Prodiguer CV's are hosted with the prodiguer-cv GitHub repo.  These files can be tampered with if either a Prodiguer GitHub account or Prodiguer server is compromised.  

# Source code (MEDIUM)  

Prodiguer source code is itself a system input.  All such code is stored upon the publically available Prodiguer GitHub space.  Write permissions to this space is restricted to Prodiguer team members and the Prodiguer system GitHub account.  Source code can be tampered with if either a Prodiguer GitHub account or Prodiguer server is compromised.  

GitHub is in daily use by millions of applications and has a [well documented security policy](https://help.github.com/articles/github-security/).  Thus it is assumed that Prodiguer source code on remote GitHub servers is trusted.  However that does not mean that the source code itself is secure as it may contain hard coded senstive information such as passwords.  Furthermore a GitHub account with write permissions to one or more of the Prodiguer repositories can of course be compromised by (for example) the use of weak passwords.  

Git versioned source residing upon local machines is of course vulnerable to local tampering if the host machine is compromised.  If a GitHub account with write permissions to the Prodiguer GitHub space is also compromised, then a pathway opens up for compromising the remote Prodiguer source as well.  

It is self-evident that Prodiguer team members must respect best practises when it comes to managing their GitHub user accounts.  Furthermore Prodiguer servers must monitor file system tampering and shutdown Prodiguer services when such tampering occurs.  
