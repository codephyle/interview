# Dynamo

- Zero-Hop DHT ( every node has the knowledge of the cluster locally! )
- 'always writable' system.
- Top 'N' nodes in the consistent ring - Preference list 
- conflict resolution
    - syntactic (using vector clocks / wall clocks)
    - semantic (by application)
- R + W > N (2 + 2 > 3)
- Hinted Handoff. N+1st node act as a proxy (request with metadata) till the actual coordinator node is back!
- Replica sync - using Merkle tree for each virtual node
- Read repair (while reading fix inconsistencies after sending response)

Problem                               Technique                                               Advantage 
--------------------------------------------------------------------------------------------------------
Partitioning                          Consistent Hashing                                      Incremental Scalability                 

High availability for writes          Vector clocks with reconciliation during reads          Version size is decoupled from update rates.     

Handling temporary failures           Sloppy Quorum and Hinted Handoff                        Provides high availability 
are not available                                                                             and durability guarantee when some of the replicas 
          
Recovering from permanent failures    Anti-entropy using Merkle trees                         Synchronizes divergent replicas on the background   

Membership and failure detection      Gossip-based membership protocol and failure detection  Preserves symmetry and avoid centralized monitoring
                                      ['seed' nodes are used for membership bootstrap]






