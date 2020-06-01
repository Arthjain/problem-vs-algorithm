To solve this problem, RouteTrieNode, RouteTrie and Router classes are implemented in the program.The path string we want to search (splitted using "/" character) is located in the RouteTrieNode base. if its found then handler is returned otherwise not found handler is returned.

TIME COMPLEXITY:

The time complexity will be O(n*m) for trie data structure [Insert and search].
where n is the number of URL(s) and
m is the length of the longest piece of URL separated by backslash.


SPACE COMPLEXITY:

The Space complexity will be O(token_length*unique_tokens_no_of_tokens)