def run(Directory):
  from os import walk
  from os.path import join

  Word = ""
  for root, _, files in walk(Directory, topdown=False):
      for file in files:
          with open(join(root, file), 'r') as f:
              for line in f.read().splitlines():
                  for line_char in line:
                      if (line_char.isupper()): Word += line_char
                      elif (line_char.islower()): Word += line_char
  return Word
