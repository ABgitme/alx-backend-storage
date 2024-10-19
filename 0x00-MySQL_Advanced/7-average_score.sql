--computes and stores the average score
--for a specific student based on the corrections table
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN p_user_id INT
)
BEGIN
    DECLARE avg_score DECIMAL(5, 2);

    -- Compute the average score for the specified user from the corrections table
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = p_user_id;

    -- Update the user's average_score in the users table
    UPDATE users
    SET average_score = IFNULL(avg_score, 0)
    WHERE id = p_user_id;
END$$

DELIMITER ;
