SELECT COUNT(*) AS fish_count, fish_name
FROM fish_info JOIN fish_name_info USING (fish_type)
GROUP BY fish_name
ORDER BY 1 DESC;