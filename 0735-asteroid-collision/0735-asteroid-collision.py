class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        pos=[]
       
        #agar mere pas ek pos number hai to muhje postive stack mai dalna hai...
        for ch in asteroids:
            #pos hai to add kardo
            if ch>=0:
                pos.append(ch)
            else:
                #negetive hai hai to check kro
                if not pos:#agr empty hai to add kardo
                    pos.append(ch)
                elif pos[-1]<0:
                    pos.append(ch)
                else:
                    #first entity are pso ka top postive and second is negative ch ki
                    destroyed=False
                    while pos and ch<0 and pos[-1]>0: 
                        if pos[-1] < -ch:
                            pos.pop()
                          
                        #top wala explode ho jayga                  
                        elif pos[-1] > (-ch):
                            #ch is destroyed ho jayga
                            destroyed=True
                            break
                        else:
                            # == wala case hai ye dono hi explode ho jayga
                            pos.pop()
                            destroyed=True
                            break
                    if not destroyed:
                        pos.append(ch)
        
        
        return pos


                        
                         



        

           