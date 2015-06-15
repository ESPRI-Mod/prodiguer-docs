# Prodiguer Environment Variable Setup

## Overview

The Prodiguer platform is distributed across 3 servers: db, mq & web.  Each server requires access to sensitive information such as passwords.  All such information is stored in environment variables details of which are listed below.  

**Note** When running the platform in development mode then all variables listed below must be assigned correctly.

## Variables  

**PRODIGUER_HOME**
Description:	Path to local prodiguer home directory.
Default:		/opt/prodiguer

**PRODIGUER_DB_MONGO_USER_PASSWORD**
Description:	Mongo database password for the _prodiguer-db-mongo-user_ account.


