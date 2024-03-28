-- # 1

WITH child_cnt AS (SELECT parent_id, count(*) AS child_count
FROM ecoli_data 
GROUP BY PARENT_ID)

SELECT id, IFNULL(child_count,0) AS child_count
FROM ecoli_data AS d LEFT JOIN child_cnt AS c ON d.id = c.parent_id
ORDER BY id;