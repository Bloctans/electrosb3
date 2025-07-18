import sys

from electrosb3 import Electro

if __name__ == "__main__":
    e = Electro()
    e.run(sys.argv[1])