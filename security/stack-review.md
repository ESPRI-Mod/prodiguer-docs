# A0 - Overview

The Prodiguer platform is a highly distributed messaging platform.  The OWASP (Open Web Application Security Project) maintains it's so-called "Top 10 project" the goal of which is to raise awareness about application security by identifying some of the most critical risks facing organizations.  Essentially it is an application security analysis framework that guides an analyst through the identification of application security risks.

This document reviews the Prodiguer platform using the OWASP framework and proposes a set of actions to be taken in order to reinforce the security robustness of the Prodiguer platform.  

# A1 - Injection

<pre><code>Injection flaws, such as SQL, OS, and LDAP injection occur when untrusted data is sent to an interpreter as part of a command or query. The attacker’s hostile data can trick the interpreter into executing unintended commands or accessing data without proper authorization.<pre><code>

Q.	Am I Vulnerable To SQL / NoSQL injection attacks ?

Prodiguer platform uses 2 databases to manage system state: 

1.	PostgreSQL relational database;

2.	MongoDB NOQSQL database.

To interact with the databases the Prodiguer platform leverages the SqlAlchemy and pymongo python libraries.  These libraries are considered the best in the python eco-system and both provide a parameterized interface that implicitly performs character escaping to obviate injection attacks.  Thus Prodiguer benefits from out of the box protection for SQL/NoSQL injection.  However it is necessary to ensure that the installed libraries are kept upto date and monitored for potential security related issues - see section A5.  

As stated these libraries perform parameter escaping so as to ensure that SQL / NoSQL injection attacks cannot occur, however this does not mean that the incoming parameters do not need to be validated and parsed by the Prodiguer platform itself.  The incoming parameters are inputs into functions exposed by the data access layer, all such inputs needs to therefore be validated prior to invoking the SqlAlchemy / PyMongo libraries.  This follows the defense in depth principle.  

Q.	Am I Vulnerable To Base64 injection attacks ?  

When processing Base64 encoded data a system may be vulnerable to Base64 injection attacks.  The Prodiguer platform accepts as Base64 encoded input data:

1.	Emails containing data destined for the MQ platform.  

The decoding of these inputs transforms the incoming Base64 to text blobs for further processing.  

Q.	Am I Vulnerable To JSON injection attacks ?

When processing JSON encoded data a system may be vulnerable to JSON injection attacks.  The Prodiguer platform accepts as JSON encoded input data:

1.	Messages flowing through the MQ platform consumed by MQ consumers.  

2.	Email attachments destined for the MQ platform.  The attachments may be either:

	2.1	PCMDI metrics files. 

3.	The prodiguer.json configuration file.  This file resides in the PRODIGUER_HOME/ops/config folder.  

4.	Data posted to several Prodiguer web-service API endpoints.  

5.	Prodiguer controlled vocabulary files.   

The decoding of these inputs transforms the incoming JSON to python dictionaries prior to further processing.  The Prodiguer platform leverages the python standard libray JSON decoder, therefore this decoder must be 'safe'.  Furthermore the decoded content must be validated against json schemas.

However prior to decoding JSON content 

Q.	Am I Vulnerable To INI file injection attacks ?  


Q.	Am I Vulnerable To XML injection attacks ?

Neither the Prodiguer platform or any of its 3rd party dependencies use XML encoded data in any of its inputs or outputs.  

DB.PGRES.SQL from WEB.API
DB.PGRES.SQL from MQ.CONSUMER
STACK.JSON from OS.CONFIG
STACK.JSON from MQ.AGENT

# A2 - Broken Authentication & Session Management

<pre><code>Application functions related to authentication and session management are often not implemented correctly, allowing attackers to compromise passwords, keys, or session tokens, or to exploit other implementation flaws to assume other users’ identities.<pre><code>

# A3 - Cross-Site Scripting (CSS)

<pre><code>XSS flaws occur whenever an application takes untrusted data and sends it to a web browser without proper validation or escaping. XSS allows attackers to execute scripts in the victim’s browser which can hijack user sessions, deface web sites, or redirect the user to malicious sites.<pre><code>

# A4 - Insecure Direct Object References

<pre><code>A direct object reference occurs when a developer exposes a reference to an internal implementation object, such as a file, directory, or database key. Without an access control check or other protection, attackers can manipulate these references to access unauthorized data.</code></pre>

# A5 - Security Misconfiguration

<pre><code>Good security requires having a secure configuration defined and deployed for the application, frameworks, application server, web server, database server, and platform. Secure settings should be defined, implemented, and maintained, as defaults are often insecure. Additionally, software should be kept up to date.</code></pre>

# A6 - Sensitive Data Exposure

<pre><code>Many web applications do not properly protect sensitive data, such as credit cards, tax IDs, and authentication credentials. Attackers may steal or modify such weakly protected data to conduct credit card fraud, identity theft, or other crimes. Sensitive data deserves extra protection such as encryption at rest or in transit, as well as special precautions when exchanged with the browser.</code></pre>

# A7 - Missing Function Level Access Control

<pre><code>Most web applications verify function level access rights before making that functionality visible in the UI. However, applications need to perform the same access control checks on the server when each function is accessed. If requests are not verified, attackers will be able to forge requests in order to access functionality without proper authorization.</code></pre>

# A8 - Cross-Site Request Forgery

<pre><code>A CSRF attack forces a logged-on victim’s browser to send a forged HTTP request, including the victim’s session cookie and any other automatically included authentication information, to a vulnerable web application. This allows the attacker to force the victim’s browser to generate requests the vulnerable application thinks are legitimate requests from the victim.</code></pre>

# A9 - Using Components With Known Vulnerabilities

<pre><code>Components, such as libraries, frameworks, and other software modules, almost always run with full privileges. If a vulnerable component is exploited, such an attack can facilitate serious data loss or server takeover. Applications using components with known vulnerabilities may undermine application defenses and enable a range of possible attacks and impacts.</code></pre>

# A10 - Unvalidated Redirects and Forwards

<pre><code>Web applications frequently redirect and forward users to other pages and websites, and use untrusted data to determine the destination pages. Without proper validation, attackers can redirect victims to phishing or malware sites, or use forwards to access unauthorized pages.</code></pre>

# A11 - Other

<pre><code>The Top 10 cover a lot of ground, but there are many other risks you should consider and evaluate in your organization. Some of these have appeared in previous versions of the Top 10, and others have not, including new attack techniques that are being identified all the time. Other important application security risks (in alphabetical order) that you should also consider include:

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
