-- 코드를 입력하세요
SELECT title, b.board_id, reply_id, b.writer_id, b.contents, date_format(b.created_date, '%Y-%m-%d') as created_date
FROM used_goods_board a JOIN used_goods_reply b
ON a.board_id = b.board_id
WHERE year(a.created_date) = 2022 AND month(a.created_date) = 10
ORDER BY b.created_date, title