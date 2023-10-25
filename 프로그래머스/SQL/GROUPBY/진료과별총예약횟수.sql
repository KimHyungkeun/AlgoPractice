-- 코드를 입력하세요
SELECT mcdp_cd as `진료과코드`, count(mcdp_cd) as `5월예약건수`
FROM appointment
WHERE apnt_ymd LIKE '2022-05%'
GROUP BY mcdp_cd
ORDER BY `5월예약건수`, `진료과코드`