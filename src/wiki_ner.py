import re
import os
import wikipedia

class WikiParser:
    """
    Parses Wikipedia Hindi articles and returns named entities
    """

    def __init__(self):
        wikipedia.set_lang("hi")


    def get_content(self, title):
        if not title:
            return ""
        
        try:
            page = wikipedia.page(title, auto_suggest=False)

            # summary = page.summary.strip()
            # summary = summary.replace('\r\n', '\n').replace('\r', '\n')
            # summary = re.sub('\n+', "\n", summary).replace('\n', '\n\n')
        
            return page.content

        except wikipedia.exceptions.PageError:
            return ""
        except wikipedia.exceptions.DisambiguationError:
            return ""


    def extract_ners(self, doc):
        content = self.get_content(doc)
        f = open('hindi-part-of-speech-tagger/hindi.input.txt', 'w+')
        f.write(content)
        f.close()

        ners = []
        ners_sentence = []

        os.system('make -C hindi-part-of-speech-tagger tag')
        f = open('hindi-part-of-speech-tagger/hindi.output', 'r')
        line = f.readline()
        prev_ner = False 
        while line:
            if '<s>' in line:
                if len(ners_sentence) > 0:
                    ners.append(ners_sentence)
                    ners_sentence = []
                prev_ner = False
            else:
                tags = line.split()
                if len(tags) >= 2 and 'NNP' in tags and tags[0] != '==':
                    if prev_ner:
                        ners_sentence[-1] = ners_sentence[-1] + ' ' + tags[0]
                    else:
                        ners_sentence.append(tags[0])
                    prev_ner = True
                else:
                    prev_ner = False
            line = f.readline()
        if len(ners_sentence) > 0:
            ners.append(ners_sentence)
            ners_sentence = []
        f.close()
    
        print(ners)



if __name__ ==  "__main__":
    wiki_extract = WikiParser()
    wiki_extract.extract_ners(wikipedia.random())
