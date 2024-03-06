SELECT b.writer_id, u.nickname,
       CONCAT_WS(' ', city, street_address1, street_address2) AS 전체주소, 
       CONCAT_WS('-', LEFT(u.tlno, 3), MID(u.tlno, 4, 4), RIGHT(u.tlno, 4)) AS 전화번호
FROM used_goods_board AS b JOIN used_goods_user AS u 
    ON b.writer_id = u.user_id
GROUP BY b.writer_id
HAVING COUNT(*) >= 3
ORDER BY b.writer_id DESC;
