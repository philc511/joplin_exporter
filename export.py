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
    content = f.readlines()

  for line in content:
    print(line)

  print('XXX')
  print('XXX')


if __name__ == "__main__":
   main(['-isource/0b38f33abf634bf9b17ab47a550bcc35.md'])    