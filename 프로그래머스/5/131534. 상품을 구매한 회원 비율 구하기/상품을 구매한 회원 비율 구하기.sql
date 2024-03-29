-- #4

SELECT YEAR(sales_date) AS year, MONTH(sales_date) AS month, 
        COUNT(DISTINCT user_id) AS puchased_users, 
        ROUND((COUNT(DISTINCT user_id)/(SELECT COUNT(user_id) FROM user_info 
                         WHERE YEAR(joined) = 2021)),1) AS puchased_ratio 
FROM online_sale
WHERE user_id IN (SELECT user_id FROM user_info WHERE YEAR(joined) = 2021)
GROUP BY YEAR(sales_date), MONTH(sales_date)
ORDER BY 1, 2;
