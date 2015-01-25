CREATE TABLE sessions (
  "key"    TEXT      NOT NULL UNIQUE,
  "value"  INTEGER   NOT NULL
);

CREATE TABLE users (
  "id"             SERIAL    NOT NULL PRIMARY KEY,
  "password"       TEXT,
  "cid"            INT       NOT NULL UNIQUE,
  "fname"          TEXT      NOT NULL,
  "lname"          TEXT      NOT NULL,
  "email_primary"  TEXT      NOT NULL UNIQUE,
  "email_csusb"    TEXT               UNIQUE,
  "standing"       TEXT      NOT NULL,
  "gender"         TEXT,
  "shirt_size"     TEXT,
  "shirt_received" TIMESTAMP,
  "majors"         TEXT      NOT NULL,
  "minors"         TEXT,
  "paid_until"     TIMESTAMP,
  "created"        TIMESTAMP NOT NULL,
  "role"           INTEGER   NOT NULL
);

CREATE TABLE content (
  "id"            SERIAL    NOT NULL PRIMARY KEY,
  "url"           TEXT      NOT NULL UNIQUE,
  "title"         TEXT      NOT NULL,
  "created_by"    INTEGER   NOT NULL,
  "created_on"    TIMESTAMP NOT NULL,
  "edited_by"     INTEGER   NOT NULL,
  "edited_on"     TIMESTAMP NOT NULL,
  "content"       TEXT      NOT NULL,
  "require_level" INTEGER   NULL     DEFAULT NULL,
  "in_navigation" INTEGER   NOT NULL DEFAULT 0
);