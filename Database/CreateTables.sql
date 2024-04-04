CREATE DATABASE SoccerEvents;

CREATE TABLE EventType (
	event_id INT PRIMARY KEY,
	event_name VARCHAR(255)
);

CREATE TABLE Tactics (
	tactic_id INT PRIMARY KEY,
	formation VARCHAR(255),
	lineup OBJECT
);

CREATE TABLE DataFrame (
	data_frame_id INT PRIMARY KEY,
	data_frame_name VARCHAR(255),
	nickname VARCHAR(255),
	dob DATE NOT NULL,
	country_id INT,
	country_name VARCHAR(255)
);

CREATE TABLE Team (
	team_id INT PRIMARY KEY,
	team_name VARCHAR(255),
	team_gender VARCHAR(255),
	team_group VARCHAR(255),
	country VARCHAR(255),
	manager_id INT ARRAY REFERENCES DataFrame(data_frame_id)
);

CREATE TABLE Positions (
	position_id INT PRIMARY KEY,
	position_name VARCHAR(255),
	from_time TIMESTAMP,
	to_time TIMESTAMP,
	from_period INT,
	to_period INT,
	start_reason VARCHAR(255),
	end_reason VARCHAR(255)
);

CREATE TABLE Players (
	player_id INT PRIMARY KEY,
	player_name VARCHAR(255)
	nickname VARCHAR(255),
	jersey_number INT,
	country VARCHAR(255),
	cards OBJECT ARRAY,
	player_position INT ARRAY REFERENCES Positions(position_id)
);

CREATE TABLE Lineups (
	team_id INT PRIMARY KEY REFERENCES Team(team_id),
	team_name VARCHAR(255),
	lineup Players ARRAY REFERENCES Players(player_id)
);

CREATE TABLE Events (
    event_id SERIAL PRIMARY KEY,
	event_index INT,
	event_period INT,
	event_timestamp TIMESTAMP,
	minutes INT,
	seconds INT,
	event_type INT REFERENCES EventType(event_id),
	possessions INT,
	possessions_team VARCHAR(255) REFERENCES Team(team_name),
	play_pattern OBJECT,
	team_id INT REFERENCES Team(team_id),
	duration double,
	tactic_id INT REFERENCES Tactics(tactic_id)
);

CREATE TABLE Stadium (
	stadium_id INT PRIMARY KEY,
	stadium_name VARCHAR(255),
	stadium_country VARCHAR(255)
);

CREATE TABLE Referee (
	ref_id INT,
	ref_name VARCHAR(255) PRIMARY KEY,
	ref_country VARCHAR(255)
);

CREATE TABLE Season (
	season_name VARCHAR(255),
	season_id INT PRIMARY KEY,
);

CREATE TABLE Competitions (
    comp_id INT PRIMARY KEY,
	season_id INT REFERENCES Season(season_id),
	comp_name VARCHAR(255),
	comp_gender VARCHAR(255),
	country VARCHAR(255),
	season_name VARCHAR(255),
	match_updated TIMESTAMP,
	match_avalible boolean,
	youth boolean,
	international boolean
);

CREATE TABLE Matches (
	match_id INT PRIMARY KEY,
	competition_id INT REFERENCES Competitions(comp_id),
	country_name VARCHAR(255),
	season INT REFERENCES Season(season_id),
	match_date DATE,
	kickoff TIMESTAMP,
	stadium_id INT REFERENCES Stadium(stadium_id),
	country_stadium VARCHAR(255),
	ref_name VARCHAR(255) REFERENCES Referee(ref_id),
	ref_country VARCHAR(255),
	home_team INT REFERENCES Team(team_id),
	away_team INT REFERENCES Team(team_id),
	home_score INT,
	away_score INT,
	match_status VARCHAR(255),
	match_week INT,
	competition_stage VARCHAR(255),
	last_updated DATE,
	data_version INT
);