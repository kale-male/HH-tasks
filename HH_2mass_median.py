def readInts(file):
	return [int(i) for i in file.readline().split()]


def med (a, b):
    i = j = k =0
    prev = cur = None
    while k < (len(a)+len(b))//2 + 1:
        prev = cur
        if i >= len(a) or (j < len(b) and a[i] > b[j]):            
            cur = b[j]
            j += 1
        else:
            cur = a[i]
            i += 1
        k += 1
    return (cur+prev)/2

if __name__ == "__main__":
    fname = "./input.txt"
    with open(fname) as f:
        a = readInts(f)
        b = readInts(f)
    print(med(a, b))
