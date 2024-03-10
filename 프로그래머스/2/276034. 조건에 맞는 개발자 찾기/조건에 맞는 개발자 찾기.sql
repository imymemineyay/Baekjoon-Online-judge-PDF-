-- #2

SELECT DISTINCT id, email, first_name, last_name
    FROM developers CROSS JOIN skillcodes
    WHERE (skill_code & code) AND (name IN ('python','c#'))
    ORDER BY id;