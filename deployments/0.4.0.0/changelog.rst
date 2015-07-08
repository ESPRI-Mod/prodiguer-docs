Prodiguer Platform - Server Changelog
======================================

- version: 0.4.0.0

General changes
--------------------------------------

- Updated Python virtual environment dependencies

- Updated configuration to use environment variables

- Moved source code folder up one level

DB Changes
--------------------------------------

- New sequence: monitoring.tbl_environment_metric_id_seq

- New table: monitoring.tbl_environment_metrics

- New column: monitoring.tbl_job.accounting_project

- New column: monitoring.tbl_job.typeof

- New column: monitoring.tbl_simulation.accounting_project

- New column: monitoring.tbl_simulation.activity_raw

- New column: monitoring.tbl_simulation.compute_node_raw

- New column: monitoring.tbl_simulation.compute_node_login_raw

- New column: monitoring.tbl_simulation.compute_node_machine_raw

- New column: monitoring.tbl_simulation.model_raw

- New column: monitoring.tbl_simulation.space_raw

Documentation Changes
--------------------------------------

- Prepared code base for sphinxification

- Updated shell install guide

- Updated OS setup guide

FE Changes
--------------------------------------

- External library dependencies updated (e.g. jquery, underscore, backbone ... etc)

- Post-processing jobs being streamed over web sockets

- Simulation page displays post-processing jobs

- Rationalised HTML page names

- Spin up job is correctly displayed

- Incomplete jobs are correctly displayed

- Job type field is displayed

- Simulation accounting project field is displayed

- Job accounting project field is displayed

- Factored out code shared between simulation list and simulation detail pages

- Updated simulation parser so that all job type collections are fully built

- Added external dependency code source maps

- Updated metrics APi test page to point to updated endpoints

- Added inter-monitoring link to simulation detail page

- Split jobs tables according to job type

MQ changes
--------------------------------------

- Created agent: in-monitoring-2000: post-processing job start

- Created agent: in-monitoring-2100: post-processing job complete

- Created agent: in-monitoring-2900: post-processing job error

- Created agent: in-monitoring-3000: post-processing (from checker) job start

- Created agent: in-monitoring-3100: post-processing (from checker) job complete

- Created agent: in-monitoring-3900: post-processing (from checker) job error

- Created agent: in-monitoring-2000: post-processing job start

- Created agent: in-monitoring-7100: environment metrics

- Created queue: in-monitoring-compute

- Created queue: in-monitoring-post-processing

- Created queue: in-metrics-env

- Created queue: in-metrics-sim

- Dropped queue: in-monitoring

- Dropped queue: internal-sms

- Dropped queue: internal-smtp

- Refactored agent: ext-smtp-realtime

- Updated agent: ext-smtp excludes messages considered obsolete

- Updated agent: ext-smtp excludes messages defined within configuration

- Updated agent: in-monitoring-7100 processes attachments

- Updated agent: in-monitoring-0000 persists raw CV related simulation fields to db

- Updated agent: in-monitoring-0000 persists Accounting Project field to db

- Updated agent: in-monitoring-1000 persists Accounting Project field to db

- Miscellaneous: updated rabbitmq.json config file

- Miscellaneous: updated agent entry point to route to new sub-agents

- Miscellaneous: presenting client SSL cert is now optional

- Miscellaneous: streamlined logging

Shell Changes
--------------------------------------

- New command: prodiguer-db-pgres-migrate

- New command: prodiguer-db-pgres-reset-cv-table

- New command: prodiguer-db-pgres-reset-email-table

- New command: prodiguer-db-pgres-reset-message-table

- New command: prodiguer-mq-purge-debug-queues

- New command: prodiguer-stack-update-aliases

- New command: prodiguer-stack-update-config

- New command: prodiguer-stack-upgrade-venv

- New command: prodiguer-stack-upgrade-venvs

Unit Test Changes
--------------------------------------

- Refactored: simulation metrics unit tests

WEB Changes
--------------------------------------

- Refactored web service endpoint url's

- All requests to all endpoints are now fully validated

- Ensured correct HTTP error response codes are returned

- Dropped endpoint: /api/1/ops/list_endpoints

- Restructured so that endpoint handlers are in a dedicated sub-package

- Restructured so that utility functions are in a dedicated sub-package

- New endpoint handler base class: ProdiguerWebServiceHandler

- Dropped obsolete handler utility functions

- Simulation metrics: ensured that row id is always returned

- Simulation metrics: ensured that returned metrics are formatted with OrderedDict

- Aggregations discovery: added endpoint hook in readiness for integration with GL's library

- Post-processing job events streamed to web socket clients
