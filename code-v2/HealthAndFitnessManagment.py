import socket
import sys
sys.path.append('./externalLib')
import psycopg2

#Author Group 113
#Version April 10, 2024

#Credit to (https://psycopg.org/) for postgres connection service

def setup(db_user: str, db_pass:str):
    """
    Initializes the connection to the database.
        Parameters:
            db_user (str): The username to the postgres server
            db_pass (str):The password to the postgres server
        Returns:
            cursor: an object connected to the database
    """    
    db_name = "HealthAndFitness"
    db_host = "localhost"
    db_port = 5432
    conn = psycopg2.connect(database= db_name,
                           host = db_host,
                           user = db_user,
                           password = db_pass,
                           port = db_port)
    #Return the item to control database actions
    return conn.cursor()



#print program info and commands
print("#########################################################################")
print("Welcome to the Python database manipulator!")
print("CREDIT TO ONLINE PACKAGE 'psycopg2' (https://psycopg.org/) WHICH ALLOWS THE DATABASE CONNECTION")
print("!!!THIS PROGRAM ASSUMES THAT THE PORT, HOSTNAME, AND DATABASE_NAME WERE NOT ALTERED!!!\n\t If they were altered, please adjust the setup() function before use...")
print("Enter the DB server's name and passowrd to connect:")

#Prompt for name and pasword of the postgres server that should be connected
name = input("\tEnter the DB server username: ")
password = input("\tEnter the DB server password: ")
cursor = setup(name, password)
print("Connection success! Call the functions above to manipulate the database...\n")