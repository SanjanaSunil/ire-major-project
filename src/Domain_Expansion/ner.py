import os
from os import listdir
from os.path import isfile, join
import pickle

class DataNER:
    """
    Performs NER on scraped data
    """

    def __init__(self, path):
        self.ners = []
        self.ner_files = []
        self.get_data_files(path)

    
    def get_data_files(self, path):
        dirs = []
        dirs.append(path)

        while len(dirs) > 0:
            sub_dirs = []
            for data_path in dirs:
                for f in listdir(data_path):
                    file_path = join(data_path, f)
                    if isfile(file_path):
                        self.ner_files.append(file_path)
                    else:
                        sub_dirs.append(file_path)
            dirs = sub_dirs
        

    def is_hindi_word(self, word):
        for char in word:
            if not (ord(u'\u0900') <= ord(char) <= ord(u'\u097F')):
                return False
        return True


    def perform_ner(self):
        for ner_f in self.ner_files:
            print(ner_f)
            f = open(ner_f, 'r')
            content = f.read()
            f.close()

            f = open('../hindi-part-of-speech-tagger/hindi.input.txt', 'w+')
            f.write(content)
            f.close()

            ners_sentence = []

            os.system('make -C ../hindi-part-of-speech-tagger tag')
            f = open('../hindi-part-of-speech-tagger/hindi.output', 'r')
            
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
    data_ner = DataNER('../../data')
    data_ner.perform_ner()

    f = open('ner_list.txt','wb')
    pickle.dump(data_ner.ners, f)
    f.close()