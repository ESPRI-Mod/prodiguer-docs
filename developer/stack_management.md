# Prodiguer Stack Management

## Overview

The Prodiguer stack is the set of software packages and associated command line interface that has been developed by IPSL staff.  It is installed using git and then maintained using the prodiguer-stack-XXXXX commands from the command line. 

## Assumptions

You are running linux OS upon a suitably powerful machine.  The machine has been [setup correctly](https://github.com/Prodiguer/prodiguer-docs/blob/master/developer/setup_machine.md).

## Stack installation  

<pre><code>git clone https://github.com/Prodiguer/prodiguer-shell.git /opt/prodiguer  
echo 'source /opt/prodiguer/aliases.sh' >> ~/.bash_profile  
source ~/.bash_profile  
prodiguer-stack-install
</pre></code>

This will perform the following tasks:  

1.	Download prodiguer source code onto your machine.  

2.	Setup an operations directory: /opt/prodiguer/ops  

3.	Create a python executable isolated from the local system python executable.  

4.	Create various python virtual environments used by the platform.  

## Stack commands    

To display set of prodiguer commands:  

<pre><code>prodiguer-[**TAB-KEY**]</pre></code>

To display prodiguer command help text:  

<pre><code>help-prodiguer-[**TAB-KEY**]</pre></code>

## Stack updating  

To update the entire stack:  
<pre><code>prodiguer-stack-update</pre></code>

To update just the source code:  
<pre><code>prodiguer-stack-update-source</pre></code>

To update just the virtual environments:  
<pre><code>prodiguer-stack-update-venvs</pre></code>

**NOTE** 99% of the time you will only need to update the source, i.e. prodiguer-stack-update-source.

## Stack uninstallation  

<pre><code>prodiguer-stack-uninstall</pre></code>
