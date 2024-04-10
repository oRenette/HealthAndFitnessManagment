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
def member_registration():
    """
    The registration for the user
    
    Requests the first and last name aswell as the email
    Requests their health stats
    
    Creates new tuples for the Profile and Health tables and adds the new tuple ID's to the member's profile. 
    """
    
    print("\nPlease input the following data for registration:\n")
    first_name = input("\tFirst Name:")
    last_name = input("\tLast Name:")
    email = input("\tEmail:")
    
    weight = input("\tWeight:")
    age = input("\tAge:")
    gender = input("\tGender (Male/Female/Other):")
    height = input("\tHeight:")
    
    if gender.lower() == "male":
        gender = true
    else:
        gender = false
    
    cursor.execute("insert into Profile (first_name, last_name, email) values (%s, %s, %s)", (first_name, last_name, email))
    cursor.execute("select profile_id from Profile where email = %s", (email))
    prof_id = cursor.fetchall()
    
    cursor.execute("insert into HealthStatistics (weight, age, male, height) values (%s,%s,%s,%s)", (weight, age, gender, height))
    cursor.execute("select health_id from HealthStatistics where weight = %s, age = %s, male = %s, height = %s", (weight, age, gender, height))
    health_id = cursor.fetchall()    
    
    cursor.execute("insert into Members (profile_id, health_id) values (%s, %s)", (prof_id, health_id))
        
def profile_management():
    """
    Updates the profile of the member with the new stats they give
    
    Input (No Parameter):
        profile (int): choice between updating profile or health stats
    Return:
        True if the update is successful, False otherwise
    
    """
    print("\nWhat would you like to edit? (Please input the number)")
    try:
        profile = int(input("1.Fitness Goals\n2.HealthStatistics"))
    except ValueError:
        print("Not a valid option. Must be a number value")
        return False
    
    if profile == 1:
        print("Please enter your new fitness goals.")
        weight = input("Target weight:")
        target = input("Target Deadline in form Month/Day/Year:")
        cursor.execute("update FitnessGoals set weight = %s, schedule = %s where (member_id = %s)", (weight, target, mid))
    else:
        print("\nInput new health statistics.")
        weight = input("\tWeight:")
        age = input("\tAge:")
        gender = input("\tGender (Male/Female/Other):")
        height = input("\tHeight:")
        cursor.execute("update HealthStatistics set (weight = %s, age = %s, male = %s, height = %s) where (member_id = %s)", (weight, age, gender, height, mid))
    return True
            
def dahsboard():
    """
    Displays the profile, health and classes of the member that logged in
    """
    cursor.execute("select profile_id, health_id from Members where member_id = %s", (mid))
    rows = cursor.fetchall()
    for row in rows:
        cursor.execute("select weight, time_deadline from Profile where profile_id = %s", (row[0]))
        prof = cursor.fetchall()
        for p in prof:
            print(f"Weight: {p[0]}/tDeadline: {p[1]}\n")
        cursor.execute("select (weight, age, male, height) from HealthStatistics where health_id = %s", (row[1]))
        health = cursor.fetchall()
        for h in health:
            print(f"Weight: {h[0]}/tAge: {h[1]}/tMale?: {h[2]}/tHeight: {h[3]}/n")
            
    cursor.execute("select class_id from MemberClassBookings where member_id = %s", (mid))
    classes = cursor.fetchall()
    
    print("Class Schedule")
    for c in classes:
        clas = cursor.execute("select class_id, class_name, day_schedule, start_time, end_time from Classes where class_id = %s", c)
        print(f"{clas[0]}. {clas[1]} -- Day: {clas[2]} Time: {clas[3]} -> {clas[4]}")

def schedule_management():
    """
    Updates the class schedule of the member based of off their ID
    Inputs (No Parameters):
        choice (int): The choice of adding a class or cancelling a class
    Return:
        True if the update is successful, False otherwise
    """
    try:
        choice = int(input("1.Add Classes to schedule\n2.Remove Classes from schedule"))
    except ValueError:
        print("Not a valid option. Must type value associated with option.")
        return False
        
    if choice == 1:
        cursor.execute("select class_id, class_name, day_schedule, start_time, end_time from Classes")
        classes = cursor.fetchall()
        print("Choose a booking to ADD from the following classes: ")
        for c in classes:
            print(f"\n{c[0]}. {c[1]}")
        clas = input("Please select the class number.")
        
        cursor.exectue("insert into MemberClassBookings values (%s, %s)", (mid, clas))
        print("Class has been added!")
        return true
    elif choice == 2:
        cursor.execute("select class_id, class_name, day_schedule, start_time, end_time from Classes where member_id = %s", (mid)) 
        classes = cursor.fetchall()
        print("Choose a booking to REMOVE from the following classes: ")
        for c in classes:
            print(f"\n{c[0]}. {c[1]}")
        clas = input("Please select the class number.") 
        
        cursor.execute("update MemberClassBookings set status = 'cancelled' where (member_id = %s and class_id = %s)", (mid, clas))
        print("Class has been cancelled!")
        return true
    else:
        print("Not an option")
        return False
        

