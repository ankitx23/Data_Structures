# You work for a fashion design company. 
# They have come up with a new design for some textile they would like to mass produce. 
# You are charged with the job to program the pattern into the sewing machine that creates the textile pattern. 
# Please take us through a solution to create the following pattern.
# @*@*@*@*@*
# *@*@*@*@*@
# @*@*@*@*@*
# *@*@*@*@*@
# @*@*@*@*@*
# *@*@*@*@*@

for i in range (7):     
        for j in range(11):
            if i%2==1: 
                if j%2==0:
                    print ("@" , end='')
                else: 
                    print("*", end='')    
            else:
                if j%2==1:
                    print ("@" , end='')
                else: 
                    print("*", end='')                   
        print()


