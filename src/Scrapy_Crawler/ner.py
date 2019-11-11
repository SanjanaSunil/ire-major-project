import os
import csv
import pickle

class DataNER:
    """
    Performs NER on scraped data
    """

    def __init__(self, path):
        self.ners = []
        self.ner_files = []
        self.perform_ner(path)
        

    def is_hindi_word(self, word):
        for char in word:
            if not (ord(u'\u0900') <= ord(char) <= ord(u'\u097F')):
                return False
        return True


    def perform_ner(self, path):
        with open(path, 'rt') as inp_f:
            data = csv.reader(inp_f)
            iter_cnt = 0
            for row in data:
                print(iter_cnt, '==================')
                if iter_cnt > 1000:
                    break
                iter_cnt += 1
                f = open('hindi-part-of-speech-tagger/hindi.input.txt', 'w+')
                f.write(row[3])
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
    data_ner = DataNER('output.csv')

    f = open('ner_list.txt','wb')
    pickle.dump(data_ner.ners, f)
    f.close()