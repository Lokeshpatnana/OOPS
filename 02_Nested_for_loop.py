b=[
    [11,12,13],
    [14,15,16],
    [17,18,19,20]
]
print(b)  # Total list will be printed
print(b[0])  #[11,12,13]
print(b[0][2])  #13

# We want the numbers in the list in a vertical order without any square braces
for i in b:
    for j in i:
        print(j)