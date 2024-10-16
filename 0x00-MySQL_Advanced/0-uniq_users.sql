-- 'SERIAL' makes the id auto-incremented and sets it as the primary key
-- 'UNIQUE' ensures that the email is unique in the table
-- No NOT NULL constraint on name, it can be NULL
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
