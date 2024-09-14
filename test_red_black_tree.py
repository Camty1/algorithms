#!/usr/bin/env python3.11
from trees import RedBlackTree, RedBlackTreeNode

tree = RedBlackTree()
items = [11, 14, 2, 15, 1, 7, 8, 5, 4]
for i in items:
    node = RedBlackTreeNode(i)
    tree.insert(node)
    print(tree)

node = tree.search(5)
tree.delete(node)
print(tree)
tree.insert(5)
print(tree)
