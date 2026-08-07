class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        psum={} 
        currsum=0
        maxi=0
        for i,num in enumerate(hours):
            if num>8:
                currsum+=1
            else:
                currsum-=1
            if currsum>0:
                maxi=i+1
            
            else: 
                if currsum-1 in psum:
                    length= i-psum[currsum-1]
                    maxi=max(maxi,length) 
                
            if currsum not in psum:

                psum[currsum]=i
        return maxi

            

    

        