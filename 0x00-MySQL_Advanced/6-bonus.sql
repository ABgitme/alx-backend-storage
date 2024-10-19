--script that creates a stored procedure
--AddBonus to add a new correction for a student,
--ensuring the project exists,
-- or creating it if it does not
DELIMITER $$

CREATE PROCEDURE AddBonus(
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score INT
)
BEGIN
    DECLARE project_id INT;

    -- Check if the project already exists, if not, insert the project
    SELECT id INTO project_id
    FROM projects
    WHERE name = project_name
    LIMIT 1;

    IF project_id IS NULL THEN
        -- Insert new project and get the new project_id
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;

    -- Insert the correction for the student
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, project_id, score);
END$$

DELIMITER ;

