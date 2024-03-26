-- #3

SELECT order_id, product_id, DATE_FORMAT(out_date, '%Y-%m-%d') AS out_date, 
    CASE 
        WHEN DATE_FORMAT(out_date,'%m-%d') <= '05-01' THEN '출고완료'
        WHEN DATE_FORMAT(out_date,'%m-%d') > '05-01' THEN '출고대기'
        ELSE '출고미정'
    END AS 출고여부
FROM food_order
ORDER BY order_id;