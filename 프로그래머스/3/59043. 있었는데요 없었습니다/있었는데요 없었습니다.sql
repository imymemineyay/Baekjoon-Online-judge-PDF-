-- #2
SELECT o.animal_id, o.name 
FROM animal_outs AS o LEFT JOIN animal_ins AS i USING (animal_id)
WHERE o.datetime < i.datetime
ORDER BY i.datetime ;