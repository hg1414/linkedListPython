from linkedListSimple import Node

node4 = Node(4)
node3 = Node(3, node4)
node2 = Node(2, node3)
node1 = Node(1, node2)
node0 = Node(0, node1)
print(len(node0))