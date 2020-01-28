"""Objective
In this challenge, we're getting started with conditional statements.

Task
Given an integer, N, perform the following conditional actions:"""

import math
import os
import random
import re
import sys

N = int(input())
#1. If N is odd, print Weird
if N%2!=0:
    print('Weird')
#2. If N  is even and in the inclusive range of 2 to 5 , print Not Weird    
else:
    if N<=5:
        print('Not Weird')
#3. If N is even and in the inclusive range of 6 to 20 , print Weird
    elif N<=20:
        print('Weird')
#4. If N is even and greater than 20, print Not Weird    
    else:
        print('Not Weird')
