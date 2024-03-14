-- #2 

SELECT o.animal_id, o.animal_type, o.name 
FROM animal_outs AS o LEFT JOIN animal_ins AS i USING (animal_id)
WHERE i.sex_upon_intake like 'intact%' 
    AND (o.sex_upon_outcome like 'spayed%' OR o.sex_upon_outcome like 'neutered%')
ORDER BY o.animal_id;