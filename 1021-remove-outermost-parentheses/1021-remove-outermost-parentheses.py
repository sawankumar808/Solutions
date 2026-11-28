class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        st=[]
        depth=0
        for ch in s:
            if ch=='(': #agr ( ye hai to depth bda do
                if depth>0: #agr depth badi hai tp append
                    st.append(ch)
                depth+=1
            else:
                depth-=1
                if depth>0:
                    st.append(ch)

        return "".join(st)
            
        
    