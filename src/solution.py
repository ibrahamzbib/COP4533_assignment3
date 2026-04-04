import sys


def parse_input(filename):
    
    if filename is not None:
        f = open(filename, "r")
        lines = f.read().split()
        f.close()
    else:
        print("invalid file name\n")
        

    idx = 0

    k = int(lines[idx])
    idx += 1

    char_values = {}
    for i in range(k):
        char = lines[idx]
        val = int(lines[idx + 1])
        char_values[char] = val
        idx += 2

    a = lines[idx]
    b = lines[idx + 1]

    return char_values, a, b

def main():
    filename = None
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    char_values, a, b = parse_input(filename)
 


if __name__ == "__main__":
    main()