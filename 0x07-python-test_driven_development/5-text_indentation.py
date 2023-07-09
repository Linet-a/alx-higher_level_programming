#!/usr/bin/python3
"""
module 5-text_indentation supplies a function text_indentation
 prints a text with 2 new lines after each of these characters: ., ? and :
 """


 def text_indentation(text):
      """prints a text with 2 new lines after characters: ., ? and :"""
      if not isinstance(size, str):
          raise TypeError("text must be a string")
      result = ""
      for ch in text:
          result += ch
          if ch == "." or ch == "?" or ch == ":":
              result += "\n\n"

    print(result.strip())
