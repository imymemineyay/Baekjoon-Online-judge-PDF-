-- #2 

-- first_half의 pk 는 flavor, fk는 shipment_id
-- july의 pk는 shipment_id, fk는 flavor

-- first_half 1 : july 다 (flavor을 조회하는 문제이기 때문)

SELECT flavor
FROM first_half AS h JOIN july AS j USING(flavor)
-- first_half 의 총 주문량은 july와 조인되면서 중복되게 됨 
-- 따라서 avg를 해서 중복 제거값으로 구해줘야함
GROUP BY flavor
ORDER BY AVG(h.total_order) + SUM(j.total_order) DESC
LIMIT 3;
