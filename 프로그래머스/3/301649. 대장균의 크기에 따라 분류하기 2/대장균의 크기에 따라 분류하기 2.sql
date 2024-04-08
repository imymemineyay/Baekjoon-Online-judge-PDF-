-- 코드를 작성해주세요
WITH rank_size AS 
(SELECT id,
        PERCENT_RANK() OVER (ORDER BY size_of_colony DESC) AS ranking
FROM ecoli_data)

SELECT id,
        CASE 
            WHEN ranking <= 0.25 THEN 'CRITICAL'
            WHEN ranking <= 0.50 THEN 'HIGH'
            WHEN ranking <= 0.75 THEN 'MEDIUM'
            ELSE 'LOW'
        END AS colony_name
FROM rank_size
ORDER BY id;