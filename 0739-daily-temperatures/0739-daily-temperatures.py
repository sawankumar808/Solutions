class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n=len(temperatures)
        ans=[0] * n
        st=[]

        for i in range(n):
            while st and temperatures[i] > temperatures[st[-1]]:
                previousday=st.pop()
                ans[previousday]= i - previousday
            st.append(i)
        return ans

        

        #brute force approach n*2 tc  
        # n=len(temperatures)
        # ans=[0] * n

        # for i in range(len(temperatures)):
        #     for j in range(i+1, len(temperatures)):
        #     #i ko move karna hai jabtak bada number number nahi milta hai
        #         if temperatures[j] > temperatures[i]:
        #             ans[i]=j-i 
        #             break
        # return ans
        
        