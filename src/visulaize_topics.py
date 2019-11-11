import argparse


def get_words(dir_loc):
    all_words = set()
    f = open(dir_loc, 'r')
    lines = f.readlines()
    for line in lines:
        word = line.strip("\n")
        all_words.add(word)
    return all_words


def main(data_path, out_path):
    word_list = get_words(data_path)
    print(word_list)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    ## Required parameters
    parser.add_argument("-i","--data_file_path", type=str, required=True)
    parser.add_argument("-o", "--output_file_path", type=str, required=True)


args = parser.parse_args()
    
main(   data_path=args.data_file_path, 
        out_path=args.output_file_path)
