-- #2 

SELECT DISTINCT car_id
FROM car_rental_company_car JOIN car_rental_company_rental_history USING(car_id)
WHERE car_type = '세단' AND MONTH(start_date) = 10
ORDER BY car_id DESC;