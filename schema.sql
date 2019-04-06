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
    owner_id integer,
    number_of_users integer
);


ALTER TABLE instachat.chat OWNER TO instadev;

--
-- Name: chat_chat_id_seq; Type: SEQUENCE; Schema: instachat; Owner: instadev
--

CREATE SEQUENCE instachat.chat_chat_id_seq
    AS integer
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
-- Name: creates; Type: TABLE; Schema: instachat; Owner: instadev
--

CREATE TABLE instachat.creates (
    user_id integer NOT NULL,
    post_id integer NOT NULL
);


ALTER TABLE instachat.creates OWNER TO instadev;

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
-- Name: hashtag_hashtag_id_seq; Type: SEQUENCE; Schema: instachat; Owner: instadev
--

CREATE SEQUENCE instachat.hashtag_hashtag_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE instachat.hashtag_hashtag_id_seq OWNER TO instadev;

--
-- Name: hashtag_hashtag_id_seq; Type: SEQUENCE OWNED BY; Schema: instachat; Owner: instadev
--

ALTER SEQUENCE instachat.hashtag_hashtag_id_seq OWNED BY instachat.hashtag.hashtag_id;


--
-- Name: image; Type: TABLE; Schema: instachat; Owner: instadev
--

CREATE TABLE instachat.image (
    image_id integer NOT NULL,
    post_id integer,
    image_file character varying(256)
);


ALTER TABLE instachat.image OWNER TO instadev;

--
-- Name: image_image_id_seq; Type: SEQUENCE; Schema: instachat; Owner: instadev
--

CREATE SEQUENCE instachat.image_image_id_seq
    AS integer
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
    user_id integer,
    phone character(10)
);


ALTER TABLE instachat.phone OWNER TO instadev;

--
-- Name: phone_phone_id_seq; Type: SEQUENCE; Schema: instachat; Owner: instadev
--

CREATE SEQUENCE instachat.phone_phone_id_seq
    AS integer
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
-- Name: post; Type: TABLE; Schema: instachat; Owner: instadev
--

CREATE TABLE instachat.post (
    post_id integer NOT NULL,
    post_caption character varying(280),
    post_date character varying(10)
);


ALTER TABLE instachat.post OWNER TO instadev;

--
-- Name: post_belongs; Type: TABLE; Schema: instachat; Owner: instadev
--

CREATE TABLE instachat.post_belongs (
    chat_id integer NOT NULL,
    post_id integer NOT NULL
);


ALTER TABLE instachat.post_belongs OWNER TO instadev;

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

ALTER SEQUENCE instachat.post_post_id_seq OWNED BY instachat.post.post_id;


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
-- Name: user_user_id_seq; Type: SEQUENCE; Schema: instachat; Owner: instadev
--

CREATE SEQUENCE instachat.user_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE instachat.user_user_id_seq OWNER TO instadev;

--
-- Name: user_user_id_seq; Type: SEQUENCE OWNED BY; Schema: instachat; Owner: instadev
--

ALTER SEQUENCE instachat.user_user_id_seq OWNED BY instachat."user".user_id;


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
-- Name: chats_chat_id_seq; Type: SEQUENCE; Schema: public; Owner: instadev
--

CREATE SEQUENCE public.chats_chat_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.chats_chat_id_seq OWNER TO instadev;

--
-- Name: chats_chat_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: instadev
--

ALTER SEQUENCE public.chats_chat_id_seq OWNED BY public.chats.chat_id;


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
-- Name: post_post_id_seq; Type: SEQUENCE; Schema: public; Owner: instadev
--

CREATE SEQUENCE public.post_post_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.post_post_id_seq OWNER TO instadev;

--
-- Name: post_post_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: instadev
--

ALTER SEQUENCE public.post_post_id_seq OWNED BY public.post.post_id;


--
-- Name: chat chat_id; Type: DEFAULT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.chat ALTER COLUMN chat_id SET DEFAULT nextval('instachat.chat_chat_id_seq'::regclass);


