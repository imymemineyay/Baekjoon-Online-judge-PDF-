-- #3

SELECT u.user_id, u.nickname, 
    CONCAT(u.city,' ', u.street_address1, ' ', u.street_address2) AS '전체주소', 
    CONCAT(LEFT(u.tlno,3),'-',MID(u.tlno,4,4),'-',RIGHT(u.tlno,4)) AS 전화번호
FROM used_goods_board AS b JOIN used_goods_user AS u 
    ON b.writer_id = u.user_id
GROUP BY u.user_id
HAVING COUNT(board_id) >= 3
ORDER BY u.user_id DESC;