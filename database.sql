CREATE TABLE sessions (
  "id"     SERIAL    NOT NULL PRIMARY KEY,
  "key"    TEXT      NOT NULL UNIQUE,
  "user"   INTEGER   NOT NULL,
  "ip"     TEXT      NOT NULL,
  "start"  TIMESTAMP NOT NULL,
  "active" TIMESTAMP NOT NULL,
  "valid"  BOOLEAN   NOT NULL
);

CREATE TABLE users (
  "id"       SERIAL    NOT NULL PRIMARY KEY,
  "username" TEXT      NOT NULL UNIQUE,
  "password" TEXT      NOT NULL,
  "salt"     TEXT      NOT NULL,
  "email"    TEXT      NOT NULL UNIQUE,
  "created"  TIMESTAMP NOT NULL,
  "role"     INTEGER   NOT NULL
);

CREATE TABLE content (
  "id"         SERIAL    NOT NULL PRIMARY KEY,
  "url"        TEXT      NOT NULL UNIQUE,
  "title"      TEXT      NOT NULL,
  "created_by" INTEGER   NOT NULL,
  "created_on" TIMESTAMP NOT NULL,
  "edited_by"  INTEGER   NOT NULL,
  "edited_on"  TIMESTAMP NOT NULL,
  "content"    TEXT      NOT NULL
);