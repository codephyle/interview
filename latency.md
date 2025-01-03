Latency Comparison Numbers (~2012)
----------------------------------
L1 cache reference			                        0.5 ns								                                            
Branch mispredict			                        5   ns								
L2 cache reference			                        7   ns				            14× L1 cache			
Mutex lock/unlock			                       25   ns								
Main memory reference			                  100   ns				            20× L2 cache, 200× L1 cache	
Compress 1K bytes with Zippy		            3,000   ns         3 μs							
Send 1K bytes over 1 Gbps network	           10,000   ns        10 μs							
Read 4K randomly from SSD*		              150,000   ns       150 μs			    ~1GB/sec SSD			
Read 1 MB sequentially from memory	          250,000   ns       250 μs							
Round trip within same datacenter	          500,000   ns       500 μs							
Read 1 MB sequentially from SSD*	        1,000,000   ns     1,000 μs	    1 ms    ~1GB/sec SSD, 4× memory		
Disk seek				                   10,000,000   ns    10,000 μs	   10 ms  	20× datacenter roundtrip	
Read 1 MB sequentially from disk	       20,000,000   ns    20,000 μs	   20 ms  	80× memory, 20× SSD		
Send packet CA→Netherlands→CA		      150,000,000   ns   150,000 μs	  150 ms 					


https://leetcode.com/problems/validate-binary-search-tree/discuss/32112/Learn-one-iterative-inorder-traversal-apply-it-to-multiple-tree-questions-(Java-Solution)