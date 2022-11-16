for i in range(0,10000):
	if os.path.exists("/Users/0007/Desktop/Actual 3D Punks/Master/Blend_My_NFTs Output .825 Roughness - Smaller Scale/Generated NFT Batches/Batch1/BMNFT_metaData/Data_Actual 3D Punk _%d.json" % (i)):
		print ("yes, found it, number %d is here. Going to change" % (i))
		with open("/Users/0007/Desktop/Actual 3D Punks/Master/Blend_My_NFTs Output .825 Roughness - Smaller Scale/Generated NFT Batches/Batch1/BMNFT_metaData/Data_Actual 3D Punk _%d.json" % (i), 'r') as file:
			filedata = file.read()

			filedata = filedata.replace('Punk _%d' % (i), 'Punk #%d' % (i))
			if (filedata.find('NFT') == -1):
				print("THERE WAS AN ERROR. NFT WAS NOT FOUND ON #%d" % (i))
			if (filedata.find('Blemishes') == -1):
				print("THERE WAS AN ERROR. BLEMISHES WAS NOT FOUND ON #%d" % (i))
			filedata = filedata.replace(filedata[filedata.find('NFT'):filedata.find('Blemishes')-3], 'description": "Actual 3D Punks is the authentic 3D metaverse-ready collection of punks. This 10,000 NFT collection consists of punks in GLB format, the ')
			filedata = filedata.replace("GLB format, the ", "GLB format, the 'JPG of 3D files', for full integration in AR/VR and all things Web3")
			filedata = filedata.replace('Web3','Web3.",\n "image": "ipfs://QmZPdgAXHaWvrLzQt5yTU9X3AiBSwWe4EvkKmGRUytzqUE/Actual3DPunk_%d.jpg",\n "animation_url": "ipfs://QmPiTf9gXc7JgR6uA7GeYLCQzfUAawoBHbq7iRA6qCpKJg/Actual3DPunk_%d.glb",\n "attributes": [\n  {\n' % (i, i))
			for j in range(1,11):
				if (filedata.find('_') == -1):
					print("THERE WAS AN ERROR. _ WAS NOT FOUND ON #%d" % (i))
				if (filedata.find('NFT') == -1):
					print("THERE WAS AN ERROR. 0 WAS NOT FOUND ON #%d" % (i))
				filedata = filedata.replace(filedata[filedata.find('_',filedata.find('"attributes":')):filedata.find('"',filedata.find('_', filedata.find('"attributes":')))], '')
			filedata = filedata.replace('"Blemishes": "','"trait_type":\n  "Blemishes",\n   "value": "')
			if (filedata.find(',', filedata.find('value')) == -1):
				print("THERE WAS AN ERROR. , WAS NOT FOUND ON #%d AFTER VALUE" % (i))
			if (filedata.find('value') == -1):
				print("THERE WAS AN ERROR. VALUE WAS NOT FOUND ON #%d" % (i))
			tempindex = filedata.find(',' , filedata.find('value'))
			filedata = filedata[0:tempindex] + '\n  },\n  {\n   "trait_type":' + filedata[tempindex+1:]
			filedata = filedata.replace('"Ears": ', '"Ears",\n   "value": ')
			if (filedata.find(',' , filedata.find('value',filedata.find('"Ears"'))) == -1):
				print("THERE WAS AN ERROR. , AFTER VALUE AFTER EARS WAS NOT FOUND ON #%d" % (i))
			if (filedata.find('value',filedata.find('"Ears"')) == -1):
				print("THERE WAS AN ERROR. VALUE AFTER EARS WAS NOT FOUND ON #%d" % (i))
			if (filedata.find('"Ears"') == -1):
				print("THERE WAS AN ERROR. EARS WAS NOT FOUND ON #%d" % (i))
			tempindex = filedata.find(',' , filedata.find('value',filedata.find('"Ears"')))
			filedata = filedata[0:tempindex] + '\n  },\n  {\n   "trait_type":' + filedata[tempindex+1:]
			filedata = filedata.replace('"Eyes": ', '"Eyes",\n   "value": ')
			if (filedata.find(',' , filedata.find('value',filedata.find('"Eyes"'))) == -1):
				print("THERE WAS AN ERROR. , AFTER VALUE AFTER EYES WAS NOT FOUND ON #%d" % (i))
			if (filedata.find('value',filedata.find('"Eyes"')) == -1):
				print("THERE WAS AN ERROR. VALUE AFTER EYES WAS NOT FOUND ON #%d" % (i))
			if (filedata.find('"Eyes"') == -1):
				print("THERE WAS AN ERROR. EYES WAS NOT FOUND ON #%d" % (i))
			tempindex = filedata.find(',' , filedata.find('value',filedata.find('"Eyes"')))
			filedata = filedata[0:tempindex] + '\n  },\n  {\n   "trait_type":' + filedata[tempindex+1:]
			filedata = filedata.replace('"Facial Hair": ', '"Facial Hair",\n   "value": ')
			if (filedata.find(',' , filedata.find('value',filedata.find('"Facial Hair"'))) == -1):
				print("THERE WAS AN ERROR. , AFTER VALUE AFTER FACIAL HAIR WAS NOT FOUND ON #%d" % (i))
			if (filedata.find('value',filedata.find('"Facial Hair"')) == -1):
				print("THERE WAS AN ERROR. VALUE AFTER FACIAL HAIR WAS NOT FOUND ON #%d" % (i))
			if (filedata.find('"Facial Hair"') == -1):
				print("THERE WAS AN ERROR. FACIAL HAIR WAS NOT FOUND ON #%d" % (i))
			tempindex = filedata.find(',' , filedata.find('value',filedata.find('"Facial Hair"')))
			filedata = filedata[0:tempindex] + '\n  },\n  {\n   "trait_type":' + filedata[tempindex+1:]
			filedata = filedata.replace('"Hair": ', '"Hair",\n   "value": ')
			if (filedata.find(',' , filedata.find('value',filedata.find('"Hair"'))) == -1):
				print("THERE WAS AN ERROR. , AFTER VALUE AFTER HAIR WAS NOT FOUND ON #%d" % (i))
			if (filedata.find('value',filedata.find('"Hair"')) == -1):
				print("THERE WAS AN ERROR. VALUE AFTER HAIR WAS NOT FOUND ON #%d" % (i))
			if (filedata.find('"Hair"') == -1):
				print("THERE WAS AN ERROR. HAIR WAS NOT FOUND ON #%d" % (i))
			tempindex = filedata.find(',' , filedata.find('value',filedata.find('"Hair"')))
			filedata = filedata[0:tempindex] + '\n  },\n  {\n   "trait_type":' + filedata[tempindex+1:]
			filedata = filedata.replace('"Mouth": ', '"Mouth",\n   "value": ')
			if (filedata.find(',' , filedata.find('value',filedata.find('"Mouth"'))) == -1):
				print("THERE WAS AN ERROR. , AFTER VALUE AFTER MOUTH WAS NOT FOUND ON #%d" % (i))
			if (filedata.find('value',filedata.find('"Mouth"')) == -1):
				print("THERE WAS AN ERROR. VALUE AFTER MOUTH WAS NOT FOUND ON #%d" % (i))
			if (filedata.find('"Mouth"') == -1):
				print("THERE WAS AN ERROR. MOUTH WAS NOT FOUND ON #%d" % (i))
			tempindex = filedata.find(',' , filedata.find('value',filedata.find('"Mouth"')))
			filedata = filedata[0:tempindex] + '\n  },\n  {\n   "trait_type":' + filedata[tempindex+1:]
			filedata = filedata.replace('"Mouth Prop": ', '"Mouth Prop",\n   "value": ')
			if (filedata.find(',' , filedata.find('value',filedata.find('"Mouth Prop"'))) == -1):
				print("THERE WAS AN ERROR. , AFTER VALUE AFTER MOUTH PROP WAS NOT FOUND ON #%d" % (i))
			if (filedata.find('value',filedata.find('"Mouth Prop"')) == -1):
				print("THERE WAS AN ERROR. VALUE AFTER MOUTH PROP WAS NOT FOUND ON #%d" % (i))
			if (filedata.find('"Mouth Prop"') == -1):
				print("THERE WAS AN ERROR. MOUTH PROP WAS NOT FOUND ON #%d" % (i))
			tempindex = filedata.find(',' , filedata.find('value',filedata.find('"Mouth Prop"')))
			filedata = filedata[0:tempindex] + '\n  },\n  {\n   "trait_type":' + filedata[tempindex+1:]
			filedata = filedata.replace('"Neck Accessory": ', '"Neck Accessory",\n   "value": ')
			if (filedata.find(',' , filedata.find('value',filedata.find('"Neck Accessory"'))) == -1):
				print("THERE WAS AN ERROR. , AFTER VALUE AFTER NECK ACCESSORY WAS NOT FOUND ON #%d" % (i))
			if (filedata.find('value',filedata.find('"Neck Accessory"')) == -1):
				print("THERE WAS AN ERROR. VALUE AFTER NECK ACCESSORY WAS NOT FOUND ON #%d" % (i))
			if (filedata.find('"Neck Accessory"') == -1):
				print("THERE WAS AN ERROR. NECK ACCESSORY WAS NOT FOUND ON #%d" % (i))
			tempindex = filedata.find(',' , filedata.find('value',filedata.find('"Neck Accessory"')))
			filedata = filedata[0:tempindex] + '\n  },\n  {\n   "trait_type":' + filedata[tempindex+1:]
			filedata = filedata.replace('"Nose": ', '"Nose",\n   "value": ')
			if (filedata.find(',' , filedata.find('value',filedata.find('"Nose"'))) == -1):
				print("THERE WAS AN ERROR. , AFTER VALUE AFTER NOSE WAS NOT FOUND ON #%d" % (i))
			if (filedata.find('value',filedata.find('"Nose"')) == -1):
				print("THERE WAS AN ERROR. VALUE AFTER NOSE WAS NOT FOUND ON #%d" % (i))
			if (filedata.find('"Nose"') == -1):
				print("THERE WAS AN ERROR. NOSE WAS NOT FOUND ON #%d" % (i))
			tempindex = filedata.find(',' , filedata.find('value',filedata.find('"Nose"')))
			filedata = filedata[0:tempindex] + '\n  },\n  {\n   "trait_type":' + filedata[tempindex+1:]
			filedata = filedata.replace('"Type": ', '"Type",\n   "value": ')
			if (filedata.find(' }\n}') == -1):
				print("THERE WAS AN ERROR. THE ' }SLASH-N' CODE AT THE END WASN'T FOUND ON #%d" % (i))
			filedata = filedata.replace(' }\n}','  }\n ]\n}')

			filedata = filedata.replace(' No Neck','No Neck')
			with open("/Users/0007/Desktop/Actual 3D Punks/Master/Blend_My_NFTs Output .825 Roughness - Smaller Scale/Generated NFT Batches/Batch1/BMNFT_metaData/Data_Actual 3D Punk _%d.json" % (i), 'w') as file:
				file.write(filedata)
				print("good. %d" % (i))
	else:
		print ("no, not here, can't find %d SO THERE IS AN ERROR. I REPEAT THERE IS AN ERROR, FIND OUT WHAT HAPPENED" % (i))





