#LeetCode problem 937: Reorder Data in Log Files
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterLog=[]
        digitLog=[]
        result =[]
        d={}
        for i in logs:
            temp = i.split(" ")            
            if temp[1].isdigit():
                digitLog.append(i)
            else:
                letterLog.append(i)
        letterLog.sort(key = lambda x: x.split()[0])
        letterLog.sort(key = lambda x: x.split()[1:])           
        return letterLog+digitLog