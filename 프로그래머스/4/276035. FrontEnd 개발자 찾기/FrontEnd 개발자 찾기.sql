SELECT DISTINCT(id), email, first_name, last_name
    FROM skillcodes, developers
    WHERE (skill_code & code) AND category = "Front End"
    ORDER BY id;