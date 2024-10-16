-- List all Glam rock bands ranked by their longevity
-- Use the split year if the band has split
-- Otherwise, use 2022 as the current year
-- Filter bands with 'Glam' as part of their style
-- Rank by longevity (lifespan)
SELECT
    band_name,
    CASE
        WHEN split IS NOT NULL THEN (split - formed)
        ELSE (2022 - formed)
    END AS lifespan
FROM
    metal_bands
WHERE
    style LIKE '%Glam%'
ORDER BY
    lifespan DESC;
