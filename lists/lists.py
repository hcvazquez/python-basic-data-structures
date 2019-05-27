'''
perform the following commands:

insert i e: Insert integer e at position .
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
'''

if __name__ == '__main__':
    N = int(raw_input())
    result = []
    for i in range(0, N):
        cmd = raw_input()
        args = cmd.split(" ")
        if args[0] == "insert":
            result.insert(int(args[1]), int(args[2]))    
        elif args[0] == "print":
            print(result)
        elif args[0] == "remove":
            result.remove(int(args[1]))
        elif args[0] == "append":
            result.append(int(args[1]))
        elif args[0] == "sort":
            result.sort()
        elif args[0] == "pop":
            result.pop()
        elif args[0] == "reverse":
            result.reverse()