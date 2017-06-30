import math
def position2azimute(position1, position0):
    dY = position1[2]- position0[2]
    dX = position1[1]- position0[1]
    azimute = math.atan2(dY, dX)
    return azimute
