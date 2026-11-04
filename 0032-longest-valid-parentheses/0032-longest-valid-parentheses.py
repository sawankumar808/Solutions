class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st=[-1]
        maxlen=0
        for i, ch in enumerate(s):
            if ch=='(':
                st.append(i)
            else:
                st.pop()

                if not st:
                    #aga rkhali hai to reset karo 
                    #left string ko negelct kardo
                    st.append(i)

                else:
                    currlen= i - st[-1]
                    maxlen=max(maxlen, currlen)
        return maxlen


            
        