SELECT model_id, speed, hd FROM PC
	WHERE (PC.Cd = '12x' OR PC.Cd = '24x') AND (PC.Price < money(600));