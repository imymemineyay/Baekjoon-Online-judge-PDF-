-- #2 

SELECT i.name, i.datetime
FROM animal_ins AS i LEFT JOIN animal_outs AS o USING(animal_id)
WHERE o.datetime IS NULL 
ORDER BY i.datetime 
LIMIT 3;