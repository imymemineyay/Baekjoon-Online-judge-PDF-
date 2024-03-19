-- #3
SELECT category, price AS max_price, product_name
FROM food_product
WHERE (category, price) IN (SELECT category, max(price)
                           FROM food_product
                           WHERE category IN ('과자', '국', '김치', '식용유')
                           GROUP BY category)
ORDER BY price DESC;