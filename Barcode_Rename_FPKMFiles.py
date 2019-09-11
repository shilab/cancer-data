import os

def rename():
    mapDict = {}
    spentList = []
    with open("barcodes.txt", 'r') as infile:
        for line in infile.readlines():
            line = line.strip()
            col = line.split('\t')
            uuid = col[0]
            barcode = col[1]
            uuidList = ''.join(uuid).strip('\"').split()
            barcodeList = ''.join(barcode).strip('\"').split()
            for x in uuidList:
                for y in barcodeList:
                    mapDict[x] = y
                    files = [f for f in os.listdir('.') if os.path.isfile(f)]
                    for f in files:
                        filename = (f)[:-9]
                        for k in sorted(mapDict.keys()):
                            if filename != k:
                                continue
                            if k in spentList:
                                continue
                            else:
                                new_file = mapDict[k]
                                spentList.append(k)  
                                os.replace(f, new_file)
                                
                    
if __name__ == '__main__':
    rename() 
