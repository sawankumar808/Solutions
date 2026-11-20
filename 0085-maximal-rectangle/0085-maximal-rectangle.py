class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        rows=len(matrix)
        col=len(matrix[0])

        heights=[0]*col
        maxArea=-1
        for i in range(rows):
            for j in range(col):
                if matrix[i][j]=='1':
                    heights[j]+=1
                else:
                    heights[j]=0


            area = self.getMaxArea(heights)
            maxArea=max(maxArea, area)
        return maxArea

    def getMaxArea(self, heights):
        n=len(heights)

        prev=[-1]*n
        nxt=[n]*n
        self.findPreviousSmaller(heights, prev)
        self.findNextSmaller(heights, nxt)
         
        maxArea=-1
        for i in range(n):
            height=heights[i]
            width=nxt[i]-prev[i]-1
            area=width* height
            maxArea=max(maxArea, area)
        return maxArea
    def findPreviousSmaller(self, heights, prev):
        st=[]
        n=len(heights)
        for i in range(n):
            currindex=i
            while st and heights[st[-1]]>= heights[currindex]:
                st.pop()
            if  st:
                prev[i]=st[-1]
            st.append(currindex)
                
    def findNextSmaller(self,heights, nxt):
        st=[]
        n=len(heights)
        for i in range(n-1,-1,-1):
            currindex=i
            while st and heights[st[-1]]>= heights[currindex]:
                st.pop()
            if st:
                nxt[i]=st[-1]
            st.append(i)






    
        