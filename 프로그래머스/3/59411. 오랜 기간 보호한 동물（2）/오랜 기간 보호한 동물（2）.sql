-- #3

SELECT i.animal_id, i.name
FROM animal_ins AS i JOIN animal_outs AS o USING(animal_id)
ORDER BY o.datetime - i.datetime DESC
LIMIT 2;