import random

newPage(1000, 2000)

for y in range(0, height(), 500):
    for x in range(0, width(), 500):
        fontSize(50)
        myFont = random.choice(installedFonts())
        font(myFont)
        fill(1, 0, 0)
        text('A', (x, y))
        with savedState():
            fill(0, 1, 0)
            font('Georgia')
            text('Z', (x+50, y+50))
            scale(.5)
        text('?', (x+100, y+100))
            
            #image('https://www.thesprucepets.com/thmb/3n2aM62d0XslM9vF9B_cLs0yhSU=/960x0/filters:no_upscale():max_bytes(150000):strip_icc()/golden-retriever-puppy-in-grass-923135452-5c887d4146e0fb00013365ba.jpg', (x*2,y*2))