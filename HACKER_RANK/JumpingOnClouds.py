def jumpingOnClouds(c):
    i = jump = 0
    while i < len(c) - 2 :
        if c[i + 2] == 0:
            jump += 1
            i += 2
        elif c[i + 1] == 0:
            jump += 1
            i += 1
    
    if i == len(c) - 2:
        jump += 1
    return jump 

print(jumpingOnClouds([0,1,0,0,0,1,0]))