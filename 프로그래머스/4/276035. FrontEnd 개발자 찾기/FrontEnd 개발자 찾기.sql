-- # 2

SELECT DISTINCT id, email, first_name, last_name
FROM skillcodes JOIN developers
WHERE (skill_code & code) AND category = 'Front End'
ORDER BY id;