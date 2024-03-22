-- #2

SELECT SUM(score) AS score, emp_no,emp_name, position, email 
FROM hr_employees JOIN hr_grade USING(emp_no)
WHERE year=2022
GROUP BY emp_no
ORDER BY 1 DESC
LIMIT 1;