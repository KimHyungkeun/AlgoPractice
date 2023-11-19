-- 코드를 입력하세요
SELECT apnt_no, pt_name, p.pt_no, a.mcdp_cd, dr_name, apnt_ymd
FROM patient p JOIN appointment a JOIN doctor d
ON p.pt_no = a.pt_no AND a.mddr_id = d.dr_id
WHERE a.mcdp_cd = "CS" AND date_format(apnt_ymd, '%Y-%m-%d') = '2022-04-13' AND apnt_cncl_yn = "N"
ORDER BY apnt_ymd