# TODO: TUI

# with open('words5.txt', 'r') as f:
#   words = f.read().splitlines()

from rich import print
from words import words


_1st_letter = ''
_2nd_letter = ''
_3rd_letter = ''
_4th_letter = ''
_5th_letter = ''
_1st_not_letters = ''
_2nd_not_letters = ''
_3rd_not_letters = ''
_4th_not_letters = ''
_5th_not_letters = ''
has_letters_ = ''
has_not_letters_ = ''

# 1 beginnt mit 'SU'
# 2 enthält 'A'
# 3 enthält nicht 'TL'
# 4 hat nach 'SU' noch 3 Buchstaben
# 1         2            3         4
"^p(?=[a-z]*er)(?![a-z]*[ahjuo])[a-z]{3}$"
# PERKY
# ^pe(?=[a-z]*rk)(?![a-z]*[ahjuo])[a-z]{3}$

letter_frequencies = {
  "e": 0.13,
  "t": 0.091,
  "a": 0.082,
  "o": 0.075,
  "i": 0.07,
  "n": 0.067,
  "s": 0.063,
  "h": 0.061,
  "r": 0.06,
  "d": 0.043,
  "l": 0.04,
  "c": 0.028,
  "u": 0.028,
  "m": 0.025,
  "w": 0.024,
  "f": 0.022,
  "g": 0.02,
  "y": 0.02,
  "p": 0.019,
  "b": 0.015,
  "v": 0.0098,
  "k": 0.0077,
  "j": 0.0015,
  "x": 0.0015,
  "q": 0.00095,
  "z": 0.00074
}


def word_score(word):
  letters_in_word = list(set(word.lower()))
  word_letter_frequencies = [letter_frequencies.get(letter, 0) for letter in letters_in_word]
  word_score = sum(word_letter_frequencies)
  return word_score


def top_10_words(lwords: list):
  return list(reversed(sorted(lwords, key=word_score)))[:10]


def letter_on_1(word):
  return word[0] == _1st_letter


def letter_on_2(word):
  return word[1] == _2nd_letter


def letter_on_3(word):
  return word[2] == _3rd_letter


def letter_on_4(word):
  return word[3] == _4th_letter


def letter_on_5(word):
  return word[4] == _5th_letter


def letters_not_on_1(word):
  for letter in _1st_not_letters:
    if letter == word[0]:
      return False
  return True


def letters_not_on_2(word):
  for letter in _2nd_not_letters:
    if letter == word[1]:
      return False
  return True


def letters_not_on_3(word):
  for letter in _3rd_not_letters:
    if letter == word[2]:
      return False
  return True


def letters_not_on_4(word):
  for letter in _4th_not_letters:
    if letter == word[3]:
      return False
  return True


def letters_not_on_5(word):
  for letter in _5th_not_letters:
    if letter == word[4]:
      return False
  return True


def has_letters(word):
  for letter in has_letters_:
    if letter not in word:
      return False
  return True


def has_not_letters(word):
  for letter in has_not_letters_:
    if letter in word:
      return False
  return True


print(len(words), 'words in words5.txt')

if _1st_letter:
  words = list(filter(letter_on_1, words))

if _2nd_letter:
  words = list(filter(letter_on_2, words))

if _3rd_letter:
  words = list(filter(letter_on_3, words))

if _4th_letter:
  words = list(filter(letter_on_4, words))

if _5th_letter:
  words = list(filter(letter_on_5, words))

if _1st_not_letters:
  words = list(filter(letters_not_on_1, words))

if _2nd_not_letters:
  words = list(filter(letters_not_on_2, words))

if _3rd_not_letters:
  words = list(filter(letters_not_on_3, words))

if _4th_not_letters:
  words = list(filter(letters_not_on_4, words))

if _5th_not_letters:
  words = list(filter(letters_not_on_5, words))

if has_letters_:
  words = list(filter(has_letters, words))
  print(f'{len(words)} haben \t"{has_letters_}"')

if has_not_letters_:
  words = list(filter(has_not_letters, words))
  print(f'{len(words)} haben nicht \t"{has_not_letters_}"')

print(f'{len(words)} Wörter übrig')

# Höchster wordscore hat?
lTop_10_words = top_10_words(words)

for idx, word in enumerate(lTop_10_words):
  print(f'{idx}: {word} - {word_score(word)}')

print('\n', lTop_10_words[0].upper(), '\n')