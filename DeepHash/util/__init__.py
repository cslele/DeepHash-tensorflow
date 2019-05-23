import sys
import numpy as np


class Logger(object):
    def __init__(self, filename="default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
        
    def flush(self):
        self.terminal.flush()


# return -1 if x < 0, 1 if x > 0, random -1 or 1 if x ==0
def sign(x):
    s = np.sign(x)
    tmp = s[s == 0]
    s[s==0] = np.random.choice([-1, 1], tmp.shape)
    return s


if __name__ == "__main__":
    x = np.random.choice([-1, 0, 1], [5, 5])
    print(x)
    print((sign(x)))
