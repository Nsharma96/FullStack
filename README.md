# Project Log Analysis 
This is a reporting tool made in Python program using the psycopg2 module to connect to the postgre database as part of [Udacity Full Stack Web Developer Nanodegree](https://in.udacity.com/course/full-stack-web-developer-nanodegree--nd004).This tool determines top 3 most popular articles based on page views,most popular authors and also days where site experieced error greater than 1%.

# Prerequisites
- Install Virtual Box version 5.2.12 from [Virtual Box](https://www.virtualbox.org/wiki/Download_Old_Builds_5_2).
- Install Vagrant from [Vagrant](https://www.vagrantup.com/)
- Download or clone [Virtual machine configration file](https://github.com/udacity/fullstack-nanodegree-vm)
- Install [git](https://git-scm.com/)
- Install python.
# Usage
- Download and unzip or clone this repository.Clonning can be done with following command.
```
$ git clone https://github.com/Nsharma96/FullStack.git
```
- Unzip fsnd-virtual-machine.zip(Virtual machine Files)..
- cd to vagrant directory that is where ever you unzipped the fullstack-nanodegree-vm-master.zip.
```
$ Change directory to FSND-Virtual-Machine/vagrant/
```
- Copy the **ReportingTool.py** and **newsdata.sql** to /FSND-Virtual-Machine/vagrant/catalog/ directory.
- Run the Virtual Machine and ssh to vm. 
```
$ vagrant up
$ vagrant ssh
```
- Navigate to catalog Directory.
```
$ cd /catalog
```
- Load the data into PostgreSql database.
```
$ psql -d news -f newsdata.sql
```
- make sure you have pandas library install in your Virtual machine.If not installed use.
```
$ pip install pandas 
       or
$ pip install pandas --user
```
### Creating Views
This tool uses some psql views which need to be created before running ReportingTool.py.In your vm type 
```
$ psql -d news 
```
to connect your database.
- The create write following two sql commands to create necessary views.
```
news=> create view authorViewSums as select articles.author, sum(artiView.num) as authorView from authors ,articles,(select path,count(path) as num from log where status like '%200%' group by path) as artiView where '/article/' || articles.slug = artiView.path and articles.author=authors.id group by articles.author order by authorView desc;
                                  
news=> create view error_Matrix as select distinct extract(day from time ) as d ,extract(month from time) as m ,extract(year from time) as y ,count(case status when '404 NOT FOUND' then 1 else null end) as err,count(status) as total_Requests from log group by y,m,d;

```


### Run The tool
- To See the output of reporting tool type.
```
$ python2 ReportingTool.py
```
# Output
- Output of the reporting tool is shown in the command line itself.Which answers following queries.
  - Most popular 3 Articles of all times.
  - Most popluar Authors of all time.
  - Days which had an error percentage of more than 1 percent.
