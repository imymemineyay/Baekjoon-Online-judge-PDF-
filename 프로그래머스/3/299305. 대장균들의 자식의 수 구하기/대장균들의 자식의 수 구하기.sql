-- # 2

WITH id_tb AS (SELECT parent_id, COUNT(*) AS child_count 
               FROM ecoli_data GROUP BY parent_id)

SELECT id, IFNULL(child_count,0) AS child_count
FROM ecoli_data LEFT JOIN id_tb ON ecoli_data.ID = id_tb.parent_id
ORDER BY 1;