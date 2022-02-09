# TODO: TUI

# with open('words5.txt', 'r') as f:
#   words = f.read().splitlines()

from rich import print
from words import words

_1_letter = '_'
_2_letter = '_'
_3_letter = '_'
_4_letter = '_'
_5_letter = '_'
_1_not_letters = ''
_2_not_letters = ''
_3_not_letters = ''
_4_not_letters = ''
_5_not_letters = ''
_has_letters = ''
_has_not_letters = ''


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


def get_func_name(func):
  def func_name(*args, **kwargs):
    print(func.__name__, 'calling')
    return None
  return func_name


def word_score(word):
  letters_in_word = list(set(word.lower()))
  word_letter_frequencies = [letter_frequencies.get(letter, 0) for letter in letters_in_word]
  word_score = sum(word_letter_frequencies)
  return word_score


def top_10_words(lwords: list):
  return list(reversed(sorted(lwords, key=word_score)))[:10]


def letter_on_1(word):
  # print(f'letter_on_1(word) {_1_letter = }')
  return word[0] == _1_letter


def letter_on_2(word):
  return word[1] == _2_letter


def letter_on_3(word):
  return word[2] == _3_letter


def letter_on_4(word):
  return word[3] == _4_letter


def letter_on_5(word):
  return word[4] == _5_letter


def letters_not_on_1(word):
  for letter in _1_not_letters:
    if letter == word[0]:
      return False
  return True


def letters_not_on_2(word):
  for letter in _2_not_letters:
    if letter == word[1]:
      return False
  return True


def letters_not_on_3(word):
  for letter in _3_not_letters:
    if letter == word[2]:
      return False
  return True


def letters_not_on_4(word):
  for letter in _4_not_letters:
    if letter == word[3]:
      return False
  return True


def letters_not_on_5(word):
  for letter in _5_not_letters:
    if letter == word[4]:
      return False
  return True


def has_letters(word):
  for letter in _has_letters:
    if letter not in word:
      return False
  return True


def has_not_letters(word):
  for letter in _has_not_letters:
    if letter in word:
      return False
  return True


print()
print(len(words), 'Wörter in Wortliste')
print()

while True:
  if _1_letter != '_':
    print(f'ERSTER Buchstabe: {_1_letter.upper()}')
  else:
    _1_letter = input('erster Buchstabe?:\t') or '_'

  if _2_letter != '_':
    print(f'ZWEITER Buchstabe: {_2_letter.upper()}')
  else:
    _2_letter = input('zweiter Buchstabe?:\t') or '_'

  if _3_letter != '_':
    print(f'DRITTER Buchstabe: {_3_letter.upper()}')
  else:
    _3_letter = input('dritter Buchstabe?:\t') or '_'

  if _4_letter != '_':
    print(f'VIERTER Buchstabe: {_4_letter.upper()}')
  else:
    _4_letter = input('vierter Buchstabe?:\t') or '_'

  if _5_letter != '_':
    print(f'FÜNFTER Buchstabe: {_5_letter.upper()}')
  else:
    _5_letter = input('fünfter Buchstabe?:\t') or '_'

  if _1_letter == '_':
    _1_not_letters += input('erster Buchstabe NICHT?:\t')
  if _2_letter == '_':
    _2_not_letters += input('zweiter Buchstabe NICHT?:\t')
  if _3_letter == '_':
    _3_not_letters += input('dritter Buchstabe NICHT?:\t')
  if _4_letter == '_':
    _4_not_letters += input('vierter Buchstabe NICHT?:\t')
  if _5_letter == '_':
    _5_not_letters += input('fünfter Buchstabe NICHT?:\t')

  _has_letters += f'{_1_letter}{_2_letter}{_3_letter}{_4_letter}{_5_letter}'.replace('_', '')
  _has_letters += f'{_1_not_letters}{_2_not_letters}{_3_not_letters}{_4_not_letters}{_5_not_letters}'

  _has_letters = "".join(set(_has_letters))
  _has_not_letters = "".join(set(_has_not_letters))

  _has_letters += input(f'hat Buchstaben?\t[{_has_letters.upper()}] : ')
  _has_not_letters += input(f'hat Buchstaben NICHT?\t[{_has_not_letters.upper()}] : ')

  print()
  print(f'-> {_1_letter.upper()}{_2_letter.upper()}{_3_letter.upper()}{_4_letter.upper()}{_5_letter.upper()} <-')
  print()

  if _1_letter != '_':
    words = list(filter(letter_on_1, words))

  if _2_letter != '_':
    words = list(filter(letter_on_2, words))

  if _3_letter != '_':
    words = list(filter(letter_on_3, words))

  if _4_letter != '_':
    words = list(filter(letter_on_4, words))

  if _5_letter != '_':
    words = list(filter(letter_on_5, words))

  if _1_not_letters:
    words = list(filter(letters_not_on_1, words))

  if _2_not_letters:
    words = list(filter(letters_not_on_2, words))

  if _3_not_letters:
    words = list(filter(letters_not_on_3, words))

  if _4_not_letters:
    words = list(filter(letters_not_on_4, words))

  if _5_not_letters:
    words = list(filter(letters_not_on_5, words))

  if _has_letters:
    words = list(filter(has_letters, words))
    print()
    print(f'{len(words)} haben \t"{_has_letters.upper()}"')

  if _has_not_letters:
    words = list(filter(has_not_letters, words))
    print()
    print(f'{len(words)} haben nicht \t"{_has_not_letters.upper()}"')

  print(f'{len(words)} Wörter übrig')
  print()

  # Höchster wordscore hat?
  lTop_10_words = top_10_words(words)

  for idx, word in enumerate(lTop_10_words):
    print(f'{idx}: {word} - {word_score(word)}')

  print('\n', lTop_10_words[0].upper(), '\n')

  input('nächster Versuch...')
