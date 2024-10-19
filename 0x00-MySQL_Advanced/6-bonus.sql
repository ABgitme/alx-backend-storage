--script that creates a stored procedure AddBonus to add a new correction for a student,
--ensuring the project exists,
-- or creating it if it does not
DELIMITER $$;

CREATE PROCEDURE AddBonus(
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score INT
)
BEGIN
    -- Insert the project if it does not exist (ignores duplicates)
    INSERT IGNORE INTO projects (name) VALUES (project_name);

    -- Retrieve the project_id (whether newly inserted or already existing)
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (
        user_id, 
        (SELECT id FROM projects WHERE name = project_name LIMIT 1), 
        score
    );
END$$
DELIMITER ;
