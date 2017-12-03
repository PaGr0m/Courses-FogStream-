CREATE TABLE Printer (
	ID_Code_Printer Int NOT NULL DEFAULT nextval ('ID_Code_Printer') primary key,
	Model_id Int NOT NULL,
	Color Char(1) NOT NULL,
	Type Text NOT NULL,
	Price Money NOT NULL,
	FOREIGN KEY (Model_id) REFERENCES Product(ID_Model));
	