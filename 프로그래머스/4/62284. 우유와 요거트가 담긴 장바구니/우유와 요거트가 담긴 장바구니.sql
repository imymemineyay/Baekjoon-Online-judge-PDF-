-- #1 

WITH milk_tb AS (SELECT cart_id, name
                FROM cart_products
                WHERE name = 'Milk'),
    yogurt_tb AS (SELECT cart_id, name
                 FROM cart_products
                 WHERE name ='Yogurt')
                
SELECT DISTINCT cart_id
FROM milk_tb JOIN yogurt_tb USING(cart_id)
ORDER BY cart_id;
                 
                 