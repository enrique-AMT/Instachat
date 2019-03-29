--
-- PostgreSQL database dump
--

-- Dumped from database version 10.6 (Ubuntu 10.6-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.6 (Ubuntu 10.6-0ubuntu0.18.04.1)

-- Started on 2019-03-28 22:25:36 AST

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
-- TOC entry 7 (class 2615 OID 24594)
-- Name: instachat; Type: SCHEMA; Schema: -; Owner: instadev
--

CREATE SCHEMA instachat;


ALTER SCHEMA instachat OWNER TO instadev;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 206 (class 1259 OID 24646)
-- Name: belongs; Type: TABLE; Schema: instachat; Owner: instadev
--

CREATE TABLE instachat.belongs (
    chat_id integer NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE instachat.belongs OWNER TO instadev;

--
-- TOC entry 205 (class 1259 OID 24635)
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
-- TOC entry 204 (class 1259 OID 24633)
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
-- TOC entry 2965 (class 0 OID 0)
-- Dependencies: 204
-- Name: chat_chat_id_seq; Type: SEQUENCE OWNED BY; Schema: instachat; Owner: instadev
--

ALTER SEQUENCE instachat.chat_chat_id_seq OWNED BY instachat.chat.chat_id;


--
-- TOC entry 202 (class 1259 OID 24607)
-- Name: phone; Type: TABLE; Schema: instachat; Owner: instadev
--

CREATE TABLE instachat.phone (
    phone_id integer NOT NULL,
    user_id integer,
    phone character(10)
);


ALTER TABLE instachat.phone OWNER TO instadev;

--
-- TOC entry 201 (class 1259 OID 24605)
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
-- TOC entry 2966 (class 0 OID 0)
-- Dependencies: 201
-- Name: phone_phone_id_seq; Type: SEQUENCE OWNED BY; Schema: instachat; Owner: instadev
--

ALTER SEQUENCE instachat.phone_phone_id_seq OWNED BY instachat.phone.phone_id;


--
-- TOC entry 203 (class 1259 OID 24618)
-- Name: u_contacts; Type: TABLE; Schema: instachat; Owner: instadev
--

CREATE TABLE instachat.u_contacts (
    user_id integer NOT NULL,
    contact_id integer NOT NULL
);


ALTER TABLE instachat.u_contacts OWNER TO instadev;

--
-- TOC entry 200 (class 1259 OID 24597)
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
-- TOC entry 199 (class 1259 OID 24595)
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
-- TOC entry 2967 (class 0 OID 0)
-- Dependencies: 199
-- Name: user_user_id_seq; Type: SEQUENCE OWNED BY; Schema: instachat; Owner: instadev
--

ALTER SEQUENCE instachat.user_user_id_seq OWNED BY instachat."user".user_id;


--
-- TOC entry 2812 (class 2604 OID 24638)
-- Name: chat chat_id; Type: DEFAULT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.chat ALTER COLUMN chat_id SET DEFAULT nextval('instachat.chat_chat_id_seq'::regclass);


--
-- TOC entry 2811 (class 2604 OID 24610)
-- Name: phone phone_id; Type: DEFAULT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.phone ALTER COLUMN phone_id SET DEFAULT nextval('instachat.phone_phone_id_seq'::regclass);


--
-- TOC entry 2810 (class 2604 OID 24600)
-- Name: user user_id; Type: DEFAULT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat."user" ALTER COLUMN user_id SET DEFAULT nextval('instachat.user_user_id_seq'::regclass);


--
-- TOC entry 2959 (class 0 OID 24646)
-- Dependencies: 206
-- Data for Name: belongs; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.belongs (chat_id, user_id) FROM stdin;
\.


--
-- TOC entry 2958 (class 0 OID 24635)
-- Dependencies: 205
-- Data for Name: chat; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.chat (chat_id, chat_name, owner_id, number_of_users) FROM stdin;
1	hello	1	1
\.


--
-- TOC entry 2955 (class 0 OID 24607)
-- Dependencies: 202
-- Data for Name: phone; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.phone (phone_id, user_id, phone) FROM stdin;
1	1	7873830072
\.


--
-- TOC entry 2956 (class 0 OID 24618)
-- Dependencies: 203
-- Data for Name: u_contacts; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat.u_contacts (user_id, contact_id) FROM stdin;
1	2
\.


--
-- TOC entry 2953 (class 0 OID 24597)
-- Dependencies: 200
-- Data for Name: user; Type: TABLE DATA; Schema: instachat; Owner: instadev
--

COPY instachat."user" (user_id, first_name, last_name, u_email_address, u_password) FROM stdin;
1	Pedro	Rivera	p.rivera@upr.edu	jaja saludos
3	Juan	Lopez	juan.lopez32@upr.edu	testing1212
4	Bienvenido	Velez	bienvenido.velez@upr	java2020
2	Amir	Chinaei	amir.chinaei@upr.edu	nosvemos
\.


--
-- TOC entry 2968 (class 0 OID 0)
-- Dependencies: 204
-- Name: chat_chat_id_seq; Type: SEQUENCE SET; Schema: instachat; Owner: instadev
--

SELECT pg_catalog.setval('instachat.chat_chat_id_seq', 1, true);


--
-- TOC entry 2969 (class 0 OID 0)
-- Dependencies: 201
-- Name: phone_phone_id_seq; Type: SEQUENCE SET; Schema: instachat; Owner: instadev
--

SELECT pg_catalog.setval('instachat.phone_phone_id_seq', 1, true);


--
-- TOC entry 2970 (class 0 OID 0)
-- Dependencies: 199
-- Name: user_user_id_seq; Type: SEQUENCE SET; Schema: instachat; Owner: instadev
--

SELECT pg_catalog.setval('instachat.user_user_id_seq', 3, true);


--
-- TOC entry 2824 (class 2606 OID 24650)
-- Name: belongs belongs_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.belongs
    ADD CONSTRAINT belongs_pkey PRIMARY KEY (user_id, chat_id);


--
-- TOC entry 2822 (class 2606 OID 24640)
-- Name: chat chat_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.chat
    ADD CONSTRAINT chat_pkey PRIMARY KEY (chat_id);


--
-- TOC entry 2818 (class 2606 OID 24612)
-- Name: phone phone_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.phone
    ADD CONSTRAINT phone_pkey PRIMARY KEY (phone_id);


--
-- TOC entry 2820 (class 2606 OID 24622)
-- Name: u_contacts u_contacts_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.u_contacts
    ADD CONSTRAINT u_contacts_pkey PRIMARY KEY (user_id, contact_id);


--
-- TOC entry 2814 (class 2606 OID 24602)
-- Name: user user_pkey; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_id);


--
-- TOC entry 2816 (class 2606 OID 24604)
-- Name: user user_u_email_address_key; Type: CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat."user"
    ADD CONSTRAINT user_u_email_address_key UNIQUE (u_email_address);


--
-- TOC entry 2829 (class 2606 OID 24651)
-- Name: belongs belongs_chat_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.belongs
    ADD CONSTRAINT belongs_chat_id_fkey FOREIGN KEY (chat_id) REFERENCES instachat.chat(chat_id);


--
-- TOC entry 2830 (class 2606 OID 24656)
-- Name: belongs belongs_user_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.belongs
    ADD CONSTRAINT belongs_user_id_fkey FOREIGN KEY (user_id) REFERENCES instachat."user"(user_id);


--
-- TOC entry 2828 (class 2606 OID 24641)
-- Name: chat chat_owner_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.chat
    ADD CONSTRAINT chat_owner_id_fkey FOREIGN KEY (owner_id) REFERENCES instachat."user"(user_id);


--
-- TOC entry 2825 (class 2606 OID 24613)
-- Name: phone phone_user_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.phone
    ADD CONSTRAINT phone_user_id_fkey FOREIGN KEY (user_id) REFERENCES instachat."user"(user_id);


--
-- TOC entry 2827 (class 2606 OID 24628)
-- Name: u_contacts u_contacts_contact_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.u_contacts
    ADD CONSTRAINT u_contacts_contact_id_fkey FOREIGN KEY (contact_id) REFERENCES instachat."user"(user_id);


--
-- TOC entry 2826 (class 2606 OID 24623)
-- Name: u_contacts u_contacts_user_id_fkey; Type: FK CONSTRAINT; Schema: instachat; Owner: instadev
--

ALTER TABLE ONLY instachat.u_contacts
    ADD CONSTRAINT u_contacts_user_id_fkey FOREIGN KEY (user_id) REFERENCES instachat."user"(user_id);


-- Completed on 2019-03-28 22:25:36 AST

--
-- PostgreSQL database dump complete
--

