import wikipedia
finished = True
user_input = input("Search:")
while user_input != '':
    try:
        search = wikipedia.page(user_input)
        print(search.title)
        print(search.summary)
        print(search.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print (e.options)
    user_input = input("Search:")



