import math
import pickle

FILENAME = "Saves.txt"


class Settings(object):

    def __init__(self):
        self.fullscreen = False
        self.resolution = [640, 480]

    def resolution_sqrt(self):
        return int(math.sqrt(self.resolution[0] * self.resolution[1]))


def loadSettings(filename):
    try:
        with open(filename, "rb") as file:
            loaded = pickle.load(file)
            return loaded
    except (NameError, EOFError):
        print("Cannot restore settings from file %s" % filename)
        return Settings()
    except FileNotFoundError:
        print("Starting with defaults")
        return Settings()


def saveSettings(settings, filename):
    with open(filename, "wb") as saves:
        pickle.dump(settings, saves)
