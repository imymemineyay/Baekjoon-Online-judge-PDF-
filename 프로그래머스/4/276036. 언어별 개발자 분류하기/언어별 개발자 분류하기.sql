-- #2 

WITH grade_info AS (
    SELECT DISTINCT 
           CASE
              WHEN skill_code & (SELECT SUM(code) FROM skillcodes
                                 GROUP BY category HAVING category = 'Front End' )  
                    AND skill_code & (SELECT code 
                                      FROM skillcodes 
                                      WHERE name = 'Python') THEN 'A'
              WHEN skill_code & (SELECT code FROM skillcodes WHERE name = 'C#')  THEN 'B'
              WHEN skill_code & (SELECT SUM(code) FROM skillcodes
                                 GROUP BY category HAVING category = 'Front End' ) THEN 'C'
           END AS grade, id, email
    FROM developers FULL JOIN skillcodes
    WHERE code & skill_code
    ORDER BY id
)

SELECT grade, id, email FROM grade_info WHERE grade IS NOT NULL ORDER BY grade,id;