# Overview

**The mission of this project is to provide an authenticated database that can service multiple blockchain needs, and will be included with a way to implement in different data structures.**

Blockchains utilize authenticated data structures, like the Patricia Merkle Trie, extensively to preserve immutability of their individual chains. These data structures can differ from chain to chain, but share a common optimization problems, and are built as bolt-on versions of NoSQL databases like levelDB. By building on top of current databases, these authenticated data structures are unable to take full advantage of the system and suffer from performance issues (slow reads and writes).

