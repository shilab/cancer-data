from collections import defaultdict
muteDict = defaultdict(list)
cancer = input(">>>what cancer type?\n>>>")
infilename = cancer + '_mutations.txt'
outfilename = cancer + 'mute_Count.txt'
with open(infilename, 'r') as infile:
    count = 0
    for line in infile.readlines():
        if line.startswith('STUDY_ID'):
            continue
        else:
            line =  line.split()
            mute = line[2]
            sample = line[1]
            if mute == 'NA':
                continue
            else:
                muteDict[(sample,mute)] = []
with open(outfilename, 'a') as outfile:
    for k,v in sorted(muteDict.items()):
        count += 1
        muteDict[k].append(count)
        outfile.write(k[0] + '\t' + k[1] + '\t' + str(v[0]) + '\n')
