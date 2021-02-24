python_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
python_students = dict(python_students)
k = sorted(set((python_students.values())))[1]
lst = []
[i for i,j in python_students.items() if j == k]


for i in sorted(lst):
    print(i)

# def takeSecond(elem):
#     return elem[1]
# P=sorted(python_students,key=takeSecond)
# K=sorted(list(set(i[1] for i in P)))
# M=sorted([i[0] for i in P if i[1]==K[1]])
# for j in M:
#     print(j)