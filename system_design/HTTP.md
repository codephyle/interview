## TLS  

### TLS 1.2

    ------                                                       ------
    Client                                                       Server (Public, Private key)
    ------                                                       ------

                 ----------  TCP SYN ---------------->

    1. TCP       <---------  TCP SYN+ACK -------------

                 ----------  TCP ACK ---------------->

                     < TCP connection established >

                 -------- Client Hello -------------->
                    1. Supported cypher suites
                    2. TLS version
    2. CERT
       CHECK     <--------- Server Hello -------------
                    1. Decided Cypher / TLS version

                 <---------- Certificate -------------
                    Public key + other things

                 <--------- Server Hello Done -------

    3. KEY 
       EXCAHNGE  ----------- ENCRYPTED SESSION KEY  [Mostly RSA or diffie-hellman]
                             WITH SERVER PUBLIC KEY--->
                                                              (Decrypts session key using private key)


            
            
              
### TLS 1.3
   
   1. Number of supported cypher suites reduced
   2. RSA support is dropped. Only Diffie-Hellman 
      key exchange of ephemral keys for the keys
   3. 0-RTT [When accessing a site that has been visited, a client can send data on the first message to the server by leveraging pre-shared keys (PSK) from the prior session — thus “zero round-trip time” (0-RTT).]

  

    ------                                                       ------
    Client                                                       Server (Public, Private key)
    ------                                                       ------

                 ----------  TCP SYN ---------------->

    1. TCP      
                 <---------  TCP SYN+ACK -------------

                 ----------  TCP ACK ---------------->

                     < TCP connection established >

                 -------- Client Hello + KEY Share -------->
                   
    2. CERT CHECK + KEY exchange
            
                 <--------- Server Hello 
                    Key Share + Certificate + Finished ----

