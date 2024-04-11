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
            The schedule of that trainer and their information
    """
    try: 
        tid = int(input("Enter your trainer id: "))
    except ValueError:
        print('Invalid trainer id: Not an integer')
        return 
    week_day = input("Enter the weekday of avalibility: ")
    start_time = input("Enter the start time (hh:mm): ")
    end_time = input("Enter the end time (hh:mm): ")
    #Parse input to determine validity
    day_list = ["Sunday", "Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday"]
    start_split = start_time.split(":")
    end_split = end_time.split(":")
    
    #Validating inputs
    if week_day not in day_list:
        print('Invalid week day: "{}" not a valid entry'.format(week_day))
        return
    try:
        if (len(start_split) != 2 and len(start_split) != 3) or (len(end_split) != 2 and len(end_split) != 3):
            print('Invalid time format: must be "hh:mm:ss" or "hh:mm"')
            return
        elif int(start_split[0]) < 0 or int(start_split[0]) > 24 or int(end_split[0]) < 0 or int(end_split[0]) > 24:
            print('Invalid hour: hours must be between 0-24 (inclusive)')
            return
        elif int(start_split[1]) < 0 or int(start_split[1]) > 60 or int(end_split[1]) < 0 or int(end_split[1]) > 60:
            print('Invalid minutes: minutes must be between 0-60 (inclusive)')
            return
    
        if len(start_split) == 3 and (int(start_split[2]) < 0 or int(start_split[2]) > 60):
            print('Invalid seconds: hours must be between 0-60 (inclusive)')
            return  
        if len(end_split) == 3 and (int(end_split[2]) < 0 or int(end_split[2]) > 60):
            print('Invalid seconds: hours must be between 0-60 (inclusive)')
            return   
    
        if (int(start_split[0]) == 24 and (int(start_split[1]) > 0 or int(start_split[2]) > 0)) or (int(end_split[0]) == 24 and (int(end_split[1]) > 0 or int(end_split[2]) > 0)):
            print('Invalid time: Time cannot be past 24 hours')
            return   
    except ValueError:
        print('Invalid time input: Not an integer in (hh:mm)')
        return    
    if start_time > end_time:
        print('Invalid inputs: start time must be before end time')
        return
    
    #Collect current schedule info
    cursor.execute("SELECT day_schedule FROM Trainers WHERE trainer_id = {};".format(tid))
    new_table = cursor.fetchall()
    #Weird formatting with the way the arrays are interpreted
    trainer_current_day_lst = new_table[0][0][1:len(new_table[0][0])-1].split(",")
    #If day of week needs to be added
    if (week_day not in trainer_current_day_lst) and (len(trainer_current_day_lst) < 7):
        cursor.execute("UPDATE Trainers SET day_schedule[{}] = '{}', start_time[{}] = '{}', end_time[{}] = '{}' WHERE trainer_id = {};".format(str(len(trainer_current_day_lst)+1),week_day,str(len(trainer_current_day_lst)+1),start_time,str(len(trainer_current_day_lst)+1),end_time,str(tid)))
        connection.commit()
        print("UPDATE SUCCESS! Trainer schedule for {} has been added.".format(week_day))     
    else:
        #Otherwise, it needs to be updated
        i = 1
        for day_of_week in trainer_current_day_lst:
            if week_day == day_of_week and i <= 7:
                cursor.execute("UPDATE Trainers SET day_schedule[{}] = '{}', start_time[{}] = '{}', end_time[{}] = '{}' WHERE trainer_id = {};".format(str(i),week_day,str(i),start_time,str(i),end_time,str(tid)))
                connection.commit()
                print("UPDATE SUCCESS! Trainer schedule for {} has been updated.".format(week_day))
                break
            i += 1
    
    #Return updated/modified schedule
    cursor.execute("SELECT * FROM Trainers WHERE trainer_id = {}".format(str(tid)))
    return cursor.fetchall()

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
    cursor.execute("SELECT * FROM Profile WHERE first_name = '{}';".format(first_name))
    new_table = cursor.fetchall()
    print("SEARCH SUCCESS! Displaying information about member {}:".format(first_name))
    for row in new_table:
        print(row)
    return new_table     
    

# Administrative Staff Functions:

#     1. Room Booking Management
def bookingManagement():
    """
        Allows admin users delete or add bookings
            Inputs:
            admin_id of the admin logged in
            booking_id of the booking being deleted\added
            member_id of member booking room
            class_id of class taking place in booked room
        """
    admin_id = input("Please enter your admin id:")
    try:
        choice = int(input("1: cancel a booking\n2: add a booking"))
    except ValueError:
        print("Not a valid option. Must type value associated with option.")
        return False

    if choice == 1:
        try:
            booking_id = int(input("What is the booking_id you want to delete?"))
        except ValueError:
            print("Booking id must be an integer value")
            return False

        # Check if admin is authorized to delete the booking
        cursor.execute("SELECT admin_id FROM AdminClassBookings WHERE booking_id = %s", (booking_id))
        result = cursor.fetchone()
        if result and result[0] == admin_id:
            # Delete the booking
            cursor.execute("DELETE FROM MemberClassBookings WHERE booking_id = %s", (booking_id))
            print("Booking deleted successfully.")
        else:
            print("Admin is not authorized to delete this booking.")
        return True
    elif choice == 2:
        cursor.execute("SELECT * FROM AdminStaff WHERE admin_id = %s", (admin_id))
        admin_exists = cursor.fetchone()
        if admin_exists:
            print("To add a room booking please provide the following information:")
            member_id = input("The id of member booking the class:")
            class_id = input("Enter the class id of the class being booked in the room:")
            status = 'Booked'
            # Add the room booking
            cursor.execute(
                "INSERT INTO MemberClassBookings (member_id, class_id, status) VALUES (%s, %s, %s)",
                (member_id, class_id, status))
            print("Room booking added successfully!")
        else:
            print("Admin does not exist.")
        return True
    else:
        print("Not an option")
        return False


#     2. Equipment Maintenance Monitoring
def equipmentMaintenance():
    """
    Allows admin users to review the status of equipment and repair if necessary
        Inputs:
        equipment_id of equipment added/replaced/removed
        equipment_name of equipment added
        eqipment_condition of equipment added
    """
    try:
        choice = int(input("1: View all equipment condition\n2: Replaced equipment\n3: Add new equipment\n4: Remove equipment"))
    except ValueError:
        print("Not a valid option. Must type value associated with option.")
        return False
    if choice == 1:
        # Print out condition of all equipment
        cursor.execute("SELECT equipment_name, equipment_condition FROM Equipment")
        result = cursor.fetchall()
        print(result)
        return True
    elif choice == 2:
        equipment_id = input("Please enter the id of the equipment you have replaced:")
        cursor.execute("UPDATE Equipment SET equipment_condition = 'Good' WHERE equipment_id = %s", (equipment_id,))
        print("The selected equipment has been repaired")
        return True
    elif choice == 3:
        equipment_name = input("Please enter the name of the equipment added:")
        equipment_condition = input("Please enter the condition of the equipment added:")
        cursor.execute("INSERT INTO Equipment (equipment_name, equipment_condition) "
                       "VALUES (%s, %s)", (equipment_name, equipment_condition))
        print("The equipment has been added to the database")
        return True
    elif choice == 4:
        equipment_id = input("Please enter the id of the equipment you want to delete:")
        cursor.execute("DELETE FROM Equipment WHERE equipment_id = %s", (equipment_id))
        print("The equipment has been deleted from the database")
        return True
    else:
        print("Not an option")
        return False

#     3. Class Schedule Updating
def classScheduleUpdating():
    """
    Allows admin users to update the scheduling of classes
        Inputs:
        class_id of class changed
        week_day of changed class
        start_time of changed class
        end_time of changed class
    """
    try:
        choice = int(input("1: View all class times\n2: Change a class time"))
    except ValueError:
        print("Not a valid option. Must type value associated with option.")
        return False

    if choice == 1:
        cursor.execute("SELECT class_id, class_name, day_schedule, start_time, end_time FROM Classes")
        return True
    elif choice == 2:
        class_id = input("Please enter the class id of the class you want to reschedule:")
        week_day = input("Enter the new weekday of the class: ")
        start_time = input("Enter the new start time (hh:mm): ")
        end_time = input("Enter the new end time (hh:mm): ")
        cursor.execute("UPDATE Classes SET day_schedule = %s, start_time = %s, end_time = %s "
                       "WHERE class_id = %s", week_day, start_time, end_time, class_id)
        return True
    else:
        print("Not an option")
        return False

#     4. Billing and Payment Processing
def billingAndPayment():
    """
    Allows admin users to email bills, add bills, and process payments of members
        Inputs:
        member_id of member being emailed, billed, or processed
        admin_id of admin adding bill
        amount_payed of bill by a member
    """
    try:
        choice = int(input("1: Email bills to a member\n2: Add to member's bill\n3: Process members payment"))
    except ValueError:
        print("Not a valid option. Must type value associated with option.")
        return False

    if choice == 1:
        try:
            member_id = int(input("Enter the member id:"))
        except ValueError:
            print("Member id must be an integer value")
            return False
        amount = cursor.execute("SELECT amount FROM billings WHERE member_id = %s", member_id)
        cursor.execute("SELECT profile.email, billings.amount FROM profile "
                       "JOIN members ON profile.profile_id = members.profile_id "
                       "JOIN billings ON members.member_id = billings.member_id "
                       "WHERE members.member_id = %s", member_id)
        print("An email has been sent to the member with %s id for an billing amount of $%s", member_id, amount)
        return True
    elif choice == 2:
        try:
            admin_id = int(input("Enter your admin id:"))
            member_id = int(input("Enter the id of the member:"))
        except ValueError:
            print("Member/Admin id must be an integer value")
            return False
        try:
            user_input = input("Enter the billing amount:")
            amount = float(user_input)
        except ValueError:
            print("Amount must be a double value")
            return False
        cursor.execute("INSERT INTO billings (member_id, admin_id, amount) VALUES (%s, %s, %s)", member_id, admin_id, amount)
        return True
    elif choice == 3:
        try:
            member_id = int(input("Enter the id of the member:"))
        except ValueError:
            print("Member id must be an integer value")
            return False
        try:
            user_input = input("Enter the amount payed by member:")
            amount_payed = float(user_input)
        except ValueError:
            print("Amount must be a double value")
            return False

        prev_amount = cursor.execute("SELECT amount FROM billings WHERE member_id = %s", member_id)
        amount = prev_amount - amount_payed
        cursor.execute("UPDATE billings SET amount = %s WHERE member_id = %s", amount, member_id)
        return True
    else:
        print("Not an option")
        return False

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
                            bookingManagement()
                        case 2:
                            equipmentMaintenance()
                        case 3:
                            classScheduleUpdating()
                        case 4:
                            billingAndPayment()
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
    return conn

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
    connection = setup(name, password)
    cursor = connection.cursor()
    print("Connection success!")
    '''

    UI()
