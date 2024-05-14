def enlarge(image,factor):
    return image.repeat(factor,axis=0).repeat(factor,axis=1)

def shrink(image,factor):
    if type(factor) == int:
        return image[::factor,::factor]
    else:
        enlarged = enlarge(image,10)
        return shrink(enlarged,int(10*factor))