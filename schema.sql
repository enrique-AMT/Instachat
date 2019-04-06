--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.14
-- Dumped by pg_dump version 9.5.14

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: instachat; Type: SCHEMA; Schema: -; Owner: instadev
--

CREATE SCHEMA instachat;


ALTER SCHEMA instachat OWNER TO instadev;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: belongs; Type: TABLE; Schema: instachat; Owner: instadev
--

CREATE TABLE instachat.belongs (
    chat_id integer NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE instachat.belongs OWNER TO instadev;

--
-- Name: chat; Type: TABLE; Schema: instachat; Owner: instadev
--

CREATE TABLE instachat.chat (
    chat_id integer NOT NULL,
    chat_name character varying(20),
    owner_id integer
);


ALTER TABLE instachat.chat OWNER TO instadev;

--
-- Name: has_hashtag; Type: TABLE; Schema: instachat; Owner: instadev
--

CREATE TABLE instachat.has_hashtag (
    post_id integer NOT NULL,
    hashtag_id integer NOT NULL
);


ALTER TABLE instachat.has_hashtag OWNER TO instadev;

--
-- Name: hashtag; Type: TABLE; Schema: instachat; Owner: instadev
--

CREATE TABLE instachat.hashtag (
    hashtag_id integer NOT NULL,
    hash_name character varying(128)
);


ALTER TABLE instachat.hashtag OWNER TO instadev;

--
-- Name: image; Type: TABLE; Schema: instachat; Owner: instadev
--

CREATE TABLE instachat.image (
    image_id integer NOT NULL,
    image_file character varying(128)
);


ALTER TABLE instachat.image OWNER TO instadev;

--
-- Name: phone; Type: TABLE; Schema: instachat; Owner: instadev
--

CREATE TABLE instachat.phone (
    phone_id integer NOT NULL,
    user_id integer,
    phone character(10)
);


ALTER TABLE instachat.phone OWNER TO instadev;

--
-- Name: post; Type: TABLE; Schema: instachat; Owner: instadev
--

CREATE TABLE instachat.post (
    post_id integer NOT NULL,
    post_caption character varying(280),
    post_date character varying(10)
);


ALTER TABLE instachat.post OWNER TO instadev;

--
-- Name: react; Type: TABLE; Schema: instachat; Owner: instadev
--

CREATE TABLE instachat.react (
    react_id integer NOT NULL,
    react_type character varying(7),
    react_date character(10),
    user_that_reacted integer,
    p_reacted integer,
    reply_reacted integer
);


ALTER TABLE instachat.react OWNER TO instadev;

--
-- Name: react_react_id_seq; Type: SEQUENCE; Schema: instachat; Owner: instadev
--

CREATE SEQUENCE instachat.react_react_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE instachat.react_react_id_seq OWNER TO instadev;

--
-- Name: react_react_id_seq; Type: SEQUENCE OWNED BY; Schema: instachat; Owner: instadev
--

ALTER SEQUENCE instachat.react_react_id_seq OWNED BY instachat.react.react_id;


--
-- Name: reply; Type: TABLE; Schema: instachat; Owner: instadev
--

CREATE TABLE instachat.reply (
    reply_id integer NOT NULL,
    reply_date character(10),
    reply_text character varying(250),
    p_replied integer
);


ALTER TABLE instachat.reply OWNER TO instadev;

--
-- Name: reply_reply_id_seq; Type: SEQUENCE; Schema: instachat; Owner: instadev
--

CREATE SEQUENCE instachat.reply_reply_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE instachat.reply_reply_id_seq OWNER TO instadev;

--
-- Name: reply_reply_id_seq; Type: SEQUENCE OWNED BY; Schema: instachat; Owner: instadev
--

ALTER SEQUENCE instachat.reply_reply_id_seq OWNED BY instachat.reply.reply_id;


--
-- Name: u_contacts; Type: TABLE; Schema: instachat; Owner: instadev
--

CREATE TABLE instachat.u_contacts (
    user_id integer NOT NULL,
    contact_id integer NOT NULL
);


ALTER TABLE instachat.u_contacts OWNER TO instadev;

--
-- Name: user; Type: TABLE; Schema: instachat; Owner: instadev
--

CREATE TABLE instachat."user" (
    user_id integer NOT NULL,
    first_name character varying(20),
    last_name character varying(20),
    u_email_address character varying(20) NOT NULL,
    u_password character varying(72) NOT NULL
);


ALTER TABLE instachat."user" OWNER TO instadev;

--
-- Name: chats; Type: TABLE; Schema: public; Owner: instadev
--

CREATE TABLE public.chats (
    chat_id integer NOT NULL,
    chat_name character varying(20),
    number_of_users integer,
    user_id character varying(200),
    active_user_count integer,
    owner_id integer
);


ALTER TABLE public.chats OWNER TO instadev;

--
-- Name: post; Type: TABLE; Schema: public; Owner: instadev
--

CREATE TABLE public.post (
    post_id integer NOT NULL,
    post_caption character varying(280),
    post_date character varying(10)
);


ALTER TABLE public.post OWNER TO instadev;

--
-- Name: react_id; Type: DEFAULT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.react ALTER COLUMN react_id SET DEFAULT nextval('instachat.react_react_id_seq'::regclass);


--
-- Name: reply_id; Type: DEFAULT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.reply ALTER COLUMN reply_id SET DEFAULT nextval('instachat.reply_reply_id_seq'::regclass);


--
-- Data for Name: belongs; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.belongs (chat_id, user_id) FROM stdin;
\.


--
-- Data for Name: chat; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.chat (chat_id, chat_name, owner_id) FROM stdin;
1	hello	1
\.


--
-- Data for Name: has_hashtag; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.has_hashtag (post_id, hashtag_id) FROM stdin;
1	1
\.


--
-- Data for Name: hashtag; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.hashtag (hashtag_id, hash_name) FROM stdin;
1	mecolgue
\.


--
-- Data for Name: image; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.image (image_id, image_file) FROM stdin;
1	hola.png
\.


--
-- Data for Name: phone; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.phone (phone_id, user_id, phone) FROM stdin;
1	1	7873830072
\.


--
-- Data for Name: post; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.post (post_id, post_caption, post_date) FROM stdin;
1	jajaja este test	4/1/2019
2	sin imagen	4/1/2019
\.


--
-- Data for Name: react; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.react (react_id, react_type, react_date, user_that_reacted, p_reacted, reply_reacted) FROM stdin;
1	like	01-01-2000	4	1	1
2	dislike	01-01-2000	1	1	1
\.


--
-- Name: react_react_id_seq; Type: SEQUENCE SET; Schema: instachat; Owner: instadev
--

SELECT pg_catalog.setval('instachat.react_react_id_seq', 2, true);


--
-- Data for Name: reply; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.reply (reply_id, reply_date, reply_text, p_replied) FROM stdin;
1	04-06-2019	jajaja brutal el test	1
2	04-01-2019	no enviaron na	1
3	04-01-2019	seguiremos esperando	1
4	04-01-2019	pon la imagen entonces	2
\.


--
-- Name: reply_reply_id_seq; Type: SEQUENCE SET; Schema: instachat; Owner: instadev
--

SELECT pg_catalog.setval('instachat.reply_reply_id_seq', 4, true);


--
-- Data for Name: u_contacts; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.u_contacts (user_id, contact_id) FROM stdin;
1	2
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat."user" (user_id, first_name, last_name, u_email_address, u_password) FROM stdin;
1	Pedro	Rivera	p.rivera@upr.edu	jaja saludos
3	Juan	Lopez	juan.lopez32@upr.edu	testing1212
4	Bienvenido	Velez	bienvenido.velez@upr	java2020
2	Amir	Chinaei	amir.chinaei@upr.edu	nosvemos
\.


--
-- Data for Name: chats; Type: TABLE DATA; Schema: public; Owner: instadev
--

COPY public.chats (chat_id, chat_name, number_of_users, user_id, active_user_count, owner_id) FROM stdin;
1	testing	5	[Pedrito, Manuel, Bienve, Wilson, Amir]	4	283
\.


--
-- Data for Name: post; Type: TABLE DATA; Schema: public; Owner: instadev
--

COPY public.post (post_id, post_caption, post_date) FROM stdin;
1	sin imagen	4/1/2019
\.


--
-- Name: belongs_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.belongs
    ADD CONSTRAINT belongs_pkey PRIMARY KEY (user_id, chat_id);


--
-- Name: chat_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.chat
    ADD CONSTRAINT chat_pkey PRIMARY KEY (chat_id);


--
-- Name: has_hashtag_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.has_hashtag
    ADD CONSTRAINT has_hashtag_pkey PRIMARY KEY (post_id, hashtag_id);


--
-- Name: hashtag_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.hashtag
    ADD CONSTRAINT hashtag_pkey PRIMARY KEY (hashtag_id);


--
-- Name: image_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.image
    ADD CONSTRAINT image_pkey PRIMARY KEY (image_id);


--
-- Name: phone_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.phone
    ADD CONSTRAINT phone_pkey PRIMARY KEY (phone_id);


--
-- Name: post_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.post
    ADD CONSTRAINT post_pkey PRIMARY KEY (post_id);


--
-- Name: react_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.react
    ADD CONSTRAINT react_pkey PRIMARY KEY (react_id);


--
-- Name: reply_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.reply
    ADD CONSTRAINT reply_pkey PRIMARY KEY (reply_id);


--
-- Name: u_contacts_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.u_contacts
    ADD CONSTRAINT u_contacts_pkey PRIMARY KEY (user_id, contact_id);


--
-- Name: user_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_id);


