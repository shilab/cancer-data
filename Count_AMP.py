idList = []
cancer = input('what cancer type ?\n>>>') 
infiles = cancer + 'cna.txt'
outfiles = cancer + 'cna_Count.txt' 
with open(infiles, 'r') as infile:
    count = 0
    for line in infile.readlines():
        line =  line.split()
        cna = line[2]
        sample = line[1]
        if sample in idList:
            continue
        if cna == 'APEX2':
            continue
        if cna == 'NA':
            continue
        if cna == '0':
            continue
        if cna == '-1':
            continue
        else:
            idList.append(sample)
            count += 1
        
        print(count)

