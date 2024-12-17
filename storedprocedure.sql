DELIMITER //

-- Get all questions
CREATE PROCEDURE GetAllQuestions()
BEGIN
    SELECT * FROM userauth_question;
END // 

-- Get all users
CREATE PROCEDURE GetAllUsers()
BEGIN
    SELECT * FROM userauth_user;
END //

-- Create new question
CREATE PROCEDURE CreateQuestion(IN p_title VARCHAR(255), IN p_content VARCHAR(255))
BEGIN
    INSERT INTO userauth_question (title, content, created_at, updated_at)
    VALUES (p_title, p_content, NOW(), NOW());
END //

-- Update question
CREATE PROCEDURE UpdateQuestion(IN p_id INT, IN p_title VARCHAR(255), IN p_content VARCHAR(255))
BEGIN
    UPDATE userauth_question
    SET title = p_title, content = p_content, updated_at = NOW()
    WHERE id = p_id;
END //

-- Delete question
CREATE PROCEDURE DeleteQuestion(IN p_id INT)
BEGIN
    DELETE FROM userauth_question WHERE id = p_id;
END //

-- Edit User
CREATE PROCEDURE EditUser(IN p_id INT, IN p_first_name VARCHAR(255), IN p_last_name VARCHAR(255), IN p_email VARCHAR(255))
BEGIN
    UPDATE userauth_user
    SET first_name = p_first_name,
        last_name = p_last_name,
        email = p_email,
        updated_at = NOW()
    WHERE id = p_id;
END //


DELIMITER ;