--
-- Name: user_u_email_address_key; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat."user"
    ADD CONSTRAINT user_u_email_address_key UNIQUE (u_email_address);


--
-- Name: chats_pkey; Type: CONSTRAINT; Schema: public; Owner: instadev
--

ALTER TABLE ONLY public.chats
    ADD CONSTRAINT chats_pkey PRIMARY KEY (chat_id);


--
-- Name: post_pkey; Type: CONSTRAINT; Schema: public; Owner: instadev
--

ALTER TABLE ONLY public.post
    ADD CONSTRAINT post_pkey PRIMARY KEY (post_id);


--
-- Name: belongs_chat_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.belongs
    ADD CONSTRAINT belongs_chat_id_fkey FOREIGN KEY (chat_id) REFERENCES instachat.chat(chat_id);


--
-- Name: belongs_user_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.belongs
    ADD CONSTRAINT belongs_user_id_fkey FOREIGN KEY (user_id) REFERENCES instachat."user"(user_id);


--
-- Name: chat_owner_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.chat
    ADD CONSTRAINT chat_owner_id_fkey FOREIGN KEY (owner_id) REFERENCES instachat."user"(user_id);


--
-- Name: has_hashtag_hashtag_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.has_hashtag
    ADD CONSTRAINT has_hashtag_hashtag_id_fkey FOREIGN KEY (hashtag_id) REFERENCES instachat.hashtag(hashtag_id);


