spam = {'color': 'red', 'age': '42'}
print(spam.get('color', 0))
spam.setdefault('eggs', 15)
print(spam)