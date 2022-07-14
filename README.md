# -Unstructured-DATABASE

Description: In this project we create database to handle unstructured data for this we use NOSQL database and created schema attributes on fly during runtime and uses JSON format to store the data. In front end we parse this JSON data into table format and apply Full Text search algorithm on nested JSON data using stemming algorithm where we pass Text as search vector. Also from front end we can Import data from JSON, CSV ,XLS and pdf format and Export in JSON, CSV and XLS. Prerequisites and Installation: 

• List of all the dependencies:

 1. In this project first we install Django for backend

		pip install Django
	
2. Setup MONGODB database install MONGODB Compass GUI

3. For connection between Django and MONGODB we uses PyMongo. PyMongo is very efficient for writing JSON data to MongoDB and allows the use of MongoDB queries 	in the Python code itself. We can retrieve data in a dictionary like syntax using PyMongo.

		pip install pymongo[snappy,gssapi,srv,tls]

4. Also, install dnspython for using mongodb+srv://:

  		pip install dnspython
		
5. Install Djongo to connect MONGODB with Django:
		
		pip install djongo
		
and add this into setting.py in project folder DATABASES = 
	
	{
		'default': { 'ENGINE': 'djongo', 
		'NAME': 'your-db-name',
		'ENFORCE_SCHEMA': False, 
		'CLIENT': { 'host': 'mongodb+srv://:@/?retryWrites=true&w=majority' }
	} 
	}

In this 'ENFORCE_SCHEMA': False this line remove migration requirement in Django when we add new schema attribute. Then at last apply migration.

Also Locally install Monogodb in our system and create database and database collection and name of the database should be same as name present in setting.py DATABASES code.

6. To install all dependencies in project

		pip install requirements.txt

Once all things are set up, we can now start the server and check that your set up was successful. In the console, run the following command:

python manage.py runserver
Then, in your browser go to http://127.0.0.1:8000/admin
