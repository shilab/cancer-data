import os

def tumor_exp():
    matchList = []
    cancer_type = input("Cancer type?\n")
    outfile_name = cancer_type + '_' + 'Tumor' + '_' +  'GeneExp' + '.' + 'txt'
    tumorCodeList = ['01', '02', '03', '04', '05', '06', '07', '08', '09']
    matchedList = []
    tumorList = []
    with open(outfile_name, 'a') as outfile:
        outfile.write('id\tgene\tgene_expression\n')
        for filename in os.listdir('.'):
            if not filename.startswith('TCGA'): 
                continue
            else:
                if (filename)[-3:-1] in tumorCodeList:
                    if (filename) in tumorList:
                        continue
                    else:
                        ta = (filename)
                        tumorList.append(ta)
                   
                    with open(os.path.join('.', filename)) as f:
                        with open(outfile_name, 'a') as outfile:
                            for line in f.readlines():
                                cols2 = line.strip().split('\t')
                                ID = ta
                                ensg = cols2[0].split('.')
                                ensg = ensg[0]
                                exp = cols2[1]
                                outfile.write(ID + '\t' + ensg + '\t' + exp + '\n')    
                                                   
if __name__ == '__main__':
    tumor_exp()
                               
                         
      
              
                    
                    
                
                        
                        
                    

                                      










            
                            
                               
                                
                                 
                                    
                                                                    
                         
                            
                                           
                          
                      
                                     
                                
                                
                                    
                                     

                                   
                                    
               
    
                                                
                                                      

                                    
                                                     
                                                        
                                              


