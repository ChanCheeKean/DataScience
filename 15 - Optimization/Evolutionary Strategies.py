import numpy as np
from matplotlib import pyplot as plt
import random as rd
import math as mt

Mew = 120
Lambda = Mew*6 # Where the ratio of Mew to Lambda is 1:6
a = 0.8

Stopping_Criteria = 30

Initial_X1 = 0
Initial_X2 = 8

Initial_Sig_1 = 1.25
Initial_Sig_2 = 1.00



Initial_Variables = (Initial_X1,Initial_Sig_1,
                     Initial_X2,Initial_Sig_2)



Obj_Fun = ((Initial_X2 - ((5.1/(4*mt.pi**2))*Initial_X1**2) + 
            ((5/mt.pi)*Initial_X1) - 6)**2 + 10*(1-(1/(8*mt.pi)))*mt.cos(Initial_X1) + 10)


print("Obj_Fun:",Obj_Fun)


New_Pop = np.empty((0,5))

n_list_1 = np.empty((0,5))

Best_Child_from_X = np.empty((0,5))

Final_Best_in_Generation_X = []
Final_Best = []

for i in range(Mew): # Shuffles the elements in the vector n times and stores them
    X1_Rand = np.random.uniform(-5, 10)
    X2_Rand = np.random.uniform(0, 15)
    Obj_Fun_Init = ((X2_Rand - ((5.1/(4*mt.pi**2))*X1_Rand**2) + 
            ((5/mt.pi)*X1_Rand) - 6)**2 + 10*(1-(1/(8*mt.pi)))*mt.cos(X1_Rand) + 10)
    rand_sol_1 = (Obj_Fun_Init,X1_Rand,Initial_Sig_1,X2_Rand,Initial_Sig_2)
    n_list_1 = np.vstack((n_list_1,rand_sol_1))


### STARTS HERE ###

See_Parents = np.empty((0,5))

Keep_the_Best_Child_Safe = np.empty((0,5))

Gen = 1


