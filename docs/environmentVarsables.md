# Environment Variables 

This document provides descriptions for the environment variables used in the configuration

## PROJECT_NAME
- **Description:** Name of the backend project 
- **Example Value:** `blog-bubbles-api`


## BACKEND_CORS_ORIGINS
- **Description:** An array of Http URLS or "*" where cors will be allowed 
- **Example Value:** `["*"]`

## POSTGRES_USER
- **Description:** Username of postgres database
- **Example Value:** `postgres`

## POSTGRES_PASSWORD
- **Description:** Password of postgres database
- **Example Value:** `postgres`

## POSTGRES_SERVER
- **Description:** Host address of postgres database
- **Example Value:** `localhost`

## POSTGRES_DB
- **Description:** DB name of postgres database
- **Example Value:** `app`

## SECERET_KEY
- **Description:** A random string used to encrypt the JWT token
- **Example Value:** `secret`

## ALGORITHM
- **Description:** Algorithm used to encrypt the JWT token
- **Example Value:** `HS256`