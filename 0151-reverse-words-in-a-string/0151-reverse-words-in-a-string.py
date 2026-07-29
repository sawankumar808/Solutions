class Solution:
    def reverseWords(self, s: str) -> str:
       word=[]
       n=len(s)
       i=n-1
       while(i>=0):
        while(i>=0 and s[i]==" "):
            i-=1
        if(i<0):
            break
        j=i
        while(i>=0 and s[i]!=" "):
            i-=1
        word.append(s[i+1: j+1])
        
        
       return " ".join(word)

        


    

        