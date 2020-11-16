# Frequently Asked Questions

## What is the genesis of Proxima? How did it occur to you to use Urkel tree to create an efficient data layer for the blockchain?

Proxima was conceived because of issues with data availability, security, and developer integration for blockchains. None of the toolsets at present, are able to provide a traditional development experience without compromising on security or performance.

Urkel was chosen over other data structures/libraries (like Patricia Merkle Trie) because it was built as a database, not on top of another database. This makes it more performant than other blockchain systems.

We are currently in the process of moving the Urkel DB to a more generalized scope so that it can be implemented with arbitrary key lengths, greater flexibility with data structures, and standardized error codes.

## Can you tell us what Urkel tree is and how it is used in Handshake?

The Urkel tree is a flat-file Merkle Tree, it looks similar in nature to Sorted String Tables, except instead of having the classic B+ tree as an indexing mechanism, it has a Merkle Trie. It was developed to provide shorter proofs and higher throughput for reads/writes than the traditional implementations.

Handshake protocol uses the Urkel database as an authenticated structure to store their certificates and domain data for their naming service. This functionality is similar to the Google Certificate Transparency database Trillian (https://github.com/google/trillian).

## How does Proxima deal with different types of data in the smart contract?

Proxima handles different data types by including its own set of schema and data type support. Values placed into the ProximaDB are cast to bytes but retrieved as JSON. This can be further augmented with blockchain-specific deserialization/serialization of data.

## Would Proxima work with DAGs?

Since Proxima relies on auditing the blockchains themselves, the risk factors for this type of integration would be the consensus of the DAG itself. If transactions can be cryptographically tied to the DAG, then Proxima can use this relation when it audits the data. For standard blockchains, this is easy because each transaction is a part of the Merkle Hash of a single block that is mined through signatures or PoW.

## Why use a trie?

Tries are used because they represent a data structure that is sorted and deterministic. This means that synchorinzations can occur in a distirbuted fashion (order of updates will not matter), and range queries can be done.

## How are range queries, filters, and other database operations proven through the ProximaDB?

At this point, the ProximaDB supplies a Proof-of-soundness for all queries (Range queries, filters, etc). This proof ensures that all data given is in the database. Further additions to the protocol involve including Proofs-of-Completeness, where it can be proven that the data given in a query is all of the data that matches a filter or range.

This problem incorporates two subsets:

-   **Range Queries**
    Ranges can be proven to be complete by looking at the ends of a sorted Merkle Trie, and building a partial Merkle Trie from it. This shows that there is no element outside of the desired range, and allows the querier to prove that every element within the query can build the partial tree. This topic has been breached in the Google [Sparse Merkle Trie](https://github.com/google/trillian), and [github discussions](https://gist.github.com/chris-belcher/eb9abe417d74a7b5f20aabe6bff10de0). In this case, we use a Merkle trie (a deterministically sorted tree) to ensure sorting, and we submit range queries to the keys.

-   **Filter Queries**
    Filters where multiple requirements can be met, can be done by indexing an entity according to multiple constraints, submitting range queries to these different indexes and then doing a union or intersection based on the results of these queries.

One difficulty of this approach is the difficulty of combining multiple range queries at the same time. There have been several approaches that utilize accumulators and aggregate functions to provide [efficient nonmembership proofs](https://www.cs.purdue.edu/homes/ninghui/papers/accumulator_acns07.pdf). The naive approach would be to include every element in the ranges with their proofs for membership/nonmembership. The proof would include the subset of all the entities that matched the requirements, and a set of those that do not. Proofs could be derived by checking membership/nonmembership for all filters.

A potential alternative would be to encrypt the data via a homomorphic encryption of the [entire entity schema](https://www.math.u-bordeaux.fr/~gcastagn/publi/isit_homo.pdf), and to perform the boolean operations on the encrypted schema and filter. In cases where privacy is necessary, this is a powerful alternative.
