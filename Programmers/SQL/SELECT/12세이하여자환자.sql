-- 코드를 입력하세요
SELECT pt_name, pt_no, gend_cd, age,
CASE WHEN tlno is null then 'NONE' else tlno END as tlno
FROM patient
WHERE age <= 12 AND gend_cd = 'W'
ORDER BY age DESC, pt_name ASC