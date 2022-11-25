class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        if out_string == "":
            return "Not thing to show"
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    union_ans = LinkedList()
    if llist_1.head is None and llist_2.head is None:
        return None
    set1 = set()
    set2 = set()

    cur1 = llist_1.head
    while cur1:
        set1.add(cur1.value)
        cur1 = cur1.next

    cur2 = llist_2.head
    while cur2:
        set2.add(cur2.value)
        cur2 = cur2.next

    temp = set1.union(set2)
    for i in temp:
        union_ans.append(i)

    return union_ans


def intersection(llist_1, llist_2):
    intersection_ans = LinkedList()
    if llist_1.head is None and llist_2.head is None:
        return None
    set1 = set()
    set2 = set()

    cur1 = llist_1.head
    while cur1:
        set1.add(cur1.value)
        cur1 = cur1.next

    cur2 = llist_2.head
    while cur2:
        set2.add(cur2.value)
        cur2 = cur2.next

    temp = set1.intersection(set2)

    for i in temp:
        intersection_ans.append(i)

    return intersection_ans

# Test case 1


linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

# element_1 = [3,2,4,35,6,65,6,4,3,21]
# element_2 = [6,32,4,9,6,1,11,21,1]

element_1 = [1, 2, 3, 4, 5]
element_2 = [3, 4, 7, 8]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))
