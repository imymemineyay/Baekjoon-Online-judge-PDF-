WITH hg AS (SELECT emp_no, sum(score) score
                FROM hr_grade
                WHERE year = '2022'
                GROUP BY emp_no
                ORDER BY score DESC
                LIMIT 1)
                
SELECT hg.score, hg.emp_no, he.emp_name, he.position, he.email
    FROM hr_employees he JOIN hg ON he.emp_no = hg.emp_no
