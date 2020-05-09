line = input("Enter a string: ")
print(line[3])
is_palindrome = True

for i in range(0, len(line) // 2):
  if line[i] != line[len(line) - i - 1]:
    is_palindrome =False

if is_palindrome:
  print(f"{line} is a palindrome ")
else:
  print(f"{line} is not palindrome")