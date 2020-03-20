"""Zakładam (patrząc na rysunek), że drzewo nie jest zbalansowane
    TO DO: Testy, opis co to przedstawia
"""


class Tree:
    def __init__(self, n=0, left=None, right=None):
        self.value = n
        self.leftTree = left
        self.rightTree = right

    def sum_subtree_values(self):
        to_return = self.value
        if self.leftTree is not None:
            to_return += self.leftTree.sum_subtree_values()
        if self.rightTree is not None:
            to_return += self.rightTree.sum_subtree_values()
        return to_return

    def __subtree_node_quantity(self):
        to_return = 1
        if self.leftTree is not None:
            to_return += self.leftTree.__subtree_node_quantity()
        if self.rightTree is not None:
            to_return += self.rightTree.__subtree_node_quantity()
        return to_return

    def mean_value(self):
        return self.sum_subtree_values() / self.__subtree_node_quantity()

    def __get_subtree_values(self):
        to_return = [self.value]
        if self.leftTree is not None:
            to_return.extend(self.leftTree.__get_subtree_values())
        if self.rightTree is not None:
            to_return.extend(self.rightTree.__get_subtree_values())
        return to_return

    def median_value(self):
        q = self.__subtree_node_quantity() / 2
        tab = self.__get_subtree_values()
        tab.sort()
        print(tab)
        if q == 0:
            return tab[0]
        elif q.is_integer():
            return (tab[int(q - 1)] + tab[int(q)]) / 2
        else:
            return tab[int(q - 1)]

    def __str__(self):
        to_return = "[" + str(self.value)

        if self.leftTree is not None:
            to_return += Tree.__str__(self.leftTree)
        else:
            to_return += "[]"
        if self.rightTree is not None:
            to_return += Tree.__str__(self.rightTree)
        else:
            to_return += "[]"
        to_return += "]"
        return to_return

# tree = Tree(1, Tree(2), None)
# #tree = Tree(10, Tree(100, t), Tree(100, t))
# #tree = Tree(5,Tree(3, Tree(2), Tree(5)),Tree(7, Tree(1), Tree(0, Tree(2), Tree(8, None, Tree(5)))))
# print(tree)
# print(tree.sum_subtree_values())
# # print(tree.__subtree_node_quantity())
# print(tree.median_value())
