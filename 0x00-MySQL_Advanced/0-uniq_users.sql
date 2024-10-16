
CREATE TABLE IF NOT EXISTS users (
    -- 'SERIAL' makes the id auto-incremented and sets it as the primary key
    id SERIAL PRIMARY KEY,
    -- 'UNIQUE' ensures that the email is unique in the table
    email VARCHAR(255) NOT NULL UNIQUE,
    -- No NOT NULL constraint on name, it can be NULL
    name VARCHAR(255)
);
