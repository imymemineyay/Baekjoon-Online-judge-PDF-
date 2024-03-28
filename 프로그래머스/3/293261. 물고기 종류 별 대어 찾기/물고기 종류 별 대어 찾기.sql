-- #2

SELECT id, fish_name, length
FROM fish_info JOIN fish_name_info USING(fish_type)
WHERE (fish_type, length) IN (SELECT fish_type, MAX(length) AS length
                            FROM fish_info
                            GROUP BY fish_type)
ORDER BY id;
