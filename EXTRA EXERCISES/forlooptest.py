#       0
#      000
#     00000
#    0000000
#   000000000
#  00000000000
# 0000000000000

num = int(input("How many rows "))
for i in range(1,num+1):
    for j in range(1, num-i+1):
        print(" ",end="")
    for k in range(1, i+1):
        print("*",end=" ")
    print()
#-------------------------------------


#*
#**
#***
#****
#*****

num = int(input("How many rows? "))
for i in range(1,num+1):
    for j in range(1, i+1):
        print("*",end=" ")
    print()
#------------------------------------

# +----+----+
# |    |    |
# |    |    |
# |    |    |
# |    |    |
# +----+----+


def grid():
    top_line = (("+"+("-"*4))*2+"+")
    mid_line = (("|"+(" "*4))*2+"|")


    for i in range(1):
        print(top_line)
    print(mid_line)
    for i in range(4):
        print(mid_line)
    print(top_line)
    for i in range(4):
        print(mid_line)
    print(top_line)

grid()





