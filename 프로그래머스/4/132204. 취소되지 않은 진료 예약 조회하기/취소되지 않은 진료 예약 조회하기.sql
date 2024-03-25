-- #2 
-- '2022-04-13' 취소되지 않은 흉부외과 
-- 진료예약번호(appointment), 환자이름(patient), 환자번호(appointment), 
-- 진료과코드(appointment), 의사이름(doctor), 진료예약일시(appointment)

-- doctor랑 appointment랑 결합한 후 예약일시와 , 흉부외과를 기준으로 데이터 추출
-- 위 테이블과 patient 결합 

SELECT a.apnt_no, p.pt_name, p.pt_no, a.mcdp_cd, d.dr_name, a.apnt_ymd
FROM appointment AS a 
    JOIN doctor AS d ON a.mddr_id = d.dr_id
    JOIN patient AS p USING(pt_no)
WHERE DATE_FORMAT(a.apnt_ymd,'%Y-%m-%d')='2022-04-13' 
    AND a.mcdp_cd='CS' AND a.apnt_cncl_yn='N'
ORDER BY 6;