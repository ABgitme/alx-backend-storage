-- First, let's assume the table structure is like this:
-- CREATE TABLE users (
--   id INT PRIMARY KEY,
--   email VARCHAR(255),
--   valid_email BOOLEAN
-- );

-- Create the trigger
CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
WHEN (OLD.email IS DISTINCT FROM NEW.email)
BEGIN
  SET NEW.valid_email = FALSE;
END;
