# Challenge description:
# Design and implement a data structure for Least Frequently Used (LFU) cache. It should
# support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the
# cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the
# cache reaches its capacity, it should invalidate the least frequently used item before
# inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or
# more keys that have the same frequency), the least recently used key would be evicted.

# Note that the number of times an item is used is the number of calls to the get and put
# functions for that item since it was inserted. This number is set to zero when the item
# is removed.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:

# LFUCache cache = new LFUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.get(3);       // returns 3.
# cache.put(4, 4);    // evicts key 1.
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4

class LFUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        :rtype: none
        """
        self.capacity = capacity
        self.size = 0
        self.keys = [None] * capacity # store keys
        self.vals = [None] * capacity # store values
        self.usage = [0] * capacity # track num times put and get
        self.time = [0] * capacity # track last time it was used (steps)

    # increment time array
    def incrementTime(self):
        for i in range(self.size):
            self.time[i] += 1
        return

    # return list of least used index / indices
    def leastUsed(self):
        output = [0]
        minimum = self.usage[0]
        for i in range(0,self.size):
            if self.usage[i] > minimum:
                continue
            elif self.usage[i] == minimum:
                output.append(i)
            else:
                output = [i]
                minimum = self.usage[i]
        return output

    # return last used index
    def lastUsed(self, removed):
        maximum = 0
        cut = 0
        for index in removed:
            if self.time[index] > maximum:
                maximum = self.time[index]
                cut = index
        return cut

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # print("keys: " + str(self.keys))
        # print("vals: " + str(self.vals))
        try:
            i = self.keys.index(key)
            self.usage[i] += 1
            self.incrementTime()
            self.time[i] = 0
            return self.vals[i]
        except:
            return -1
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: none
        """
        # print("keys: " + str(self.keys))
        # print("vals: " + str(self.vals))
        if self.capacity == 0:
            return
        if key in self.keys:
            i = self.keys.index(key)
            self.vals[i] = value
            self.usage[i] += 1
            self.incrementTime
            self.time[i] = 0
            return

        if self.size < self.capacity:
            self.keys[self.size], self.vals[self.size] = key, value
            self.incrementTime()
            self.usage[self.size] = 1
            self.size += 1
            return

        else:
            i = self.leastUsed()
            if len(i) > 1:
                i = self.lastUsed(i)
            else:
                i = i[0]
            self.keys[i], self.vals[i] = key, value
            self.incrementTime()
            self.usage[i] = 1
            self.time[i] = 0
            return

if __name__ == '__main__':
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    check1 = cache.get(1)       # returns 1
    cache.put(3, 3)    # evicts key 2
    check2 = cache.get(2)       # returns -1 (not found)
    check3 = cache.get(3)       # returns 3.
    cache.put(4, 4)    # evicts key 1.
    check4 = cache.get(1)       # returns -1 (not found)
    check5 = cache.get(3)       # returns 3
    check6 = cache.get(4)       # returns 4

    cache2 = LFUCache(0)
    cache2.put(0,0)
    check7 = cache2.get(0)      # returns -1

    cache3 = LFUCache(1)
    cache3.put(0,0)
    check8 = cache3.get(0)      # return 0

    cache4 = LFUCache(2)
    cache4.put(2,1)
    cache4.put(2,2)
    check9 = cache4.get(2)      # return 2
    cache4.put(1,1)
    cache4.put(4,1)
    check10 = cache4.get(2)     # return 2

    cache5 = LFUCache(2)
    cache5.put(2,1)
    cache5.put(2,2)
    check11 = cache5.get(2)     # return 2
    cache5.put(1,1)
    cache5.put(2,1)
    check12 = cache5.get(2)     # return 1

    cache6 = LFUCache(2)
    cache6.put(2,6)
    check13 = cache6.get(1)     # return -1
    cache6.put(1,5)
    check14 = cache6.get(1)     # return 5
    cache6.put(1,2)
    check15 = cache6.get(1)     # return 2
    check16 = cache6.get(2)     # return 6

    cache7 = LFUCache(2)
    cache7.put(2,1)
    cache7.put(1,1)
    cache7.put(2,3)
    cache7.put(4,1)
    check17 = cache7.get(1) # return -1
    check18 = cache7.get(2) # return 3

    assert check1 == 1
    assert check2 == -1
    assert check3 == 3
    assert check4 == -1
    assert check5 == 3
    assert check6 == 4
    assert check7 == -1
    assert check8 == 0
    assert check9 == 2
    assert check10 == 2
    assert check11 == 2
    assert check12 == 1
    assert check13 == -1
    assert check14 == 5
    assert check15 == 2
    assert check16 == 6
    assert check17 == -1
    assert check18 == 3



