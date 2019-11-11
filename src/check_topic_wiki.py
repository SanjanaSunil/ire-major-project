"""
Takes as input a list of lists of NER's in sentence and returns
"""
import argparse
import pickle
import wikipediaapi

from tqdm import tqdm

wiki_hi = wikipediaapi.Wikipedia('hi')

def check_phrase(phrase):
    page_py = wiki_hi.page(phrase)
    return page_py.exists()

def get_sentences(input_file):
    sentences = list()
    f = open(input_file, 'r')
    data = f.read()
    data = data.split("],")
    for entry in data:
        entry = entry.strip()
        entry = entry.strip("[")
        entry = entry.strip("]]")
        entry = entry.strip("[[")
        entry_words = entry.split(",")
        entry_words = [item.strip().replace("\'", "") for item in entry_words]
            
        sentences.append(entry_words)
        # print("Entry is:", entry_words)
    return sentences

def get_sentences_pickle(input_file):
    new_sentences = list()
    f = open(input_file, 'rb')
    sentences = pickle.load(f)
    # print(sentences)
    for sentence in sentences:
        entry_words = [item.strip().replace("\'", "") for item in sentence]
        new_sentences.append(entry_words)
    # print(new_sentences)
    return new_sentences

def get_words(sentences):
    word_list = list()
    for sentence in tqdm(sentences):
        for word in sentence:
            if not check_phrase(word):
                word_list.append(word)
    return word_list

def save(output, dir):
    with open(dir, 'w') as f:
        for s in output:
            f.write(str(s) + '\n')

def main(data_path, out_path, is_pickle):
    if not is_pickle:
        sentences = get_sentences(data_path)
    else:
        sentences = get_sentences_pickle(data_path)

    non_wiki_words = get_words(sentences)
    # non_wiki_bigrams = get_bigrams(sentences)
    # print(non_wiki_words)
    save(non_wiki_words, out_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    ## Required parameters
    parser.add_argument("-i","--data_file_path", type=str, required=True)
    parser.add_argument("-o", "--output_file_path", type=str, required=True)
    parser.add_argument("-p", "--pickle_file", type=bool, required=True)

args = parser.parse_args()
    
main(   data_path=args.data_file_path, 
        out_path=args.output_file_path,
        is_pickle=args.pickle_file)
