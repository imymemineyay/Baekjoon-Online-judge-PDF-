SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
    FROM developers
    WHERE skill_code & (SELECT SUM(code) FROM skillcodes WHERE name in('Python', 'C#'))
    ORDER BY id ;