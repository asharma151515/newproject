import wikipedia

while True:
    search = input("Enter a page title or search phrase: ")
    if not search:
        break

    try:
        page = wikipedia.page(search)
        print("Title:", page.title)
        print("Summary:", page.summary)
        print("URL:", page.url)
        print()
    except wikipedia.DisambiguationError as e:
        print("Disambiguation page. Possible options:")
        options = e.options
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        print()
    except wikipedia.PageError:
        print("The page you are trying to search does not exist.")
        print()