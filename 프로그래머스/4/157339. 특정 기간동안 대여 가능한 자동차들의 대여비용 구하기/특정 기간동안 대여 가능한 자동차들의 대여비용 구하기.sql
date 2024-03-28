-- #3 

WITH availability AS (SELECT car_id
                     FROM car_rental_company_rental_history
                     WHERE '2022-11-01' BETWEEN start_date AND end_date
                     OR '2022-11-31' BETWEEN start_date AND end_date)
                     
SELECT c.car_id, c.car_type, 
    ROUND((daily_fee*30)*(1-discount_rate/100),0)AS fee
FROM car_rental_company_car AS c 
    LEFT JOIN car_rental_company_rental_history AS h USING(car_id) 
    JOIN car_rental_company_discount_plan AS p USING(car_type)
WHERE c.car_type IN ('세단','SUV')
    AND c.car_id NOT IN (SELECT car_id FROM availability)
    AND p.duration_type = '30일 이상'
GROUP BY c.car_id
HAVING fee >= 500000 AND fee < 2000000
ORDER BY 3 DESC, 2, 1 DESC;