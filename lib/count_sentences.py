#!/usr/bin/env python3

class MyString:
  def __init__(self, value=''):
    self.value = value


  def get_value(self):
    return self.get_value
  
  def set_value(self, value):
    if isinstance(value,str):
      self._value = value
    else:
      print("The value must be a string.")

  value = property(get_value, set_value)

  def is_sentence(self):
    return self._value.endswith(".")
  
  def is_question(self):
     return self._value.endswith("?")
  
  def is_exclamation(self):
     return self._value.endswith("!")
  
  def count_sentences(self):
      sections = self._value.split() 
      text_list =[section for section in sections if section.endswith(".") or section.endswith("?") or section.endswith("!")]
      return len(text_list)
    