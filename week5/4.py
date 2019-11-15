class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def solution(k, room_number):
    answer = []
    d = {}
    
    dummy = Node(-1)
    prev = dummy
    
    for i in range(1, k + 1):
        node = Node(i)
        prev.next = node
        prev = node
    node.next = Node(-1)
    
    node = dummy.next
    for i in range(1, k + 1, 1):
        d[i] = [0, node]
        node = node.next

    for n in room_number:
        if d[n][0] == 0:
            answer.append(n)
            _, node = d[n]
            curr = node
            while node and d[node.val][0] == 1:
       
                node = node.next
            curr.next = node
            d[n] = [1, curr]
        else:
            _, node = d[n]
            curr = node
            while node and d[node.val][0] == 1:
                print(node.val)
                node = node.next
            answer.append(node.val)
            d[node.val] = [1, node]
            curr.next = node
    return answer


solution(10, [1,3,4,1,3,1])