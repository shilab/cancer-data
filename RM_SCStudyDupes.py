import re
from collections import defaultdict
regex = re.compile(r'(\d+|\s+)')
tpmoscDict = defaultdict(list)
wcDict = defaultdict(list)
normDict = {}
finalDict = {}
cancer = input('What cancer type?\n>>>')
inputFile = cancer + '_cnaEvents.txt'
outputFile = cancer + '_cnaDupesRemoved.txt'
with open(inputFile, 'r') as infile:
    for line in infile.readlines():
        cols = line.strip().split('\t')
        sample = cols[0]
        cn = cols[1]
        if sample.startswith('TP') or sample.startswith('MO') or sample.startswith('SC'):
            s = regex.split(sample)
            if s[2] == "":
                continue
            else:
                s.pop(2)
                ss = ''.join(s)
                tpmoscDict[ss].append(cn)
           
        if sample.startswith('WCMC'):
            ws = regex.split(sample)
            if ws[4] == 'N' or not ws[3] == '1':
                continue
            else:
                wss = ''.join(ws)
                ws = wss.split('_')
                [ws[0]].append(cn)

    
