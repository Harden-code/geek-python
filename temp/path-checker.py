json = [{'id': 1, 'name': 'root', 'value': 1, 'paren_root': 0},
        {'id': 2, 'name': 'A', 'value': 2, 'paren_root': 1},
        {'id': 3, 'name': 'B', 'value': 3, 'paren_root': 1},
        {'id': 4, 'name': 'C', 'value': 4, 'paren_root': 2},
        {'id': 5, 'name': 'D', 'value': 5, 'paren_root': 2},
        {'id': 6, 'name': 'E', 'value': 6, 'paren_root': 2},
        {'id': 7, 'name': 'F', 'value': 7, 'paren_root': 3},
        {'id': 8, 'name': 'G', 'value': 8, 'paren_root': 3},
        {'id': 9, 'name': 'H', 'value': 9, 'paren_root': 4},
        {'id': 10, 'name': 'I', 'value': 11, 'paren_root': 5},
        {'id': 11, 'name': 'J', 'value': 11, 'paren_root': 6},
        {'id': 12, 'name': 'K', 'value': 12, 'paren_root': 7},
        {'id': 13, 'name': 'L', 'value': 13, 'paren_root': 8}]

from anytree import Node, RenderTree

result = []


def dfs(rootNode, rootValue, list, result):
    for v in list:
        if v['paren_root'] == rootValue['id']:
            node = Node(v['name'], parent=rootNode)
            dfs(node, v, list, result)
            # process
            result.append(v['value'])
            print(v['id'], result)

# build root
rootValue = {'id': 1, 'name': 'root', 'value': 1, 'paren_root': 0}
root = Node(rootValue['name'])
dfs(root, rootValue, json, result)
# print
for pre, fill, node in RenderTree(root):
    print("%s%s" % (pre, node.name))

from graphviz import Digraph

dot = Digraph()

def add_node(node):
    if node.parent:
        dot.edge(node.parent.name, node.name)
    for child in node.children:
        dot.node(node.name, node.name)
        add_node(child)

# Add nodes to the graphviz Digraph object
add_node(root)

# Render the graphviz Digraph object as a PNG image
dot.render('tree.png', view=True)
