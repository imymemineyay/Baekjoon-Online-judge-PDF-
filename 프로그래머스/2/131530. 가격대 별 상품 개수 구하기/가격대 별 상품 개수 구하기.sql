-- # 2

SELECT TRUNCATE(price/10000,0)*10000 AS price_group, COUNT(*) AS products
FROM product
GROUP BY price_group
ORDER BY 1;