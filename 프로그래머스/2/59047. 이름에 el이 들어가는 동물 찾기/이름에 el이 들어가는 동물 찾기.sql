-- #2 

SELECT animal_id, name
FROM animal_ins 
WHERE animal_type = 'Dog' AND name like '%el%'
ORDER BY name;
