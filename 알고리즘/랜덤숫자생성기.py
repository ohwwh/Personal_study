#!/opt/homebrew/bin/python3

import sys
import random

numbers = list(range(1, int(sys.argv[1]) + 1))
random.shuffle(numbers)
print(numbers)