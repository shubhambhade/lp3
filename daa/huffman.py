import heapq

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''
        
    def __lt__(self, nxt):
        return self.freq < nxt.freq

def print_codes(node, val=''):
    newVal = val + str(node.huff)
    if node.left:
        print_codes(node.left, newVal)
    if node.right:
        print_codes(node.right, newVal)
    if not node.left and not node.right:
        print(f"{node.symbol} -> {newVal}")

def get_input():
    chars = []
    freq = []
    
    n = int(input("Enter the number of characters: "))
    
    for _ in range(n):
        char = input("Enter a character: ")
        f = int(input(f"Enter the frequency for '{char}': "))
        chars.append(char)
        freq.append(f)
    
    return chars, freq

# Main logic
if __name__ == '__main__':
    chars, freq = get_input()
    
    nodes = [Node(freq[x], chars[x]) for x in range(len(chars))]
        
    heapq.heapify(nodes)
        
    while len(nodes) > 1:
        left, right = heapq.heappop(nodes), heapq.heappop(nodes)
        left.huff, right.huff = '0', '1'
        heapq.heappush(nodes, Node(left.freq + right.freq, left.symbol + right.symbol, left, right))
    
    print_codes(nodes[0])
