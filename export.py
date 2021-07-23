import sys, getopt, json, os

def main(argv):
  inputfolder = ''
  try:
    opts, args = getopt.getopt(argv,"hi:",["idir="])
  except getopt.GetoptError:
    print('test.py -i <inputdir>')
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print('test.py -i <inputdir>')
      sys.exit()
    elif opt in ("-i", "--idir"):
      inputfolder = arg

  files = os.listdir(inputfolder)

  notes = get_notes(files, inputfolder)

  all = {
    "activeNotes": notes,
    "trashedNotes": []
  }

  print(json.dumps(all, indent=2))

def get_notes(files, inputfolder):
  notes = []

  for file in files:
    with open(os.path.join(inputfolder, file)) as f:
      all_content = f.read()
  
    notes.append(create_note(all_content))

  return notes

def create_note(md_doc):
  lines = md_doc.splitlines()

  content = ''
  is_content = True
  id = ""
  creation_date = ""
  last_modified = ""
  
  for line in lines:
    if line.startswith('id: '):
      is_content = False
      id = line.replace('id: ','')
    elif line.startswith('created_time: '):
      creation_date = line.replace('created_time: ','')
    elif line.startswith('updated_time: '):
      last_modified = line.replace('updated_time: ','')
    else:
      if is_content:
        content += line
        content += "\r\n"
  return {
    "id" : id,
    "content" : content,
    "creationDate" : creation_date,
    "lastModified" : last_modified,
    "markdown" : True
  }

if __name__ == "__main__":
   main(['-isource'])    
