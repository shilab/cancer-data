def tumor_parser():
    symbolDict = {}
    matchDict = {}
    keyList = []
    cancer_type = input('Cancer type?\n')
    infile_name = cancer_type + '_Tumor_GeneExp.txt'
    input_string = input('Enter the genes **IN ALL CAPS** that you would like to analyze, each separated by a comma.\nHit ENTER when the list is complete.\n')
    geneList = input_string.replace(" "," ").split(",")
    gString = '\t'.join(geneList)
    outfile_name = cancer_type + '_TumGenExp.txt'
    with open(outfile_name, 'a') as out:
        with open('geneSymbols.txt', 'r') as infile1:
            for line in infile1.readlines():
                line = line.strip()
                col = line.split('\t')
                ensg = col[0]
                symbol = col[1]
                ensgList = ''.join(ensg).strip('\"').split()
                symbolList = ''.join(symbol).strip('\"').split()
                for e in ensgList:
                    for s in symbolList:
                        if s not in geneList:
                            continue
                        else:
                            symbolDict[e] = s
                            files = open(infile_name,'r')
                        for f in files.readlines():
                            cols = f.strip().split('\t')
                            ID = cols[0]
                            ensg = cols[1]
                            exp = cols[2]
                           
                            for k,v in sorted(symbolDict.items()):
                                if ensg != k:
                                    continue
                                else:
                                    matchDict[v] = {ID:exp}
                                    for value in sorted(matchDict.items()):
                                        if value in keyList:
                                            continue
                                        else:
                                            keyList.append(value)
                                            out.write(ID + '\t' + symbol + '\t' + exp + '\n')
                                
                                    
if __name__ == '__main__':
    tumor_parser()            
