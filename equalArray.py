from collections import Counter

class Solution:
    def checkEqual(a, b) -> bool:
        #code here
        freqA = Counter(a)
        freqB = Counter(b)
        
        for key, value in freqA.items():
            if key in freqB:
                if value == freqB.get(key):
                    continue
                elif value != freqB.get(key):
                    return False
        return True



    
