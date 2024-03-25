-- #2 
 
-- 종류 = '트럭'
-- 대여기록별 대여 금액 AS FEE 

SELECT DISTINCT history_id,
    CASE 
        WHEN DATEDIFF(end_date,start_date)+1 < 7 THEN ROUND((DATEDIFF(end_date,start_date)+1) * daily_fee,0)
        ELSE ROUND((DATEDIFF(end_date,start_date)+1) * daily_fee * (1-discount_rate/100),0)
        END AS fee
FROM car_rental_company_car AS c 
    JOIN car_rental_company_rental_history AS h USING(car_id)
    JOIN car_rental_company_discount_plan AS d USING(car_type)
WHERE c.car_type = '트럭' AND 
    CASE 
        WHEN DATEDIFF(end_date,start_date)+1 >= 90 THEN duration_type = '90일 이상'
        WHEN DATEDIFF(end_date,start_date)+1 >= 30 THEN duration_type = '30일 이상'
        WHEN DATEDIFF(end_date,start_date)+1 >= 7 THEN duration_type = '7일 이상'
        ELSE duration_type
    END
ORDER BY  2 DESC , 1 DESC ;