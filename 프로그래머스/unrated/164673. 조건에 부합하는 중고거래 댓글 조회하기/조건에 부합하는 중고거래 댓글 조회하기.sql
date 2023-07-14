-- 코드를 입력하세요
SELECT a.TITLE as TITLE, a.board_id as BOARD_ID, b.reply_id as REPLY_ID,  b.writer_id as WRITER_ID,  b.contents as CONTENTS, substring_index(b.created_date,' ',1) as CREATED_DATE
from 
(select title, board_id, created_date 
      from used_goods_board 
      where month(created_date)=10) a, used_goods_reply as b 
      where a.board_id = b.board_id
      order by b.created_date, a.title ;