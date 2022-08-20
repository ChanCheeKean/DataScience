import numpy as np
import matplotlib.pyplot as plt

# initial solution you'd like to start at
x = 2 
y = 1
z = ((x**2)+y-11)**2+(x+(y**2)-7)**2

# hyperparameters (user inputted parameters)
T0 = 1000
temp_for_plot = T0
M = 200
N = 10
alpha = 0.85 
k = 0.1

temp = [] 
obj_val = []
        
for i in range(M): 
    for j in range(N):
        
        # for x variable
        rand_num_x_1 = np.random.rand() 
        rand_num_x_2 = np.random.rand() 
        if rand_num_x_1 >= 0.5:
            step_size_x = k * rand_num_x_2
        else:
            step_size_x = -k * rand_num_x_2 
        
        # for y variable
        rand_num_y_1 = np.random.rand()
        rand_num_y_2 = np.random.rand()
        if rand_num_y_1 >= 0.5:
            step_size_y = k * rand_num_y_2 
        else:
            step_size_y = -k * rand_num_y_2
        
        # setting next move
        x_temporary = x + step_size_x
        y_temporary = y + step_size_y
        
        # next value
        obj_val_possible = ((x_temporary**2)+y_temporary-11)**2 + (x_temporary+(y_temporary**2)-7)**2
        # current value
        obj_val_current = ((x**2)+y-11)**2+(x+(y**2)-7)**2
        
        rand_num = np.random.rand()

        formula = 1/(np.exp((obj_val_possible - obj_val_current)/T0))
                
        if obj_val_possible <= obj_val_current:
            x = x_temporary
            y = y_temporary
        elif rand_num <= formula:
            x = x_temporary
            y = y_temporary
        else: 
            x = x
            y = y
            
    temp.append(T0) 
    obj_val.append(obj_val_current) 
    T0 = alpha*T0 

print()
print("x is: %0.3f" % x)
print("y is: %0.3f" % y)
print("obj val is: %0.3f" % obj_val_current)
print()
print("------------------------------")


plt.plot(temp,obj_val)
plt.title("Z at Temperature Values",fontsize=20, fontweight='bold')
plt.xlabel("Temperature",fontsize=18, fontweight='bold')
plt.ylabel("Z",fontsize=18, fontweight='bold')

plt.xlim(temp_for_plot,0)
plt.xticks(np.arange(min(temp),max(temp),100),fontweight='bold')
plt.yticks(fontweight='bold')

plt.show()



