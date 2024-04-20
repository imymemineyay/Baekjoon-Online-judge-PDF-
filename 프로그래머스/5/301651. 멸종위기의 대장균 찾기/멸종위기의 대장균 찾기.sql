WITH RECURSIVE generation AS 
(
    SELECT id, parent_id, 1 AS cnt
    FROM ecoli_data
    WHERE parent_id IS NULL
    
    UNION ALL
    
    SELECT ed.id, ed.parent_id, g.cnt + 1 
    FROM ecoli_data AS ed JOIN generation AS g ON ed.parent_id = g.id
    WHERE ed.parent_id IS NOT NULL
)


SELECT COUNT(*) AS COUNT, cnt AS GENERATION
FROM generation 
WHERE id NOT IN (SELECT DISTINCT parent_id 
                 FROM ecoli_data 
                 WHERE parent_id IS NOT NULL) 
GROUP BY cnt
ORDER BY generation;
