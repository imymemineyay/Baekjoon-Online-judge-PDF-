-- # 3

WITH rental_tb AS (
    SELECT car_id, '대여중' AS AVAILABILITY
    FROM car_rental_company_rental_history
    WHERE '2022-10-16' BETWEEN start_date AND end_date)
    
SELECT car_id, IFNULL(AVAILABILITY,'대여 가능') AS availability
FROM car_rental_company_rental_history LEFT JOIN rental_tb USING(car_id)
GROUP BY car_id
ORDER BY car_id DESC;

