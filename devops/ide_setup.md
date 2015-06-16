# Prodiguer IDE Setup

This guide streamlines preparing an IDE (Integrated Development Environment) for Prodiguer platform development.  The supported IDE types are: 
* [sublime-text](http://www.sublimetext.com/)

## Assumptions

You have installed the [prodiguer stack](https://github.com/Prodiguer/prodiguer-docs/blob/master/devops/stack_management.md).  

You have setup sublime text for [python development](https://realpython.com/blog/python/setting-up-sublime-text-3-for-full-stack-python-development/).

## Setting up [sublime-text](http://www.sublimetext.com/)  

1.	Create sublime-text directories: 
<pre><code>mkdir -p /opt/prodiguer/ops/ide/sublime/locals</pre></code>

2.	Create symbolic links to prodiguer stack:  
<pre><code>ln -s /opt/prodiguer/repos/prodiguer-client /opt/prodiguer/ops/ide/sublime/locals/client
ln -s /Users/macg/dev/local/prodiguer/cv /opt/prodiguer/ops/ide/sublime/locals/cv
ln -s /Users/macg/dev/local/prodiguer/docs /opt/prodiguer/ops/ide/sublime/locals/docs
ln -s /Users/macg/dev/local/prodiguer/docs-devops /opt/prodiguer/ops/ide/sublime/locals/docs-devops
ln -s /Users/macg/dev/local/prodiguer/fe /opt/prodiguer/ops/ide/sublime/locals/fe
ln -s /Users/macg/dev/local/prodiguer/fe-monitoring /opt/prodiguer/ops/ide/sublime/locals/fe-monitoring
ln -s /Users/macg/dev/local/prodiguer/fe-simulation /opt/prodiguer/ops/ide/sublime/locals/fe-simulation
ln -s /Users/macg/dev/local/prodiguer/server /opt/prodiguer/ops/ide/sublime/locals/server
ln -s /Users/macg/dev/local/prodiguer/shell /opt/prodiguer/ops/ide/sublime/locals/shell
</pre></code>

3.	Open sublime-text.  

4.	Open new sublime-text project (CTL-SHIFT-N).  

5.	From main menu click: Project -->  Save Project as ...

6.	Save project to: /opt/prodiguer/ops/ide/sublime
	Save project as: prodiguer.sublime-project

7.  From main menu click: Project -->  Add Folder to Project ...

8.	Select folder: /opt/prodiguer/ops/ide/sublime/locals

The IDE will import the symbolic links into the project folder view.  If you wish to add links to other directories within the prodiguer stack then simply repeat step 2.  