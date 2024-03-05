WITH front AS (SELECT SUM(code) AS tot
                FROM skillcodes
                WHERE category = 'Front End')

SELECT CASE
          WHEN (skill_code&(SELECT tot FROM front)) AND (skill_code&(SELECT code FROM skillcodes WHERE name ='Python')) 
          THEN 'A'
          WHEN skill_code&(SELECT code FROM skillcodes WHERE name ='C#') 
          THEN 'B'
          WHEN (skill_code&(SELECT tot FROM front)) 
          THEN 'C'    
       END AS grade,id,email
    FROM developers 
    GROUP BY id, email,skill_code
    HAVING grade IS NOT NULL
    ORDER BY grade, id;