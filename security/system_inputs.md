# Prodiguer platform system inputs  

From a security perspective a fundamental system task is the validation of all system inputs prior to acceptance for further processing.  Such validation involves enforcing constraints related to both input encoding and content.  For example validating a JSON encoded text input requires verifying that the text is valid and safe JSON and then verifying that the decoded JSON confirms to validation rules such as "The msgCode field is required". 

The defense in depth principle states that system inputs should be validated at both the system's external & internal boundaries.  For example an external system boundary may be a publically available web-service.  Such a web-service may call an database access function exposed by a system sub-component.  Thus input validation needs to occur within the web-service (external system boundary) and in the database access function (internal system boundary).

This document details the set of Prodiguer platform system inputs.  

# Messages published to the MQ platform by libIGCM.  

libIGCM publishes data to the MQ platform via email.  Each email consists of a subject, a body and optional attachments.  The email subject is simple text.  The email body is base64 encoded JSON text.  The email attachments are either .ini or .json files.  Anyone can send an email to the Prodiguer email server thus this attack vector is wide.  

Messages published to the MQ platform by libIGCM are considered to be a HIGH security threat.  

# Stack configuration files.  

The Prodiguer platform loads several configuration files either at start up or in response to invocation of a prodiguer command.  These files can be tampered with if a Prodiguer server is compromised.  The list of such files is as follows:  

* PRODIGUER_HOME/ops/config/prodiguer.json  

* PRODIGUER_HOME/ops/config/prodiguer.sh  

* PRODIGUER_HOME/ops/config/mq-supervisord.conf  

* PRODIGUER_HOME/ops/config/web-supervisord.conf  

Stack configuration file tampering is considered to be a MEDIUM security threat.  

# Stack environment variables  

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

Stack environment variable tampering is considered to be a MEDIUM security threat.  

# Stack template files.  

The Prodiguer platform a few template files that are used when updating the stack.  These files can be tampered with if a Prodiguer GitHub account is compromised.  The list of such files is as follows:  

* PRODIGUER_HOME/shell/templates/config/mq-rabbit.json  

* PRODIGUER_HOME/shell/templates/venv/requirement-server.txt  

Stack configuration file tampering is considered to be a MEDIUM security threat.  

# Service configuration files.  

The Prodiguer platform leverages several 3rd party services each of which loads configuration file(s) at start up.  Any or all of these files can be tampered with if a Prodiguer server is compromised.  The list of such services are as follows:  

* RabbitMQ

* NGinx  

* PostgreSQL  

* MongoDB  

Service configuration file tampering is considered to be a MEDIUM security threat.

# WEB service endpoints.  

The Prodiguer WEB service exposes a set of HTTP(S) endpoints.  HTTP requests made to these endpoints are handler by Prodiguer web handlers.  Each handler processes the incoming HTTP requests.  Request processing may alter system state, e.g. by updating a database.  These endpoints can be attacked simply by sending mal-formed HTTP requests.  They can also be attacked by over-writing well-formed requests via request interception.  

* /api/1/monitoring/fe/cv
* /api/1/monitoring/fe/setup/all
* /api/1/monitoring/fe/setup/one
* /api/1/monitoring/fe/ws/all
* /api/1/monitoring/event
* /api/1/metric/add
* /api/1/metric/delete
* /api/1/metric/fetch
* /api/1/metric/fetch_count
* /api/1/metric/fetch_columns
* /api/1/metric/fetch_list
* /api/1/metric/fetch_setup
* /api/1/metric/rename
* /api/1/metric/set_hashes
* /api/1/ops/heartbeat
* /api/1/ops/list_endpoints

WEB service endpoint tampering is considered to be a HIGH security threat.  

# Controlled vocabularies.  

The Prodiguer platform loads controlled vocabularies (CV's) to validate data flowing the system.  Such validation ensures that an input conforms to a whitelist.  The validation of CV related data is in some cases soft, i.e. new terms are accepted by the system.  

All Prodiguer CV termsets are hosted with the prodiguer-cv GitHub repo.  The prodiguer-git-user account has write permissions to this account.  Therefore GitHub related security best proactises come into scope.

# Source code  

Prodiguer source code is itself a system input.  All such code is stored upon the publically available Prodiguer GitHub space.  Write permissions to this space is restricted to Prodiguer team members with the sole exception that the prodiguer-git-user system account has write permissions to the prodiguer-cv repo.  

GitHub is in daily use by millions of applications and has a [well documented security policy](https://help.github.com/articles/github-security/).  Thus it is assumed that Prodiguer source code on remote GitHub servers is trusted.  However that does not mean that the source code itself is secure as it may contain hard coded passwords or production config files.  Furthermore a GitHub account with write permissions to one or more of the Prodiguer repositories can of course be compromised by (for example) the use of weak passwords.  

Git versioned source residing upon local machines is of course vulnerable to local tampering if the host machine is compromised.  If a GitHub account with write permissions to the Prodiguer GitHub space is also compromised, then a pathway opens up for compromising the remote Prodiguer source as well.  

It is self-evident that Prodiguer team members must respect best practises when it comes to managing their GitHub user accounts.  Furthermore Prodiguer servers must monitor file system tampering and shutdown Prodiguer services when such tampering occurs.  

Source code tampering is considered to be a MEDIUM security threat.

