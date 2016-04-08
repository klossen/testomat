#Abgleich Skript mit vorhandenen Audiofiles und umgekehrt

import os
assetno=list()
filelist=list()
count=0
count1=0

#Abfrage Datenquellen
Titelnummer=raw_input('Titelnummer des zu pruefenden Buchs: ')
Assetnummern='j:/Desktop/'+Titelnummer+'_Assetnolist.txt'
Audioordner='j:/Desktop/BookID_'+Titelnummer

abweichungen=open('j:/desktop/Abweichungen_'+Titelnummer+'.txt', 'w')

#Liste Skript
handle=open(Assetnummern)
for line in handle:
	line=line.strip()+'.mp3'
	if len(line)>4:
		assetno.append(line)
print '+++++++++'
print len(assetno), 'Assetnummern laut Skript'

#Liste Audiofiles
for root, dirs, files in os.walk(Audioordner):
	for filename in files:
		if filename.endswith('.mp3'):
			filelist.append(filename)
print len(filelist), 'mp3-Dateien im Ordner'

#check Skript vs Audiofiles		
for element in assetno:
	if element in filelist:
		continue
	else:
		abweichungen.write(element)
		abweichungen.write(' steht im Skript, liegt aber nicht als Audiodatei vor.\n')
		count=count+1
if count>0:
	print count, 'Abweichungen Skript-Audios'

#check Audiofiles vs Skript
for file in filelist:
	if file in assetno:
		continue
	else:
		abweichungen.write(file)
		abweichungen.write(' liegt als Audio vor, steht aber nicht im Skript.\n')
		count1=count1+1
if count1>0:
	print count1, 'Abweichungen Audios-Skript'

#Eigenlob
if count+count1==0:
	print 'Alles bestens, keine Abweichungen.'	


