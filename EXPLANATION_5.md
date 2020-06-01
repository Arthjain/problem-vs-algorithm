Trie classes and Trie Nodes are implemented in the program. The character string that we want to search for suffixes is located in the Trie Node. The Trie Node tree is then traversed recursively and we we reach the end, the result suffix is added to the list of suffixes and the list is returned to the user.

TIME COMPLEXITY:

Analysis:
For the trie, time complexity of searching and inserting from a trie depends on the length of the word a that’s being searched for, inserted, and the number of total words, n, making the runtime of these operations O(a*n). Looking into the space complexity of a trie, the worst case, would be when we have a word (or words), with no common characters between them, hence having, a node for each letter. Resulting in a space complexity of O(n).

SPACE COMPLEXITY:

The Space complexity will be O(word_length*unique_chars*no_of_words)
