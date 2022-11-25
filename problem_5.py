from dataclasses import dataclass
import datetime
import time
import hashlib
import random

class Block:

    def __init__(self, previous_hash, data):
        self.previous_hash = previous_hash
        self.data = str(data)
        self.timestamp = datetime.datetime.now(datetime.timezone.utc)
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(self.previous_hash.encode('utf-8'))
        sha.update(str(self.timestamp).encode('utf-8'))
        sha.update(self.data.encode('utf-8'))
        return sha.hexdigest()

    def __repr__(self):
        repr_str  = 'hash: {}'.format(self.hash)
        repr_str += '\tprevious hash: {}'.format(self.previous_hash)
        repr_str += '\ttimestamp: {}'.format(self.timestamp)
        repr_str += '\tdata: {}'.format(self.data)
        return repr_str 


class Node:
    def __init__(self, index, block, previous_block) -> None:
        self.index = index
        self.block = block
        self.previous = previous_block
    

class Blockchain:

    def __init__(self) -> None:
        self.index = 0
        first_block = Block('0'*64, '1')
        self.head = Node(self.index, first_block, None)

    def append(self, data):
        self.index += 1
        temp_block = Block(self.head.block.hash, data)
        temp_node = Node(self.index, temp_block, self.head)
        self.head = temp_node

    def __repr__(self):
        node = self.head
        repr_str = ''
        while node is not None:
            repr_str += '\nblock index: {}\n'.format(node.index)
            repr_str += str(node.block)
            node = node.previous
        repr_str += '\n'
        return repr_str 


    
print('# Testcase 1: Create block chain with only 1 first block')
my_blockchain = Blockchain()
print(my_blockchain)   # block index: 0 expect data: 1 with timestamp


print('# Testcase 2: add two more block with timeskip=0.5 second')
my_blockchain = Blockchain()
time.sleep(0.5)
my_blockchain.append('2')
time.sleep(0.5)
my_blockchain.append('3')
print(my_blockchain)        
                            # block index: 0 expect data: 3 with timestamp + 0.5
                            # block index: 0 expect data: 2 with timestamp + 0.5
                            # block index: 0 expect data: 1 with timestamp


print('# Testcase 3: add two more block without timeskip')
my_blockchain.append('4')
my_blockchain.append('5')
print(my_blockchain)    
                        # block index: 0 expect data: 3 with timestamp_testcase3
                        # block index: 0 expect data: 3 with timestamp_testcase3
                        # block index: 0 expect data: 3 with timestamp_testcase2 + 0.5
                        # block index: 0 expect data: 2 with timestamp_testcase2 + 0.5
                        # block index: 0 expect data: 1 with timestamp


print('# Testcase 4: add alot more block without timeskip')
for i in range(8888):
    data = str(random.random())
    my_blockchain.append(data)

curr_node = my_blockchain.head

print('Print out 5 last nodes')
for _ in range(5):
    print('index: {}'.format(curr_node.index))
    print(curr_node.block)
    curr_node = curr_node.previous