idList = []
cancer = input(">>>what cancer type?\n>>>")
infilename = cancer + 'mutations.txt'
outfilename = cancer + 'mute_Count.txt'
with open(infilename, 'r') as infile:
    with open(outfilename, 'a') as outfile:
        count = 0
        for line in infile.readlines():
            line =  line.split()
            mute = line[2]
            sample = line[1]
            if sample in idList:
                continue
            if mute == 'NA':
                continue
            if mute == 'APEX2':
                continue
            else:
                idList.append(sample)
                count += 1
            outfile.write(mute + '\n' + str(count))
