# code here
s="Wow!!!, we are going ahead with our course to learn machine learning ---are'nt you excited? :)"
punctuation='''`~!@#$%^&*(){}|[]\-_+=,.><?/'":; '''

input_str=s
for char in  input_str:
  if char in punctuation:
    s=s.replace(char," ")

print(s)
