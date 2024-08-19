DROP TABLE IF EXISTS "classification";
DROP SEQUENCE IF EXISTS classification_id_seq;
CREATE SEQUENCE classification_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."classification" (
    "id" integer DEFAULT nextval('classification_id_seq') NOT NULL,
    "classification" character varying(255),
    "material_type" character varying(255),
    "chemical_composition" character varying(255),
    "clan" character varying(255),
    "clazz" character varying(255),
    CONSTRAINT "classification_pkey" PRIMARY KEY ("id")
) WITH (oids = false);


DROP TABLE IF EXISTS "date";
DROP SEQUENCE IF EXISTS date_id_seq;
CREATE SEQUENCE date_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."date" (
    "id" integer DEFAULT nextval('date_id_seq') NOT NULL,
    "date" timestamp,
    "month" integer,
    "quarter" integer,
    "year" integer,
    CONSTRAINT "date_pkey" PRIMARY KEY ("id")
) WITH (oids = false);


DROP TABLE IF EXISTS "location";
DROP SEQUENCE IF EXISTS location_id_seq;
CREATE SEQUENCE location_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."location" (
    "id" integer DEFAULT nextval('location_id_seq') NOT NULL,
    "latitude" FLOAT,
    "longitude" FLOAT,
    "city" character varying(255),
    "state" character varying(255),
    "country" character varying(255),
    CONSTRAINT "location_pkey" PRIMARY KEY ("id")
) WITH (oids = false);


DROP TABLE IF EXISTS "meteorite";
DROP SEQUENCE IF EXISTS meteorite_id_seq;
CREATE SEQUENCE meteorite_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."meteorite" (
    "mass" real NOT NULL,
    "id_location" integer NOT NULL,
    "id_classification" integer NOT NULL,
    "id_date" integer NOT NULL,
    PRIMARY KEY (id_location, id_classification, id_date)
) WITH (oids = false);


ALTER TABLE ONLY "public"."meteorite" ADD CONSTRAINT "meteorite_id_classification_fkey" FOREIGN KEY (id_classification) REFERENCES classification(id) NOT DEFERRABLE;
ALTER TABLE ONLY "public"."meteorite" ADD CONSTRAINT "meteorite_id_date_fkey" FOREIGN KEY (id_date) REFERENCES date(id) NOT DEFERRABLE;
ALTER TABLE ONLY "public"."meteorite" ADD CONSTRAINT "meteorite_id_location_fkey" FOREIGN KEY (id_location) REFERENCES location(id) NOT DEFERRABLE;