def member_login():
    """
    member login based off of their email
    Assumption: User is registered
    
    Returns True if login successful and False otherwise
    """
    
    email = input("Please enter your email to login.")
    
    cursor.execute("select profile_id from Profile where email = %s", (email))
    prof_id = cursor.fetchall()
    if prof_id is empty:
        print("Email doesn't exist")
        return False
    
    cursor.execute("select from Members where profile_id = %s", (prof_id[0]))
    login_id = cursor.fetchall()
    mid = login_id[0]
    return True

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



#Non User-Functionality Methods
def UI():
    """
    Provides a Command Line Based UI for the user to interact with the DB
    """
    
    func = -1
    member_logged_in = False
    
    while func != 0:
        if func not in [1,2,3]:
            print("\n\nPlease select a user functionality category. Type 0 to quit.")
        
            try:
                func = int(input(" 1. Member\n 2. Trainer\n 3. Admin\n"))
            except ValueError:
                print("Invalid input. Try again.")
        else:
            match func:
                case 1:
                    print("\nMember Fucntions")
                    print("Please select a functionality.")                    
                    if member_logged_in == False:
                        try:
                            user_func = int(input(" 1. User Registration\n 2. User Login\n 3.Return\n"))
                        except ValueError:
                            print("Invalid Input. Try again.")
                            
                        match user_func:
                            case 1:
                                member_registration()
                            case 2:
                                member_login()
                            case 3:
                                func = 4
                            case _:
                                print("Invalid")
                    else:
                        try:
                            user_func = int(input(" 1. Edit Profile\n 2. Edit Schedule\n 3. View Dashboard\n 4.User Logout\n"))
                        except ValueError:
                            print("Invalid Input. Try again.")          
                        
                        match user_func:
                            case 1:
                                profile_management()
                            case 2:
                                schedule_management()
                            case 3:
                                dashboard()
                            case 4:
                                member_logged_in = False
                            case _:
                                print("Invalid")
                case 2:
                    print("\nTrainer Functions\n")
                    print("Please select a functionality")
                    
                    try:
                        user_func = int(input(" 1. Schedule Management\n 2. View Member Profiles\n 3.Return\n"))
                    except ValueError:
                        print("Invalid Input. Try again.")       
                        
                    match user_func:
                        case 1:
                            setSchedule()
                        case 2:
                            viewProfile()
                        case 3:
                            func = 4
                        case _:
                            print("Invalid")
                case 3:
                    print("\nAdmin Functions\n")
                    print("please select a functionality")
                    
                    try:
                        user_func = int(input(" 1. Room Booking Management\n 2. Equipment Monitoring\n 3. Update Class Scheduling\n 4. Billing and Payment\n 5. Return"))
                    except ValueError:
                        print("Invalid Input. Try again.")   
                    
                    match user_func:
                        case 1:
                            #call Room Booking Management
                            print(user_func)
                        case 2:
                            #Call Equipment Monitoring
                            print(user_func)
                        case 3:
                            #Call Update Class
                            print(user_func)
                        case 4:
                            #Call billing
                            print(user_func)
                        case 5:
                            func = 4
                        case _:
                            print("Invalid")
        
    print("QUITING....")    
    
    

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

if __name__ == '__main__':
    #print program info and commands
    print("#########################################################################")
    print("Welcome to the Python database manipulator!")
    print("CREDIT TO ONLINE PACKAGE 'psycopg2' (https://psycopg.org/) WHICH ALLOWS THE DATABASE CONNECTION")
    print("!!!THIS PROGRAM ASSUMES THAT THE PORT, HOSTNAME, AND DATABASE_NAME WERE NOT ALTERED!!!\n\t If they were altered, please adjust the setup() function before use...")
    print("Enter the DB server's name and passowrd to connect:")

    #Prompt for name and pasword of the postgres server that should be connected
    '''
    name = input("\tEnter the DB server username: ")
    password = input("\tEnter the DB server password: ")
    cursor = setup(name, password)
    print("Connection success! Call the functions above to manipulate the database...\n")
    '''

    UI()
