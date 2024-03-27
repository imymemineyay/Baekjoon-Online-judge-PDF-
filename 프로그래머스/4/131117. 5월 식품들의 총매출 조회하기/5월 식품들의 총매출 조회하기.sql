-- #3

SELECT p.product_id, p.product_name, SUM(amount*price) AS total_sales
FROM food_product AS p JOIN food_order AS o USING (product_id)
WHERE DATE_FORMAT(o.produce_date, '%Y-%m') = '2022-05'
GROUP BY p.product_id,p.product_name
ORDER BY 3 DESC, 1;