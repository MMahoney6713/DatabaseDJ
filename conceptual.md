### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?

psql is one of many database systems that follows the SQL rules for interacting with a database

- What is the difference between SQL and PostgreSQL?

SQL is the rules, psql is the program implemented with the rules

- In `psql`, how do you connect to a database?

\c database_name

- What is the difference between `HAVING` and `WHERE`?

HAVING is for a join, WHERE is for a query

- What is the difference between an `INNER` and `OUTER` join?

INNER joins show only the items in common, OUTER joins will show items not in common as well

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?

LEFT/RIGHT will show the non-common items, biased to the left/right table in the join

- What is an ORM? What do they do?

object relational mapper, connects database functionality with model objects for use in programming languages

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?

Browser side requests can be made directly from browser to external API, but wouldn't want to send
user auth data across those requests. Server side requests can be good for anything that requires database
query or user auth, if external API requires token

- What is CSRF? What is the purpose of the CSRF token?

CrossSiteRequestForgery, the token enables making sure that a request is coming from the same source rather
than a different source

- What is the purpose of `form.hidden_tag()`?

Makes sure that CSRF token is returned and is not visible