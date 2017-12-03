CREATE TABLE PC (
	ID_Code_PC Int NOT NULL DEFAULT nextval ('ID_Code_PC') primary key,
	Model_id Int NOT NULL,
	Speed Float NOT NULL,
	Ram Float NOT NULL,
	Hd Float NOT NULL,
	Cd Char(4) NOT NULL,
	Price Money NOT NULL,
	FOREIGN KEY (Model_id) REFERENCES Product(ID_Model));
	