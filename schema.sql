--
-- PostgreSQL database dump
--

-- Dumped from database version 11.5
-- Dumped by pg_dump version 11.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: instachat; Type: SCHEMA; Schema: -; Owner: instadev
--

CREATE SCHEMA instachat;


ALTER SCHEMA instachat OWNER TO instadev;

--
-- Name: pgcrypto; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS pgcrypto WITH SCHEMA public;


--
-- Name: EXTENSION pgcrypto; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pgcrypto IS 'cryptographic functions';


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
    p_with_hashtag integer NOT NULL,
    hashtag_id integer NOT NULL
);


ALTER TABLE instachat.has_hashtag OWNER TO instadev;

--
-- Name: hashtag; Type: TABLE; Schema: instachat; Owner: instadev
--

CREATE TABLE instachat.hashtag (
    hash_name character varying(128),
    hashtag_id integer NOT NULL
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
    post_date timestamp without time zone DEFAULT now() NOT NULL,
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
    user_that_react integer,
    p_reacted integer,
    reply_reacted integer,
    react_date timestamp without time zone DEFAULT now() NOT NULL
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
    reply_text character varying(250),
    p_replied integer,
    user_that_replied integer,
    reply_date timestamp without time zone DEFAULT now() NOT NULL
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
-- Name: user; Type: TABLE; Schema: instachat; Owner: instadev
--

CREATE TABLE instachat."user" (
    user_id integer NOT NULL,
    first_name character varying(20),
    last_name character varying(20),
    u_email_address character varying(128) NOT NULL,
    u_password character varying(72) NOT NULL,
    username character varying(20)
);


ALTER TABLE instachat."user" OWNER TO instadev;

--
-- Name: serial_user_id_seq; Type: SEQUENCE; Schema: instachat; Owner: instadev
--

CREATE SEQUENCE instachat.serial_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE instachat.serial_user_id_seq OWNER TO instadev;

--
-- Name: serial_user_id_seq; Type: SEQUENCE OWNED BY; Schema: instachat; Owner: instadev
--

ALTER SEQUENCE instachat.serial_user_id_seq OWNED BY instachat."user".user_id;


--
-- Name: u_contacts; Type: TABLE; Schema: instachat; Owner: instadev
--

CREATE TABLE instachat.u_contacts (
    user_id integer NOT NULL,
    contact_of integer NOT NULL
);


ALTER TABLE instachat.u_contacts OWNER TO instadev;

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
-- Name: serial_user_id_seq; Type: SEQUENCE; Schema: public; Owner: instadev
--

CREATE SEQUENCE public.serial_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.serial_user_id_seq OWNER TO instadev;

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
-- Name: react react_id; Type: DEFAULT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.react ALTER COLUMN react_id SET DEFAULT nextval('instachat.react_react_id_seq'::regclass);


--
-- Name: reply reply_id; Type: DEFAULT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.reply ALTER COLUMN reply_id SET DEFAULT nextval('instachat.reply_reply_id_seq'::regclass);


--
-- Name: user user_id; Type: DEFAULT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat."user" ALTER COLUMN user_id SET DEFAULT nextval('instachat.serial_user_id_seq'::regclass);


--
-- Data for Name: belongs; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.belongs (u_belongs, c_user_belongs) FROM stdin;
\.


--
-- Data for Name: chat; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.chat (chat_id, chat_name, owner_id) FROM stdin;
\.


--
-- Data for Name: has_hashtag; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.has_hashtag (p_with_hashtag, hashtag_id) FROM stdin;
\.


--
-- Data for Name: hashtag; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.hashtag (hash_name, hashtag_id) FROM stdin;
\.


--
-- Data for Name: image; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.image (image_id, image_file, p_with_image) FROM stdin;
\.


--
-- Data for Name: phone; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.phone (phone_id, u_phone, phone) FROM stdin;
\.


--
-- Data for Name: post; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.post (post_caption, post_date, p_created_by, c_post_belongs, post_id) FROM stdin;
\.


--
-- Data for Name: react; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.react (react_id, react_type, user_that_react, p_reacted, reply_reacted, react_date) FROM stdin;
\.


--
-- Data for Name: reply; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.reply (reply_id, reply_text, p_replied, user_that_replied, reply_date) FROM stdin;
\.


--
-- Data for Name: u_contacts; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.u_contacts (user_id, contact_of) FROM stdin;
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat."user" (user_id, first_name, last_name, u_email_address, u_password, username) FROM stdin;
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

SELECT pg_catalog.setval('instachat.chat_chat_id_seq', 6, true);


--
-- Name: hashtag_hashtag_id_seq; Type: SEQUENCE SET; Schema: instachat; Owner: instadev
--

SELECT pg_catalog.setval('instachat.hashtag_hashtag_id_seq', 16, true);


--
-- Name: image_image_id_seq; Type: SEQUENCE SET; Schema: instachat; Owner: instadev
--

SELECT pg_catalog.setval('instachat.image_image_id_seq', 6, true);


--
-- Name: phone_phone_id_seq; Type: SEQUENCE SET; Schema: instachat; Owner: instadev
--

SELECT pg_catalog.setval('instachat.phone_phone_id_seq', 2, true);


--
-- Name: post_post_id_seq; Type: SEQUENCE SET; Schema: instachat; Owner: instadev
--

SELECT pg_catalog.setval('instachat.post_post_id_seq', 39, true);


--
-- Name: react_react_id_seq; Type: SEQUENCE SET; Schema: instachat; Owner: instadev
--

SELECT pg_catalog.setval('instachat.react_react_id_seq', 33, true);


--
-- Name: reply_reply_id_seq; Type: SEQUENCE SET; Schema: instachat; Owner: instadev
--

SELECT pg_catalog.setval('instachat.reply_reply_id_seq', 8, true);


--
-- Name: serial_user_id_seq; Type: SEQUENCE SET; Schema: instachat; Owner: instadev
--

SELECT pg_catalog.setval('instachat.serial_user_id_seq', 14, true);


--
-- Name: serial_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: instadev
--

SELECT pg_catalog.setval('public.serial_user_id_seq', 1, false);


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
-- Name: react something; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.react
    ADD CONSTRAINT something UNIQUE (user_that_react, p_reacted);


--
-- Name: u_contacts u_contacts_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.u_contacts
    ADD CONSTRAINT u_contacts_pkey PRIMARY KEY (user_id, contact_of);


--
-- Name: hashtag unique_hashtag; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.hashtag
    ADD CONSTRAINT unique_hashtag UNIQUE (hash_name);


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
-- Name: user user_username_key; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat."user"
    ADD CONSTRAINT user_username_key UNIQUE (username);


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
    ADD CONSTRAINT belongs_c_user_belongs_fkey FOREIGN KEY (c_user_belongs) REFERENCES instachat.chat(chat_id) ON DELETE CASCADE;


--
-- Name: belongs belons_u_belongs_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.belongs
    ADD CONSTRAINT belons_u_belongs_fkey FOREIGN KEY (u_belongs) REFERENCES instachat."user"(user_id) ON DELETE CASCADE;


--
-- Name: chat chat_owner_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.chat
    ADD CONSTRAINT chat_owner_id_fkey FOREIGN KEY (owner_id) REFERENCES instachat."user"(user_id) ON DELETE CASCADE;


--
-- Name: has_hashtag has_hashtag_hashtag_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.has_hashtag
    ADD CONSTRAINT has_hashtag_hashtag_id_fkey FOREIGN KEY (hashtag_id) REFERENCES instachat.hashtag(hashtag_id) ON DELETE CASCADE;


--
-- Name: has_hashtag has_hashtag_p_with_hashtag_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.has_hashtag
    ADD CONSTRAINT has_hashtag_p_with_hashtag_fkey FOREIGN KEY (p_with_hashtag) REFERENCES instachat.post(post_id) ON DELETE CASCADE;


--
-- Name: image image_p_with_image_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.image
    ADD CONSTRAINT image_p_with_image_fkey FOREIGN KEY (p_with_image) REFERENCES instachat.post(post_id) ON DELETE CASCADE;


--
-- Name: phone phone_u_phone_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.phone
    ADD CONSTRAINT phone_u_phone_fkey FOREIGN KEY (u_phone) REFERENCES instachat."user"(user_id) ON DELETE CASCADE;


--
-- Name: post post_c_post_belongs_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.post
    ADD CONSTRAINT post_c_post_belongs_fkey FOREIGN KEY (c_post_belongs) REFERENCES instachat.chat(chat_id) ON DELETE CASCADE;


--
-- Name: post post_p_created_by_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.post
    ADD CONSTRAINT post_p_created_by_fkey FOREIGN KEY (p_created_by) REFERENCES instachat."user"(user_id) ON DELETE CASCADE;


--
-- Name: react react_p_reacted_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.react
    ADD CONSTRAINT react_p_reacted_fkey FOREIGN KEY (p_reacted) REFERENCES instachat.post(post_id) ON DELETE CASCADE;


--
-- Name: react react_r_reacted_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.react
    ADD CONSTRAINT react_r_reacted_fkey FOREIGN KEY (reply_reacted) REFERENCES instachat.reply(reply_id) ON DELETE CASCADE;


--
-- Name: react react_u_that_react_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.react
    ADD CONSTRAINT react_u_that_react_fkey FOREIGN KEY (user_that_react) REFERENCES instachat."user"(user_id) ON DELETE CASCADE;


--
-- Name: reply reply_p_replied_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.reply
    ADD CONSTRAINT reply_p_replied_fkey FOREIGN KEY (p_replied) REFERENCES instachat.post(post_id) ON DELETE CASCADE;


--
-- Name: reply reply_user_that_replied_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.reply
    ADD CONSTRAINT reply_user_that_replied_fkey FOREIGN KEY (user_that_replied) REFERENCES instachat."user"(user_id) ON DELETE CASCADE;


--
-- Name: u_contacts u_contacts_contact_of_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.u_contacts
    ADD CONSTRAINT u_contacts_contact_of_fkey FOREIGN KEY (contact_of) REFERENCES instachat."user"(user_id) ON DELETE CASCADE;


--
-- Name: u_contacts u_contacts_user_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.u_contacts
    ADD CONSTRAINT u_contacts_user_id_fkey FOREIGN KEY (user_id) REFERENCES instachat."user"(user_id) ON DELETE CASCADE;


--
-- Name: u_contacts u_contacts_user_id_fkey1; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.u_contacts
    ADD CONSTRAINT u_contacts_user_id_fkey1 FOREIGN KEY (user_id) REFERENCES instachat."user"(user_id);


--
-- PostgreSQL database dump complete
--

