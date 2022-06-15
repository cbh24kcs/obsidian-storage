import os

os.chdir('../')

for dirpath, dirnames, files in os.walk('.'):
    if '.git' in dirpath: continue
    full_path = dirpath + '\\.gitkeep'
    print(full_path)
    f = open(full_path, 'w')
    f.flush()
    f.close()