from flask import Flask # 
import requests, os
import psycopg2


app = Flask(__name__) 

@app.route("/")
def weather():
    params = {'q': os.environ['MYAPP_CITY'], 'appid': os.environ['MYAPP_API_KEY'], 'units': 'metric'}
    receive = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
    temp = receive.json()['main']['temp']
    desc = receive.json()['weather'][0]['description']
    name = os.environ['MYAPP_NAME']
    

    #Establishing the connection
    conn = psycopg2.connect(
    database="alexdb", user='alex', password='postgres', host='127.0.0.1', port= '5432'
    )
    #Setting auto commit false
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()


    #Execute a command: this creates a new table Preparing SQL queries to INSERT a record into the database.
    cursor.execute("CREATE TABLE IF NOT EXISTS desc_table (id serial PRIMARY KEY, data varchar);")
    # IF NOT EXIST
    # Pass data to fill a query placeholders and let Psycopg perform
    # the correct conversion (no more SQL injections!)
    var = f"INSERT INTO desc_table (data) VALUES ( '{ receive.json()['weather'][0]['description'] }' )"
    cursor.execute(var)

    # Query the database and obtain data as Python objects
    cursor.execute("SELECT * FROM desc_table;")
    cursor.fetchone()

    # Make the changes to the database persistent  #Commit your changes in the database
    conn.commit()

    # Close communication with the database # Closing the connection
    cursor.close()
    conn.close()
    return f"Hi {name}, today in {os.environ['MYAPP_CITY']} is {temp}°C {desc}."

