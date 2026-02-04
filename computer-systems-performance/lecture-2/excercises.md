# Information about the experiment

### Goal

Investigate the performance of new partitioning methods. Test against both sequential and parallel
methods.

### System

- Hardware: Sun SPARC T1 
    - Cores: 8
    - Threads: 4 per core
    - 16 GB of ram
- Operating System: Solaris
- Software: Partitioning algorithm
- TLB entries: 64

### Metrics

- Throughput (tuples per second)
- TLB misses
- Cache misses.
- Size of metadata. 

### Parameters

Larger pagesize = higher cache hit rate, since more virtual addresses can be stored in each pagesize.

**Pagesize**

- 8 KB
- 64 KB
- 4 MB
- 256 MB

**Threads**

Ranges between 1-32.

**Hashbits** 

Hashbits (Amount of partitions). From 0 - 18 hashbits.


### Levels

### Type of experiment

Real experiments.

### Workloads

For the Thread count the amount of hashbit was 2^24.
Workload is uses synthetic data.
16 byte tuples, 8 byte partitioning key, 8 byte payload.
For the payload we can basically just write 0's, but the generation of the partitioning key is important.
Uniform data.


By changing data distribution we can introduce imbalances accross paritions, which can result in suboptimal distribution of work to cores and threads.

### #Runs

On average they performed 8 runs.

## Algorithms

**Independent output:** Individual threads have their own seperate output buffers.
In the paper, they stop right after doing the partitioning. No aggregation of results is needed.

**Concurrent partitioning:** Threads access the same output buffers and need synchronization primitives to make it thread safe. In high contention environments, 
this can become serial.

**Count-then-move:** Do a pass over data, count how many you should have in each partition. Even if you use shared buffers, no synchronization is needed,
since the offset of the data is already known beforehand. Thus each thread need not worry about other threads trying to content their space in the buffer.

**Parallel buffers:** Each thread has a chunk of space in the shared buffer. Synchronization is only needed when the partition should be merged at the end.

Chunk size of 128 tuples, possibly setting it to 1 during runtime. 

## Hardware for the server


