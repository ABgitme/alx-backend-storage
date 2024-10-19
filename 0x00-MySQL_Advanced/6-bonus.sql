--script that creates a stored procedure
--AddBonus to add a new correction for a student,
--ensuring the project exists,
-- or creating it if it does not
DELIMITER $$

CREATE PROCEDURE AddBonus(
    IN p_user_id INT,
    IN p_project_name VARCHAR(255),
    IN p_score DECIMAL(5, 2)
)
BEGIN
    DECLARE v_project_id INT;

    -- Check if the project already exists
    SELECT id INTO v_project_id
    FROM projects
    WHERE name = p_project_name
    LIMIT 1;

    -- If the project does not exist, insert it and get the new ID
    IF v_project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (p_project_name);
        SET v_project_id = LAST_INSERT_ID();
    END IF;

    -- Insert the correction for the student
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (p_user_id, v_project_id, p_score);
END$$
DELIMITER ;
