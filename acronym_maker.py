def make_acronyms(text_stream):
   for word in text_stream.split():
      print(word[0].upper() + '.', end='')
   print('\n', end='')