N = int(input())
lst = []
for i in range(N):
    command_line = input().strip().split()
    command = command_line[0]
    if command == 'insert':
        lst.insert(int(command_line[2]), int(command_line[1]))
    elif command == 'print':
        print(lst)
    elif command =='remove':
        lst.remove(int(command_line[1]))
    elif command == 'append':
        lst.append(int(command_line[1]))
    elif command == 'sort':
        lst.sort()
    elif command == 'pop':
        lst.pop()
    elif command == 'reverse':
        lst.reverse()