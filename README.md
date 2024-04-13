# HealthAndFitnessManagment
Provides functions to manage a Health and Fitness Managment Database.
## Setup
* Video Tutorial: https://www.youtube.com/watch?v=CiJusgWjKjA
* Launch pgadmin4
* Locate the 'database-v2' folder
  * Open the 'CreateTable.sql' file and execute it
    * If creating through pgadmin4, name the DB 'HealthAndFitness' and remove the 'CREATE DATABASE HealthAndFitness' querey from the file before executing
  * Open the 'dml.sql' file and execute it
    * This will create and inject the 'HealthAndFitness' database to its init state
* Locate the 'code-v2' folder
  * Open the 'databaseManipulator.py' in your prefered IDE and run the script
    * Interact with the IDE shell to use application
      * Instructions shown in the application
  * Alternatively, run the program using the command line instead of an IDE
  * Follow the in-application instructions to use the program
* Please note that the program assumes default values for the DB port, name, and hostname
  * These values must be altered in the setup() function if they have been changed by the user
## Additional Information
* The 'Diagrams' folder contains the ER Model and Relational Diagram for the database
## Credit
* psycopg2 online library - connection the the postgres database server
* Located in .\code-v2\externalLib
* https://psycopg.org/
## Authors
* Owen Renette
* Nolan Kisser
* Sebi Magyar-Samoila

