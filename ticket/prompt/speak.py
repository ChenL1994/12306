import winsound
import os
__curdir = os.path.split(os.path.realpath(__file__))[0]


def say(times=1):
    for i in range(times):
        winsound.PlaySound(os.path.join(
            __curdir, "sin.wav"), winsound.SND_FILENAME)
