## System design 

**With the possibility of Network failures/partitions, Strong Consistency and High Availability can not be achieved simultaneously** - Brewer's Conjecture - CAP theorm

Trade-offs

1. Performance vs Scalability
2. Latency vs Throughtput
3. Availability vs Consistency

Performance problem - System is slow for a single user
Scalability problem - System is fast for a single user, but slow under load

Latency - Time taken to process and respond to a request
Throughput - Rate at which a system can process the requests. 

** Strive for maximum throught with acceptable latency **

### 1. Requirements, Goals and Assumptions
    
- Query model (access patterns) 
    - Primary-key access
    - Joins?
- SLA

- Trade offs (Further details)
    * Security
    * Reliability
    * Consistency
    * Latency
    * Availability
    * Cost-effectiveness
    * Performance and Flexibility etc.

    
## 2. System Architecture

- System Interface (UX)
- Read/Write ratio
- Data Storage and Partitioning
- Replication and Replica Synchronization
- Data Versioning (MVCC)
- Load Balancing
- Membership and Node failure detection
- Overload handling a.k.a Rate limiting / Load shedding
- Request routing
- State trasfer
- Concurrency and Job Scheduling
- Monitoring, Alarming / Self stabilization / Auto recovery
- Configuration Management
- Conflict Resolution
    When - Read or Write
    Who - Data Store ("last write wins") or Application (merge writes)
- Failure modes, changing requirements, security etc.,


## 3. Concepts

1. Hedge requests
2. Read your writes (zookie) global consistency
3. Cache stampede
4. Data Sharding (Slicer or Shard Manager)
5. 80/20 rule. 80% of the time, only 20% of the code/data runs

## Miscellaneous 

Base64 encoding

## System Implementations
- The reliability and scalability of a system is dependent on how its application state is managed
- Read (point and range), Update (bloom filters / Fence pointers to avoid disk-io) and Memory amplifications
- Latency amplification. Latency increases with utilization. 

- Timeouts 
    - measure -> dynamic timeouts ex., min(p99, 100)
    - timeout budget in service chain. short-circuit if no budget.

- Retries
    - Exponential backoffs with jitter
    - Retries before failure
    - Retries with timeout and probablistic retries

- High variance service cause latency amplification

- Queue amplifies Latency
  Queues - Disks, CPU, Socket, Connection Pool, Threads, Load Balancers 

    Ϙ ∞ 𝞺 / 1 - 𝞺  

    Ϙ -> Queue Length => Latency
    𝞺 -> utilization

- Back pressure to edge to do load shedding

## Building blocks

1. Scalability
    - Data Partitioning.
    - Servers in consistent hashing ring / sometimes hierarchical + discovery (cockroachDB)
    - Consistent Hashing.
        Virtual nodes (same node occuping multiple logical places in the ring)

2. Availability
    - Replication
    - Primary-Secondary 
    - Peer-to-Peer


### Correlated Failure
  
  A system suffers a correlated failure when multiple independent components fail due to the same underlying cause. 

  For ex, all services are brougt down because of the fd limit
  
   
Safety vs. Liveness