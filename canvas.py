
# initial size
rectSize = 1000

# make an animation loop over pages
for page in range(0, 360, 1):
    # make a new page
    newPage(1000, 1000)
    # move to the center of the canvas
    translate(width()/2, height()/2)
    # set our stroke to red
    stroke(1, 0, 0)
    # make our shapes empty
    fill(None)
    # keep track of our scale (starting at 1 )
    scaleValue = 1
    # now make a loop of rects
    for iteration in range(50):
        # set our stroke width and compensate for
        # the scale Value to keep it consistent
        strokeWidth(2/scaleValue)
        # draw our rect
        rect(-rectSize/2, -rectSize/2, rectSize, rectSize)
        # now scale the whole doc
        scale(.95)
        # keep track of that change
        scaleValue *= .95
        # now rotate the whole doc
        rotate(page/4)
        
# save the result
saveImage('~/desktop/funkySpiral.gif')