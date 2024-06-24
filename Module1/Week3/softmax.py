import torch
import torch.nn as nn

#Softmax 
softmax_function = nn.Softmax()
data = torch.Tensor([1, 2, 3])
output = softmax_function(data)
print(output)

#Softmax Stable
class Softmax(nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        exp_z = torch.exp(x - torch.max(x)) 
        return exp_z / exp_z.sum()


softmax = Softmax()
output = softmax(data)
print(output)
