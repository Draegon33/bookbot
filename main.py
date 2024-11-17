def main():
  with open("books/frankenstein.txt") as f:
    file_contents = f.read()

    print(f"---Begin report of {f.name} ---\n")
    
    print(f"{word_count(file_contents)} words found in the document\n")

    for k, v in char_count(file_contents).items():
      print(f"The '{k}' character was found {v} times")

    print("\n--End Report--")

def word_count(text):
  return len(text.split())

def char_count(text):
  char_list = {}
  for c in text.lower():
    if (c in char_list) and c.isalpha():
      char_list[c] += 1
    elif c.isalpha():
      char_list[c] = 1

  return char_list


main()