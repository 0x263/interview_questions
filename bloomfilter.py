"""
Bloomfilter
    Create a data structure that determines whether a combination of hashes has been seen before.
        * If every hash in the list has been seen before, then return True. Otherwise, return False.
        * False positives are tolerable but never have false negatives.

    Functions:
        * add: mark a list of hashes as seen
        * check: check whether a list of hashes has been seen before
        * remove: mark a list of hashes as invalid or unseen
"""

class Bloomfilter():
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [0 for _ in range(capacity)]
    
    def add(self, list_hashes):
        for h in list_hashes:
            self.table[h % self.capacity] += 1
    
    def check(self, list_hashes):
        for h in list_hashes:
            if self.table[h % self.capacity] < 1:
                return False
        
        return True
    
    def remove(self, list_hashes):
        if self.check(list_hashes) == False:
            return
        
        for h in list_hashes:
            mod_calc = h % self.capacity
            if self.table[mod_calc] > 0:
                self.table[mod_calc] -= 1

    
    def __str__(self):
        return ','.join([str('%d(%d)' % (i, self.table[i])) for i in range(self.capacity) if self.table[i] != 0])
        


def run_tests():
    bloom_filter = Bloomfilter(100)
    
    bloom_filter.add([1, 2, 3])
    bloom_filter.add([2, 3, 4])
    bloom_filter.add([3, 4, 5])
    
    print(bloom_filter.check([1, 3, 5])) # True
    print(bloom_filter.check([1, 2, 4])) # True
    print(bloom_filter.check([5, 6, 7])) # False
    
    bloom_filter.remove([1, 2, 3])
    print(bloom_filter.check([1, 2, 3])) # return False
    
    bloom_filter.add([1, 2, 3])
    print(bloom_filter.check([1, 2, 3])) # return True
    

    bloom_filter.remove([3, 5, 7])
    print(bloom_filter)

    
if __name__ == '__main__':
    run_tests()