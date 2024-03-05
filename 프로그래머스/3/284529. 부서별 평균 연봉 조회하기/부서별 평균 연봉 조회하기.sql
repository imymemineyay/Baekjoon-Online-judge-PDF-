SELECT e.dept_id, d.dept_name_en, ROUND(AVG(e.sal),0) AS avg_sal
    FROM hr_employees AS e 
        JOIN hr_department AS d 
        ON e.dept_id = d.dept_id
    GROUP BY e.dept_id
    ORDER BY avg_sal DESC;