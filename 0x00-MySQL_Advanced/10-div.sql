--function SafeDiv that divides
--two integers and returns 0 if the second integer is 0
DELIMITER $$

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    -- Check if the second argument is 0
    IF b = 0 THEN
        -- Return 0 if division by zero would occur
        RETURN 0;
    ELSE
        -- Perform the division and return the result
        RETURN a / b;
    END IF;
END $$

DELIMITER ;
