import numpy as np
import pandas as pd
import itertools as itr

### --> DYNAMIC TABU LIST <-- ###
### --> Short-term and long-term memories <-- ###


Dist = pd.DataFrame([[0,1,2,3,1,2,3,4],[1,0,1,2,2,1,2,3],[2,1,0,1,3,2,1,2],
                      [3,2,1,0,4,3,2,1],[1,2,3,4,0,1,2,3],[2,1,2,3,1,0,1,2],
                      [3,2,1,2,2,1,0,1],[4,3,2,1,3,2,1,0]],
                    columns=["A","B","C","D","E","F","G","H"],
                    index=["A","B","C","D","E","F","G","H"])

Flow = pd.DataFrame([[0,5,2,4,1,0,0,6],[5,0,3,0,2,2,2,0],[2,3,0,0,0,0,0,5],
                      [4,0,0,0,5,2,2,10],[1,2,0,5,0,10,0,0],[0,2,0,2,10,0,5,1],
                      [0,2,0,2,0,5,0,10],[6,0,5,10,0,1,10,0]],
                    columns=["A","B","C","D","E","F","G","H"],
                    index=["A","B","C","D","E","F","G","H"])


X0 = ["D","A","C","B","G","E","F","H"]


# Make a dataframe of the initial solution

New_Dist_DF = Dist.reindex(columns=X0, index=X0)
New_Dist_Arr = np.array(New_Dist_DF)


# Make a dataframe of the cost of the initial solution

Objfun1_start = pd.DataFrame(New_Dist_Arr*Flow)
Objfun1_start_Arr = np.array(Objfun1_start)


sum_start_int = sum(sum(Objfun1_start_Arr))

print(sum_start_int)


Initial_For_Final = X0[:] # For printing it at the end

print()
print("Initial Solution:",Initial_For_Final)

######################
######################
######################


Runs = 60

### TABU LIST ###
Length_of_Tabu_List = 10

Tabu_List = np.empty((0,len(X0)+1))

One_Final_Guy_Final = []

Iterations = 1

Save_Solutions_Here = np.empty((0,len(X0)+1))


