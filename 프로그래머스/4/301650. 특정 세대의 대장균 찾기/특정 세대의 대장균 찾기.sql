SELECT id
FROM ecoli_data 
WHERE parent_id IN (SELECT id FROM ecoli_data WHERE parent_id IN (SELECT id FROM ecoli_data WHERE parent_id IS NULL))
ORDER BY id;
