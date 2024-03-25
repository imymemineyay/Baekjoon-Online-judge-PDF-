-- #2 
SELECT car_id, 
    ROUND(SUM((DATEDIFF(end_date,start_date)+1)) / COUNT(*),1) AS average_duration
    
FROM car_rental_company_rental_history
GROUP BY car_id 
HAVING average_duration >=7
ORDER BY 2 DESC, 1 DESC;