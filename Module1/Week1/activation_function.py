import math
# Hàm is_number kiểm tra có validation không
def is_number(n):
    try:
        return float(n)  
    except:
        return ValueError        
#Hàm activation
def activation_function(x, fname):
    n = is_number(x)
    if fname.lower() == "sigmoid": return 1 / (1 + math.exp(-n))
    if fname.lower() == "relu": return max(0,n)
    if fname.lower() == "elu": return max(0.01*(math.exp(-n) -1), n)
    
#Hàm check 
def check_activation_function(fname):
    if fname.lower() not in ["sigmoid", "relu", "elu"]:
        return print(f'{fname} is not existed')
    return True


x = input("x = ")
if is_number(x):
    fname = input("Input activation Function (sigmoid|relu|elu): ")
    if check_activation_function(fname):
        print(activation_function(x, fname))
        