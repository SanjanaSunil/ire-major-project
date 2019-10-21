import re
import os
import wikipedia

class WikiParser:
    """
    Parses Wikipedia Hindi articles and returns named entities
    """

    def __init__(self):
        wikipedia.set_lang("hi")
        self.ners = []


    def get_content(self, title):
        if not title:
            return ""
        
        try:
            page = wikipedia.page(title, auto_suggest=False)
            return page.content
        except wikipedia.exceptions.PageError:
            return ""
        except wikipedia.exceptions.DisambiguationError:
            return ""


    def is_hindi_word(self, word):
        for char in word:
            if not (ord(u'\u0900') <= ord(char) <= ord(u'\u097F')):
                return False
        return True


    def extract_ners(self, doc):
        content = self.get_content(doc)
        f = open('hindi-part-of-speech-tagger/hindi.input.txt', 'w+')
        f.write(content)
        f.close()

        ners_sentence = []

        os.system('make -C hindi-part-of-speech-tagger tag')
        f = open('hindi-part-of-speech-tagger/hindi.output', 'r')

        line = f.readline()
        prev_tagged = False 
        while line:
            tagged = False
            if '<s>' in line:
                if len(ners_sentence) > 0:
                    self.ners.append(ners_sentence)
                    ners_sentence = []
            else:
                tags = line.split()
                if len(tags) >= 2 and 'NNP' in tags:
                    if self.is_hindi_word(tags[0]):         
                        if prev_tagged:
                            ners_sentence[-1] = ners_sentence[-1] + ' ' + tags[0]
                        else:
                            ners_sentence.append(tags[0])
                        tagged = True
            prev_tagged = tagged
            line = f.readline()

        if len(ners_sentence) > 0:
            self.ners.append(ners_sentence)
            ners_sentence = []
        
        f.close()



if __name__ ==  "__main__":
    wiki_extract = WikiParser()

    for i in range(10):
        wiki_extract.extract_ners(wikipedia.random())
    
    print(wiki_extract.ners)