--
-- Name: hashtag hashtag_id; Type: DEFAULT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.hashtag ALTER COLUMN hashtag_id SET DEFAULT nextval('instachat.hashtag_hashtag_id_seq'::regclass);


--
-- Name: image image_id; Type: DEFAULT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.image ALTER COLUMN image_id SET DEFAULT nextval('instachat.image_image_id_seq'::regclass);


--
-- Name: phone phone_id; Type: DEFAULT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.phone ALTER COLUMN phone_id SET DEFAULT nextval('instachat.phone_phone_id_seq'::regclass);


--
-- Name: post post_id; Type: DEFAULT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.post ALTER COLUMN post_id SET DEFAULT nextval('instachat.post_post_id_seq'::regclass);


--
-- Name: user user_id; Type: DEFAULT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat."user" ALTER COLUMN user_id SET DEFAULT nextval('instachat.user_user_id_seq'::regclass);


--
-- Name: chats chat_id; Type: DEFAULT; Schema: public; Owner: instadev
--

ALTER TABLE ONLY public.chats ALTER COLUMN chat_id SET DEFAULT nextval('public.chats_chat_id_seq'::regclass);


--
-- Name: post post_id; Type: DEFAULT; Schema: public; Owner: instadev
--

ALTER TABLE ONLY public.post ALTER COLUMN post_id SET DEFAULT nextval('public.post_post_id_seq'::regclass);


--
-- Data for Name: belongs; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.belongs (chat_id, user_id) FROM stdin;
1	1
1	2
1	3
1	4
2	2
2	3
2	4
\.


--
-- Data for Name: chat; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.chat (chat_id, chat_name, owner_id, number_of_users) FROM stdin;
2	Sin Pedrito	4	3
1	hello	1	4
\.


--
-- Data for Name: creates; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.creates (user_id, post_id) FROM stdin;
1	1
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

COPY instachat.image (image_id, post_id, image_file) FROM stdin;
1	1	/static/hola.png
\.


--
-- Data for Name: phone; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.phone (phone_id, user_id, phone) FROM stdin;
1	1	7873830072
2	2	9392590242
3	3	9399999999
4	4	9399999999
\.


--
-- Data for Name: post; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.post (post_id, post_caption, post_date) FROM stdin;
1	jaja saludos	04/01/2019
2	sin imagen	04/01/2019
\.


--
-- Data for Name: post_belongs; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.post_belongs (chat_id, post_id) FROM stdin;
1	1
1	2
\.


--
-- Data for Name: u_contacts; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.u_contacts (user_id, contact_id) FROM stdin;
1	2
1	3
1	4
2	1
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
\.


--
-- Name: chat_chat_id_seq; Type: SEQUENCE SET; Schema: instachat; Owner: instadev
--

SELECT pg_catalog.setval('instachat.chat_chat_id_seq', 2, true);


--
-- Name: hashtag_hashtag_id_seq; Type: SEQUENCE SET; Schema: instachat; Owner: instadev
--

SELECT pg_catalog.setval('instachat.hashtag_hashtag_id_seq', 1, true);


--
-- Name: image_image_id_seq; Type: SEQUENCE SET; Schema: instachat; Owner: instadev
--

SELECT pg_catalog.setval('instachat.image_image_id_seq', 1, true);


--
-- Name: phone_phone_id_seq; Type: SEQUENCE SET; Schema: instachat; Owner: instadev
--

SELECT pg_catalog.setval('instachat.phone_phone_id_seq', 4, true);


--
-- Name: post_post_id_seq; Type: SEQUENCE SET; Schema: instachat; Owner: instadev
--

SELECT pg_catalog.setval('instachat.post_post_id_seq', 2, true);


--
-- Name: user_user_id_seq; Type: SEQUENCE SET; Schema: instachat; Owner: instadev
--

SELECT pg_catalog.setval('instachat.user_user_id_seq', 3, true);


--
-- Name: chats_chat_id_seq; Type: SEQUENCE SET; Schema: public; Owner: instadev
--

