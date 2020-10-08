import random

def primary_line():
    # print("Keep it logically awesome.")

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()
    # for quote in quotes:

    # print('-------')
    # print(quote)
    last = len(quotes) -1
    rnd = random.randint(0, last)
    print(quotes[rnd])

if __name__== "__main__":
    primary_line()
