#!/usr/bin/env python3

class MyString:
  def __init__(self, value = ''):
    self.value = value
  def get_value(self):
      return self._value
  def set_value(self, value):
      if(type(value) == str):
        self._value =  value
      else:
         print('The value must be a string.')
  value = property(get_value, set_value)
  def is_sentence(self):
     if self.value.endswith('.'):
        return True
     else:
        return False
  def is_question(self):
     if self.value.endswith('?'):
        return True
     else:
        return False
  def is_exclamation(self):
     if self.value.endswith('!'):
        return True
     else:
        return False
  def count_sentences(self):
     n = 0
     string = self.value.replace('!', '.')
     string2 = ''.join(string).replace('?', '.')
     string3 = string2.split('.')
     for s in string3:
        if len(s) > 0:
           n += 1
     return n
    #  n = 0
    #  for index, l in enumerate(self.value):
    #     if not l.endswith('...') and l.endswith('.'):
    #        n += 1
    #     print(index, index+1)
    #  return n
  
  
