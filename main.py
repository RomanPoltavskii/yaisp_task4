def text_from_file(path):

    with open(path, encoding='utf-8') as file:
        text = file.read()#.replace('\n', '').replace('\r', '')
    return text


def count_vowels_consonants(word):
    vowels = set('аеёиоуэыюяАЕЁИОУЫЭЮЯ')
    consonants = set('йцкнгшщзхъфвпрлджчсмтьбЙЦКНГШЩЗХЪФВПРЛДЖЧСМТЬБ')
    vowel_count = 0
    consonant_count = 0

    for letter in word:
        if letter in vowels:
            vowel_count += 1

    for letter in word:
        if letter in consonants:
            consonant_count += 1

    #vowel_count = sum(1 for letter in word if letter in vowels)
    #consonant_count = sum(1 for letter in word if letter in consonants)

    return vowel_count, consonant_count

def find_words(text):
    words = set()
    for word in text.split():
        vowel_count, consonant_count = count_vowels_consonants(word)
        if vowel_count > consonant_count:
            words.add(word.lower())
    return list(words)

text = text_from_file('input.txt')
print(text.split())
result = find_words(text)
print(result)