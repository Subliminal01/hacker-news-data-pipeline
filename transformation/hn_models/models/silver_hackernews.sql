{{ config(materialized='table') }}

WITH raw_data AS (
    -- Grab the raw data from our DuckDB Bronze table
    SELECT * FROM bronze_hackernews
)

SELECT
    id AS story_id,
    title,
    -- Rename the problematic "by" column to something that makes sense
    "by" AS author,
    -- Ensure the score is treated as a number
    CAST(score AS INTEGER) AS score,
    -- Keep the URL if we want to link out to the article later
    url,
    -- Keep our extraction timestamp to track when this batch ran
    CAST(extracted_at AS TIMESTAMP) AS extracted_at
FROM raw_data
-- Filter out any corrupted rows that might be missing a title
WHERE title IS NOT NULL