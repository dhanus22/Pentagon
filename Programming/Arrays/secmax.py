#Program to find second maximum number
def creatarr():
    l1 = []
    while True:
        try:
            n = int(input("ENter num:"))
            l1.append(n)
        except Exception as e:
            return l1

def secmax(arr):
    max = ((-2**31)-1)
    maxind = -1
    sec = ((-2**31)-1)
    secind = -1
    for i in range(0, len(arr)):
        if max < arr[i]:
            sec = max
            secind = maxind
            max = arr[i]
            maxind = i
        elif (max != arr[i] and sec < arr[i]):
            sec = arr[i]
            secind = i
    return [max, maxind, sec, secind]

arr = creatarr()
res = secmax(arr)
print(f"The second max number is {res[2]} found at {res[3]}")



#Program to find second minimun number
def secmin(arr):
    min = (2**31)
    minind = -1
    sec = (2**31)
    secind = -1
    for i in range(0, len(arr)):
        if arr[i] < min:
            sec = min
            secind = minind
            min = arr[i]
            minind = i
        elif (min != arr[i] and sec > arr[i]):
            sec = arr[i]
            secind = i
    return [min, minind, sec, secind]

arr = creatarr()
res = secmin(arr)
print(f"The second min number is {res[2]} found at {res[3]}") 

