import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

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

T0 = 1500
M = 200
N = 10
alpha = 0.9

X0 = ["B","D","A","E","C","F","G","H"]

# Make a dataframe of the initial solution
New_Dist_DF = Dist.reindex(columns=X0, index=X0)
New_Dist_Arr = np.array(New_Dist_DF)

# Make a dataframe of the cost of the initial solution
Objfun1_start = pd.DataFrame(New_Dist_Arr*Flow)
Objfun1_start_Arr = np.array(Objfun1_start)

sum_start = sum(sum(Objfun1_start_Arr))
print(sum_start)

Temp = []
Min_Cost = []

for i in range(M):
    for j in range(N):
        ran_1 = np.random.randint(0,len(X0))
        ran_2 = np.random.randint(0,len(X0))
        
        while ran_1==ran_2:
            ran_2 = np.random.randint(0,len(X0))
            
        xt = []
        xf = []
        
        xt = X0.copy()
        xt[ran_1], xt[ran_2] = xt[ran_2], xt[ran_1]

        # current combination
        new_dis_df_init = Dist.reindex(columns=X0, index=X0)
        new_dis_init_arr = np.array(new_dis_df_init)
        
        # new combination
        new_dis_df_new = Dist.reindex(columns=xt, index=xt)
        new_dis_new_arr = np.array(new_dis_df_new)
        
        # Obj Function of the current solution
        objfun_init = pd.DataFrame(new_dis_init_arr*Flow)
        objfun_init_arr = np.array(objfun_init)
        
        # Obj Function of the new solution
        objfun_new = pd.DataFrame(new_dis_new_arr*Flow)
        objfun_new_arr = np.array(objfun_new)
        
        sum_init = sum(sum(objfun_init_arr))
        sum_new = sum(sum(objfun_new_arr))
        
        rand1 = np.random.rand()
        form = 1/(np.exp(sum_new-sum_init)/T0)
        
        if sum_new<=sum_init:
            X0=xt
        elif rand1<=form:
            X0=xt
        else:
            X0=X0
        
    Temp.append(T0)
    Min_Cost.append(sum_init)
    T0 = alpha*T0
    
print()
print("Final Solution:",X0)
print("Minimized Cost:",sum_init)
        
plt.plot(Temp,Min_Cost)
plt.title("Cost vs. Temp.", fontsize=20,fontweight='bold')
plt.xlabel("Temp.", fontsize=18,fontweight='bold')
plt.ylabel("Cost", fontsize=18,fontweight='bold')
plt.xlim(1500,0)

plt.xticks(np.arange(min(Temp),max(Temp),100),fontweight='bold')
plt.yticks(fontweight='bold')
plt.show()
