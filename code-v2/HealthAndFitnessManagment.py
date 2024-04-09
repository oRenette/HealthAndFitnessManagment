import socket
import sys
sys.path.append('./externalLib')
import psycopg2

#Author Group 113
#Version April 10, 2024

#Credit to (https://psycopg.org/) for postgres connection service

# Member Functions:
#     1. User Registration
#     2. Profile Management (Updating personal information, fitness goals, health metrics)
#     3. Dashboard Display (Displaying exercise routines, fitness achievements, health statistics)
#     4. Schedule Management (Scheduling personal training sessions or group fitness classes. The system


# Trainer Functions:
#     1. Schedule Management (Trainer can set the time for which they are available.)
def setSchedule():
    """
    Updates the desired Trainer based off id and prints out a confirmation message
        Inputs (Not parameters):
            tid (int): The Trainers id in which to update
            week_day (str): The day of week for the schedule update
            start_time (str): The start time of avalibility (XX:XX:XX)
            end_time (str): The end time of avalibility (XX:XX:XX)
        Return:
            True if the update is a success, False otherwise
    """
    try: 
        tid = int(input("Enter your trainer id: "))
    except ValueError:
        print('Invalid trainer id: Not an integer')
        return False    
    week_day = input("Enter the weekday of avalibility: ")
    start_time = input("Enter the start time (hh:mm): ")
    end_time = input("Enter the end time (hh:mm): ")
    #Parse input to determine validity
    day_list = ["Sunday", "Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday"]
    start_split = start_time.split(":")
    end_split = end_time.split(":")
    if week_day not in day_list:
        print('Invalid week day: "{}" not a valid entry'.format(week_day))
        return False
    
    try:
        if (len(start_split) != 2 and len(start_split) != 3) or (len(end_split) != 2 and len(end_split) != 3):
            print('Invalid time format: must be "hh:mm:ss" or "hh:mm"')
            return False
        elif int(start_split[0]) < 0 or int(start_split[0] > 24) or int(end_split[0]) < 0 or int(end_split[0] > 24):
            print('Invalid hour: hours must be between 0-24 (inclusive)')
            return False
        elif int(start_split[1]) < 0 or int(start_split[1] > 60) or int(end_split[1]) < 0 or int(end_split[1] > 60):
            print('Invalid minutes: minutes must be between 0-60 (inclusive)')
            return False
    
        if len(start_split) == 3 and (int(start_split[2]) < 0 or int(start_split[2] > 60)):
            print('Invalid seconds: hours must be between 0-60 (inclusive)')
            return False   
        if len(end_split) == 3 and (int(end_split[2]) < 0 or int(end_split[2]) > 60):
            print('Invalid seconds: hours must be between 0-60 (inclusive)')
            return False    
    
        if (int(start_split[0]) == 24 and (int(start_split[1] > 0) or int(start_split[2] > 0))) or (int(end_split[0]) == 24 and (int(end_split[1] > 0) or int(end_split[2] > 0))):
            print('Invalid time: Time cannot be past 24 hours')
            return False    
    except ValueError:
        print('Invalid time input: Not an integer in (hh:mm)')
        return False      
    
    if start_time > end_time:
        print('Invalid inputs: start time must be before end time')
        return False
    
    #Find the index to insert the date at
    for i in range(7):
        if day_list[i] == week_day:
            break
        
    cursor.execute("UPDATE Trainers\nSET day_schedule[{}] = '{}', start_time[{}] = '{}', end_time[{}] = '{}' \nWHERE trainer_id = {};".format(i,week_day,i,start_time,i,end_time,tid))
    print("UPDATE SUCCESS! Trainer schedule has been updated.")
    
    return True

#     2. Member Profile Viewing (Search by Member’s name)
def viewProfile():
    """
    Retreives the profile informatition and prints it before returning it
        Inputs (Not parameters):
            first_name (str): The member's first name
        Return:
            A list containing the The profile information tuples
    """
    first_name = input("Search member profile by first name: ")
    cursor.execute("SELECT * \nFROM Profile \nWHERE first_name = '{}';".format(first_name))
    new_table = cursor.fetchall()
    for row in new_table:
        print(row)
    return new_table    
    

# Administrative Staff Functions:
#     1. Room Booking Management
#     2. Equipment Maintenance Monitoring
#     3. Class Schedule Updating
#     4. Billing and Payment Processing (Your system should assume integration with a payment service
#          [Note: Do not actually integrate with a payment service])

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
