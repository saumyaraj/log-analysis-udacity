# Newspaper Log Analysis - Udacity project
This project is for analyzing the web logs for a newspaper application

## Project Requirements
Reporting tool should answer the following questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

* Project follows good SQL coding practices: Each question should be answered with a single database query.
* The code is error free and conforms to the PEP8 style recommendations.
* The code presents its output in clearly formatted plain text.

## System setup and how to view this project
This project makes use of Udacity's Linux-based virtual machine (VM) configuration which includes all of the necessary software to run the application.
1. Download [Vagrant](https://www.vagrantup.com/) and install.
2. Download [Virtual Box](https://www.virtualbox.org/) and install.
3. Clone this repository to a directory of your choice.
4. Download the **newsdata.sql** (extract from **newsdata.zip**) and **newsdata.py** files from the respository and move them to your **vagrant** directory within your VM.

#### Run these commands from the terminal in the folder where your vagrant is installed in:
1. ```vagrant up``` to start up the VM.
2. ```vagrant ssh``` to log into the VM.
3. ```cd /vagrant``` to change to your vagrant directory.
4. ```psql -d news -f newsdata.sql``` to load the data and create the tables.
5. ```python3 newsdata.py``` to run the reporting tool.
6. sudo apt-get install postgresql
7. sudo apt-get install python-psycopg2
8. sudo apt-get install libpq-dev
9. pip3 install psycopg2

## Output
![Output](/output.png)

## Helpful Resources
* [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
* [PostgreSQL 9.5 Documentation](https://www.postgresql.org/docs/9.5/static/index.html)
* [Vagrant](https://www.vagrantup.com/downloads)
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