for i in range(Stopping_Criteria):
    
    print()
    print("Generation at:",Gen)
    
    New_Pop = np.empty((0,5))
    
    n_list_Parents_2 = np.empty((0,5))
    n_list_Children_2 = np.empty((0,5))
    
    All_Parents = np.empty((0,5))
    All_Children = np.empty((0,5))
    
    One_Fifth_Final = 0
    
    
    for i in range(Mew):
        '''
        print()
        print("Parent #",Par_Num)
        '''
        One_Fifth = 0
        
        Select_Parent_1 = np.random.randint(0,Mew) #1
        Select_Parent_2 = np.random.randint(0,Mew) #20
        Select_Parent_3 = np.random.randint(0,Mew)
        Select_Parent_4 = np.random.randint(0,Mew)
        Select_Parent_5 = np.random.randint(0,Mew)
        
        n_list_1 = np.array(n_list_1)
        
        Rand_Parent_1 = n_list_1[Select_Parent_1,:]
        Rand_Parent_2 = n_list_1[Select_Parent_2,:]
        Rand_Parent_3 = n_list_1[Select_Parent_3,:]
        Rand_Parent_4 = n_list_1[Select_Parent_4,:]
        Rand_Parent_5 = n_list_1[Select_Parent_5,:]
        
        
        Sol_Temp = (Rand_Parent_2[1],Rand_Parent_3[2],Rand_Parent_4[3],Rand_Parent_5[4])
        Sol_Temp = np.array(Sol_Temp)
        
        Sol_Not_Temp = (((Rand_Parent_1[[1]]+Sol_Temp[[0]])/2),((Rand_Parent_1[[2]]+Sol_Temp[[1]])/2),
                        ((Rand_Parent_1[[3]]+Sol_Temp[[2]])/2),((Rand_Parent_1[[4]]+Sol_Temp[[3]])/2))
        
        Sol_Not_Temp = np.array(Sol_Not_Temp)
        
        
        Obj_Fun_Parent = ((Sol_Not_Temp[2] - ((5.1/(4*mt.pi**2))*Sol_Not_Temp[0]**2) + 
                        ((5/mt.pi)*Sol_Not_Temp[0]) - 6)**2 + 
        10*(1-(1/(8*mt.pi)))*mt.cos(Sol_Not_Temp[0]) + 10)
        
        
        Rand_Parent_to_Use = np.append(Obj_Fun_Parent,Sol_Not_Temp)
        
        See_Parents = np.vstack((See_Parents,Rand_Parent_to_Use))
        
        n_list_Parents_1 = (Obj_Fun_Parent,Rand_Parent_to_Use[1],Initial_Sig_1,Rand_Parent_to_Use[3],Initial_Sig_2)
        n_list_Parents_2 = np.vstack((n_list_Parents_2,n_list_Parents_1))
        
        All_in_Generation_P = np.column_stack((Obj_Fun_Parent,Rand_Parent_to_Use[1],
                                               Initial_Sig_1,Rand_Parent_to_Use[3],
                                               Initial_Sig_2))
        
        All_Parents = np.vstack((All_Parents,All_in_Generation_P))
        
        Child_Num = 1
        
        Child_from_X = np.empty((0,5))
        
        for j in range(int(Lambda/Mew)):
            '''
            print()
            print("Child #",Child_Num)
            '''
            Sig_Rand_1 = Initial_Sig_1*np.random.normal(0,1)
            Sig_Rand_2 = Initial_Sig_2*np.random.normal(0,1)
            '''
            print("Dana:",Sig_Rand)
            '''
            X1_new = Rand_Parent_to_Use[1] + Sig_Rand_1
            X2_new = Rand_Parent_to_Use[3] + Sig_Rand_2
            
            
            Obj_Fun_Child = ((X2_new - ((5.1/(4*mt.pi**2))*X1_new**2) + 
                        ((5/mt.pi)*X1_new) - 6)**2 + 10*(1-(1/(8*mt.pi)))*mt.cos(X1_new) + 10)
            
            
            if Obj_Fun_Child < Obj_Fun_Parent:
                One_Fifth += 1
            else:
                One_Fifth += 0
            
            
            All_in_Generation_C = np.column_stack((Obj_Fun_Child,X1_new,Sig_Rand_1,
                                                   X2_new,Sig_Rand_2))
            
            All_Children = np.vstack((All_Children,All_in_Generation_C))
            
            Child_Num = Child_Num+1
            
            
            
            Child_from_X = np.vstack((Child_from_X,All_in_Generation_C))
            
        
        
        One_Fifth_Final += One_Fifth
        
    
    t = 0
    Best_Child = []
    
    for i in All_Children:
        
        if (All_Children[t,:1]) <= min(All_Children[:,:1]):
            R1_2_Final = []
            R1_2_Final = [All_Children[t,:1]]
            Best_Child = All_Children[t,:]
        t = t+1
    
    Final_Best_in_Generation_X = Best_Child
    
    print()
    print("Final_Best_in_Generation_X:",Final_Best_in_Generation_X)
    
    Keep_the_Best_Child_Safe = np.vstack((Keep_the_Best_Child_Safe,Final_Best_in_Generation_X))
    
    # The 1/5th rule
        
    Final_Ratio_of_Success = One_Fifth_Final/Lambda
    
    
    Mod_G = Gen%10

    if Mod_G == 5 or Mod_G == 0:
        
        if Final_Ratio_of_Success > 1/5:
            Initial_Sig_1 = Initial_Sig_1/a
            Initial_Sig_2 = Initial_Sig_2/a
        elif Final_Ratio_of_Success < 1/5:
            Initial_Sig_1 = Initial_Sig_1*a
            Initial_Sig_2 = Initial_Sig_2*a
        elif Final_Ratio_of_Success == 1/5:
            Initial_Sig_1 = Initial_Sig_1
            Initial_Sig_2 = Initial_Sig_2
    else:
        Initial_Sig_1 = Initial_Sig_1
        Initial_Sig_2 = Initial_Sig_2
    
    # All the parents and all the genrated children
    
    New_Pop_Parents = np.array(sorted(All_Parents,key=lambda x: x[0]))
    New_Pop_Children = np.array(sorted(All_Children,key=lambda x: x[0]))
    
    
    # Take 10% of parents and 90% of children for next generation
    
    
    New_Population_Parents = New_Pop_Parents[:int(Mew*(10/100)),:]
    New_Population_Children = New_Pop_Children[:int(Mew*(90/100)),:]
    
    
    New_Pop = np.vstack((New_Population_Parents,New_Population_Children))
    
    New_Pop_New = np.vstack((New_Population_Parents,New_Population_Children))
    
    np.random.shuffle(New_Pop)
    
    
    n_list_1 = New_Pop

    Gen = Gen+1
    '''
    print()
    print("Initial_Sig:",Initial_Sig)
    print("Sig_Rand:",Sig_Rand)
    '''
t = 0
Best_in_All = []

for i in Keep_the_Best_Child_Safe:
    
    if (Keep_the_Best_Child_Safe[t,:1]) <= min(Keep_the_Best_Child_Safe[:,:1]):
        Best_in_All = Keep_the_Best_Child_Safe[t,:]
    t = t+1

Final_Best = np.concatenate((Best_in_All[[0]],Best_in_All[[1]],Best_in_All[[3]]))

Final_Best = Final_Best[np.newaxis]

print()
print("Final_Best:",Final_Best)
print()


      
print("The Lowest Value is:",Final_Best[:,0])

Here = (Final_Best[:,0]).tolist()
Here = float(Here[0])


plt.plot(Keep_the_Best_Child_Safe[:,0])
plt.axhline(y=Here,color="r",linestyle='--')
plt.title("The Branin rcos Function",fontsize=20,fontweight='bold')
plt.xlabel("# of Iterations",fontsize=18,fontweight='bold')
plt.ylabel("Value of f(x1,x2)",fontsize=18,fontweight='bold')
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
xyz=(Gen/2.5, Here)
xyzz = (Gen/2.4, Here+0.0025)
plt.annotate("Minimum Reached at: %.4f" % Here, xy=xyz, xytext=xyzz,
             arrowprops=dict(facecolor='black', shrink=0.001,width=1,headwidth=5),
             fontsize=12,fontweight='bold')
plt.show()