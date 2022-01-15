favorite_languages = { 
  'den': 'python', 
  'vanya': 'js', 
  'kirill': 'php', 
  'renat': 'python', 
  }
for name, value in sorted(favorite_languages.items()): 
    print(f"{name.title()}, thank you for taking the poll. {value.title()}")
