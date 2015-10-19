def readInts(text):
    return int(input(text))
	    
def search (n, m):
    k = 0
    s = {m}
    seen = {m}
    while n not in s:
        k += 1
        temp = set()
        for i in s:
            nums = [i - 1, i - 2]
            if i%2 == 0:
                nums.append(i//2)
            for j in nums:
                if j >= n and j not in seen:
                    temp.add(j)
        s = temp
        seen |= temp
    return k

if __name__ == "__main__":
    n = readInts("Input n: ")
    m = readInts("Input m: ")
    print(search (n, m))
