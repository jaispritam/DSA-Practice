#leet code
#59. Spiral Matrix II

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        db = [[0] * n for _ in range(n)]   
        num = 1    
        layer = 0    
        while layer  <  (n+1) //  2   :   
            for i in  range (layer,n-layer) :     
                db[layer][i] =  num  
                num +=  1     
            for i in  range (layer + 1 , n - layer)  :   
                db[i][n-1-layer] =  num   
                num +=  1    
            if n - 1 - layer !=  layer :   
                for i in range  (n-layer-2 ,  layer-1, -1)  :   
                    db[n-1-layer][i]= num   
                    num +=  1   
            if n-1-layer  !=  layer  :    
                for i in  range  (n-2-layer ,  layer , -1) :  
                    db[i][layer] =  num     
                    num +=  1    
            layer +=  1    
        return db
