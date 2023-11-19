-- 코드를 입력하세요
SELECT board_id, writer_id, title, price, 
CASE
    WHEN status = 'SALE' then '판매중'
    WHEN status = 'RESERVED' then '예약중'
    WHEN status = 'DONE' then '거래완료'
END as status
FROM USED_GOODS_BOARD
WHERE CREATED_DATE = '2022-10-05'
ORDER BY board_id DESC