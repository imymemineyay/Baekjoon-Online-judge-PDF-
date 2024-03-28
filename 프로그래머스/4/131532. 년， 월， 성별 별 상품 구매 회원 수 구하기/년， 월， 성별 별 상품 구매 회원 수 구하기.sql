-- #3

SELECT YEAR(o.sales_date) AS year, 
       MONTH(o.sales_date) AS month, 
       i.gender, 
       COUNT( DISTINCT o.user_id) AS users
       
FROM user_info AS i JOIN online_sale AS o USING(user_id)

WHERE i.gender IS NOT NULL

GROUP BY YEAR(o.sales_date), MONTH(o.sales_date), i.gender

ORDER BY YEAR(o.sales_date), MONTH(o.sales_date), i.gender;
