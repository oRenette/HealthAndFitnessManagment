CREATE DATABASE HealthAndFitness;

CREATE TYPE week_day AS enum ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday');
CREATE TYPE Booking_Status AS ENUM ('Booked', 'Cancelled', 'Modified');

CREATE TABLE Exercises (
  exercise_id SERIAL PRIMARY KEY,
  exercise_name varchar(255)
);

CREATE TABLE Profile (
  profile_id SERIAL PRIMARY KEY,
  first_name varchar(255),
  last_name varchar(255),
  email varchar(255)
);

CREATE TABLE Trainers (
  trainer_id SERIAL PRIMARY KEY,
  first_name varchar(255),
  last_name varchar(255),
  email varchar(255),
  day_schedule week_day ARRAY[7],
  start_time time ARRAY[7],
  end_time time ARRAY[7]
);

CREATE TABLE AdminStaff (
  admin_id SERIAL PRIMARY KEY,
  first_name varchar(255),
  last_name varchar(255),
  email varchar(255)
);

CREATE TABLE HealthStatistics (
  health_id SERIAL PRIMARY KEY,
  weight int,
  age int,
  male boolean,
  height float
);

CREATE TABLE Members (
  member_id SERIAL PRIMARY KEY,
  profile_id int REFERENCES Profile(profile_id),
  health_id int REFERENCES HealthStatistics(health_id),
  day_schedule date ARRAY[7],
  start_time time[7],
  end_time time[7]
);

CREATE TABLE Billings (
  bill_id SERIAL PRIMARY KEY,
  member_id int REFERENCES Members(member_id),
  admin_id int REFERENCES AdminStaff(admin_id),
  amount double precision
);

CREATE TABLE Rooms (
  room_id SERIAL PRIMARY KEY,
  room_number int UNIQUE NOT NULL,
  capacity int
);

CREATE TABLE Classes (
  class_id SERIAL PRIMARY KEY,
  trainer_id int REFERENCES Trainers(trainer_id),
  room_id int REFERENCES Rooms(room_id),
  is_group boolean,
  day_schedule week_day,
  start_time time,
  end_time time,
  creation_time timestamp,
  price double precision
);

CREATE TABLE Class_Members (
  class_id int REFERENCES Classes(class_id),
  member_id int REFERENCES Members(member_id),
  PRIMARY KEY (class_id, member_id)
);

CREATE TABLE Class_Exercises (
  class_id int REFERENCES Classes(class_id),
  exercise_id int REFERENCES Exercises(exercise_id),
  PRIMARY KEY (class_id, exercise_id)
);

CREATE TABLE Member_Class_Bookings (
  booking_id SERIAL PRIMARY KEY,
  member_id INT REFERENCES Members(member_id),
  class_id INT REFERENCES Classes(class_id),
  booking_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  status Booking_Status DEFAULT 'Booked'
);

CREATE TABLE Admin_Class_Bookings (
  booking_id INT REFERENCES Member_Class_Bookings(booking_id) ON DELETE CASCADE,
  admin_id INT REFERENCES AdminStaff(admin_id),
  modified_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (booking_id, admin_id)
);


CREATE TABLE FitnessGoals (
  goal_id SERIAL PRIMARY KEY,
  member_id int REFERENCES Members(member_id),
  weight int,
  time_deadline date
);
