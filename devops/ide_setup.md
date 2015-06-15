# Prodiguer IDE Setup

This guide streamlines preparing an IDE (Integrated Development Environment) for Prodiguer platform development.  The supported IDE types are: 
* [sublime-text](http://www.sublimetext.com/);

## Assumptions

You have installed the [prodiguer stack](https://github.com/Prodiguer/prodiguer-docs/blob/master/devops/stack_management.md).  

## Setting up [sublime-text](http://www.sublimetext.com/)  

1.	Create a sublime-text project directory: 
<pre><code>mkdir -p /opt/prodiguer/ops/ide/sublime
mkdir -p /opt/prodiguer/ops/ide/sublime-locals
</pre></code>

2.	Create prodiguer stack symbolic links:  
<pre><code>ln -s /opt/prodiguer/repos/prodiguer-client /opt/prodiguer/ops/ide/sublime-locals/client
ln -s /Users/macg/dev/local/prodiguer/cv /opt/prodiguer/ops/ide/sublime-locals/cv
ln -s /Users/macg/dev/local/prodiguer/docs /opt/prodiguer/ops/ide/sublime-locals/docs
ln -s /Users/macg/dev/local/prodiguer/fe /opt/prodiguer/ops/ide/sublime-locals/fe
ln -s /Users/macg/dev/local/prodiguer/fe-monitoring /opt/prodiguer/ops/ide/sublime-locals/fe-monitoring
ln -s /Users/macg/dev/local/prodiguer/fe-simulation /opt/prodiguer/ops/ide/sublime-locals/fe-simulation
ln -s /Users/macg/dev/local/prodiguer/server /opt/prodiguer/ops/ide/sublime-locals/server
ln -s /Users/macg/dev/local/prodiguer/shell /opt/prodiguer/ops/ide/sublime-locals/shell
</pre></code>

3.	Open sublime-text.  

4.  Create prodiguer sublime-text project.

5.	


