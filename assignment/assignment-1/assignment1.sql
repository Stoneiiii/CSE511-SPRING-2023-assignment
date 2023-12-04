
--set primary key
ALTER TABLE IF EXISTS public.authors
    ADD CONSTRAINT authors_pkey PRIMARY KEY (id);

ALTER TABLE IF EXISTS public.submissions
    ADD CONSTRAINT submissions_pkey PRIMARY KEY (id);
	
ALTER TABLE IF EXISTS public.subreddits
    ADD CONSTRAINT subreddits_pkey PRIMARY KEY (id);

ALTER TABLE IF EXISTS public.comments
    ADD CONSTRAINT comments_pkey PRIMARY KEY (id);

--set unique constraint	
alter table authors
add constraint unique_name unique(name);

--set foreign key
ALTER TABLE IF EXISTS public.comments
    ADD CONSTRAINT comments_fkey_author FOREIGN KEY (author)
    REFERENCES public.authors (name) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

ALTER TABLE IF EXISTS public.submissions
    ADD CONSTRAINT submissions_fkey_author FOREIGN KEY (author)
    REFERENCES public.authors (name) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

--set unique constraint
alter table subreddits
add constraint subr_unique_name unique(name);

--set unique constraint
alter table subreddits
add constraint subr_unique_d_name unique(display_name);

--set foreign key
ALTER TABLE IF EXISTS public.comments
    ADD CONSTRAINT comments_fkey_subr FOREIGN KEY (subreddit)
    REFERENCES public.subreddits (display_name) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;
	
ALTER TABLE IF EXISTS public.comments
    ADD CONSTRAINT comments_fkey_subr_id FOREIGN KEY (subreddit_id)
    REFERENCES public.subreddits (name) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;
	
ALTER TABLE IF EXISTS public.submissions
    ADD CONSTRAINT submissions_fkey_subr_id FOREIGN KEY (subreddit_id)
    REFERENCES public.subreddits (name) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