--
-- Name: has_hashtag_post_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.has_hashtag
    ADD CONSTRAINT has_hashtag_post_id_fkey FOREIGN KEY (post_id) REFERENCES instachat.post(post_id);


--
-- Name: phone_user_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.phone
    ADD CONSTRAINT phone_user_id_fkey FOREIGN KEY (user_id) REFERENCES instachat."user"(user_id);


--
-- Name: react_p_reacted_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.react
    ADD CONSTRAINT react_p_reacted_fkey FOREIGN KEY (p_reacted) REFERENCES instachat.post(post_id);


--
-- Name: react_reply_reacted_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.react
    ADD CONSTRAINT react_reply_reacted_fkey FOREIGN KEY (reply_reacted) REFERENCES instachat.react(react_id);


--
-- Name: react_user_that_reacted_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.react
    ADD CONSTRAINT react_user_that_reacted_fkey FOREIGN KEY (user_that_reacted) REFERENCES instachat."user"(user_id);


--
-- Name: reply_p_replied_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.reply
    ADD CONSTRAINT reply_p_replied_fkey FOREIGN KEY (p_replied) REFERENCES instachat.post(post_id);


--
-- Name: u_contacts_contact_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.u_contacts
    ADD CONSTRAINT u_contacts_contact_id_fkey FOREIGN KEY (contact_id) REFERENCES instachat."user"(user_id);


--
-- Name: u_contacts_user_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.u_contacts
    ADD CONSTRAINT u_contacts_user_id_fkey FOREIGN KEY (user_id) REFERENCES instachat."user"(user_id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

