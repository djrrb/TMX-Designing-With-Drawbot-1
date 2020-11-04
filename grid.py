#message = 'hello world'
#print(message)


# this is a list
messageList = ['hello', 'how are you?', "i'm fine"]

grid = 100
fill(0/255, 136/255, 171/255)

for y in range(0, height(), grid):
    for x in range(0, width(), grid):
        print(x, y)
        oval(x, y, grid, grid)
