length = int(input("Rijen? "))
width = int(input("Kolommen? "))

def create_grid(grid):

   x = 0
   y = 0

   table = ""

   while y < length:
      while x < width:
         table += grid[width * x + y] + '|'
         x +=1
      print("\n")
      y +=1

   return table

print(create_grid(table))


