#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    for i in range(1,10+1,1):
        res = n * i
        print(f"{n} x {i} = {res}")