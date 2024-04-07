CREATE DATABASE HealthAndFitness;

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
  schedule date ARRAY,
  view_member_profile int ARRAY
);

CREATE TABLE AdminStaff (
  admin_id SERIAL PRIMARY KEY,
  first_name varchar(255),
  last_name varchar(255)
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
  schedule date ARRAY
);

CREATE TABLE Billings (
  bill_id SERIAL PRIMARY KEY,
  member_id int REFERENCES Members(member_id),
  admin_id int REFERENCES AdminStaff(admin_id),
  amount double
);

CREATE TABLE Rooms (
  room_id SERIAL PRIMARY KEY,
  room_number int UNIQUE NOT NULL,
  capacity int
);

CREATE TABLE Bookings (
  booking_id int PRIMARY KEY,
  admin_id int REFERENCES AdminStaff(admin_id),
  room_ids int ARRAY REFERENCES Rooms(room_id),
  member_ids int ARRAY REFERENCES Members(member_id),
  trainer_ids int ARRAY REFERENCES Trainers(trainer_id)
);

CREATE TABLE FitnessGoals (
  goal_id int PRIMARY KEY,
  member_id int REFERENCES Members(member_id),
  weight int,
  time_deadline date
);

CREATE TABLE Exercises (
  exercise_id int PRIMARY KEY,
  exercise_name varchar(255)
);

CREATE TABLE "Class" (
  class_id int PRIMARY KEY,
  trainer_id int REFERENCES Trainers(trainer_id),
  room_id int REFERENCES Rooms(room_id),
  is_group boolean,
  member_ids int ARRAY REFERENCES Members(member_id),
  exercise_ids int ARRAY REFERENCES Exercises(exercise_id),
  start_time date,
  end_time date,
  creation_time timestamp,
  price double
);
