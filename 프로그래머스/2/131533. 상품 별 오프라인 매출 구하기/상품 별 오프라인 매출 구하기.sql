-- #2 

SELECT product_code, ROUND(AVG(p.price) * SUM(o.sales_amount),0) AS sales
FROM product AS p JOIN offline_sale AS o USING(product_id)
GROUP BY p.product_id
ORDER BY sales DESC, p.product_code;
