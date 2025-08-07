# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

for _ in range(T):
    s = input()
    even_chars = ""
    odd_chars = ""
    
    for i in range(len(s)):
        if i % 2 == 0:
            even_chars += s[i]
        else:
            odd_chars += s[i] 

    print(even_chars, odd_chars)
