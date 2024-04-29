import math
class SqRtDecomposition():
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.block_size = int(math.sqrt(self.n))
        self.block = [0] * self.block_size
        self.id = -1
    def preprocess(self):
        for i in range(self.n):
            if i % self.block_size == 0:
                self.id += 1
    
            self.block[self.id] += self.arr[i]
        
    def query(self, l, r):
        sum = 0

        while(l <= r):
            if(l % self.block_size == 0 and l+self.block_size - 1 <= r):
                sum+= self.block[l//self.block_size]
                l+= self.block_size
                
            sum+= self.arr[l]
            l+=1
            
        print("query ", sum )

        
a = SqRtDecomposition([0, 1, 2, 3, 4, 5, 7, 7, 8])
a.preprocess()
a.query(6, 7)

