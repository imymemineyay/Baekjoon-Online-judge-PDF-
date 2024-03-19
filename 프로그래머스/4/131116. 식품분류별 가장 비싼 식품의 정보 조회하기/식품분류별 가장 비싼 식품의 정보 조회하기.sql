-- #2
WITH a AS(
    SELECT category, max(price) AS max_price, product_name 
    FROM food_product
    WHERE category IN ('과자', '국', '김치', '식용유')
    GROUP BY category, product_name),
    b AS( 
    SELECT category, max(price) AS max_price 
    FROM food_product
    WHERE category IN ('과자', '국', '김치', '식용유')
    GROUP BY category)

SELECT * 
FROM a JOIN b USING(category, max_price)
ORDER BY max_price DESC;
