-- #2 
-- FIRST_HALF n :  ICECREAM_INFO 1

SELECT ingredient_type, SUM(total_order) AS total_order
FROM first_half JOIN icecream_info USING (flavor)
GROUP BY ingredient_type
ORDER BY total_order ;