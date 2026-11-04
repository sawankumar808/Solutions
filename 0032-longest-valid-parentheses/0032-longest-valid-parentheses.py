class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxlen = 0
        op=0
        close=0
        
        for ch in s:
            if ch=='(':
                op+=1
            else:
                close+=1

            if close>op:
                op=0
                close=0
            elif op==close:
                maxlen=max(maxlen,2*op )
        op=0
        close=0
        for ch in reversed(s):
            if ch=='(':
                op+=1
            else:
                close+=1

            if op>close:
                op=0
                close=0
            elif op==close:
                maxlen=max(maxlen, 2*op)
        return maxlen




        #iski tc or sc O(n) hai kyu stack use kiya 
        '''st=[-1]
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
'''

            
        