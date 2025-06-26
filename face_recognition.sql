--
-- PostgreSQL database dump
--

-- Dumped from database version 17.4
-- Dumped by pg_dump version 17.4

-- Started on 2025-06-26 23:52:24

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 217 (class 1259 OID 33449)
-- Name: face_save; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.face_save (
    id_face uuid NOT NULL,
    name character varying(255),
    face_embed double precision[],
    image_base64 text
);


ALTER TABLE public.face_save OWNER TO postgres;

--
-- TOC entry 4787 (class 0 OID 33449)
-- Dependencies: 217
-- Data for Name: face_save; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.face_save (id_face, name, face_embed, image_base64) FROM stdin;
\.


--
-- TOC entry 4641 (class 2606 OID 33455)
-- Name: face_save face_save_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.face_save
    ADD CONSTRAINT face_save_pkey PRIMARY KEY (id_face);


-- Completed on 2025-06-26 23:52:26

--
-- PostgreSQL database dump complete
--

