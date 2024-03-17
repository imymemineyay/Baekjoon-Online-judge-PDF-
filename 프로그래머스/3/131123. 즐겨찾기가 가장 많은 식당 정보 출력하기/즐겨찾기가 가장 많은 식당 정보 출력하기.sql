-- #2 
WITH max_favorites AS (SELECT food_type, max(favorites) favorites FROM rest_info
                  GROUP BY food_type)

SELECT i.food_type, i.rest_id, i.rest_name, i.favorites
FROM rest_info AS i JOIN max_favorites USING (food_type, favorites)
ORDER BY food_type DESC;