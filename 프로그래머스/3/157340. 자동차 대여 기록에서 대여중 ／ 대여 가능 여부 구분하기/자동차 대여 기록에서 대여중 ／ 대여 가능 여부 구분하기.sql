-- #2

-- 2022-10-16일에 대여가 가능한 car_id를 추출하는 것 
-- 해당일자에 대여 가능여부에 따라서 '대여중'과 '대여 가능'으로 표시 

-- 해당 날짜 대여중인 차량만 추출
-- 전체와 merge후 null값인 것 대여가능으로 변경 
WITH rental AS (
    SELECT DISTINCT car_id,'대여중' AS availability
    FROM car_rental_company_rental_history
    WHERE '2022-10-16' BETWEEN start_date AND end_date)
    
    
SELECT DISTINCT car_id, IFNULL(availability, '대여 가능') AS availability
FROM car_rental_company_rental_history LEFT JOIN rental USING(car_id)
ORDER BY car_id DESC;

