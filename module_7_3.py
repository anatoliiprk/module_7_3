print('------\nЗадача "Найдет везде"\n------')

class WordsFinder:
    def __init__(self, *file_names: tuple):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation = ',.=!?;:'
        for i in range(len(self.file_names)):
            words = []
            with open(self.file_names[i], 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    line = line.translate(str.maketrans('', '', punctuation))
                    line = line.replace(' - ', ' ')
                    words.extend(line.split())
                all_words[self.file_names[i]] = words
        return all_words

    def find(self, word: str):
        find_word = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            for i in range(len(words)):
                if word == words[i]:
                    find_word[name] = i + 1
                    return find_word

    def count(self, word: str):
        count_word = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            counter = 0
            for i in range(len(words)):
                if word == words[i]:
                    counter += 1
                    count_word[name] = counter
        return count_word

finder1 = WordsFinder('test_file.txt', 'test.txt', 'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())

print(finder1.find('TeXt'))
print(finder1.count('teXT'))

print('------')