CREATE TABLE Repositories (
	Full_name Text NOT NULL primary key,
	Name Text,
	Tag Text,
	Star INT,
	Update_time Timestamp,
	Login_user Text,
	Tags_url Text,
	FOREIGN KEY (Login_user) REFERENCES Users(Login));
