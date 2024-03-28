-- #3

-- 조건: '2022-04-13' CS apnt_cncl_yn = 'N'

SELECT a.apnt_no, pt_name, a.pt_no, a.mcdp_cd, dr_name, a.apnt_ymd
FROM appointment AS a JOIN patient USING(pt_no)
    JOIN doctor AS d ON d.dr_id = a.mddr_id
WHERE Date_FORMAT(a.apnt_ymd, '%Y-%m-%d') = '2022-04-13' AND a.mcdp_cd = 'CS' AND a.apnt_cncl_yn = 'N'
ORDER BY a.apnt_ymd;