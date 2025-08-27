# Uses regular expression
import re
def is_pangram_old(sentence):
    alphabets_only = re.sub(r'[^a-z]', '', sentence.lower())
    char_set = set(alphabets_only)
    return len(char_set) == 26

# Single line pythonic
def is_pangram_pythonic(s):
    return set('abcdefghijklmnopqrstuvwxyz') <= set(s.lower())

# Fast, early exit, no unnecessary lower() ops
def is_pangram(s):
  alphabets = set('abcdefghijklmnopqrstuvwxyz')
  for c in s:
    c = c.lower()
    if c in alphabets:
      alphabets.remove(c)
      if not alphabets: return True
  return False