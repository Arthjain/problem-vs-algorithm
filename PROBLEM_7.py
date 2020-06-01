class RouteTrie:
    def __init__(self, handler=None):
        self.root = RouteTrieNode(handler=handler)

    def insert(self, request_path, handler):
        sub_path_list = request_path.split("/")
        if len(sub_path_list) <= 1:
            return

        cur_node = self.root
        for sub_path in sub_path_list[1:]:
            if sub_path in cur_node.sub_path_dict:
                cur_node = cur_node.sub_path_dict[sub_path]
            else:
                child_route_trie_node = RouteTrieNode()
                cur_node.sub_path_dict[sub_path] = child_route_trie_node
                cur_node = child_route_trie_node
        cur_node.handler = handler

    def find(self, request_path):
        if request_path[-1] == "/":
            request_path = request_path[:-1]
        sub_path_list = request_path.split("/")

        cur_node = self.root
        if len(sub_path_list) <= 1:
            return cur_node.handler
        for sub_path in sub_path_list[1:]:
            if sub_path in cur_node.sub_path_dict:
                cur_node = cur_node.sub_path_dict[sub_path]
            else:
                return None

        return cur_node.handler

    def __str__(self):
        output_str = [""]

        def print_node(node, output_str):
            output_str[0] += f"Node handler: {node.handler}\n"
            for sub_path in node.sub_path_dict:
                output_str[0] += f"Sub path: {sub_path}\n"

                print_node(node.sub_path_dict[sub_path], output_str)

        print_node(self.root, output_str)

        return output_str[0]

class RouteTrieNode:
    def __init__(self, handler=None):
        self.handler = handler
        self.sub_path_dict = dict()

    def insert(self, sub_path, handler=None):
        route_trie_node = RouteTrieNode(handler)
        self.sub_path_dict[sub_path] = route_trie_node


class Router:
    def __init__(self, root_handler=None, not_found_handler=None):
        self.route_trie = RouteTrie(handler=root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, request_path, handler):
        self.route_trie.insert(request_path, handler)

    def lookup(self, request_path):
        handler = self.route_trie.find(request_path)

        if handler is None:
            return self.not_found_handler
        else:
            return handler


router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# Test case 1 - look up root handler with path "/"
print("Test case 1 - look up root handler with path '/'")
# should print 'root handler'
print(router.lookup("/"))

# Test case 2 - not found handler with path '/home'
print("Test case 2 - not found handler with path '/home'")
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home"))

# Test case 3 - look up about handler with path '/home/about'
print("Test case 3 - about handler with path '/home/about'")
# should print 'about handler'
print(router.lookup("/home/about"))
