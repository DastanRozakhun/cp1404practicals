"""
CP1404/CP5632 Practical
Program to display info from wikipedia based on page title input
"""
import wikipedia

def main():
    page_title = str(input("Enter page title: "))
    while page_title != '':
        try:
            wiki_page = wikipedia.page(page_title, auto_suggest=False)
            print(wiki_page.title)
            print(wiki_page.summary)
            print(wiki_page.url)

        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search: ")
            print(e.options)

        except wikipedia.exceptions.PageError:
            print(f"Page id {page_title} does not match any pages. Try another id!")

        page_title = str(input("\nEnter page title: "))

    print("Thank you.")

main()
