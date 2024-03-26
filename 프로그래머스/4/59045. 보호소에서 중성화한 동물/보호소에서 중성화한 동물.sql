-- #3

SELECT i.animal_id, i.animal_type, i.name
FROM animal_ins AS i JOIN animal_outs AS o USING(animal_id)
WHERE i.sex_upon_intake like '%Intact%' 
    AND (o.sex_upon_outcome like '%Spayed%' 
         OR o.sex_upon_outcome like '%Neutered%')
ORDER BY animal_id;