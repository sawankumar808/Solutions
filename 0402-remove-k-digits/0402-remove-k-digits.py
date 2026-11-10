class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ans=""
        st=[]
        for ch in (num):
            while st and k>0 and ch < st[-1]:
                st.pop()
                k-=1
            st.append(ch) 
        # agr abhi bhi removeble bach rhe to piche se hata do

        if k>0:
            st=st[:-k]
        result = "".join(st).lstrip('0')
                              
        return result if result else '0'

        
                                                                                                                                                                                                                                                             


          

        