im = ImageObject('https://www.thesprucepets.com/thmb/3n2aM62d0XslM9vF9B_cLs0yhSU=/960x0/filters:no_upscale():max_bytes(150000):strip_icc()/golden-retriever-puppy-in-grass-923135452-5c887d4146e0fb00013365ba.jpg')



#im.sepiaTone(1)
im.vignette(width()/2, 2)
im.kaleidoscope(10)

print(im.size())
newPage(*im.size())


image(im, (0,0))