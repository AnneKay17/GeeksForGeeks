from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        freqA = Counter(a)
        freqB = Counter(b)

        for key, value in freqB.items():
            if key in freqA:
                if value <= freqA.get(key):
                    continue
                else:
                    return False
            else:
                return False
        return True
        
    
    
    
    
