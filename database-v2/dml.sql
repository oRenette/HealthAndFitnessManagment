-- Inserting data into Exercises table
INSERT INTO Exercises (exercise_name) VALUES
('Cardio'),
('Weightlifting'),
('Yoga'),
('Pilates'),
('CrossFit');

-- Inserting data into Profile table
INSERT INTO Profile (first_name, last_name, email) VALUES
('John', 'Doe', 'john.doe@example.com'),
('Alice', 'Smith', 'alice.smith@example.com'),
('Bob', 'Johnson', 'bob.johnson@example.com');

-- Inserting data into Trainers table
INSERT INTO Trainers (first_name, last_name, email, day_schedule, start_time, end_time) VALUES
('Mike', 'Anderson', 'mike.anderson@example.com', '{Monday}', '{08:00:00}', '{12:00:00}'),
('Sarah', 'Clark', 'sarah.clark@example.com', '{Wednesday}', '{10:00:00}', '{14:00:00}'),
('David', 'Wilson', 'david.wilson@example.com', '{Friday}', '{15:00:00}', '{19:00:00}');

-- Inserting data into AdminStaff table
INSERT INTO AdminStaff (first_name, last_name, email) VALUES
('Emily', 'Brown', 'emily.brown@example.com'),
('Michael', 'Taylor', 'michael.taylor@example.com');

-- Inserting data into HealthStatistics table
INSERT INTO HealthStatistics (weight, age, male, height) VALUES
(70, 25, true, 175),
(65, 30, false, 160),
(80, 40, true, 180);

-- Inserting data into Members table
INSERT INTO Members (profile_id, health_id) Values 
(1, 1),
(2, 2),
(3, 3);

-- Inserting data into Billings table
INSERT INTO Billings (member_id, admin_id, amount) VALUES
(1, 1, 50),
(2, 2, 60),
(3, 1, 70);

-- Inserting data into Rooms table
INSERT INTO Rooms (room_number, capacity) VALUES
(101, 20),
(102, 15),
(103, 25);

-- Inserting data into Classes table
INSERT INTO Classes (class_name, trainer_id, room_id, is_group, day_schedule, start_time, end_time, price) VALUES
('Morning Yoga', 3, 1, true, 'Monday', '08:00:00', '09:00:00', 15),
('Evening Cardio', 1, 2, true, 'Wednesday', '18:00:00', '19:00:00', 20),
('Weightlifting Workshop', 2, 3, false, 'Friday', '16:00:00', '18:00:00', 25);

-- Inserting data into ClassMembers table
INSERT INTO ClassMembers (class_id, member_id) VALUES
(1, 1),
(2, 2),
(3, 3);

-- Inserting data into ClassExercises table
INSERT INTO ClassExercises (class_id, exercise_id) VALUES
(1, 3),
(2, 1),
(3, 2);

-- Inserting data into MemberClassBookings table
INSERT INTO MemberClassBookings (member_id, class_id, status) VALUES
(1, 1, 'Booked'),
(2, 2, 'Booked'),
(3, 3, 'Booked');

-- Inserting data into AdminClassBookings table
INSERT INTO AdminClassBookings (booking_id, admin_id) VALUES
(1, 1),
(2, 2),
(3, 1);

-- Inserting data into FitnessGoals table
INSERT INTO FitnessGoals (member_id, weight, time_deadline) VALUES
(1, 65, '2024-06-30'),
(2, 60, '2024-07-15'),
(3, 75, '2024-05-20');

-- Inserting data into Equipment table
INSERT INTO Equipment (equipment_id, equipment_name, equipment_condition) VALUES
(1, 'Dumbell', 'Good'),
(2, 'Yoga Mat', 'Good'),
(3, 'Peloton Bike', 'Used'),
(4, 'Treadmill', 'Broken');
