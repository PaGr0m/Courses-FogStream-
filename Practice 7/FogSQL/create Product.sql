CREATE TABLE Product(
	ID_Model Int NOT NULL DEFAULT nextval ('ID_Model') primary key,
	Maker Text NOT NULL,
	Type Text NOT NULL)