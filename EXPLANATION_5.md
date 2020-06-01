Trie classes and Trie Nodes are implemented in the program. The character string that we want to search for suffixes is located in the Trie Node. The Trie Node tree is then traversed recursively and we we reach the end, the result suffix is added to the list of suffixes and the list is returned to the user.

Time Complexity:
insert and find: Both takes O(n), cause 1 iteration per char
suffixes: O(n * m): iterate over children + the suffixes operation with the children of each child
Space Complexity:
insert: O(n), the auxiliary space used by the algorithms assigning the node and keep it update while the process is executed
suffixes: O(n * m), results variable will occupy n + m, plus the n * m of the recursive stack
