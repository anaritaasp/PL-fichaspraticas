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
def read(file_names):
  for name in file_names:
    if re.findall('^\.*[\w-]+(\.[a-z]+)+$',name):
        print("válido")
    else:
        print("inválido")   

read(file_names)