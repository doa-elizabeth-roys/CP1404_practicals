import wikipedia
finished = True
user_input = input("Search:")
while user_input != '':
    try:
        search = wikipedia.summary(user_input)
        print(search)
    except wikipedia.exceptions.DisambiguationError as e:
        print (e.options)
    user_input = input("Search:")



