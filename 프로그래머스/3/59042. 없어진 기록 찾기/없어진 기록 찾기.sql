-- #2 

SELECT o.animal_id, o.name
FROM animal_outs AS o LEFT OUTER JOIN animal_ins AS i USING (animal_id)
WHERE i.datetime IS NULL
ORDER BY o.animal_id;