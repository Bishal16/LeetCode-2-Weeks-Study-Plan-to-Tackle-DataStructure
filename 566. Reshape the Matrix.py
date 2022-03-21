class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        if r*c != len(mat)*len(mat[0]):
            return mat
        
        ans=[]
        x,t =0,[]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                t.append(mat[i][j]) 
                x+=1
                if x==c:
                    x=0
                    ans.append(t)
                    t=[]                          
        return ans
    
    
    
    