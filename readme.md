#Udacity Catalog Project

This is a simple catalog app built with Python, Flask and SQLAlchemy. The app supports user authentication and authorization using OAuth 2.0 and Google Login .
Logged in users can add categories and items, as well as edit, delete categories and items that they have created. Users who are not logged in can view the contents of the catalog but cannot make changes.

####Installation

1. nstall git .  To install git on Mac from: http://git-scm.com/download/mac. To install git on Windows,from: http://git-scm.com/download/win.
2. install python  To install python on Mac from: https://www.python.org/ftp/python/2.7.12/python-2.7.12-macosx10.6.pkg. To install python on Windows from: https://www.python.org/ftp/python/2.7.12/python-2.7.12.msi.
3.install Virtual Box from https://www.virtualbox.org/wiki/Downloads.
4.install Vagrant from https://www.vagrantup.com/downloads.
5. Open git .
6. Change to directory by run :`cd Downloads/vagrant file`
3. run `chcp.com 1252`
4. Move to the *vagrant* folder by entering: `cd ~/vagrant/`
5. Clone the github repository by running the command below:
  - Run: `git clone https://github.com/ruslanml/Udacity-Catalog-Project.git`
  - This will create a directory inside the *vagrant* directory titled *catalog*.
6. Run Vagrant by this command: `vagrant up`
7. run this command: `vagrant ssh` to log in
8. Move to *catalog* directory by entering: `cd /vagrant/catalog/`
9. Run the project file by run: `python project.py`
10.open your browser and go to : `http://localhost:5000/`