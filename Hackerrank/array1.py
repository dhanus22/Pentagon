# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phonebook = { }

for _ in range(n):
    name, number = input().split()
    phonebook[name] = number
    
while True:
    try:
        query = input()
        if query in phonebook:
            print(f"{query}={phonebook[query]}")
        else:
            print("Not found")
    except EOFError:
            break
    
        