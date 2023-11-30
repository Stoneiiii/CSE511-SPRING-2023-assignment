#!/bin/bash

#creat comments table
psql -U postgres -w -c "CREATE TABLE public.comments
(
    distinguished text,
    downs integer,
    created_utc integer,
    controversiality integer,
    edited boolean,
    gilded integer,
    author_flair_css_class text,
    id text,
    author text,
    retrieved_on integer,
    score_hidden boolean,
    subreddit_id text,
    score integer,
    name text,
    author_flair_text text,
    link_id text,
    archived boolean,
    ups integer,
    parent_id text,
    subreddit text,
    body text
);"

#creat authors table
psql -U postgres -w -c "CREATE TABLE public.authors
(
	id text,
	retrieved_on integer,
	name text,
	created_utc integer,
	link_karma integer,
	comment_karma integer,
	profile_img text,
	profile_color text,
	profile_over_18 boolean
);"

#creat submissions table
psql -U postgres -w -c "CREATE TABLE public.submissions
(
	downs integer,
	url text,
	id text,
	edited boolean,
	num_reports integer,
	created_utc integer,
	name text,
	title text,
	author text,
	permalink text,
	num_comments integer,
	likes boolean,
	subreddit_id text,
	ups integer
);"

#creat subreddits table
psql -U postgres -w -c "CREATE TABLE public.subreddits
(
	banner_background_image text,
	created_utc integer,
	description text,
	display_name text,
	header_img text,
	hide_ads boolean,
	id text,
	over18 boolean,
	public_description text,
	retrieved_utc integer,
	name text,
	subreddit_type text,
	subscribers integer,
	title text,
	whitelist_status text
);"


#Importing data by using pg_bulkload
pg_bulkload -i ./comments.csv -O comments  -o "TYPE=CSV" -o "DELIMITER=," -o "OFFSET=1" -d postgres -U postgres -w

pg_bulkload -i ./authors.csv -O authors  -o "TYPE=CSV" -o "DELIMITER=," -o "OFFSET=1" -d postgres -U postgres -w

pg_bulkload -i ./submissions.csv -O submissions  -o "TYPE=CSV" -o "DELIMITER=," -o "OFFSET=1" -d postgres -U postgres -w

pg_bulkload -i ./subreddits.csv -O subreddits  -o "TYPE=CSV" -o "DELIMITER=," -o "OFFSET=1" -d postgres -U postgres -w

psql -f assignment1.sql


