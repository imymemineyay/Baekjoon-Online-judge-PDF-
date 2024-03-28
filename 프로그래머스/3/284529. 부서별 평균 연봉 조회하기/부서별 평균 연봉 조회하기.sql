-- #3

SELECT d.dept_id, d.dept_name_en, ROUND(AVG(e.sal),0) AS avg_sal
FROM hr_department AS d JOIN hr_employees AS e USING(dept_id)
GROUP BY d.dept_id
ORDER BY 3 DESC;
