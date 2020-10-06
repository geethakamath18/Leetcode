#LeetCode problem 692: Top K Frequent Words
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d=dict()
        a=[]
        for i in words:
            d[i]=d.get(i,0)+1
        res=sorted(d.items(),key=lambda item: (-item[1], item[0]))
        for i, j in res:
            a.append(i)
        return(a[:k])