for i in range(Runs):
    
    print()
    print("--> This is the %i" % Iterations, "th Iteration <--")
    
    # To create all surrounding neighborhood
    
    List_of_N = list(itr.combinations(X0, 2)) # From X0, it shows how many combinations of 2's can it get; 8 choose 2
    
    Counter_for_N = 0
    
    All_N_for_i = np.empty((0,len(X0)))
    
    
    
    for i in List_of_N:
        X_Swap = []
        A_Counter = List_of_N[Counter_for_N] # Goes through each set
        A_1 = A_Counter[0] # First element
        A_2 = A_Counter[1] # Second element
        
        # ["D","A","C","B","G","E","F","H"]
        
        # Making a new list of the new set of departments, with 2-opt (swap)
        u= 0
        for j in X0: # For elements in X0, swap the set chosen and store it
            if X0[u] == A_1:
                X_Swap = np.append(X_Swap,A_2)
            elif X0[u] == A_2:
                X_Swap = np.append(X_Swap,A_1)
            else:
                X_Swap = np.append(X_Swap,X0[u])
            
            X_Swap = X_Swap[np.newaxis] # New "X0" after swap
    
            u = u+1
        
        
        
        All_N_for_i = np.vstack((All_N_for_i,X_Swap)) # Stack all the combinations
        
        Counter_for_N = Counter_for_N+1
    
    
    
    
    OF_Values_for_N_i = np.empty((0,len(X0)+1)) # +1 to add the OF values
    OF_Values_all_N = np.empty((0,len(X0)+1)) # +1 to add the OF values
    
    ######################
    ######################
    ######################
    
    
    
    N_Count = 1
    
    # Calculating OF for the i-th solution in N
    for i in All_N_for_i:
        
        New_Dist_DF = Dist.reindex(columns=i, index=i)
        New_Dist_Arr = np.array(New_Dist_DF)
        
        # Make a dataframe of the cost of the initial solution
        Objfun1_start = pd.DataFrame(New_Dist_Arr*Flow)
        Objfun1_start_Arr = np.array(Objfun1_start)
        
        Total_Cost_N_i = sum(sum(Objfun1_start_Arr))    
        
        
        i = i[np.newaxis]
        
        OF_Values_for_N_i = np.column_stack((Total_Cost_N_i,i)) # Stack the OF value to the deertment vector
        
        OF_Values_all_N = np.vstack((OF_Values_all_N,OF_Values_for_N_i))
        
        N_Count = N_Count+1

    # Ordered OF of neighborhood, sorted by OF value
    OF_Values_all_N_Ordered = np.array(sorted(OF_Values_all_N,key=lambda x: x[0]))
    
    
    ######################
    ######################
    ######################
    
    
    # Check if solution is already in Tabu list, if yes, choose the next one
    t = 0
    Current_Sol = OF_Values_all_N_Ordered[t] # Current solution
    
    while Current_Sol[0] in Tabu_List[:,0]: # If current solution is in Tabu list
        Current_Sol = OF_Values_all_N_Ordered[t]
        t = t+1
    
    
    if len(Tabu_List) >= Length_of_Tabu_List: # If Tabu list is full
        Tabu_List = np.delete(Tabu_List, (Length_of_Tabu_List-1), axis=0) # Delete the last row
        
    Tabu_List = np.vstack((Current_Sol,Tabu_List))
    
    
    Save_Solutions_Here = np.vstack((Current_Sol,Save_Solutions_Here)) # Save solutions, which is the best in each run
    
    
    ######################
    ######################
    ######################
    
    
    # In order to "kick-start" the search when stuck in a local optimum, for diversification

    Mod_Iterations = Iterations%10  
    
    Ran_1 = np.random.randint(1,len(X0)+1)
    Ran_2 = np.random.randint(1,len(X0)+1)
    Ran_3 = np.random.randint(1,len(X0)+1)
    
    if Mod_Iterations == 0:
        Xt = []
        A1 = Current_Sol[Ran_1]
        A2 = Current_Sol[Ran_2]
        
        # Making a new list of the new set of departments
        S_Temp = Current_Sol
        
        w = 0
        for i in S_Temp:
            if S_Temp[w] == A1:
                Xt=np.append(Xt,A2)
            elif S_Temp[w] == A2:
                Xt=np.append(Xt,A1)
            else:
                Xt=np.append(Xt,S_Temp[w])
            w = w+1
        
        Current_Sol = Xt
        
        
        # Same department gets switched
        
        Xt = []
        A1 = Current_Sol[Ran_1]
        A2 = Current_Sol[Ran_3]
        
        # Making a new list of the new set of departments
        w = 0
        for i in Current_Sol:
            if Current_Sol[w] == A1:
                Xt=np.append(Xt,A2)
            elif Current_Sol[w] == A2:
                Xt=np.append(Xt,A1)
            else:
                Xt=np.append(Xt,Current_Sol[w])
            w = w+1
        
        Current_Sol = Xt
        
    
    X0 = Current_Sol[1:]
    
    Iterations = Iterations+1
    
    
    # Change length of Tabu List every 5 runs, between 5 and 20, dynamic Tabu list
    if Mod_Iterations == 5 or Mod_Iterations == 0:
        Length_of_Tabu_List = np.random.randint(5,20)
    


t = 0
Final_Here = []
for i in Save_Solutions_Here:
    
    if (Save_Solutions_Here[t,0]) <= min(Save_Solutions_Here[:,0]):
        Final_Here = Save_Solutions_Here[t,:]
    t = t+1
        
One_Final_Guy_Final = Final_Here[np.newaxis]



print()
print()
print("DYNAMIC TABU LIST")
print()
print("Initial Solution:",Initial_For_Final)
print("Initial Cost:", sum_start_int)
print()
print("Min in all Iterations:",One_Final_Guy_Final)
print("The Lowest Cost is:",One_Final_Guy_Final[:,0])







