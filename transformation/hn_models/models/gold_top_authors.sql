{{ config(materialized='table') }}

WITH silver_data AS (
    -- Read from our clean Silver table, not the Bronze one!
    SELECT * FROM {{ ref('silver_hackernews') }}
)

SELECT
    author,
    COUNT(story_id) AS total_stories,
    SUM(score) AS total_score,
    MAX(extracted_at) AS last_active_at
FROM silver_data
GROUP BY author
ORDER BY total_score DESC