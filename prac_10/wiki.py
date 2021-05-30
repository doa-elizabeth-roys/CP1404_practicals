import wikipedia
search = wikipedia.summary(input("Search:"))
while search != '':
    print(search)
    search = wikipedia.summary(input("Search:"))



