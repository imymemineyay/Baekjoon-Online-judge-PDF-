-- #2 
SELECT pt_name, pt_no, gend_cd, age, IFNULL(tlno,'NONE') tlno
    FROM patient
    WHERE age <=12 AND gend_cd='w'
    ORDER BY age DESC, pt_name;