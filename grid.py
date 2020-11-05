#message = 'hello world'
#print(message)


# this is a list
messageList = ['hello', 'how are you?', "i'm fine"]

# this is the value for our grid
grid = 100

# loop through the pages
for page in range(10):
    # make a new page
    newPage(1000, 1000)
    # draw a red background
    fill(1, 0, 0)
    rect(0, 0, width(), height())
    # loop through all the rows
    for y in range(0, height(), grid):
        # loop through all the columns
        for x in range(0, width(), grid):
            # choose a random color
            fill(random(), random(), random())
            print(x, y)
            # draw my oval
            oval(x, y, grid, grid)

# save the result in various formats
for ext in ['gif', 'pdf', 'mp4']: 
    saveImage('~/desktop/myFunGrid.'+ext)