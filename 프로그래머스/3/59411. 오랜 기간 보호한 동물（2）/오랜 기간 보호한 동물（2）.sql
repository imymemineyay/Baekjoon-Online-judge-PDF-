-- #2
SELECT i.animal_id, i.name 
FROM animal_ins AS i LEFT JOIN animal_outs AS o USING(animal_id)
WHERE o.datetime IS NOT NULL
ORDER BY DATEDIFF(o.datetime,i.datetime)+1 DESC
LIMIT 2;