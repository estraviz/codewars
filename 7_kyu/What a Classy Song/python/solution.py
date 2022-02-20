# What a "Classy" Song
class Song:

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.listeners = set()

    def how_many(self, people):
        new_listeners = 0
        for person in people:
            listener = person.lower()
            if listener not in self.listeners:
                self.listeners.add(listener)
                new_listeners += 1
        return new_listeners
