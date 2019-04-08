def make_album(artist_name: str, album_title: str, tracks_number: int = None) -> {}:
    album = {"artist_name": artist_name, "album_title": album_title}
    if tracks_number:
        album["tracks_number"] = tracks_number
    return album


meteora = make_album("Linkin Park", "Meteora")
significant_other = make_album("Limp Bizkit", "Significant Other")
smash = make_album("Offspring", "Smash", 14)

music_albums = [meteora, significant_other, smash]
for music_album in music_albums:
    print(music_album)
