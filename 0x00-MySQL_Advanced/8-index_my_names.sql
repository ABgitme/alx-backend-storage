-- Import the table dump
-- Make sure to unzip the 'names.sql.zip' and import it before running the following SQL script.

-- Create an index on the first letter of the 'name' column
CREATE INDEX idx_name_first
ON names (LEFT(name, 1));
