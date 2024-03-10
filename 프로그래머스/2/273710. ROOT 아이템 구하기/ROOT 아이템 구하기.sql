-- #2

SELECT item_id, item_name 
    FROM item_info
    WHERE item_id IN (SELECT item_id FROM item_tree WHERE parent_item_id IS NULL)
    ORDER BY item_id;