import math


def timerOut(t):
    hours = math.floor(t / 60 / 60)
    minutes = math.floor(t / 60 - hours * 60)
    seconds = t - minutes * 60 - hours * 60 * 60
    return ("{:0>2}:{:0>2}:{:0>2}".format(hours, minutes, seconds))
