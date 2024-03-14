WITH max_length_fish AS (SELECT * 
                         FROM fish_name_info 
                            JOIN (SELECT fish_type, MAX(length) AS length
                                    FROM fish_info 
                                    GROUP BY fish_type) AS b 
                            USING(fish_type))

SELECT id, fish_name, length
FROM fish_info JOIN max_length_fish USING(fish_type, length)