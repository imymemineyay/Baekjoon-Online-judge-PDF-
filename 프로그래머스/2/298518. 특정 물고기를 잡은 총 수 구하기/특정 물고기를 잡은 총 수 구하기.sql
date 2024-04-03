-- 코드를 작성해주세요
SELECT COUNT(id) AS FISH_COUNT
FROM fish_info JOIN fish_name_info USING(fish_type)
WHERE fish_name_info.fish_name IN ('BASS','SNAPPER')