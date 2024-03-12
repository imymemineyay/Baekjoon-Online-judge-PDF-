-- #2
-- '세단' , 'SUV' 데이터 추출 / 단 Duration_type 30일 이상 만 추출 
SELECT c.car_id, c.car_type, 
        TRUNCATE(c.daily_fee*30*(1-p.discount_rate/100),0) AS fee
FROM car_rental_company_car AS c
    JOIN car_rental_company_discount_plan AS p USING(car_type) 
    WHERE p.car_type IN ('세단', 'SUV') AND p.DURATION_TYPE = '30일 이상' AND 
-- fee 가 50만원 이상 ~ 200만원 미만
    TRUNCATE(c.daily_fee*30*(1-p.discount_rate/100),0) BETWEEN 500000 AND 2000000 
    AND
-- '세단' , 'SUV' 데이터 추출 / 단, 조건에 맞는 기간에 있는 것만 
       c.car_id NOT IN (SELECT car_id 
                       FROM car_rental_company_rental_history 
                       WHERE end_date >= '2022-11-01' 
                            AND start_date <= '2022-11-30')
                            
