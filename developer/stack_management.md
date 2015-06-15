# Prodiguer Stack Management

The Prodiguer stack is the set of software packages and associated command line interface that has been developed by IPSL staff.  It is installed using git and then maintained from the command line. 

## Assumptions

Your linux machine has been [setup correctly](https://github.com/Prodiguer/prodiguer-docs/blob/master/developer/setup_machine.md).  

You have installed the prodiguer command shell:  
<pre><code>git clone https://github.com/Prodiguer/prodiguer-shell.git /opt/prodiguer  
echo 'source /opt/prodiguer/aliases.sh' >> ~/.bash_profile  
source ~/.bash_profile
</pre></code>

## Stack installation  

<pre><code>prodiguer-stack-install</pre></code>

This will perform the following tasks:  

1.	Download prodiguer source code onto your machine.  

2.	Setup an operations directory: /opt/prodiguer/ops  

3.	Create a python executable isolated from the local system python executable.  

4.	Create various python virtual environments used by the platform.  

## Environment variables  

Once the stack is installed upon your machine you will need to setup the various environment variables relevant to your installation.  These are documented [here](https://github.com/Prodiguer/prodiguer-docs/blob/master/developer/environment_variables.md).

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
