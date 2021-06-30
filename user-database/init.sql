CREATE TABLE system_users (
	user_id SERIAL PRIMARY KEY,
	forename varchar(30) NOT NULL,
	surname varchar(30) NOT NULL,
	email varchar(50) NOT NULL,
	phone_number varchar(15) NOT NULL
);