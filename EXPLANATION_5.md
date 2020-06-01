Trie classes and Trie Nodes are implemented in the program. The character string that we want to search for suffixes is located in the Trie Node. The Trie Node tree is then traversed recursively and we we reach the end, the result suffix is added to the list of suffixes and the list is returned to the user.

TIME COMPLEXITY:

The time complexity will O(word_length*unique_chars*no_of_words)


SPACE COMPLEXITY:

The Space complexity will be O(word_length*unique_chars*no_of_words)