SELECT pg_catalog.setval('public.chats_chat_id_seq', 1, true);


--
-- Name: post_post_id_seq; Type: SEQUENCE SET; Schema: public; Owner: instadev
--

SELECT pg_catalog.setval('public.post_post_id_seq', 1, false);


--
-- Name: belongs belongs_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.belongs
    ADD CONSTRAINT belongs_pkey PRIMARY KEY (user_id, chat_id);


--
-- Name: chat chat_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.chat
    ADD CONSTRAINT chat_pkey PRIMARY KEY (chat_id);


--
-- Name: creates creates_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.creates
    ADD CONSTRAINT creates_pkey PRIMARY KEY (user_id, post_id);


--
-- Name: has_hashtag has_hashtag_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.has_hashtag
    ADD CONSTRAINT has_hashtag_pkey PRIMARY KEY (post_id, hashtag_id);


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
-- Name: post_belongs post_belongs_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.post_belongs
    ADD CONSTRAINT post_belongs_pkey PRIMARY KEY (chat_id, post_id);


--
-- Name: post post_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.post
    ADD CONSTRAINT post_pkey PRIMARY KEY (post_id);


--
-- Name: u_contacts u_contacts_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.u_contacts
    ADD CONSTRAINT u_contacts_pkey PRIMARY KEY (user_id, contact_id);


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
-- Name: belongs belongs_chat_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.belongs
    ADD CONSTRAINT belongs_chat_id_fkey FOREIGN KEY (chat_id) REFERENCES instachat.chat(chat_id);


--
-- Name: belongs belongs_user_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.belongs
    ADD CONSTRAINT belongs_user_id_fkey FOREIGN KEY (user_id) REFERENCES instachat."user"(user_id);


--
-- Name: chat chat_owner_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.chat
    ADD CONSTRAINT chat_owner_id_fkey FOREIGN KEY (owner_id) REFERENCES instachat."user"(user_id);


--
-- Name: creates creates_post_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.creates
    ADD CONSTRAINT creates_post_id_fkey FOREIGN KEY (post_id) REFERENCES instachat.post(post_id);


--
-- Name: creates creates_user_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.creates
    ADD CONSTRAINT creates_user_id_fkey FOREIGN KEY (user_id) REFERENCES instachat."user"(user_id);


--
-- Name: has_hashtag has_hashtag_hashtag_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.has_hashtag
    ADD CONSTRAINT has_hashtag_hashtag_id_fkey FOREIGN KEY (hashtag_id) REFERENCES instachat.hashtag(hashtag_id);


--
-- Name: has_hashtag has_hashtag_post_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.has_hashtag
    ADD CONSTRAINT has_hashtag_post_id_fkey FOREIGN KEY (post_id) REFERENCES instachat.post(post_id);


--
-- Name: image image_post_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.image
    ADD CONSTRAINT image_post_id_fkey FOREIGN KEY (post_id) REFERENCES instachat.post(post_id);


--
-- Name: phone phone_user_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.phone
    ADD CONSTRAINT phone_user_id_fkey FOREIGN KEY (user_id) REFERENCES instachat."user"(user_id);


--
-- Name: post_belongs post_belongs_chat_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.post_belongs
    ADD CONSTRAINT post_belongs_chat_id_fkey FOREIGN KEY (chat_id) REFERENCES instachat.chat(chat_id);


--
-- Name: post_belongs post_belongs_post_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.post_belongs
    ADD CONSTRAINT post_belongs_post_id_fkey FOREIGN KEY (post_id) REFERENCES instachat.post(post_id);


--
-- Name: u_contacts u_contacts_contact_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.u_contacts
    ADD CONSTRAINT u_contacts_contact_id_fkey FOREIGN KEY (contact_id) REFERENCES instachat."user"(user_id);


--
-- Name: u_contacts u_contacts_user_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.u_contacts
    ADD CONSTRAINT u_contacts_user_id_fkey FOREIGN KEY (user_id) REFERENCES instachat."user"(user_id);


--
-- PostgreSQL database dump complete
--
