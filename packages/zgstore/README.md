# `zgtree` :evergreen:
=========================

A [fully persistent](http://en.wikipedia.org/wiki/Persistent_data_structure) [red-black tree](http://en.wikipedia.org/wiki/Red%E2%80%93black_tree) rewritten in 100% TypeScript.  Works both in node.js and in the browser via [browserify](http://browserify.org/).

Functional (or fully persistent) data structures allow for non-destructive updates.  So if you insert an element into the tree, it returns a new tree with the inserted element rather than destructively updating the existing tree in place.  Doing this requires using extra memory, and if one were naive it could cost as much as reallocating the entire tree.  Instead, this data structure saves some memory by recycling references to previously allocated subtrees.  This requires using only O(log(n)) additional memory per update instead of a full O(n) copy.

Some advantages of this is that it is possible to apply insertions and removals to the tree while still iterating over previous versions of the tree.  Functional and persistent data structures can also be useful in many geometric algorithms like point location within triangulations or ray queries, and can be used to analyze the history of executing various algorithms.  This added power though comes at a cost, since it is generally a bit slower to use a functional data structure than an imperative version.  However, if your application needs this behavior then you may consider using this module.

# Install

    npm install zgtree

# Example

Here is an example of some basic usage:

```Typescript
//Load the library
import {createRBTree as makeTree} from '../zgtree';

//Create a tree
var tree1 = createTree();

//Insert some items into the tree
var tree2 = tree1.insert(1, "foo");
var tree3 = tree2.insert(2, "bar");

//Remove something
var tree4 = tree3.remove(1);
```

# API

[**Tree API reference**](/docs/interfaces/itree.md)

[**Tree Iterator API reference**](/docs/interfaces/iiterator.md)

[**Globals**](/docs/globals.md)

### Acknowledgements

This repo is a fork of the [functional-red-black-tree repository](https://github.com/mikolalysenko/functional-red-black-tree);

