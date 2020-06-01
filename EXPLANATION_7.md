To solve this problem, RouteTrieNode, RouteTrie and Router classes are implemented in the program.The path string we want to search (splitted using "/" character) is located in the RouteTrieNode base. if its found then handler is returned otherwise not found handler is returned.

Time Complexity:
insert: O(n) The insert operation saying that n = each '/', takes O(n) because there is one iteration per path part
find: O(n) Almost the same process, iterating through input one time, O(n)
Space Complexity:
insert: path_parts occupies n but splitted, so takes O(n)
find: path_parts occupies n but splitted, so takes O(n)
