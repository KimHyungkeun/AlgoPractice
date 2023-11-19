-- 코드를 입력하세요
SELECT concat('/home/grep/src/', l.board_id, '/', file_id, file_name, file_ext) as file_path
FROM used_goods_board l JOIN used_goods_file r
ON l.board_id = r.board_id
WHERE l.views = (SELECT max(views) FROM used_goods_board)
ORDER BY file_id DESC