class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        op=0
        add=0
        for ch in s:
            if ch=='(':
                op+=1
            else:
                if op>0:
                    op-=1
                else:
                    add+=1
        return op+add
        
        
        '''st=[]
        count=0

        for ch in s:
            if ch=='(':
                st.append(ch)

            else:
                if len(st)<1:
                    count+=1

                else:
                    st.pop()
#time complexity and space comp is O(n)
        return len(st)+count''' 

        

