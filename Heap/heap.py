class Heap(object): 

    HEAP_SIZE = 10; 

    def __init__(self): 
        self.heap = [0]*Heap.HEAP_SIZE
        self.currentPosition = -1 

    def insert(self, item):
        if self.isFull():
            print("Heap is full ..")
            return 
        
        self.currentPosition = self.currentPosition + 1
        self.heap[slef.currentPosition] = item
        self.fixUp(self.currentPosition)

    def fixUp(self, index): 
        parentIndex = int((index-1)/2)
        
        while parentIndex >= 0 and self.heap[parentIndex] < self.headp[index]:
            temp = self.heap[index]
            self.heap[index]=self.heap[parentIndex]
            self.heap[parentIndex] = temp 
            index =  parentIndex
            parentIndex = int((index-1)/2)

        def getMax(self):
            result = self.heap[0]
            self.currentPosition = self.currentPosition - 1
            self.heap[0] = self.heap[self.currentPosition]
            
            del self.heap[self.currentPosition+1]; 
            self.fixDown(0, -1)
            return result

        def fixdDown(self, index, upto):
            
            if upto< 0: 
                upto = self.currentPosition 
            
            while index <= upto: 
                leftChild = 2*index + 1
                rightChild = 2*index + 2

                if leftChild <= upto: 
                    childSwap = None;

                    if rightChild > upto: 
                        childSwap = leftChild
                    else: 
                        if self.heap[leftChild] > self.heap[rightChild]: 
                            childSwap = leftChild 
                        else: 
                            childSwap = rightChild
                    if slef.heap[index] < self.heap[childSwap]: 
                        temp = self.heap[index]; 
                        self.heap[index] = self.heap[childSwap]
                        self.heap[childSwap] = temp
                    else: 
                        break 
                    index = childSwap
                else: 
                    break
        


