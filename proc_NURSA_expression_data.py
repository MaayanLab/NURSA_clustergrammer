def main():

  filename = 'data/time_dependent_cardiovascular.txt'
  f = open(filename, 'r')
  lines = f.readlines()
  f.close()

  # 0: Experiment ID
  # 1: Experiment Name
  # 2: Symbol
  # 3: Entrez Gene ID
  # 4: Fold Change
  # 5: p-value

  # initialize matrix
  ###################
  all_exp = []
  all_gene = []
  for i in range(len(lines)):
    inst_line = lines[i].strip().split('\t')

    all_exp.append(inst_line[1])

  print(len(all_exp))
  all_exp = sorted(list(set(all_exp)))
  print(len(all_exp))
  print(all_exp)

  # gather data
  ###################
  for i in range(len(lines)):
    inst_line = lines[i].strip().split('\t')
    if i > 0:

      inst_col = inst_line[1]
      inst_row = inst_line[2]
      inst_val = inst_line[4]


  # save matrix
  ###################


main()