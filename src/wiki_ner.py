import re
import wikipedia

class WikiParser:
    """
    Parses Wikipedia Hindi articles and returns content
    """

    def __init__(self):
        wikipedia.set_lang("hi")


    def get_content(self, title):
        if not title:
            return ""
        
        try:
            page = wikipedia.page(title, auto_suggest=False)

            summary = page.summary.strip()
            summary = summary.replace('\r\n', '\n').replace('\r', '\n')
            summary = re.sub('\n+', "\n", summary).replace('\n', '\n\n')
        
            return page.content

        except wikipedia.exceptions.PageError:
            return ""
        except wikipedia.exceptions.DisambiguationError:
            return ""



if __name__ ==  "__main__":
    wiki_extract = WikiParser()
    print(wiki_extract.get_content("उत्तर प्रदेश"))
