### Project Name: Item Catalog
This project catalogs items that logged in users can create, edit and delete. Anyone may view information about them and get Json Endpoints for them.

#### Requirements
- Virtual Box [https://www.virtualbox.org/wiki/Downloads]
- Vagrant [https://www.vagrantup.com/downloads.html]
- Flask Library 
-Oath2client
-Google Account


#### Files
itemcatalog.py
catalogdatabasesetup.py
Catalog.db
client_secrets.json
Templates folder[Edit, Display, additem and sign in html files


I first made the the server display various html templates at various address. I then made the Item class and intitialized the database. I wrote flask code to back up the templates by 
using the database. I then created Google Sign in button by registering with Google and using a template for the login button with help from my mentor. 

JSON Endpoints may be accessed by requesting '/json/'  followed by an item id.

The Python script was made with Python 3.7 on a Ubuntu virtual machine with Vagrant. Use Git Bash or other command-line interface
to go to the directory you want this in. Enter in "vagrant init" to create the enviroment. Enter "vagrant up" to get the 
enviroment running and then "vagrant ssh" to log in.
Then run "python itemcatalog.py" to run

It is reachable at localhost:5000.