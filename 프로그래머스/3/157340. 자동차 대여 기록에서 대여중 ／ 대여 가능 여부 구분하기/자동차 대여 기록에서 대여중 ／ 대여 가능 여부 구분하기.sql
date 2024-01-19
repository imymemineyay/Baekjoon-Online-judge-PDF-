SELECT CAR_ID, 
max(case when '2022-10-16' between start_date and end_date 
    then '대여중' 
    else '대여 가능' end) as AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC