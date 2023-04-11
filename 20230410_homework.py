# Домашняя работа от 03 семинара (10 апреля 2023г.) студента группы 3306 Лобова В.В.
# Необходимо реализовать метод разворота односвязного списка 


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next_node = None

    def __str__(self):
        return self.value


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next_node:
            last_node = last_node.next_node
        last_node.next_node = new_node

    def print_linked_list(self):
        node = self.head
        if node is None:
            return "Список пуст"
        result = ""
        while node:
            result += f"{node.__str__()}" + " "
            node = node.next_node
        return result
    
    def reverse_list(self):
        head = self.head
        tail = None
        while head:
            head.next_node, tail, head = tail, head, head.next_node
        self.head = tail
        

     
a = LinkedList()
a.add_to_end(21)
a.add_to_end(43)
a.add_to_end(65)
a.add_to_end(87)
a.add_to_end(98)
print('Имеем односвязный список: ')
print(a.print_linked_list())
print('Развернутый список: ')
a.reverse_list()
print(a.print_linked_list())


