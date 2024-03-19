-- #2

-- 
SELECT mcdp_cd AS "진료과 코드", COUNT(*) AS '5월예약건수'
FROM appointment
WHERE DATE_FORMAT(apnt_ymd, "%Y-%m") = '2022-05'
GROUP BY mcdp_cd
ORDER BY 2,1;