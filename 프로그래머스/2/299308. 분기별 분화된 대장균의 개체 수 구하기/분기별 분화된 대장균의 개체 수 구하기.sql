-- 코드를 작성해주세요
SELECT CONCAT(CASE
                WHEN MONTH(DIFFERENTIATION_DATE) >= 10 THEN 4
                WHEN MONTH(DIFFERENTIATION_DATE) >= 7 THEN 3
                WHEN MONTH(DIFFERENTIATION_DATE) >= 4 THEN 2
                ELSE 1
              END, 'Q') AS quarter, COUNT(id) AS ecoli_count 
FROM ecoli_data
GROUP BY quarter
ORDER BY 1 ; 
