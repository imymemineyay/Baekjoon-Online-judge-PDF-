SELECT o.animal_id, o.name 
    FROM animal_ins AS i JOIN animal_outs AS o ON i.animal_id = o.animal_id
    ORDER BY DATEDIFF(o.datetime,i.datetime) DESC
    LIMIT 2;