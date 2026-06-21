-- ════════════════════════════════════════════════════
-- SOCIAL MEDIA ENGAGEMENT ANALYSIS
-- SQL Business Queries
-- Author: Your Name | 2024
-- ════════════════════════════════════════════════════

-- ── SETUP ───────────────────────────────────────────
CREATE DATABASE IF NOT EXISTS social_media_db;
USE social_media_db;

CREATE TABLE IF NOT EXISTS social_media (
    id               INT AUTO_INCREMENT PRIMARY KEY,
    username         VARCHAR(100),
    platform         VARCHAR(50),
    content_type     VARCHAR(50),
    category         VARCHAR(50),
    country          VARCHAR(50),
    influencer_tier  VARCHAR(20),
    followers        BIGINT,
    following        INT,
    posts            INT,
    avg_likes        INT,
    avg_comments     INT,
    avg_shares       INT,
    avg_views        INT,
    engagement_rate  FLOAT,
    date_joined      DATE
);

-- NOTE: Import cleaned_data.csv into this table
-- MySQL: LOAD DATA INFILE 'cleaned_data.csv'
-- INTO TABLE social_media
-- FIELDS TERMINATED BY ','
-- IGNORE 1 ROWS;

-- ════════════════════════════════════════════════════
-- Q1: Which platform has highest avg engagement?
-- ════════════════════════════════════════════════════
SELECT
    platform,
    ROUND(AVG(engagement_rate), 2) AS avg_engagement,
    COUNT(*)                        AS total_accounts,
    ROUND(AVG(followers), 0)        AS avg_followers
FROM social_media
GROUP BY platform
ORDER BY avg_engagement DESC;

-- ════════════════════════════════════════════════════
-- Q2: Which content type performs best?
-- ════════════════════════════════════════════════════
SELECT
    content_type,
    ROUND(AVG(engagement_rate), 2) AS avg_engagement,
    COUNT(*)                        AS total_posts,
    ROUND(AVG(avg_likes), 0)        AS avg_likes
FROM social_media
GROUP BY content_type
ORDER BY avg_engagement DESC;

-- ════════════════════════════════════════════════════
-- Q3: Influencer tier comparison
-- ════════════════════════════════════════════════════
SELECT
    influencer_tier,
    COUNT(*)                        AS total_accounts,
    ROUND(AVG(engagement_rate), 2) AS avg_engagement,
    ROUND(AVG(avg_likes), 0)        AS avg_likes,
    ROUND(AVG(followers), 0)        AS avg_followers
FROM social_media
GROUP BY influencer_tier
ORDER BY avg_engagement DESC;

-- ════════════════════════════════════════════════════
-- Q4: Top 10 countries by engagement
-- ════════════════════════════════════════════════════
SELECT
    country,
    COUNT(*)                        AS accounts,
    ROUND(AVG(engagement_rate), 2) AS avg_engagement,
    ROUND(AVG(followers)/1000, 1)  AS avg_followers_k
FROM social_media
WHERE country != 'Unknown'
GROUP BY country
HAVING COUNT(*) > 10
ORDER BY avg_engagement DESC
LIMIT 10;

-- ════════════════════════════════════════════════════
-- Q5: Best platform + content type combination
-- ════════════════════════════════════════════════════
SELECT
    platform,
    content_type,
    ROUND(AVG(engagement_rate), 2) AS avg_engagement,
    COUNT(*)                        AS count
FROM social_media
GROUP BY platform, content_type
ORDER BY avg_engagement DESC
LIMIT 10;

-- ════════════════════════════════════════════════════
-- Q6: Accounts with high followers but low engagement
-- (Fake influencer detection)
-- ════════════════════════════════════════════════════
SELECT
    username,
    platform,
    followers,
    ROUND(engagement_rate, 2) AS engagement_rate,
    CASE
        WHEN engagement_rate < 1 THEN '🚨 Very Suspicious'
        WHEN engagement_rate < 2 THEN '⚠️  Suspicious'
        ELSE '✅ Normal'
    END AS status
FROM social_media
WHERE followers > 100000
  AND engagement_rate < 2
ORDER BY followers DESC
LIMIT 20;

-- ════════════════════════════════════════════════════
-- Q7: Category performance ranking
-- ════════════════════════════════════════════════════
SELECT
    category,
    ROUND(AVG(engagement_rate), 2) AS avg_engagement,
    COUNT(*)                        AS accounts,
    ROUND(AVG(avg_likes), 0)        AS avg_likes
FROM social_media
GROUP BY category
ORDER BY avg_engagement DESC;

-- ════════════════════════════════════════════════════
-- Q8: Complete platform summary dashboard
-- ════════════════════════════════════════════════════
SELECT
    platform,
    COUNT(*)                        AS total_accounts,
    ROUND(MIN(engagement_rate), 2) AS min_eng,
    ROUND(MAX(engagement_rate), 2) AS max_eng,
    ROUND(AVG(engagement_rate), 2) AS avg_eng,
    ROUND(AVG(avg_likes), 0)        AS avg_likes,
    ROUND(AVG(followers)/1000, 1)  AS avg_followers_k
FROM social_media
GROUP BY platform
ORDER BY avg_eng DESC;
