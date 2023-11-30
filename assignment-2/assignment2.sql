
CREATE TABLE query1 AS
SELECT COUNT(*)
AS "count of comments"
FROM comments
WHERE author = 'xymemez';


CREATE TABLE query2 AS
SELECT 
subreddit_type AS "subreddit type",
COUNT(subreddit_type) AS "subreddit count" 
FROM subreddits
group by subreddit_type;


CREATE TABLE query3 AS
SELECT subreddit AS name,
COUNT(subreddit) AS "comments count",
ROUND(AVG(score),2) AS "average score"
FROM comments
GROUP BY subreddit
ORDER BY "comments count" DESC LIMIT 10;



CREATE TABLE query4 AS
SELECT name, 
link_karma AS "link karma",
comment_karma AS "comment karma",
CASE WHEN link_karma>=comment_karma THEN 1 ELSE 0 END "label"
FROM authors
WHERE (comment_karma+link_karma)/2 >= 1000000
ORDER BY (comment_karma+link_karma)/2 desc;


CREATE TABLE query5 AS
SELECT s_table.subreddit_type AS "sr type", SUM(c_table.num) AS "comments num"
FROM
	(SELECT subreddit,
	COUNT(author) AS "num"
	FROM comments
	WHERE author = '[deleted_user]'
	GROUP BY subreddit) c_table
JOIN
	(SELECT display_name, subreddit_type
	FROM subreddits) s_table
ON
	(c_table.subreddit = s_table.display_name)
GROUP BY s_table.subreddit_type;


CREATE TABLE query6 AS
SELECT to_char(to_timestamp(created_utc), 'YYYY-MM-DD hh24:mi:ss') AS "utc time", subreddit, body AS "comment"
FROM comments
WHERE author = 'xymemez' and subreddit = 'starcraft';


CREATE TABLE query7 AS
SELECT submission,
ups,
subreddit
FROM(
SELECT m_table.title AS "submission", 
m_table.ups AS ups,
row_number() OVER (PARTITION BY s_table.name ORDER BY m_table.ups DESC),
s_table.display_name AS "subreddit"
FROM	
	(SELECT name, display_name
	FROM subreddits
	WHERE over18='false'
	ORDER BY created_utc ASC LIMIT 4) s_table
JOIN
	(SELECT ups, subreddit_id, title
	FROM submissions) m_table
ON
	(s_table.name = m_table.subreddit_id )
) a 
WHERE row_number <= 4 ;


CREATE TABLE query8 AS
SELECT author, ups
FROM (
	SELECT author, ups, 
	RANK() OVER(ORDER BY ups) AS min,
	RANK() OVER(ORDER BY ups desc) AS max
	FROM comments
) t
WHERE 1 in (min, max);


CREATE TABLE query9 AS
SELECT  to_char(to_timestamp(created_utc), 'YYYY-MM-DD') AS data, count(extract(day FROM to_timestamp(created_utc))) AS day
FROM comments
WHERE author = 'xymemez'
GROUP BY data;



CREATE TABLE query10 AS
SELECT (extract(month FROM to_timestamp(created_utc))) AS month, subreddit, COUNT(subreddit) AS "count"
FROM comments
WHERE (extract(month FROM to_timestamp(created_utc))) IN 
	(SELECT extract(month FROM to_timestamp(created_utc)) AS "month"
	FROM comments
	GROUP BY month
	ORDER BY count(extract(month FROM to_timestamp(created_utc))) desc LIMIT 1)
GROUP BY month, subreddit
ORDER BY count DESC LIMIT 10;
