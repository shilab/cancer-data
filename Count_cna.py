import re
regex = re.compile(r'(\d+|\s+)')
studyList = ['TP', 'MO', 'SC', 'WCNC']
cnaDict = {}
countDict = {}
dipDict = {}
naDict = {}
cancer = input('what cancer type ?\n>>>') 
infiles = cancer + '_cna.txt'
eventFile = cancer + '_cnaEvents2.txt'
with open(infiles, 'r') as infile:
    gain = 0
    amp = 0
    sdel = 0
    ddel = 0
    diploid = 0
    NA = 0
    for line in infile.readlines():
        line = line.strip().split()
        sample = line[1]
        cna = line[2]
        if line[0].startswith('STUDY_ID'):
            continue
        if cna == 'NA':
            NA += 1
            naDict['Not Analyzed'] = NA
        if cna == '0':
            diploid += 1
            dipDict['diploid'] = diploid
        else:
            if sample.startswith('TP') or sample.startswith('MO') or sample.startswith('SC'):
                s = regex.split(sample)
                if s[2] == '':
                    continue
                else:
                    ss = ''.join(s)
                    cnaDict[ss] = str(cna)
            else:
                if sample.startswith('WCMC'):
                    ws = regex.split(sample)
                    if ws[4] == '_C' in ws and ws[3] == '1':
                        wss = ''.join(ws)
                        cnaDict[wss] = str(cna)
                    else:
                        continue
                else:
                    cnaDict[sample] = str(cna)

with open(eventFile, 'a') as e:
    for k in sorted(cnaDict.keys()):
        if cnaDict[k] == '2':
            amp += 1
            countDict['Amp'] = amp
        if cnaDict[k] == '1':
            gain += 1
            countDict['Gain'] = gain
        if cnaDict[k] == '-1':
            sdel +=1
            countDict['ShalDel'] = sdel
        if cnaDict[k] == '-2':
            ddel +=1
            countDict['DeepDel'] = ddel
        e.write(k + '\t' + cnaDict[k] + '\n') 
print(cancer, ':',countDict, '\n',naDict, '\n', dipDict)

