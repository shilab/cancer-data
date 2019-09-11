## Pipeline

**Introduction**

This is for analysis of of gene expression quantification data (FPKM) from https://portal.gdc.cancer.gov. 

**Data Retrieval**                
Data manifests can be downloaded from the GDC Portal repository and the gdc-client can be downloaded at https://gdc.cancer.gov/access-data/gdc-data-transfer-tool.                

To retrieve data from command line:               
*./gdc-client download -m [manifest_name.txt]*               

**Pre-processing**                
1.) Gunzip files in all directories:                       
    *gunzip ./\**/\*.gz*
              
2.) Rename files to match their dir names:                            
    *rename_FPKM.py*                
 
3.) Make FPKM directory and copy all FPKM files into FPKM                                 

4.) Make a list of all of the filenames (UUIDs):                
    *file_list.py*                                
    
4.) Create a list with matching TCGA barcodes:                                
    *make_barcodesFile.Rmd*                              
    
5.) Use updated list to rename files by barcode:                               
    *Barcode_Rename_FPKMFiles.py*                                
    
**Comparing tumor with normal tissue**                  
1.) Parse out data for individuals which have matching (tumor and normal tissue) samples:                              
    *MultGeneExpParser.py*                                
    
2.) Boxplots and *t-tests*:               
    *MatchGeneExp.Rmd*                
    
**Correlate FPKM values in tumor tissue using multiple genes:**               
1.) Parse out tumor-only data:                
    *AllGeneParser.py*                

2.) Using geneSymbols.txt (created using [DAVID](https://david.ncifcrf.gov/conversion2.jsp)), create a new file with data only for genes of interest:               
    *NewTumParseSymb.py*                
    
3.) Create plots and calculate *Pearson's R*:               
    *GeneExpAllCancer.Rmd*                            

**Contact:**           
kat j           
kkingwoo@uncc.edu           
