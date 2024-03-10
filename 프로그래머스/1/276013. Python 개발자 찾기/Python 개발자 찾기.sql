-- #2
SELECT id, email, first_name, last_name 
    FROM developer_infos 
    WHERE skill_1 = 'python' or skill_2 = 'python' or skill_3 = 'python'
    ORDER BY id;
    