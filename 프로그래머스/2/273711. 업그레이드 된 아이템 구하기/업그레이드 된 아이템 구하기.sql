SELECT item_id, item_name, rarity
    FROM  item_info JOIN item_tree USING(item_id)
    WHERE parent_item_id in (SELECT item_id FROM item_info WHERE rarity ='rare')
    ORDER BY item_id DESC;