-- #2

SELECT LEFT(product_code,2) AS category, COUNT(*) AS products
FROM product
GROUP BY category
ORDER BY product_code;