import re
import wikipedia

# import nltk
# from nltk.tag import tnt
# from nltk.corpus import indian

class WikiParser:
    """
    Parses Wikipedia Hindi articles and returns content
    """

    def __init__(self):
        wikipedia.set_lang("hi")
        # train_data = indian.tagged_sents('hindi.pos')
        # self.tnt_pos_tagger = tnt.TnT()
        # self.tnt_pos_tagger.train(train_data)


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

    
    # def pos_tag(self, sentence):
    #     return self.tnt_pos_tagger.tag(nltk.word_tokenize(sentence))


    def extract_ners(self, doc):
        content = self.get_content(doc)
        f = open('hindi-part-of-speech-tagger/hindi.input.txt', 'w+')
        f.write(content)
        f.close()
        # sentences = content.split('।')
        # for sentence in sentences:
        #     if sentence:
        #         tags = self.pos_tag(sentence)
        #         print(tags)




if __name__ ==  "__main__":
    wiki_extract = WikiParser()
    wiki_extract.extract_ners("उत्तर प्रदेश")
