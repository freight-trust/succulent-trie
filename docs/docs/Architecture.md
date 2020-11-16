# How it works

A generalized Sparse Merkle tree as the indexing structure for an append-only sorted string table

## Overview

The mission of this project is to provide an authenticated database that can service multiple blockchain needs, and will be included with a way to implement in different data structures.

## Requirements

-   Arbitrary length keys/values
-   Range queries
-   Merkle Proofs
-   Go bindings

## Motivation

Blockchains utilize authenticated data structures, like the Patricia Merkle Trie, extensively to preserve immutability of their individual chains. These data structures can differ from chain to chain, but share a common optimization problems, and are built as bolt-on versions of NoSQL databases like levelDB.

By building on top of current databases, these authenticated data structures are unable to take full advantage of the system and suffer from performance issues (slow reads and writes).

This system has previously been implemented with binary Tries in the Urkel database, which resulted in up to 100x performance increases over the current system in terms of reads, writes, and storage footprint. Unfortunately, it is not generalized and easily applicable to other blockchains.

We intend to expand on the same line as the Urkel database and create a generalized implementation of Sparse Merkle Tree that can be used to implement Tries, Red-black, BSTs, and many other tree-based structures.

## Our Approach

The entire process will incorporate two components, the technology research, and the product. These can occur simultaneously as they are non-blocking. The motivation for the research will be to provide the backing for the optimizations used in the product itself -- e.g. compaction, data structure, partitioning, and more efficient commits. The development will be centered around implementing a generalized Merkle tree that can be used by multiple blockchains.
Generalized Sparse Merkle Tree
The Generalized Merkle Tree is used in many different blockchains and authenticated databases, as a form of history and storage of immutable state.

## Nodes

The nodes of the Merkle Tree will contain several values, they will be treated similarly to the traditional nodes with the ability for multiple children, and the recognition of heights.

```
Nodes {
  Merkle Hash
  Height
  Children
  Extra
}
```

### Children

Enables a reduction in the total number of hops that must be made. And spreads a tree out. Furthermore, this is necessary for implementations like the Ethereum trie which require 16 branches.

### Height

Allows for arbitrary heights, which is crucial to expand the trie, and improves the efficiency of the lookup from cache (allows for Sparse Merkle Trees).

## Extra

The extra variable enables trees with rebalancing aspects, such as Red-black or AVL trees. The benefit of this is that the trees can have “colors” or numbers that can be used with invariants when rebalancing.

### Proofs

Without loss of generality, the proofs for the Sparse Merkle Tree can be utilized for arbitrary numbers of children. The proofs will flow in the same manner, where the children of the root are used to verify that the hash is correct. Further information on the proofs can be found in the Sparse Merkle Tree paper.

### Verification

Without loss of generality, the proofs for the Sparse Merkle Tree can be utilized for arbitrary numbers of children. Verification can be done using the same technique.

## Store

The store is based on the traditional data store, seen in LevelDB, and implemented in the authenticated data structure, like Urkel. For this implementation, the only thing that will change will be the way in which records are indexed. A second offset will be added to accommodate arbitrary size keys and values. The image below shows a basic view of what current index/offset systems look like.

## Index

The index for each data block will change to reflect arbitrary length keys this will include the addition of a header that keeps track of the positions of the key, the value, and the position.

`file_index || offset_key || offset || position`

It should be noted that the record does not change with the header, on the manner in which the index is read.

## Roadmap

### Part 1

The theme of part one is to have the product. The first part of this plan will be to create the unit tests and the integration tests for needed features. This will also incorporate the necessary go bindings to utilize the database.

-   Arbitrary Length keys
-   Arbitrary Length values
-   Range queries
-   Merkle Proof Semantics
-   Go Bindings
-   Unit tests

### Part 2

The second part of the plan will be to get developer feedback and determine the feature roadmap.

-   Schema validation
-   Arbitrary length values
-   Implementation of IAVL, Trie
-   Client/Developer input features ( Developer input will occur )

### Part 3

The third part of the product will take the optimizations found in the research, and schema created from the clients and integrate them in order to benefit.

-   Bitmapping
-   Write back cache automatic flushing
-   Compaction efficient
-   Research

### Part 4

The fourth part will be centered around taking the optimized version of this database and pushing it to optimized languages.

-   Rust (WASM)
-   Packaging for other systems/languages (clean-up)

## Further research

The motivation for further research is to provide faster queries, fast updates, simple partitioning, and simpler storage proofs for the data structure as a whole. With this in mind, the initial topics of research will be pushed towards these areas:

-   Fast sync of data
-   Efficient compaction and storage
-   Rebalancing
    Parallelization
    Pruning
    Partitioning and sharding of data
    Efficient range, filtering proofs
