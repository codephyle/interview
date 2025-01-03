## Key Value Store (on Disk)

### B-Trees

- An n-ary tree optimized for persistent store 
- Non leaf nodes have only keys in sorted order
- Leaf nodes have keys and values
- Degree of the tree is number of slots (pointers/kids) it is going to have. This is determined by the page size of the OS or the buffer size of the Storage engine. As each entry is made of (size(key), size(machine_pointer)), degree is (size(key), size(machine_pointer) + 1) buffer_size. Note we will have 1 more pointer than the number of keys.
![Non Leaf node](./img/btree-non-leaf-node.png "Non Leaf Node")
- Leaf nodes have sibling pointers for range results

- Values are modified in place. 
- Optimized for read speed. Write speed is tradeoff.


### LSM Trees [Log-structured merge trees]