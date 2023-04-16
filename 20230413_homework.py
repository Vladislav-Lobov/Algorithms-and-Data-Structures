# Домашняя работа от 04 семинара (13 апреля 2023г.) студента группы 3306 Лобова В.В.

# Необходимо превратить собранное на семинаре дерево поиска в полноценное
# левостороннее (по желанию можно обычное) красно-черное дерево.
# И реализовать в нем метод добавления новых элементов с балансировкой.

# Красно-черное дерево имеет следующие критерии:
# • Каждая нода имеет цвет (красный или черный)
# • Корень дерева всегда черный
# • Новая нода всегда красная
# • Красные ноды могут быть только левым ребенком
# • У красной ноды все дети черного цвета

# Соответственно, чтобы данные условия выполнялись, после добавления
# элемента в дерево необходимо произвести балансировку, благодаря которой
# все критерии выше станут валидными. Для балансировки существует 3 операции –
# левый малый поворот, правый малый поворот и смена цвета.

import turtle


class Node:

    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        self.color = "red"


class Tree:

    COLOR_RED = "red"
    COLOR_BLACK = "black"

    def __init__(self):
        self.root = None

    def __find(self, node, parent, value):
        """Старая функция с семинара, ищет место для вставки"""
        if node is None:
            return None, parent, False

        if value == node.data:
            return node, parent, True

        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False

    def append(self, obj):
        obj.color = Tree.COLOR_BLACK
        """Старая функция с семинара, которая вставляет элементы в дерево без балансировки"""
        if self.root is None:
            self.root = obj
            return obj

        s, p, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj

        return obj

    def rotate_left(self, my_node):
        """Метод для поиска и правого вращения ноды на одну ступень к левой части дерева """
        child = my_node.right
        child_left = child.left
        child.left = my_node
        my_node.right = child_left
        return child

    def rotate_right(self, my_node):
        """Метод для поиска и левого вращения ноды на одну ступень к правой части дерева """
        child = my_node.left
        child_right = child.right
        child.right = my_node
        my_node.left = child_right
        return child

    def is_red(self, my_node):
        """ Метод проверяет, есть ли у данной ноды ненулевое значение,
        а затем и ее цвет равен ли он красному """
        return my_node != None and my_node.color == Tree.COLOR_RED

    def swap_colors(self, node1, node2):
        """ Метод меняет цвета нод """
        temp = node1.color
        node1.color = node2.color
        node2.color = temp

    def insert(self, data):
        """ Метод вставляет ноду с указанным значением в дерево.
        Если нет корневой ноды, то нода создается и устанавливается как корневая """
        node = None
        if self.root:
            node = self.insert_balance(self.root, data)
            if not node:
                return False
        else:
            node = Node(data)
        self.root = node
        self.root.color = Tree.COLOR_BLACK
        return True

    def insert_balance(self, my_node, data):
        """ Метод для того, чтобы дерево было сбалансированным """
        if my_node == None:
            return Node(data)
        if my_node.data > data:
            my_node.left = self.insert_balance(my_node.left, data)
        elif my_node.data < data:
            my_node.right = self.insert_balance(my_node.right, data)
        else:
            return None
        return self.balanced(my_node)

    def balanced(self, my_node):
        """ Метод проверяет, есть ли у ноды левый или правый указатель,
        после чего зависит от этого вызывается ли метод balanced """
        if self.is_red(my_node.right) and not self.is_red(my_node.left):
            my_node = self.rotate_left(my_node)
            self.swap_colors(my_node, my_node.left)
        if self.is_red(my_node.left) and self.is_red(my_node.left.left):
            my_node = self.rotate_right(my_node)
            self.swap_colors(my_node, my_node.right)
        if self.is_red(my_node.left) and self.is_red(my_node.right):
            my_node.color = Tree.COLOR_RED
            my_node.left.color = Tree.COLOR_BLACK
            my_node.right.color = Tree.COLOR_BLACK
        return my_node

    """ отображение дерева с помощью черепашьей графики """

    def draw_tree(self, starting_y, scale):
        """ инициализируем экран, черепашью графику и задаем размеры """
        screen = turtle.Screen()
        screen.bgcolor("white")
        t = turtle.Turtle()
        t.speed(0)
        t.penup()
        t.goto(0, -200)
        t.pendown()

        def draw_node(node, x, y):
            """ определяем функцию для отображения узла """
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.color(node.color)
            t.circle(20)
            t.color(Tree.COLOR_BLACK)
            t.penup()
            t.goto(x, y - 20)
            t.write(node.data, align="center", font=("Arial", 12, "normal"))

        def draw_edge(x1, y1, x2, y2):
            """ определяем функцию для отображения ребер """
            t.penup()
            t.goto(x1, y1)
            t.pendown()
            t.goto(x2, y2)

        def draw_subtree(node, x, y, dx):
            """ определяем рекурсивную функцию для отображения всего дерева """
            if node is None:
                return
            draw_node(node, x, y)
            left_child = node.left
            right_child = node.right
            if left_child is not None:
                x_left = x - dx
                y_left = y - 60
                draw_edge(x, y - 30, x_left, y_left + 30)
                draw_subtree(left_child, x_left, y_left, dx / 2)
            if right_child is not None:
                x_right = x + dx
                y_right = y - 60
                draw_edge(x, y - 30, x_right, y_right + 30)
                draw_subtree(right_child, x_right, y_right, dx / 2)

        """ вызываем рекурсивную функцию и заканчиваем отображение """
        draw_subtree(self.root, 0, starting_y, scale)
        t.hideturtle()


v = [3, 1, 2, 10, 8, 4, 5, 7, 6, 9, 20, 15, 18, 25]

simple_tree = Tree()
for x in v:
    simple_tree.append(Node(x))

turtle.hideturtle()
turtle.penup()
turtle.goto(-280, 350)
turtle.write(
    "Бинарное дерево (версия с семинара, \nвставка без балансировки):",
    move=False,
    align="center",
    font=("Arial", 16, "normal"))
simple_tree.draw_tree(starting_y=330, scale=150)

balanced_tree = Tree()
for x in v:
    balanced_tree.insert(x)

turtle.hideturtle()
turtle.penup()
turtle.goto(-295, -50)
turtle.write(
    "Сбалансированное левостороннее \nкрасно-черное дерево \n(вставка с балансировкой): ",
    move=False,
    align="center",
    font=("Arial", 16, "normal"))
balanced_tree.draw_tree(starting_y=-140, scale=150)
turtle.done()
