-- creates the table unique_id on your MySQL server
CREATE TABLE `unique_id` IF NOT EXISTS (
	id INT DEFAULT 1,
	name VARCHAR(256),
	UNIQUE (id)
);
