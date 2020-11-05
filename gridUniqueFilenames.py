import os
import datetime

#message = 'hello world'
#print(message)

def triangle(x, y, w, h):
    polygon(
        (x, y), 
        (x+w/2, y+h), 
        (x+w, y)
    )

# this is a list
messageList = ['hello', 'how are you?', "i'm fine"]

# this is the value for our grid
grid = 100

# loop through the pages
for page in range(1):
    # make a new page
    newPage(1000, 1000)
    # draw a red background
    fill(0, 0, 0)
    rect(0, 0, width(), height())
    # loop through all the rows
    for y in range(0, height(), grid):
        # loop through all the columns
        for x in range(0, width(), grid):
            # choose a random color
            fill(random(), random(), random())
            #print(x, y)
            # draw my oval
            myRandomNumber = random()
            if myRandomNumber < 1/3:
                oval(x, y, grid, grid)
            elif myRandomNumber < 2/3:
                triangle(x, y, grid, grid)
            else:
                rect(x, y, grid, grid)

# save the result in various formats
for ext in ['gif', 'pdf', 'mp4']: 
    myPath = '~/desktop/myFunGrid.'
    if os.path.exists(os.path.expanduser(myPath+ext)):
        myPath = myPath + str(datetime.datetime.now()) + '.'
    saveImage(myPath+ext)