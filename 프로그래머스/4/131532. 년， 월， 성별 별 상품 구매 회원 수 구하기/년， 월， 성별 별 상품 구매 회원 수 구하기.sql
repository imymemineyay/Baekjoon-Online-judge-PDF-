-- #2

SELECT YEAR(sales_date) AS year, MONTH(sales_date) AS month, gender, 
        COUNT(DISTINCT user_id) AS users
FROM user_info JOIN online_sale USING(user_id)
WHERE gender IS NOT NULL
GROUP BY year, month, gender 
ORDER BY year, month, gender