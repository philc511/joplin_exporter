import sys, getopt

def main(argv):
  inputfile = ''
  try:
    opts, args = getopt.getopt(argv,"hi:",["ifile="])
  except getopt.GetoptError:
    print('test.py -i <inputfile> -o <outputfile>')
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print('test.py -i <inputfile> -o <outputfile>')
      sys.exit()
    elif opt in ("-i", "--ifile"):
      inputfile = arg
  print('Input file is "', inputfile)


  with open(inputfile) as f:
    all_content = f.read()
  lines = all_content.splitlines()

  content = ''
  is_content = True
  id = ""
  creation_date = ""
  last_modified = ""
  
  for line in lines:
    if line.startswith('id: '):
      is_content = False
      id = line.replace('id: ','')
    elif line.startswith('created_time'):
      creation_date = line.replace('created_time','')
    elif line.startswith('updated_time'):
      last_modified = line.replace('updated_time','')
    else:
      if is_content:
        content += line
  note = {
    "id" : id,
    "content" : content,
    "creationDate" : creation_date,
    "lastModified" : last_modified,
    "markdown" : True
  }

  print(note)

if __name__ == "__main__":
   main(['-isource/0b38f33abf634bf9b17ab47a550bcc35.md'])    
