import pygame


class Music(object):
    def __init__(self, path, volume=1):
        self.path = path
        self.loops = 1
        self.volume = volume

    # Returns True if the sound is currently playing
    def isPlaying(self):
        return bool(pygame.mixer.music.get_busy())

    # Loops = number of times to loop the sound.
    # If loops = 1 or 1, play it once.
    # If loops > 1, play it loops + 1 times.
    # If loops = -1, loop forever.
    def start(self, loops=1):
        pygame.mixer.music.load(self.path)
        self.loops = loops
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play(loops=loops)

    # Stops the current sound from playing
    def stop(self):
        pygame.mixer.music.stop()
