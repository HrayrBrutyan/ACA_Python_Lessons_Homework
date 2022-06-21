# Programmer

class UnknownSongError(Exception):
    def __init__(self, msg):
        self.__msg = msg

    def get_msg(self):
        return "Invalid song - {}".format(self.__msg)


class Song:
    def __init__(self, artist, album, year, name):
        self.artist = artist
        self.album = album
        self.year = year
        self.name = name

    def __repr__(self):
        return "{} - {} - {} - {}".format(self.artist, self.album, self.year, self.name)


class Playlist:
    def __init__(self, filename):
        self.filename = filename
        self.tracks = []

    def load_song(self):
        self.tracks = []
        file = open(self.filename, "r")
        for line in file:
            fields = line.split("\t")  # line.strip()
            track = Song(fields[0], fields[1], fields[2], fields[3])
            self.tracks.append(track)
        print(f"Loading songs from {self.filename} file. The number of songs is {len(self.tracks)}")
        file.close()
        # print(self.tracks)

    # def __repr__(self):
    #     track_number = 1
    #     for track in self.tracks:
    #         print("N{}, artist: {}, album: {}, year: {}, name: {}".format(str(track_number), track.artist, track.album,str(track.year), track.name))
    #         track_number += 1

    def view(self):
        track_number = 1
        for track in self.tracks:
            print("N{}, artist: {}, album: {}, year: {}, name: {}".
                  format(track_number, track.artist, track.album, track.year, track.name.strip()))
            track_number += 1


class Player:
    def __init__(self, playlist, n):
        self.playlist = playlist
        self.song = n

    def __repr__(self):
        return "Current song is N{} - {}".format(self.song, self.playlist.tracks[self.song - 1])

    def show_current_song(self):
        return "Current song is N{} - {}".format(self.song, self.playlist.tracks[self.song - 1])

    def play(self, n):
        return self.playlist.tracks[n-1]

    def next_song(self):
        pass

    def previous_song(self):
        pass

    def stop(self):
        pass


###################################

# User

# s1 = Song("Animals", "The Most Of The Animals", "1966", "House Of The Rising Sun")
# print(s1)

playlist1 = Playlist("albums.txt")
playlist1.load_song()
playlist1.view()
# print(playlist1)


player1 = Player(playlist1, 4)
print(player1)
print(player1.play(8))


# print(player1.show_current_song())
# print(player1.play(1))
# print(player1)

