class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for ch  in s:
            if ch=='(' or ch=='[' or ch=='{':
                st.append(ch)
            else:
                if not st:
                    return False

                if ch==')' and st[-1]!='(':
                    return False

                elif ch==']' and st[-1]!='[':
                    return False
                elif ch=='}' and st[-1]!='{':
                    return False
                    
                else:
                    st.pop()
        #check karo ki stack empty huwa ki nahi 
        return not st
        
        