####**Introduction**

The purpose of this pipeline is to analyze [TCGA](https://portal.gdc.cancer.gov/) publicly available data containing FPKM values from HTSeq and to furthermore identify genomic alterations available at [cBioPortal](https://www.cbioportal.org/).

####**Requirements**

The following code, files, software, and applications are implemented in the pipeline.             

-  **_Applications/Software_**                       
  gdc-client          
  R 3.5.3         
  RStudio 1.1.463         
  python3
  
-  **_Code/Scripts/Modules_**            
  rename_FPKM.py            
  file_list.py            
  make_barcodeFile.Rmd        
  Barcode_Rename_FPKMFiles.py           
  MultGeneExpParser.py        
  NewTumParser.py         
  matchedGeneExp.Rmd      
  GeneExpressionAllCancer.Rmd         
  Count_cna.py        
  Count_mutes.py        
  AlterationEvents.Rmd        
  LolliplotMutes.Rmd        

-  **_Files_**            
  gdc_manifest.txt             
  barcodes.txt

####**Following the pipeline**            
This pipeline has been simplified into individual scripts for each step.  Please note, paths and filenames need to be changed.  

#####*_TCGA data_*

#####1.)           
To install and operate the gdc-client, retrieve the [data transfer tool](https://gdc.cancer.gov/access-data/gdc-data-transfer-tool). Manifests can be downloaded at the [GDC Portal](https://portal.gdc.cancer.gov/). To download data from manifest:        

```
$./gdc-client download -m gdc_manifest.txt
```

#####2.)           
Once FPKM data files are downloaded, from directory:                

````
$gunzip ./**/*.txt.gz        
```         

#####3.)            
Each file is de-identified. Rename each file to UUID (i.e. directory name):           
```
$python3 rename_FPKM.py
```         
Move all FPKM files to a new directory. If *barcodes.txt* matches current dataset, continue to step 4. Else:                     
 
- **Optional if barcode.txt outdated:**  
From new directory, create a list of filename prefixes:         
  
  ```
$python3 file_list.py
  ```         
  The output from this file should be used to execute *make_barcodesFile.Rmd*.          


#####4.)           
Rename each file in the directory to the corresponding TCGA barcode:         

```
$python3 Barcode_Rename_FPKMFiles.py
```           

#####5.)          
For creation of a file containing only samples which have normal and tumor tissue available:        

```
$python3 MultGeneExpParser.py
```         
For creation of a file containing tumor-only samples for a list of genes:         

```
$python3 NewTumParser.py
```         

#####6.)          
To create boxplots for matched samples:         

Knit *matchedGeneExp.Rmd*        

To create scatterplots for correlations between genes (tumor-only samples):        

Knit *GeneExpressionAllCancer.Rmd*         

#####*_cBioPortal data_*

Download data from [cBioPortal](cbioportal.org):    
- Select study(ies)         
- Query by gene         
- From *Download* tab, download copy-number alterations file and mutations file.        

#####1.)          

Counting occurences of genomic alteration events:         
 
```
$python3 count_cna.py 

$python3 count_mutes.py         
```     

Check for duplicates in files and reference listed data on cBioPortal web interface to ensure no data is missing from files.        
Output from these scripts can be read into excel, creating columns for additional information and creating frequencies.         

#####2.)        
To create figures based on step 1 of cBio data:         

Knit *AlterationEvents.Rmd*           
Knit *LolliplotMutes.Rmd*           


#####**Contact:**           
kat j           
kkingwoo@uncc.edu           

