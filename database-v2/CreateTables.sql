CREATE DATABASE HealthAndFitness;

CREATE TYPE week_day AS enum ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday');
CREATE TYPE Booking_Status AS ENUM ('Booked', 'Cancelled', 'Modified');

CREATE TABLE Exercises (
  exercise_id SERIAL PRIMARY KEY,
  exercise_name varchar(255) UNIQUE NOT NULL
);

CREATE TABLE Profile (
  profile_id SERIAL PRIMARY KEY,
  first_name varchar(255) NOT NULL,
  last_name varchar(255) NOT NULL,
  email varchar(255) UNIQUE NOT NULL
);

CREATE TABLE Trainers (
  trainer_id SERIAL PRIMARY KEY,
  first_name varchar(255) NOT NULL,
  last_name varchar(255) NOT NULL,
  email varchar(255) UNIQUE NOT NULL,
);

CREATE TABLE AdminStaff (
  admin_id SERIAL PRIMARY KEY,
  first_name varchar(255) NOT NULL,
  last_name varchar(255) NOT NULL,
  email varchar(255) UNIQUE NOT NULL
);

CREATE TABLE HealthStatistics (
  health_id SERIAL PRIMARY KEY,
  weight int NOT NULL,
  age int NOT NULL,
  male boolean NOT NULL,
  height float NOT NULL
);

CREATE TABLE Members (
  member_id SERIAL PRIMARY KEY,
  profile_id int REFERENCES Profile(profile_id),
  health_id int REFERENCES HealthStatistics(health_id),
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
  class_name varchar(255) NOT NULL,
  trainer_id int REFERENCES Trainers(trainer_id),
  room_id int REFERENCES Rooms(room_id),
  is_group boolean NOT NULL,
  day_schedule week_day NOT NULL,
  start_time time NOT NULL,
  end_time time NOT NULL,
  creation_time timestamp DEFAULT CURRENT_TIMESTAMP,
  price double precision NOT NULL
);

CREATE TABLE ClassMembers (
  class_id int REFERENCES Classes(class_id),
  member_id int REFERENCES Members(member_id),
  PRIMARY KEY (class_id, member_id)
);

CREATE TABLE ClassExercises (
  class_id int REFERENCES Classes(class_id),
  exercise_id int REFERENCES Exercises(exercise_id),
  PRIMARY KEY (class_id, exercise_id)
);

CREATE TABLE MemberClassBookings (
  booking_id SERIAL PRIMARY KEY,
  member_id INT REFERENCES Members(member_id),
  class_id INT REFERENCES Classes(class_id),
  booking_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  status Booking_Status DEFAULT 'Booked'
);

CREATE TABLE AdminClassBookings (
  booking_id INT REFERENCES Member_Class_Bookings(booking_id) ON DELETE CASCADE,
  admin_id INT REFERENCES AdminStaff(admin_id),
  modified_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (booking_id, admin_id)
);


CREATE TABLE FitnessGoals (
  goal_id SERIAL PRIMARY KEY,
  member_id int REFERENCES Members(member_id),
  weight int NOT NULL,
  time_deadline date NOT NULL
);
