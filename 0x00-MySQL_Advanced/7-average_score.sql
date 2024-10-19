--computes and stores the average score
--for a specific student based on the corrections table
DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    DECLARE avg_score DECIMAL(5,2);

    -- Calculate the average score for the user, set to 0 if no scores are found
    SELECT IFNULL(AVG(score), 0) INTO avg_score
    FROM corrections
    WHERE corrections.user_id = user_id;

    -- Update the user's average_score
    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
END $$

DELIMITER ;
