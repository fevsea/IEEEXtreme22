n_nodes, n_phrases = input().rstrip().split(" ")
n_nodes = int(n_nodes)
n_phrases = int(n_phrases)

graph = {}
roots = []

class Node:
    def __init__(self, id, leaf, character=None, language=None, yes=None, no=None):
        self.id = id
        self.character = character
        self.is_leaf = leaf
        self.language = language
        self.yes = yes
        self.no = no
        self.parents = []

    def get_yes(self):
        return graph[self.yes]

    def get_no(self):
        return graph[self.no]



# Construct graph
for _ in range(n_nodes):
    lane = input().rstrip().split(" ")
    if lane[0] == "I":
        id = int(lane[1])
        character = lane[2]
        yes_id = int(lane[3])
        no_id = int(lane[4])
        node = Node(id=id, leaf=False, character=character, yes=yes_id, no=no_id)
        graph[id] = node
    else:
        id = int(lane[1])
        language = lane[2]
        node = Node(id=id, leaf=True, language=language)
        graph[id] = node

# Set parents
for id, node in graph.items():
    if not node.is_leaf:
        graph[node.yes].parents.append(node)
        graph[node.no].parents.append(node)
# Calculate roots
for id, node in graph.items():
    if len(node.parents) == 0:
        roots.append(node)



def get_languages(lane):
    char_set = set(lane)
    potential_languages = []
    unexplored_nodes = list(roots)
    while len(unexplored_nodes) > 0:
        current_node: Node = unexplored_nodes.pop()
        if current_node.is_leaf:
            potential_languages.append(current_node.language)
        else:
            if current_node.character in char_set:
                unexplored_nodes.append(current_node.get_yes())
            else:
                unexplored_nodes.append(current_node.get_yes())
                unexplored_nodes.append(current_node.get_no())
    potential_languages.sort()
    return potential_languages


for i in range(n_phrases):
    lane = input()
    languages = get_languages(lane)
    print(" ".join(languages))
