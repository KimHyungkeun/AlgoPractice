-- 코드를 입력하세요
SELECT warehouse_id, warehouse_name, address, 
CASE WHEN freezer_yn is null then 'N' else freezer_yn end as freezer_yn
FROM food_warehouse
WHERE address like '경기도%'
ORDER BY warehouse_id