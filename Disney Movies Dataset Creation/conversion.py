import re

amounts = r"thousand|million|billion"
number = r"\d+(,\d{3})*\.*\d*"

word_re = rf"\${number}(-|\sto\s|-)?({number})?\s({amounts})"
value_re = rf"\${number}"


# money_convesion("$12.2 million") = 12200000 -> word syntax
# money_conversion("$790,000") = 79000 -> value syntax

def word_to_value(word) :
  value_dict = {"thousand" : 1000 , "million" : 1000000 , "billion" : 1000000000}
  return value_dict[word]

def parse_word_syntax(string) :
  value_string = re.search(number , string).group()
  value = float(value_string.replace("," , ""))
  word = re.search(amounts , string).group()
  word_value = word_to_value(word)
  return value * word_value
  
def parse_value_syntax(string) :
  value_string = re.search(number , string).group()
  value = float(value_string.replace("," , ""))
  return value

def money_conversion(money) :
  
  if isinstance(money,list) :
    money = money[0]
  
  value_syntax = re.search(value_re , money)
  word_syntax = re.search(word_re , money)
  
  if word_syntax :
    return parse_word_syntax(word_syntax.group())

  elif value_syntax :
    return parse_value_syntax(value_syntax.group())
    