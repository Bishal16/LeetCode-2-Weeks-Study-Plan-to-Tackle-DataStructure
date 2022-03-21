class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        hash1={}
        for i in ransomNote:
            if i in hash1:
                hash1[i]= hash1[i]+1
            else:
                hash1[i] = 1
        hash2={}
        for i in magazine:
            if i in hash2:
                hash2[i]= hash2[i]+1
            else:
                hash2[i] = 1        
        
        for i in list(hash1.keys()):            
            if i in list(hash2.keys()):
                if hash1[i] > hash2[i]:
                    return False
            else:                
                return False                        
        return True