def main():
  import numpy as np
  import pandas as pd

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

    if i > 0:
      all_exp.append(inst_line[1])
      all_gene.append(inst_line[2])

  all_exp = sorted(list(set(all_exp)))
  all_gene = sorted(list(set(all_gene)))

  mat = np.zeros([len(all_gene), len(all_exp)])

  # gather data
  ###################
  for i in range(len(lines)):
    inst_line = lines[i].strip().split('\t')
    if i > 0:

      inst_exp = inst_line[1]
      inst_gene = inst_line[2]
      inst_val = np.log2(float(inst_line[4]))

      row_index = all_gene.index(inst_gene)
      col_index = all_exp.index(inst_exp)

      mat[row_index, col_index] = inst_val

  # save matrix
  ###################
  df = pd.DataFrame(data=mat, columns=all_exp, index=all_gene)

  # only keep TGM2 KD experiments
  print(all_exp)

  keep_col = []
  for inst_exp in all_exp:
    if 'TGM2 KD vs' in inst_exp:
      keep_col.append(inst_exp)

  df = df[keep_col]

  # remove genes with no names
  keep_row = []
  for inst_gene in all_gene:
    if inst_gene != '':
      keep_row.append(inst_gene)

  # filter out rows (using transposes)
  df = df.transpose()
  df = df[keep_row]
  df = df.transpose()

  # add gene title
  old_rows = df.index.tolist()
  new_rows = []
  for inst_row in old_rows:
      inst_row = 'gene: ' + inst_row
      new_rows.append(inst_row)

  df.index = new_rows

  # clean experiment names
  old_names = df.columns.tolist()
  new_names = []
  for inst_name in old_names:

    inst_name = inst_name.replace('(','').replace(') |','').replace('1 microM, ','').replace(' h', 'hr').replace('WT A','WT, A')

    inst_name = 'treatment: ' + inst_name

    inst_treatment = 'ATRA exposure: '+ str(0)
    if '48' in inst_name:
      inst_treatment = 'ATRA exposure: '+ str(48)
    if '72' in inst_name:
      inst_treatment = 'ATRA exposure: '+ str(72)

    inst_tuple = (inst_name, inst_treatment)
    new_names.append(inst_tuple)

  df.columns = new_names

  df.to_csv('data/td_cardio_matrix.txt', sep='\t')

main()