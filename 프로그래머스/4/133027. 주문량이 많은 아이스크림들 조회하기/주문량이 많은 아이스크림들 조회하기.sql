-- # 3

-- [first_half] shipment_id(FK), flavor(PK), total_order 1
-- [july] shipment_id(PK), flavor(FK), total_order n


SELECT flavor 
FROM july LEFT JOIN first_half USING(flavor)
GROUP BY flavor
ORDER BY (SUM(july.total_order) + AVG(first_half.total_order))  DESC
LIMIT 3;
