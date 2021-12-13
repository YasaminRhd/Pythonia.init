def printNames (input:"names.txt"):
  file = open ("names.txt")
  a = file.read()
  l = a.split()
  n=len(l)
  for word in l:
    if "," in word:
      index = l.index(word)
      b = word.replace(",","")
      print( b , end=" ")
      if index+1 in range(n):
        print(l[index + 1])

printNames("names.txt")