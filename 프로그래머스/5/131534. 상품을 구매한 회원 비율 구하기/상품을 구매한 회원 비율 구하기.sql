SELECT YEAR(sales_date) AS year, MONTH(sales_date) AS month, 
        COUNT(DISTINCT s.user_id) puchased_users, 
        ROUND(COUNT(DISTINCT s.user_id)/ (SELECT count(*) 
                                FROM user_info
                                WHERE YEAR(JOINED) = 2021),1) AS puchased_ratio
FROM user_info AS i JOIN online_sale AS s USING(user_id)
WHERE YEAR(JOINED) = 2021
GROUP BY month
ORDER BY year, month;