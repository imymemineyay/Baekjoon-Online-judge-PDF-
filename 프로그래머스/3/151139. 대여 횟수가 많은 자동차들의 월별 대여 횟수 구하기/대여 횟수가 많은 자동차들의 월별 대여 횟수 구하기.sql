SELECT MONTH(start_date) AS month, car_id, count(*) AS records
FROM car_rental_company_rental_history
WHERE MONTH(start_date) BETWEEN 8 AND 10 
    AND car_id IN (SELECT car_id FROM car_rental_company_rental_history
                  WHERE MONTH(start_date) BETWEEN 8 AND 10
                  GROUP BY car_id
                  HAVING COUNT(history_id) >= 5)
GROUP BY car_id, MONTH(start_date) 
ORDER BY 1, 2 DESC;

