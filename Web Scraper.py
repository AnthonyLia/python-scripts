page = requests.get(url)


startOfAlt = page.text.find('alt="Punk ', page.text.find("%d Punks Owned" % 2))

print(page.text[startOfAlt+10 : startOfAlt+14]

print(page.text[page.text.find('alt="Punk ', page.text.find("%d Punks Owned" % 2))+10 : page.text.find('alt="Punk ', page.text.find("%d Punks Owned" % 2))+14]





for x in addressarray:
	page = requests.get('https://cryptopunks.app/cryptopunks/accountinfo?account=' + addressarray[addresscounter])
	
	thisaccountownedstring = ''
	for z in [0, 1, 2]:
		totalownedfirstchar = page.text[page.text.find('<b>',page.text.find('Total Punks Owned',0))+3+z]
		thisaccountownedstring = thisaccountownedstring + totalownedfirstchar
		if (page.text[page.text.find('<b>',page.text.find('Total Punks Owned',0))+4+z] == '<'):
			thisaccountownednumber = int(thisaccountownedstring)
			if (thisaccountownednumber == numberarray[addresscounter]):
				print("good. %d" % (thisaccountownednumber))
				break
			else:
				print("ERRRRORRRRRR, the %dth row has %d owned on the website, but numberarray says it has %d, check which is correct" % (addresscounter,thisaccountownednumber,numberarray[addresscounter]))
				break

	tempstartindex = 0

	for y in range(1,numberarray[addresscounter]+1):
		newidstring = page.text[page.text.find('alt="Punk ',tempstartindex)+10 : page.text.find('alt="Punk ',tempstartindex)+14]
		idarray[addresscounter] = idarray[addresscounter] + newidstring + ','
		tempstartindex = page.text.find('alt="Punk ',tempstartindex)+14 + 1
		if (numberarray[addresscounter]+1 == y):
			idarray[addresscounter] = idarray[addresscounter] + ','

	addresscounter = addresscounter + 1
	time.sleep(7)


