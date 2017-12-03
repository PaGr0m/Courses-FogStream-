CREATE TABLE Laptop (
	ID_Code_Laptop Int NOT NULL DEFAULT nextval ('ID_Code_Laptop') primary key,
	Model_id Int NOT NULL,
	Speed Float NOT NULL,
	Ram Float NOT NULL,
	Hd Float NOT NULL,
	Screen Float NOT NULL,
	Price Money NOT NULL,
	FOREIGN KEY (Model_id) REFERENCES Product(ID_Model));
	