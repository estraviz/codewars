-- First and last IP in a network
-- PostgreSQL 9.6
SELECT
  id,
  NETWORK(ip_address) AS first_address,
  BROADCAST(ip_address) AS last_address
FROM connections