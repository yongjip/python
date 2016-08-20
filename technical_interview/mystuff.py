from __future__ import division, print_function
import os

try:
    os.chdir("E:/Documents/Python/technical_interview/")
except:
    try:
        os.chdir("/media/yongjip/UUI/Python/technical_interview")
    except:
        print("wrong directory")


mystuff = {'apple': 'I AM APPLES!'}
print(mystuff['apple'])

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
