-- #3

-- # SELECT MONTH(start_date) AS month, car_id, COUNT(*) AS records 
-- # FROM car_rental_company_rental_history
-- # WHERE start_date BETWEEN '2022-08-01' AND '2022-10-31'
-- # GROUP BY MONTH(start_date), car_id

WITH rental_over_5 AS (SELECT car_id, COUNT(*) AS records 
FROM car_rental_company_rental_history
WHERE start_date BETWEEN '2022-08-01' AND '2022-10-31'
GROUP BY car_id
HAVING records >= 5 )

SELECT MONTH(start_date) AS month, car_id, COUNT(*) AS records 
FROM car_rental_company_rental_history JOIN rental_over_5 USING(car_id)
WHERE start_date BETWEEN '2022-08-01' AND '2022-10-31'
GROUP BY MONTH(start_date), car_id
ORDER BY 1, 2 DESC;
