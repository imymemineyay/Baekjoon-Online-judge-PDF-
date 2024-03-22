-- #2

SELECT dept_id, dept_name_en, ROUND(AVG(sal),0) AS avg_sal
FROM hr_department JOIN hr_employees USING(dept_id)
GROUP BY dept_id
ORDER BY 3 DESC;
