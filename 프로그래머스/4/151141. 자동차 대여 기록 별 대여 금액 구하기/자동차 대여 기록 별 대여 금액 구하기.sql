-- 1. history랑 discount duration_type으로 결합하기 
-- (1) discount duration_type 과 동일한 컬럼 생성하기 

WITH history AS (SELECT history_id, car_id, 
                 (DATEDIFF(end_date, start_date)+1) AS days,
    CASE 
        WHEN (DATEDIFF(end_date, start_date) +1) >= 90 THEN '90일 이상'
        WHEN (DATEDIFF(end_date, start_date) +1) >= 30 THEN '30일 이상'
        WHEN (DATEDIFF(end_date, start_date) +1) >= 7 THEN '7일 이상'
    END AS duration_col
FROM car_rental_company_rental_history 
WHERE car_id IN (SELECT car_id from car_rental_company_car WHERE car_type='트럭')) 

-- (2) discount 테이블에서 트럭 데이터만 추출하기 
, truck_dis AS (SELECT duration_type, discount_rate 
                   FROM car_rental_company_discount_plan
                   WHERE CAR_TYPE = '트럭')

-- (3) 새로 만든 테이블 history, truck_dis 를 duration_type으로 조인시킨다.
--     단, 주의해야할 점은 history 테이블에 있는 할인이 적용되지 않는 데이터도 포함해야 된다는 것
, hist_truck_merged AS (SELECT * FROM history AS h LEFT OUTER JOIN truck_dis AS t ON duration_col = duration_type)


-- 2. car테이블과 (3)에서 생성한 hist_truck_merged테이블을 car_id로 조인한 후 결과물 출력
SELECT history_id, 
    CASE 
    WHEN discount_rate IS NOT NULL 
    THEN ROUND(daily_fee*days*(1-discount_rate/100),0) 
    ELSE daily_fee*days
    END AS fee
    FROM car_rental_company_car JOIN hist_truck_merged USING (car_id)
    ORDER BY fee DESC, history_id DESC;