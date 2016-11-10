def main():

  filename = 'data/time_dependent_cardiovascular.txt'
  f = open(filename, 'r')
  lines = f.readlines()
  f.close()

  # initialize matrix
  ###################


  # gather data
  ###################
  for i in range(len(lines)):
    inst_line = lines[i].strip().split('\t')
    if i > 0:
      # 0: Experiment ID
      # 1: Experiment Name
      # 2: Symbol
      # 3: Entrez Gene ID
      # 4: Fold Change
      # 5: p-value

      inst_col = inst_line[1]
      inst_row = inst_line[2]
      inst_val = inst_line[4]


  # save matrix
  ###################


main()