class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        row=[False]*m
        col=[False]*n
        for i in range(m):#yha par hume sare row or col check kiye 
            for j in range(n):
                if matrix[i][j]==0:#jha bhi milegne ki 0 hai vha par
                    row[i]=True #us row ko sari ko true kardo 
                    col[j]=True#us col ko sari ko True kardo
        for i in range(m): #ab yha chek karenge ki kon si row or col hai jha par true hai changes karenha
            for j in range(n):
                if row[i] or col[j]: #yani ki agr row or col mai ek bhi true hai to usko zero set kardo
                    matrix[i][j] = 0