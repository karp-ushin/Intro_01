for x in (True, False):
    for y in (True, False):
        for z in (True, False):
            print("x=%5r, y=%5r, z=%5r, утверждение = %r" % (x, y, z, not(x or y or z) == (not x and not y and not z)))
