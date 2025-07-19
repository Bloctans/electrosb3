import sys
import electrosb3

if __name__ == "__main__":
    e = electrosb3.Electro()
    e.run(sys.argv[1])