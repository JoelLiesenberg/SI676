This readme file was generated on 2023-10-25 by Joel Liesenberg



GENERAL INFORMATION

Title of Dataset: Miscellaneous Webfile Samples

Date of data collection: Files were last modified before inventorying on 2023-10-23. Inventory of files and accompanying CSV data were 
collected on 2023-10-25. 

Source/Provenance of Dataset: Files come from a variety of external sources, and were placed together for use in the context of being 
used for this academic exercise. There does not appear to be a shared provenance among them or a connecting theme/topic. The inventoy CSV
and Python script documents were created by Joel Liesenberg on 2023-10-25.



DATA & FILE OVERVIEW

File Inventory List:
web-files-small-metadata.csv
vlwhcssc.asx
04-04-21full.asf
glmp_cig.EQ.wm.p20.t12z
oct17cc.asx
01-1480.pdf
file.pdf
Chapter03.pdf
PFCHEJ.pdf
HR2021 commtext.pdf
13080t.jpg
orca.via_.moc_.noaa_.jpg
k7989-7x.jpg
m237a2f.gif
1005107061.tif
11-3250JohnsonvFolinoEtAl.wma
NEWSLINE_802AF71F439D401585C6FCB02F358307.mp3
mj_telework_exchange_final_100710.mp3
000727.ram
BudgetandGrants012710.ppt
ADAEMPLOYMENTTaxIncentives.ppt
Non-FTE-Trainee-Activities-060109.ppt

Relationship between files: Files are separated into folders based on their format (e.g. presentation, PDF, audio, 
video, etc.). Only webfiles-small-metadata.csv exists at the top of this structure outside of these sub-folders.

Definition of CSV Metadata Columns:
index           - Marks the index position of the file within the inventory
path            - Outlines the relative filepath for each file within the larger repository
filename        - Name of the file
extension       - File extension assigned to each file
size            - Size of the file in bytes
modify_datetime - Time and date when the file was last modified
md5hash         - Md5 checksum generated for each file to ascertain file validity during inventorying process



METHODOLOGICAL INFORMATION

The inventory CSV data was collected via use of the included Python script. This script utilizes the os/os.path, haslib, csv, and datetime
modules. The metadata information was collected into a list of lists via nested loops, and then written to the CSV file included here. The
helper function used to generate md5 checksums for each of the files was created by Jesse Johnston, and adapted for usage in this
inventorying project.
