import sys
import heapq


class Node:
    def __init__(self, freq=0, symbol=None, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq


class Tree:
    def __init__(self, root=None):
        self.root = root


def getFreqDict(data):
    char_frequency = dict()
    for char in data:
        char_frequency[char] = char_frequency.get(char, 0) + 1

    return char_frequency


def new_cmp_lt(self, a, b):
    return a.freq < b.freq


heapq.cmp_lt = new_cmp_lt


def createHeap(freqDict):
    heap = []
    heapq.heapify(heap)
    for key in freqDict:
        new_node = Node(freq=freqDict[key], symbol=key)
        heapq.heappush(heap, new_node)
    return heap


def is_leaf_node(node):
    if node.left is None and node.right is None:
        return True
    return False


encodedMap = {}


def visit_node(root, huff_code=''):
    if is_leaf_node(root):
        encodedMap[root.symbol] = huff_code
    else:
        visit_node(root.left, huff_code=huff_code + '0')
        visit_node(root.right, huff_code=huff_code + '1')


def huffman_encoding(data):
    freqDict = getFreqDict(data)
    heap = createHeap(freqDict)
    encodedData = ''
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node1.huff = '0'
        node2 = heapq.heappop(heap)
        node2.huff = '1'
        new_node = Node(left=node1, right=node2, freq=node1.freq + node2.freq)
        heapq.heappush(heap, new_node)
    tree = Tree(root=heap[0])

    visit_node(heapq.heappop(heap))
    for char in data:
        encodedData += encodedMap[char]
    return encodedData, tree


def huffman_decoding(data, tree):
    decoded_data = ''
    node = tree.root
    for bit in data:
        if bit == '0':
            node = node.left
        else:
            node = node.right
        # If a leaf is reached it is possible to match the code so far
        # parsed with its corresponding character
        if is_leaf_node(node):
            # Updates decoded data
            decoded_data += node.symbol
            # Gets back to Huffman tree root
            node = tree.root
    return decoded_data


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
