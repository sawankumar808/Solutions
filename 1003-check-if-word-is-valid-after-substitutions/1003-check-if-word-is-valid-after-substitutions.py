class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for ch in s:
            if ch=='a' or ch=='b':
                st.append(ch)
            else:
                ch=='c' 
                #ab stack ke do element check karne hai dekh lo length 2 hai bhi nahi   
                if len(st)<2:
                    return False 

                if st[-1]!='b':
                    return False
                #if==b
                st.pop()
                if st[-1]!='a':
                    return False
                st.pop()
        if not st:
            return True
        else:
            return False
        


                

                                 


                       

        