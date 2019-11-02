
import os


outfile_name = input("What would you like to name your output?\n")
gene_name = input("What is the ENSG of the gene you are analyzing?\n>>>")
tumorCodeList = ['01', '02', '03', '04', '05', '06', '07', '08', '09']
matchedList = []
tumorList = []
with open(outfile_name, 'a') as outfile:
    outfile.write('ID\tNcode\tNexp\tTcode\tTexp\n')
for filename in os.listdir('.'):
    if filename.startswith('TCGA'):
        if (filename)[13:15] in tumorCodeList:
            if (filename)[8:12] in tumorList:
                continue
            else:
                stum = (filename)[13:15]
                ta = (filename)[8:12]
                tumorList.append(ta)
                with open(os.path.join('.', filename)) as f:
                    for line in f.readlines():
                        if line.startswith(gene_name):
                            cols = line.strip().split('\t')
                            texp = cols[1]
                            continue
        if (filename)[13:15] not in tumorCodeList:
            if (filename)[8:12] in matchedList:
                continue
            else:
                snorm = (filename)[13:15]
                na = (filename)[8:12]
                matchedList.append(na)
                with open(os.path.join('.', filename)) as f:
                    for line in f.readlines():
                        if line.startswith(gene_name):
                            cols = line.strip().split('\t')
                            nexp = cols[1]
                            continue
            if ta != na:
                continue
            else:
                with open(outfile_name, 'a') as outfile:
                    outfile.write('\n' + na + '\t' + snorm + '\t' + nexp + '\t' + stum + '\t' + texp ) 
                    
                    
                
                        
                        
                    

                                      










            
                            
                               
                                
                                 
                                    
                                                                    
                                            
                                    
                                    #for key, value in sorted(dataDict.items()):
                                        
                                    #        print(key + '\t' + value + '\t' + e)
                                #for k, v in sorted(dataDict.items()):
                                #    for i in v:
                                #        outfile.write(k + '\t' + i + '\t' +'\t')     
                            
                                           
                          
                      
                                     
                                
                                
                                    
                                     

                                   
                                    
               
    
                                                
                                                      

                                    
                                                     
                                                        
                                              


