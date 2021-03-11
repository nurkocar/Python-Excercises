def countingValleys(steps, path):
    # Write your code here
    sea_level = valley_number = 0
    for step in path:
        if step == 'U':
            sea_level += 1
        else:
            sea_level -= 1
        
        if sea_level == 0 and step == 'U':
            valley_number += 1
            
    return valley_number

print(countingValleys(8, 'UDDDUDUU'))