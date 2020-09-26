#LeetCode problem 401: Binary Watch
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        hours={}
        minutes={}
        res=[]
        for i in range(0,12):
            hours[i]=str(bin(i)).count('1')
        hkey=list(hours.keys())
        for i in range(0,60):
            minutes[i]=str(bin(i)).count('1')
        mkey=list(minutes.keys())
        for i in range(len(hours)):
            for j in range(len(minutes)):
                if hours[i]+minutes[j]==num and mkey[j]<10:
                    res.append(str(hkey[i])+":0"+str(mkey[j]))
                elif hours[i]+minutes[j]==num and mkey[j]>=10:
                    res.append(str(hkey[i])+":"+str(mkey[j]))
                    
        return res
                    
                