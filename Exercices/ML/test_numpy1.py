# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 18:34:30 2021

@author: vion1
"""

import numpy as np

parametre = {
    "W1" : np.random.randn(10, 100),
    "b1" : np.random.randn(10, 1),
    "W2" : np.random.randn(10, 10),
    "b2" : np.random.randn(10, 1),


}

print(parametre)