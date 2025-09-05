class minHeap:
    def __init__(self):
        self.heap_array = []
        self.element_counter = 0

    def left_child(self, parent):
        return 2 * parent + 1


    def right_child(self, parent):
        return 2 * (parent + 1)


    def parent(self, child):
        return (child - 1) // 2


    def swap(self, i, j):
        if i != j:
            temp = self.heap_array[i]
            self.heap_array[i] = self.heap_array[j]
            self.heap_array[j] = temp

    def element_count(self):
        return self.element_counter if self.element_counter > 0 else 0

    def add(self, val):
        self.heap_array.append(val)
        self.element_counter += 1
        self.bubbleUp(self.element_counter - 1)


    def bubbleUp(self, index):
        while self.heap_array[self.parent(index)] > self.heap_array[index] and index > 0:
            par_index = self.parent(index)
            self.swap(index, par_index)
            index = self.parent(index)


    def peek(self):
        return self.heap_array[0] if self.element_counter > 0 else None
    

    def remove(self):
        """Returns current min while maintaining min-heap property.
        
        After removing and saving the current min, the last element of the array is placed at the front
        and then bubbled down to maintain min-heap property. The removed min is then returned. If there are
        no values in the heap_array, returns None.

        Returns:
        Current minimum value of heap_array.
        """
        removed = None
        if self.element_counter != 0:
            removed = self.heap_array[0]
            if self.element_counter == 1:
                self.heap_array.pop()
                self.element_counter -= 1
            else:
                self.heap_array[0] = self.heap_array.pop()
                self.element_counter -= 1
                self.bubbleDown(0)
        return removed


    def bubbleDown(self, index):
        child_index = self.leftOrRight(index)
        while child_index != -1 and self.heap_array[index] > self.heap_array[child_index]:
            # swap values down, adjust indices
            self.swap(index, child_index)
            index = child_index
            child_index = self.leftOrRight(index)



    def leftOrRight(self, index):
        """Returns left/right child index if either are available.

        Helper method for bubbleDown(index). If one child is absent from a node on
        the tree, returns the index for the other child. If there are no children,
        return -1.

        Args: 
        index: Index of parent.

        Returns: 
        Index of available child.
        """
        left_index = self.left_child(index)
        right_index = self.right_child(index)
        if left_index and right_index > 0 and left_index and right_index < self.element_counter:
            leftie = self.heap_array[left_index]
            rightie = self.heap_array[right_index]
            if not leftie and rightie:
                return self.right_child(index)
            if leftie:
                return self.left_child(index)
        return -1