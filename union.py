class Solution:    
    def findUnion(a, b):
        # code here
        union = set(a)
        
        for num in b:
            union.add(num)
        return list(union)
    

                
