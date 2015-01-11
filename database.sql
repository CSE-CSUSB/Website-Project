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
  "tfa"      TEXT,
  "email"    TEXT      NOT NULL UNIQUE,
  "created"  TIMESTAMP NOT NULL,
  "role"     INTEGER   NOT NULL
);
