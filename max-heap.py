
# Math
# Left node: 2*i + 1
# Right node: 2*i + 2

#   0  1  2  3  4  5  6 
# [ 50 35 45 15 20 25 30  ---  36]  => Length: 8


class MaxHeap:

    def __init__(self):
        self.array = list()

    def is_empty(self) -> bool:
        return len(self.array) == 0

    def insert(self, num: int):
        self.array.append(num)
        self._swim()
        print(self.array)

    def peek(self,) -> int:
        if len(self.array) == 0:
            return -1
        if len(self.array) == 1:
            return self.array.pop()
        self.array[0], self.array[-1] = self.array[-1], self.array[0]
        max_ele = self.array.pop()
        self._sink()
        print(self.array)

        return max_ele
    
    def _sink(self,):

        to_sink_ith = 0

        while to_sink_ith <= len(self.array):
            # Make a general case: look for existance of childs, find the one with
            # biggest value, exchange with parent, keep sinking value till reaching
            # a leaft node (no more childs)

            node = self.array[to_sink_ith]
            left_node_ith = 2 * to_sink_ith + 1
            right_node_ith = 2 * to_sink_ith + 2

            if self.is_node_leaf(to_sink_ith):
                break

            to_promote_ith = self.promoted_child_ith(left_node_ith, right_node_ith)

            if node < self.array[to_promote_ith]:
                self._swap(to_sink_ith, to_promote_ith)
                to_sink_ith = to_promote_ith
            else:
                break
 
    def _swim(self):
        child_ith = len(self.array) - 1

        # Left node: 2*i + 1
        # Right node: 2*i + 2
        # Decide offset based on wether appended node is either a
        # left or right child
    
        child_offset = 2 if child_ith % 2 == 0 else 1
        parent_ith = (child_ith - child_offset) // 2

        while parent_ith >= 0:
            child_node = self.array[child_ith]
            parent_node = self.array[parent_ith]

            if child_node >= parent_node:
                self.array[child_ith], self.array[parent_ith] = self.array[parent_ith], self.array[child_ith]
            else:
                break

            child_ith = parent_ith
            child_offset = 2 if child_ith % 2 == 0 else 1
            parent_ith = (child_ith - child_offset) // 2
        
        return None

    def _swap(self, parent_ith, child_ith):
        self.array[parent_ith], self.array[child_ith] = (
            self.array[child_ith], self.array[parent_ith]
        )

    def is_node_leaf(self, ith: int) -> bool:
        return (
            2 * ith + 1 >= len(self.array) and
            2 * ith + 2 >= len(self.array)
        )
    
    def promoted_child_ith(self, left_ith: int, right_ith: int) -> int:
        if left_ith >= len(self.array):
            return right_ith
        if right_ith >= len(self.array):
            return left_ith

        return left_ith if self.array[left_ith] > self.array[right_ith] else right_ith


def main():
    heap  = MaxHeap()

    heap.insert(50)
    heap.insert(60)
    heap.insert(40)
    heap.insert(100)
    heap.insert(70)
    heap.insert(50)
    heap.insert(55)
    heap.peek()
    heap.peek()
    heap.peek()
    heap.peek()
    heap.peek()
    heap.peek()
    print("-"*50)
    another_heap = MaxHeap()
    for i in range(1,11):
        another_heap.insert(i)
    for _ in range(1, 11):
        another_heap.peek()


main()
