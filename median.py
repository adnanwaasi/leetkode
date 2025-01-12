class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l=nums1+nums2
        l.sort()
        length =len(l)
        out=[]
        ret=0
        if length%2==1:
            b=length // 2 
            ret=l[b]
        else:
            b=length // 2 -1
            c=length // 2 
            ret=l[b]+l[c]
            ret=ret/2 
        return ret
