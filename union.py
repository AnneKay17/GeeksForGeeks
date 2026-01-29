class Solution:    
    def findUnion(a, b):
        # code here
        union = set(a)
        
        for num in b:
            union.add(num)
        return list(union)
    print(findUnion([1,2,3,3,2], [2,4,5,1,2,6]))
                