class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictt1, dictt2 = {}, {}

        for i,item in enumerate(s):
            if item not in dictt1:
                dictt1[item] = 0
            dictt1[item] += 1

        for j,item in enumerate(t):
            if item not in dictt2:
                dictt2[item] = 0
            dictt2[item] += 1
 
        if dictt1 == dictt2:
            return True
        else:
            return False
            