Summary
=======================================================

Here is the deployment report for the 0.4.0.0 platform release.  Before reading the report it is worth reviewing the deployment note & the deployment change log. 

Deployment to all servers was quite smooth.  Nothing blocked the deployment being rolled out.  However 2 front-end related issues have been identified that need immediate attention.

Deployment issues
--------------------------------------

1.	On the MQ server the daemon logs for both stdout and stderr are being writing to the same log file rather than different log files.  

- Deployment Impact: nil

- Action: MG will update the template mq-supervisord.conf file accordingly

- Action: NC will update the /opt/prodiguer/ops/daemons/mq/supervisord.conf file on the MQ server when given green light by MG.

2.	On the prodiguer test server the prodiguer venv python version is 2.7.6.  This should be updated to 2.7.10.

- Action: MG to test shell update-python command.

- Action: NC will rollout update when given green light by MG.

3.	When executing the command prodiguer-db-pgres-migrate a warning was emitted saying that a new db sequence object had already been created.  This had no effect on the deployment.

- Deployment Impact: nil

- Action: MG to update the migrate sql script.

4.	python is buffering output to the daemon log files.  The -u python flag needs to be applied but only when debugging (e.g. when testing system deployment).

- Deployment Impact: nil

- Action: MG will provide an mq-supervisord-debug.conf template to be used during debugging.  

- Action: NC will restart the daemons using this debugging template and then revert back to the normal template when satisfied.

5.	Automated git pushes from the MQ server to the prodiguer-cv repo have not been functioning since 29/06.  Need to understand why.

- Deployment Impact: NC had to manually commit

- Action: NC will analyse why the prodiguer-cv-git-push command is failing

Deployment Patches
--------------------------------------

1.	When running the front-end from NC’s browser the calls to the underlying web-service were being rejected as NC’s browser was appending a cookie to the HTTP request headers.  On the server side HTTP request validation was enforcing the constraint that the HTTP request should not contain any cookies.  A patch was issued to relax this constraint.

	Deployment Impact: blocker - resolved with simple patch

	Action: MG will analyse why NC’s browser injected this cookie into the request and if viable add cookie validation on the server side.

	Action NC: will email MG the version of Firefox that he is currently using.


Testing issues
--------------------------------------

1.	When testing the front-end MG noticed that on the simulation detail page the list of jobs is not being displayed at all.

- Deployment impact: blocker

- Action: MG will debug front-end to verify that the web-service is returning page setup data correctly.  If the web-service response is OK then MG will debug javascript to see if a web-service parsing issue is causing the issue.  

2.	Some job related web-socket events are not being pushed to the browser.  unicode decoding issues are being logged on the web-server and this appears to be causing the event push to be aborted.

- Deployment impact: blocker

- Action: MG Will try to replicate issue in his environment.  If replicable he will analyse and issue patch.  If not he will downgrade his python version to 2.7.6 and retest.

3.	The python library ‘requests' is reporting warnings due to urllib3 not performing client certificate validation on HTTPS calls to the prodiguer web service from either the prodiguer-client or the internal-api MQ consumer. 

- Deployment impact: nil (however logs will contain these warnings)

- Action: MG will explore options for either suppressing (temporarily) this warning or for issuing a patch so that requests does not use urllib3 when performing the certificate negotiation.

4.	Dead emails are still sitting in the AMPQ-PROD mailbox.  The ext-smtp-realtime MQ agent should be placing these emails in the ext-smtp queue.  The ext-smtp MQ agent should be processing these emails and then moving them to the AMPQ-PROD-PROCESSED mailbox, even if these emails are invalid or contain duplicate messages.

- Deployment impact: nil (however we need to fully understand what is happening in this scenario)

- Action: MG to test these emails in his environment and debug accordingly.  If a code patch is required he will issue it and instruct NC to update the MQ server accordingly.


Miscellaneous
--------------------------------------

1.	It was agreed when NC has time he will attempt to familiarise himself more deeply with the prodiguer stack.  This will widen the team’s deployment knowledge base and enable him to be more fluent in relation to deployments.

- Action: MG to email NC links to documents and source code that will enable him to improve his stack knowledge.

- Action: MG to notify NC when developer documentation v1 is available.

