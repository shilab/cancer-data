#Convert TCGA UUIDs to TCGA Barcodes    
  
#Read in a list of UUIDS to convert    
UUIDS = read.table("filename_list.txt", header = FALSE, sep = '\t')

#Install TCGAutils
if (!requireNamespace('BiocManager'))
install.packages('BiocManager')
BiocManager::install()
source("https://bioconductor.org/biocLite.R")
biocLite("TCGAutils")
library(TCGAutils)

#Create a table that contains column for UUID and column for corresponding barcode.    
Barcodes = UUIDtoBarcode(UUIDS, id_type = "file_id", end_point = "sample")

#Write table to file.    
write.table(Barcodes, file = "barcodes.txt", sep="\t", row.names = FALSE)
