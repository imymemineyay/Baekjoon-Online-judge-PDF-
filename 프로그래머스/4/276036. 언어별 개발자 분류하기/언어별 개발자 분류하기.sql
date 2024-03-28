-- #3 

SELECT 
    CASE 
        WHEN skill_code & (SELECT code FROM skillcodes
                          WHERE name ='Python') 
            AND skill_code & (SELECT SUM(code) FROM skillcodes
                          WHERE category ='Front End') 
                          THEN 'A'
        WHEN skill_code & (SELECT code FROM skillcodes
                          WHERE name ='C#')THEN 'B'
        WHEN skill_code & (SELECT SUM(code) FROM skillcodes
                          WHERE category ='Front End') THEN 'C'
    END AS grade, id, email
FROM developers FULL JOIN skillcodes 
WHERE skill_code & code 
GROUP BY grade, id, email
HAVING grade IS NOT NULL
ORDER BY grade, id
;