import random
def primary():
 

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 16
  first = 8
  rnd = random.randint(0, first)
  rnd2 = random.randint(8, last)
  print(quotes[rnd])
  print(quotes[rnd2])

if __name__== "__main__":
  primary()
