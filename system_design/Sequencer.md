# Sequencer - Unique ID generation

## Methods

### UUID generation

 - NIC + some random number
 - UUID type4 pseudo random

### Simple DB autoincrement

### Service to get Ranges (Sequencer Range-Handler service)
 - returns ranges whenever a client ask for a range 
 - each client is given a range that can be cached at the client memory/disk
 - stores all the used sequences in a highly available DB
