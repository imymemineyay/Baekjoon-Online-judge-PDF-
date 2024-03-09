-- #2 
SELECT b.title, b.board_id, r.reply_id, r.writer_id, r.contents, 
       DATE_FORMAT(r.created_date,'%Y-%m-%d') AS created_date
    FROM used_goods_board AS b JOIN used_goods_reply AS r USING(board_id)
    WHERE YEAR(b.created_date) =2022 AND MONTH(b.created_date) = 10
    ORDER BY r.created_date, b.title;