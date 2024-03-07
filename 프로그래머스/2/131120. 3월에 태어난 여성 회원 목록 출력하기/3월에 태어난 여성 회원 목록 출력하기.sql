-- #2
SELECT member_id, member_name, gender, 
       DATE_FORMAT(date_of_birth,'%Y-%m-%d') AS date_of_birth
FROM member_profile
WHERE MONTH(date_of_birth) = 3 AND gender = 'w' AND tlno IS NOT NULL
ORDER BY member_id;