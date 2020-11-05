#message = 'hello world'
#print(message)


# this is a list
messageList = ['hello', 'how are you?', "i'm fine"]

grid = 100

for page in range(10):
    newPage(1000, 1000)
    for y in range(0, height(), grid):
        for x in range(0, width(), grid):
            fill(random(), random(), random())
            print(x, y)
            oval(x, y, grid, grid)
