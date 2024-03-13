-- #2

SELECT o.product_id, p.product_name, SUM(o.amount)*p.price AS total_sales
FROM food_order AS o JOIN food_product AS p USING (product_id)
WHERE produce_date like '2022-05%'
GROUP BY o.product_id
ORDER BY total_sales DESC, product_id;
