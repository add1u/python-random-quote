def primary_line():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  for quote in quotes:

      print('-------')
      print(quote)
  # print(quotes)

if __name__== "__main__":
  primary_line()
