--
-- PostgreSQL database dump
--

-- Dumped from database version 10.6 (Ubuntu 10.6-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.6 (Ubuntu 10.6-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
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
    u_belongs integer NOT NULL,
    c_user_belongs integer NOT NULL
);


ALTER TABLE instachat.belongs OWNER TO instadev;

--
-- Name: chat; Type: TABLE; Schema: instachat; Owner: instadev
--

CREATE TABLE instachat.chat (
    chat_id integer NOT NULL,
    chat_name character varying(30),
    owner_id integer
);


ALTER TABLE instachat.chat OWNER TO instadev;

--
-- Name: chat_chat_id_seq; Type: SEQUENCE; Schema: instachat; Owner: instadev
--

CREATE SEQUENCE instachat.chat_chat_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE instachat.chat_chat_id_seq OWNER TO instadev;

--
-- Name: chat_chat_id_seq; Type: SEQUENCE OWNED BY; Schema: instachat; Owner: instadev
--

ALTER SEQUENCE instachat.chat_chat_id_seq OWNED BY instachat.chat.chat_id;


--
-- Name: has_hashtag; Type: TABLE; Schema: instachat; Owner: instadev
--

CREATE TABLE instachat.has_hashtag (
    hashtag_id integer NOT NULL,
    p_with_hashtag integer NOT NULL
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
    image_file character varying(200),
    p_with_image integer
);


ALTER TABLE instachat.image OWNER TO instadev;

--
-- Name: image_image_id_seq; Type: SEQUENCE; Schema: instachat; Owner: instadev
--

CREATE SEQUENCE instachat.image_image_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE instachat.image_image_id_seq OWNER TO instadev;

--
-- Name: image_image_id_seq; Type: SEQUENCE OWNED BY; Schema: instachat; Owner: instadev
--

ALTER SEQUENCE instachat.image_image_id_seq OWNED BY instachat.image.image_id;


--
-- Name: phone; Type: TABLE; Schema: instachat; Owner: instadev
--

CREATE TABLE instachat.phone (
    phone_id integer NOT NULL,
    u_phone integer,
    phone character(10)
);


ALTER TABLE instachat.phone OWNER TO instadev;

--
-- Name: phone_phone_id_seq; Type: SEQUENCE; Schema: instachat; Owner: instadev
--

CREATE SEQUENCE instachat.phone_phone_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE instachat.phone_phone_id_seq OWNER TO instadev;

--
-- Name: phone_phone_id_seq; Type: SEQUENCE OWNED BY; Schema: instachat; Owner: instadev
--

ALTER SEQUENCE instachat.phone_phone_id_seq OWNED BY instachat.phone.phone_id;


--
-- Name: post_post_id_seq; Type: SEQUENCE; Schema: instachat; Owner: instadev
--

CREATE SEQUENCE instachat.post_post_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE instachat.post_post_id_seq OWNER TO instadev;

--
-- Name: post_post_id_seq; Type: SEQUENCE OWNED BY; Schema: instachat; Owner: instadev
--

ALTER SEQUENCE instachat.post_post_id_seq OWNED BY instachat.phone.phone_id;


--
-- Name: post; Type: TABLE; Schema: instachat; Owner: instadev
--

CREATE TABLE instachat.post (
    post_caption character varying(280),
    post_date character varying(10),
    p_created_by integer,
    c_post_belongs integer,
    post_id integer DEFAULT nextval('instachat.post_post_id_seq'::regclass) NOT NULL
);


ALTER TABLE instachat.post OWNER TO instadev;

--
-- Name: react; Type: TABLE; Schema: instachat; Owner: instadev
--

CREATE TABLE instachat.react (
    react_id integer NOT NULL,
    react_type character varying(7),
    react_date character(10),
    user_that_react integer,
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
    contact_of integer NOT NULL
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
-- Name: chat chat_id; Type: DEFAULT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.chat ALTER COLUMN chat_id SET DEFAULT nextval('instachat.chat_chat_id_seq'::regclass);


--
-- Name: image image_id; Type: DEFAULT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.image ALTER COLUMN image_id SET DEFAULT nextval('instachat.image_image_id_seq'::regclass);


--
-- Name: phone phone_id; Type: DEFAULT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.phone ALTER COLUMN phone_id SET DEFAULT nextval('instachat.phone_phone_id_seq'::regclass);


--
-- Name: react react_id; Type: DEFAULT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.react ALTER COLUMN react_id SET DEFAULT nextval('instachat.react_react_id_seq'::regclass);


--
-- Name: reply reply_id; Type: DEFAULT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.reply ALTER COLUMN reply_id SET DEFAULT nextval('instachat.reply_reply_id_seq'::regclass);


--
-- Data for Name: belongs; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.belongs (u_belongs, c_user_belongs) FROM stdin;
1	2
2	1
3	1
4	1
1	1
\.


--
-- Data for Name: chat; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.chat (chat_id, chat_name, owner_id) FROM stdin;
1	work	4
2	macaracachimbas	1
\.


--
-- Data for Name: has_hashtag; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.has_hashtag (hashtag_id, p_with_hashtag) FROM stdin;
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

COPY instachat.image (image_id, image_file, p_with_image) FROM stdin;
1	hola.png	1
2	hola2.png	3
\.


--
-- Data for Name: phone; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.phone (phone_id, u_phone, phone) FROM stdin;
1	1	7873830072
2	2	9393522252
\.


--
-- Data for Name: post; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.post (post_caption, post_date, p_created_by, c_post_belongs, post_id) FROM stdin;
A colgar a unos cuantos!	04-01-2019	3	1	1
Dale si!	04-01-2019	2	1	2
test	04/07/2019	1	1	3
testing jaja	04-01-2019	1	1	4
\.


--
-- Data for Name: react; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.react (react_id, react_type, react_date, user_that_react, p_reacted, reply_reacted) FROM stdin;
1	like	04-04-2019	1	2	\N
2	dislike	05-05-2020	3	2	\N
3	like	03-03-2019	4	1	\N
4	like	03-10-2018	3	1	\N
5	like	03-10-2018	1	1	\N
6	dislike	12-15-2017	2	1	\N
7	dislike	12-15-2015	4	2	\N
\.


--
-- Data for Name: reply; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.reply (reply_id, reply_date, reply_text, p_replied) FROM stdin;
\.


--
-- Data for Name: u_contacts; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.u_contacts (user_id, contact_of) FROM stdin;
2	1
3	1
4	1
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
-- Name: chat_chat_id_seq; Type: SEQUENCE SET; Schema: instachat; Owner: instadev
--

SELECT pg_catalog.setval('instachat.chat_chat_id_seq', 2, true);


--
-- Name: image_image_id_seq; Type: SEQUENCE SET; Schema: instachat; Owner: instadev
--

SELECT pg_catalog.setval('instachat.image_image_id_seq', 2, true);


--
-- Name: phone_phone_id_seq; Type: SEQUENCE SET; Schema: instachat; Owner: instadev
--

SELECT pg_catalog.setval('instachat.phone_phone_id_seq', 2, true);


--
-- Name: post_post_id_seq; Type: SEQUENCE SET; Schema: instachat; Owner: instadev
--

SELECT pg_catalog.setval('instachat.post_post_id_seq', 4, true);


--
-- Name: react_react_id_seq; Type: SEQUENCE SET; Schema: instachat; Owner: instadev
--

SELECT pg_catalog.setval('instachat.react_react_id_seq', 7, true);


--
-- Name: reply_reply_id_seq; Type: SEQUENCE SET; Schema: instachat; Owner: instadev
--

SELECT pg_catalog.setval('instachat.reply_reply_id_seq', 1, false);


--
-- Name: belongs belongs_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.belongs
    ADD CONSTRAINT belongs_pkey PRIMARY KEY (u_belongs, c_user_belongs);


--
-- Name: chat chat_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.chat
    ADD CONSTRAINT chat_pkey PRIMARY KEY (chat_id);


--
-- Name: has_hashtag has_hashtag_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.has_hashtag
    ADD CONSTRAINT has_hashtag_pkey PRIMARY KEY (hashtag_id, p_with_hashtag);


--
-- Name: hashtag hashtag_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.hashtag
    ADD CONSTRAINT hashtag_pkey PRIMARY KEY (hashtag_id);


--
-- Name: image image_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.image
    ADD CONSTRAINT image_pkey PRIMARY KEY (image_id);


--
-- Name: phone phone_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.phone
    ADD CONSTRAINT phone_pkey PRIMARY KEY (phone_id);


--
-- Name: post post_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.post
    ADD CONSTRAINT post_pkey PRIMARY KEY (post_id);


--
-- Name: react react_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.react
    ADD CONSTRAINT react_pkey PRIMARY KEY (react_id);


--
-- Name: reply reply_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.reply
    ADD CONSTRAINT reply_pkey PRIMARY KEY (reply_id);


--
-- Name: u_contacts u_contacts_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.u_contacts
    ADD CONSTRAINT u_contacts_pkey PRIMARY KEY (user_id, contact_of);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_id);


--
-- Name: user user_u_email_address_key; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat."user"
    ADD CONSTRAINT user_u_email_address_key UNIQUE (u_email_address);


--
-- Name: chats chats_pkey; Type: CONSTRAINT; Schema: public; Owner: instadev
--

ALTER TABLE ONLY public.chats
    ADD CONSTRAINT chats_pkey PRIMARY KEY (chat_id);


--
-- Name: post post_pkey; Type: CONSTRAINT; Schema: public; Owner: instadev
--

ALTER TABLE ONLY public.post
    ADD CONSTRAINT post_pkey PRIMARY KEY (post_id);


--
-- Name: belongs belongs_c_user_belongs_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.belongs
    ADD CONSTRAINT belongs_c_user_belongs_fkey FOREIGN KEY (c_user_belongs) REFERENCES instachat.chat(chat_id);


--
-- Name: belongs belongs_u_belongs_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.belongs
    ADD CONSTRAINT belongs_u_belongs_fkey FOREIGN KEY (u_belongs) REFERENCES instachat."user"(user_id);


--
-- Name: chat chat_owner_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.chat
    ADD CONSTRAINT chat_owner_id_fkey FOREIGN KEY (owner_id) REFERENCES instachat."user"(user_id);


--
-- Name: has_hashtag has_hashtag_hashtag_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.has_hashtag
    ADD CONSTRAINT has_hashtag_hashtag_id_fkey FOREIGN KEY (hashtag_id) REFERENCES instachat.hashtag(hashtag_id);


--
-- Name: has_hashtag has_hashtag_p_with_hashtag_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.has_hashtag
    ADD CONSTRAINT has_hashtag_p_with_hashtag_fkey FOREIGN KEY (p_with_hashtag) REFERENCES instachat.post(post_id);


--
-- Name: image image_p_with_image_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.image
    ADD CONSTRAINT image_p_with_image_fkey FOREIGN KEY (p_with_image) REFERENCES instachat.post(post_id);


--
-- Name: phone phone_u_phone_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.phone
    ADD CONSTRAINT phone_u_phone_fkey FOREIGN KEY (u_phone) REFERENCES instachat."user"(user_id);


--
-- Name: post post_c_post_belongs_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.post
    ADD CONSTRAINT post_c_post_belongs_fkey FOREIGN KEY (c_post_belongs) REFERENCES instachat.chat(chat_id);


--
-- Name: post post_p_created_by_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.post
    ADD CONSTRAINT post_p_created_by_fkey FOREIGN KEY (p_created_by) REFERENCES instachat."user"(user_id);


--
-- Name: react react_p_reacted_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.react
    ADD CONSTRAINT react_p_reacted_fkey FOREIGN KEY (p_reacted) REFERENCES instachat.post(post_id);


--
-- Name: react react_r_reacted_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.react
    ADD CONSTRAINT react_r_reacted_fkey FOREIGN KEY (reply_reacted) REFERENCES instachat.reply(reply_id);


--
-- Name: react react_u_that_react_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.react
    ADD CONSTRAINT react_u_that_react_fkey FOREIGN KEY (user_that_react) REFERENCES instachat."user"(user_id);


--
-- Name: reply reply_p_replied_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.reply
    ADD CONSTRAINT reply_p_replied_fkey FOREIGN KEY (p_replied) REFERENCES instachat.post(post_id);


--
-- Name: u_contacts u_contacts_contact_of_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.u_contacts
    ADD CONSTRAINT u_contacts_contact_of_fkey FOREIGN KEY (contact_of) REFERENCES instachat."user"(user_id);


--
-- Name: u_contacts u_contacts_user_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.u_contacts
    ADD CONSTRAINT u_contacts_user_id_fkey FOREIGN KEY (user_id) REFERENCES instachat."user"(user_id);


--
-- PostgreSQL database dump complete
--

