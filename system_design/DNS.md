### DNS Fundamentals

Server Port: 53

DNS Resolver (local server + caching with TTL)
    |
    |-----> 13 root servers across the world (A-M)
                |
                |----> TLD servers (.com/.io etc)
                            |
                            |-----> Authoritative servers


CACHING
--------

Browser -> Operating System -> local name server -> ISP Resolvers -> Internet DNS Infra

- By default, UDP is used. Zone transfer use TCP. 

- If the packet size is greater than 512 Bytes, TCP is used. DNSSEC

Fact: To maintain high availability, should the TTL value be large or small?

small, because, in case of server failures, resolver will retry a different authoritative server. 
