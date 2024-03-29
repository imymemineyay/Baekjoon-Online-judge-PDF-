-- #4
SELECT history_id, 
    CASE 
        WHEN (DATEDIFF(end_date, start_date) + 1) < 7 
            THEN (DATEDIFF(end_date, start_date) + 1) * daily_fee
        ELSE ROUND(daily_fee * (DATEDIFF(end_date, start_date) + 1) * (1-discount_rate/100),0) 
    END AS fee
FROM car_rental_company_car AS c 
    JOIN car_rental_company_rental_history AS h USING(car_id) 
    JOIN car_rental_company_discount_plan AS p USING(car_type)
WHERE c.car_type = '트럭' AND 
    CASE 
        WHEN DATEDIFF(end_date, start_date) + 1 >= 90 THEN duration_type ='90일 이상'
        WHEN DATEDIFF(end_date, start_date) + 1 >= 30 THEN duration_type ='30일 이상'
        WHEN DATEDIFF(end_date, start_date) + 1 >= 7 THEN duration_type ='7일 이상' 
        ELSE duration_type 
    END 
GROUP BY h.history_id
ORDER BY 2 DESC, history_id DESC;