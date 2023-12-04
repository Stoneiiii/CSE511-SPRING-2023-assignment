# Introduction & Background

In Assignment 1, you learned how to design and load a database. The assignment gave you an opportunity to create a database from scratch and perform optimized data insertion. Assignment 2 has the same background information as Assignment 1, and this will help you to understand how to make different queries to the tables we created in Assignment 1, and also give you the opportunity to explore how 2 queries with different clauses can have a very different impact on execution time as well. For this assignment, we will use the tables you created as a part of Assignment 1.

# Problem Statement

Considering the four created tables submissions, comments, author and subreddit, from Assignment 1. Your task is to implement the following SQL queries
1. query1: Write a SQL query to return the total number of comments authored by the user `xymemez` .
    1. Your column names MUST be: ‘count of comments’
2. query2: Write a SQL query to return the total number of subreddits for each subreddit
type.
    1. Your column names MUST be: ‘subreddit type’, ‘subreddit count’
3. query3: Write a SQL query to return the top 10 subreddits arranged by the number of comments. Calculate average score for each of these subreddits and round it to 2 decimal places.
    1. Your column names MUST be: ‘name’, ‘comments count’, ‘average score’
4. query4: Write a SQL query to print name, link_karma, comment_karma for users with >1,000,000 average karma in descending order. Additionally, also have a column ‘ label ’ which shows 1 if the link_karma >= comment_karma , else 0
    1. Your column names MUST be: ‘name’, ‘link karma’, ‘comment karma’, ‘label’
    2. You can write this query with both having and where clauses (both will be considered correct and submit only one), however, try doing both just to see the speed difference. (if you do try it) let us know the results in the README along with your theory for why!
    3. To fairly compare times between 2 queries, you need to clear the postgres cache! A helpful link: [See and clear Postgres caches/buffers? - Stack Overflow](https://stackoverflow.com/questions/1216660/see-and-clear-postgres-caches-buffers)
5. query5: Write a SQL query to give count of comments in subreddit types where the user has commented. Write this query for the user `[deleted_user]`
    1. Your column names MUST be: ‘sr type’, ‘comments num’
6. query6: Write a SQL query to print the datetime (UTC format) of the created time of comments, subreddit name and comments for the user `xymemez` in the subreddit ` starcraft`
    1. Your column names MUST be: ‘utc time’, ‘subreddit’, ‘comment’
7. query7: Write a SQL query to get the 4 most upped submissions (if any) from the 4 oldest under 18 subreddits
    1. Your column names MUST be: ‘submission’, ‘ups’, ‘subreddit’
    2. Using posgres functions might be a good idea for this!
8. query8: Write a SQL query to get the author and ups for the most upvoted and least upvoted comment on reddit.
    1. Your column names MUST be: ‘author’, ‘upvotes’
    2. Sub-queries or temp tables are a great option for such questions
9. query9: Write a SQL query to display the number of comments made by the author, `xymemez` according to the utc date arranged in ascending order.
    1. Your column names MUST be: ‘date’, ‘count’
10. query10: Write a SQL query to get the month when reddit was most active along with the 10 top subreddits and the number of posts in the subreddits in that month.
    1. Your column names MUST be: ‘month’, ‘subreddit’, ‘count’

Above all, your script MUST generate ten tables, namely, “query1”, “query2”, …, “query10” respectively for each query.
