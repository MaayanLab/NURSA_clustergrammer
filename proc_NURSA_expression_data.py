def main():

  filename = 'data/time_dependent_cardiovascular.txt'
  f = open(filename, 'r')
  lines = f.readlines()
  f.close()

  for i in range(len(lines)):
    inst_line = lines[i].strip().split()
    if i > 0:
      print(inst_line)

main()