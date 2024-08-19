import torch.nn as nn
import math
import torch
import torch.nn.functional as F

class MLP(torch.nn.Module):
    def __init__(self):
        super(MLP,self).__init__()
        self.fc1 = torch.nn.Linear(29, 64)
        self.fc2 = torch.nn.Linear(64, 64)
        self.fc = torch.nn.Linear(64, 29)
        self.elu = torch.nn.ELU

    def forward(self, feature):
        y = self.fc1(feature)
        y = F.elu(y)
        y = self.fc2(y)
        y = F.elu(y)
        y1 = self.fc(y)
        return y1