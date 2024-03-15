-- #2

-- 메인 출력 구문 : 월별 자동차 대여횟수 구하기
SELECT MONTH(start_date) AS month, car_id, count(*) AS records
FROM car_rental_company_rental_history

-- 서브쿼리 조건문 : 8~10월까지 자동차 대여한 횟수가 총 5회 이상인 차만 추출 
WHERE MONTH(start_date) BETWEEN 8 AND 10 
    AND car_id IN (SELECT car_id FROM car_rental_company_rental_history
                  WHERE MONTH(start_date) BETWEEN 8 AND 10
                  GROUP BY car_id
                  HAVING COUNT(history_id) >= 5)
GROUP BY car_id, MONTH(start_date) 
HAVING records >= 1
ORDER BY 1, 2 DESC;