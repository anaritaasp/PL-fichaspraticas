import re
file_names = [
  "document.txt", # válido
  "file name.docx", # inválido
  "image_001.jpg", # válido
  "script.sh.txt", # válido
  "test_file.txt", # válido
  "file_name.", # inválido
  "my_resume.docx", # válido
  ".hidden-file.txt", # válido
  "important-file.text file", # inválido
  "file%name.jpg" # inválido
]
def createDict(file_names):
  myFiles=dict()
  for name in file_names:
    m= re.fullmatch('^\.*[\w-]+(\.[a-z]+)+$',name)
    if m:
      extensao = m.group(1)
      if extensao in myFiles:
        myFiles[extensao].append(m.group(0))
      else:
        myFiles[extensao]=[m.group(0)]
  return myFiles


print(createDict(file_names))
