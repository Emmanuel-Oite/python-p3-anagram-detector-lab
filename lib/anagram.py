# your code goes here!from typing import List

class Anagram:
    def __init__(self, word: str):
        self.word = word.lower()
        self.sorted_word = ''.join(sorted(self.word))

    def match(self, possible_anagrams: List[str]) -> List[str]:
        return [word for word in possible_anagrams if self.is_anagram(word)]

    def is_anagram(self, word: str) -> bool:
        return self.sorted_word == ''.join(sorted(word.lower()))