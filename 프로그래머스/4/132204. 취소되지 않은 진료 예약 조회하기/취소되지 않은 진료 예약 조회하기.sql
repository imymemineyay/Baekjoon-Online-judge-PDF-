WITH cs_y AS (
        SELECT A.apnt_ymd, A.apnt_no, A.pt_no, A.mcdp_cd, A.mddr_id, P.pt_name
            FROM patient AS P JOIN appointment AS A ON P.pt_no = A.pt_no
            WHERE  A.apnt_ymd LIKE '2022-04-13%' AND A.apnt_cncl_yn = 'N' AND A.mcdp_cd='CS')
            
SELECT apnt_no, pt_name, pt_no, cs_y.mcdp_cd, dr_name, apnt_ymd
    FROM cs_y JOIN doctor ON dr_id = mddr_id
    ORDER BY apnt_ymd;