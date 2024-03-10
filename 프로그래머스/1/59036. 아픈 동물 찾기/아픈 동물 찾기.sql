-- #2 
SELECT animal_id, name
    FROM animal_ins
    WHERE intake_condition = 'sick'
    ORDER BY animal_id;