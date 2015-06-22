# T0 - General

* T0.1	Document WEB.API endpoints & their attack vectors
* T0.2	Document MQ.AGENT vulnerabilities
* T0.3	Document STACK.PYTHON vulnerabilities
* T0.4	Define Prodiguer security process (e.g. review frequency & sign-off).
* T0.5	Strengthen unit testing.

# A1 - Injection

* T1.1	Ensure MQ agents validate all message content.
* T1.2	Ensure all web service API endpoint validate all requests.
* T1.3	Ensure all data access operations validate input parameters.
* T1.4	Review external library usage for security issues: Pika, PyMongo, Requests, SQLAlchemy.
* T1.5	Ensure all JSON is safely decoded and validated.

# A2 - Broken Authentication & Session Management

* T2.1	Create DB.PGRES user accounts from WEB.API & MQ.AGENT
* T2.2	Create DB.MONGO user accounts from WEB.API & MQ.AGENT
* T2.3	Review "Metrics Garden" DB.MONGO access controls
* T2.4	Review MQ.AGENT RabbitMQ accounts & access controls ?
* T2.5	Review code base to ensure that no passwords / host addresses are hard coded.
* T2.6	Define MQ.AGENT to WEB.API access control.
* T2.7	Define FE.JS to WEB.API access control.

# A3 - Cross-Site Scripting (CSS)

* T3.1	Ensure that all data that can be displayed in the browser (i.e. FE & metrics garden) was escaped correctly when decoded from original source (e.g. MQ message).
* T3.2	Ensure that all web pages that parse query parameters on page load perform character escaping / url encoding.

# A4 - Insecure Direct Object References

A4.1	Further reading to understand the subject.

# A5 - Security Misconfiguration

A5.1	Review STACK virtual environments.
A5.2	Review STACK configuration file(s) loading.
A5.3	Define acceptable CentOS version(s).
A5.4	Define acceptable DB.PGRES version(s).
A5.5	Define acceptable DB.MONGO version(s).
A5.6	Define acceptable MQ.RABBIT version(s).
A5.7	Define acceptable WEB.NGINX version(s).
A5.8	Consider dockerization of servers.
A5.9	Consider continuous deployment to servers.
A5.10	Consider environment checker - i.e. environment validation script.
A5.11	Ensure all default server accounts are removed, e.g. 'guest', 'admin' ...etc.
A5.12	Disable directory listing for all Prodiguer platform linux process accounts.
A5.13	Ensure WEB.API does not return error messages.

# A6 - Sensitive Data Exposure

A6.1	Review sensistive data - e.g. logins.  Ensure such data is held in encrypted fields.
A6.2	Review all encryption key usage.
A6.3	Review MQ.X509 & WEB.X509 usage.
A6.4	Review WEB.API HTTP Headers.

# A7 - Missing Function Level Access Control

A7.1	Ensure that WEB.API HTTP endpoints perform request validation.
A7.2	Ensure that DB.DAO functions perform parameter validation.
A7.3	Ensure that WEB.URL's mapped to authorization control lists.

# A8 - Cross-Site Request Forgery

A8.1	Ensure that all WEB.API HTTP endpoints perform request validation.
A8.2	Ensure that all WEB.API HTTP endpoint request validation failures are logged.
A8.3	Leverage Tornado CSRF secure session cookie tokens.

# A9 - Using Components With Known Vulnerabilities

A9.1	Document external components used by the platform.
A9.2	Search CVE / NVD databases.
A9.3	Create a Prodiguer email account that subscribes to relevant component / security mailing lists.

# A10 - Unvalidated Redirects and Forwards

A10.1	Further reading to understand the subject.
A10.2	Document all redirects / forwards.

# A11 - Other

A11.1	TODO extend review to cover the below other areas of concern.

• Clickjacking
• Concurrency Flaws
• Denial of Service (Was 2004 Top 10 – Entry 2004-A9)
• Expression Language Injection (CWE-917)
• Information Leakage and Improper Error Handling (Was part of 2007 Top 10 – Entry 2007-A6) • Insufficient Anti-automation (CWE-799)
• Insufficient Logging and Accountability (Related to 2007 Top 10 – Entry 2007-A6)
• Lack of Intrusion Detection and Response
• Malicious File Execution (Was 2007 Top 10 – Entry 2007-A3)
• Mass Assignment (CWE-915)
• User Privacy</code></pre>