# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line
list_movie = ['e.t.','memoirs of a geisha', 'jaws','superman','heidi','the cowboys', 'images','tom sawyer', 'jurassic park','harry potter', 'star wars']
def alphabetical_order(movies):
  return sorted(movies)
print(alphabetical_order(list_movie))

golden_globe_movie = ['star wars','e.t.', 'memoirs of a geisha','jaws']
#check_movie = list_movie[2]
def won_golden_globe(movie_name):
  if (movie_name.lower()) in golden_globe_movie:
    print(f'{movie_name} won a golden globe!')
    return True
  else:
        print(f'{movie_name} did not won any golden globe.')
        return False

print(won_golden_globe('HEIDI'))



toto_albums = ['Star Wars', 'The Lion King', 'Miracles', 'Old Is New']


def remove_toto_albums(list):

  for title in list and toto_albums:
      
      if (title.lower().upper().title()) in toto_albums:
        toto_albums.remove(title)
      return toto_albums
  
  
print(remove_toto_albums(list_movie))

