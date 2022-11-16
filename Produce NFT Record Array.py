Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> testvariable = open('C:/Users/0007/Desktop/Actual 3D Punks/cryptopunks attribute data.csv', 'r')



for i in range (0,10000):
    linestring = wholestring.split('\n')[i]

    for j in range (1,12):
        tempstring = linestring.split(',')[j]
        if j == 1:
            if (tempstring == " Human"):
                tempSpecies = "Human"
            if (tempstring == " Alien"):
                tempType = 1
                tempGender = " Male"
            if (tempstring == " Ape"):
                tempType = 2
                tempGender = " Male"
            if (tempstring == " Zombie"):
                tempType = 11
                tempGender = " Male"
        if j == 2:
            if (tempstring == " Female"):
                tempGender = " Female"
            if (tempstring == " Male"):
                tempGender = " Male"
        if j == 3:
            if (tempstring == " Albino" and tempGender == " Female"):
                tempType = 3
            if (tempstring == " Albino" and tempGender == " Male"):
                tempType = 7
            if (tempstring == " Dark" and tempGender == " Female"):
                tempType = 4
            if (tempstring == " Dark" and tempGender == " Male"):
                tempType = 8
            if (tempstring == " Light" and tempGender == " Female"):
                tempType = 5
            if (tempstring == " Light" and tempGender == " Male"):
                tempType = 9
            if (tempstring == " Medium" and tempGender == " Female"):
                tempType = 6
            if (tempstring == " Medium" and tempGender == " Male"):
                tempType = 10
        if j == 4:
            tempHair = 1
            tempEyes = 1
            tempFacialHair = 1
            tempMouthProp = 1
            tempMouth = 1
            tempBlemishes = 1
            tempEars = 1
            tempNose = 1
            tempNeckAccessory = 1

            charnumberoftraits = tempstring.split(' ')[1]
            intnumberoftraits = ord(charnumberoftraits) - 48
            
            
        if j == 5 or j == 6 or j == 7 or j == 8 or j == 9 or j == 10 or j == 11:
            if (tempstring == " Beanie" or tempstring == " Beanie "):
                tempHair = 4
            if (tempstring == " Blonde Bob" or tempstring == " Blonde Bob "):
                tempHair = 5
            if (tempstring == " Blonde Short" or tempstring == " Blonde Short "):
                tempHair = 6
            if (tempstring == " Cap Forward" or tempstring == " Cap Forward "):
                tempHair = 9
            if (tempstring == " Cowboy Hat" or tempstring == " Cowboy Hat "):
                tempHair = 12
            if (tempstring == " Dark Hair" or tempstring == " Dark Hair "):
                tempHair = 15
            if (tempstring == " Do-rag" or tempstring == " Do-rag "):
                tempHair = 16
            if (tempstring == " Fedora" or tempstring == " Fedora "):
                tempHair = 17
            if (tempstring == " Half Shaved" or tempstring == " Half Shaved "):
                tempHair = 20
            if (tempstring == " Hoodie" or tempstring == " Hoodie "):
                tempHair = 23
            if (tempstring == " Orange Side" or tempstring == " Orange Side "):
                tempHair = 34
            if (tempstring == " Peak Spike" or tempstring == " Peak Spike "):
                tempHair = 35
            if (tempstring == " Pigtails" or tempstring == " Pigtails "):
                tempHair = 36
            if (tempstring == " Pilot Helmet" or tempstring == " Pilot Helmet "):
                tempHair = 37
            if (tempstring == " Pink With Hat" or tempstring == " Pink With Hat "):
                tempHair = 38
            if (tempstring == " Police Cap" or tempstring == " Police Cap "):
                tempHair = 39
            if (tempstring == " Purple Hair" or tempstring == " Purple Hair "):
                tempHair = 40
            if (tempstring == " Red Mohawk" or tempstring == " Red Mohawk "):
                tempHair = 41
            if (tempstring == " Shaved Head" or tempstring == " Shaved Head "):
                tempHair = 42
            if (tempstring == " Straight Hair" or tempstring == " Straight Hair "):
                tempHair = 43
            if (tempstring == " Straight Hair Blonde" or tempstring == " Straight Hair Blonde "):
                tempHair = 44
            if (tempstring == " Straight Hair Dark" or tempstring == " Straight Hair Dark "):
                tempHair = 45
            if (tempstring == " Tassle Hat" or tempstring == " Tassle Hat "):
                tempHair = 48
            if (tempstring == " Tiara" or tempstring == " Tiara "):
                tempHair = 49
            if (tempstring == " Top Hat" or tempstring == " Top Hat "):
                tempHair = 50
            if (tempstring == " Vampire Hair" or tempstring == " Vampire Hair "):
                tempHair = 51
            if (tempstring == " Wild Blonde" or tempstring == " Wild Blonde "):
                tempHair = 52
            if (tempstring == " Wild White Hair" or tempstring == " Wild White Hair "):
                tempHair = 55
            if (tempstring == " Bandana" or tempstring == " Bandana "):
                if (tempGender == " Female"):
                    tempHair = 2
                if (tempGender == " Male"):
                    tempHair = 3
            if (tempstring == " Cap" or tempstring == " Cap "):
                if (tempGender == " Female"):
                    tempHair = 7
                if (tempGender == " Male"):
                    tempHair = 8
            if (tempstring == " Clown Hair Green" or tempstring == " Clown Hair Green "):
                if (tempGender == " Female"):
                    tempHair = 10
                if (tempGender == " Male"):
                    tempHair = 11
            if (tempstring == " Crazy Hair" or tempstring == " Crazy Hair "):
                if (tempGender == " Female"):
                    tempHair = 13
                if (tempGender == " Male"):
                    tempHair = 14
            if (tempstring == " Frumpy Hair" or tempstring == " Frumpy Hair "):
                if (tempGender == " Female"):
                    tempHair = 18
                if (tempGender == " Male"):
                    tempHair = 19
            if (tempstring == " Headband" or tempstring == " Headband "):
                if (tempGender == " Female"):
                    tempHair = 21
                if (tempGender == " Male"):
                    tempHair = 22
            if (tempstring == " Knitted Cap" or tempstring == " Knitted Cap "):
                if (tempGender == " Female"):
                    tempHair = 24
                if (tempGender == " Male"):
                    tempHair = 25
            if (tempstring == " Messy Hair" or tempstring == " Messy Hair "):
                if (tempGender == " Female"):
                    tempHair = 26
                if (tempGender == " Male"):
                    tempHair = 27
            if (tempstring == " Mohawk" or tempstring == " Mohawk "):
                if (tempGender == " Female"):
                    tempHair = 28
                if (tempGender == " Male"):
                    tempHair = 29
            if (tempstring == " Mohawk Dark" or tempstring == " Mohawk Dark "):
                if (tempGender == " Female"):
                    tempHair = 30
                if (tempGender == " Male"):
                    tempHair = 31
            if (tempstring == " Mohawk Thin" or tempstring == " Mohawk Thin "):
                if (tempGender == " Female"):
                    tempHair = 32
                if (tempGender == " Male"):
                    tempHair = 33
            if (tempstring == " Stringy Hair" or tempstring == " Stringy Hair "):
                if (tempGender == " Female"):
                    tempHair = 46
                if (tempGender == " Male"):
                    tempHair = 47
            if (tempstring == " Wild Hair" or tempstring == " Wild Hair "):
                if (tempGender == " Female"):
                    tempHair = 53
                if (tempGender == " Male"):
                    tempHair = 54
            if (tempstring == " Blue Eye Shadow" or tempstring == " Blue Eye Shadow "):
                tempEyes = 6
            if (tempstring == " Green Eye Shadow" or tempstring == " Green Eye Shadow "):
                tempEyes = 17
            if (tempstring == " Purple Eye Shadow" or tempstring == " Purple Eye Shadow "):
                tempEyes = 22
            if (tempstring == " Small Shades" or tempstring == " Small Shades "):
                tempEyes = 25
            if (tempstring == " Welding Goggles" or tempstring == " Welding Goggles "):
                tempEyes = 28
            if (tempstring == " 3D Glasses" or tempstring == " 3D Glasses "):
                if (tempGender == " Female"):
                    tempEyes = 2
                if (tempGender == " Male"):
                    tempEyes = 3
            if (tempstring == " Big Shades" or tempstring == " Big Shades "):
                if (tempGender == " Female"):
                    tempEyes = 4
                if (tempGender == " Male"):
                    tempEyes = 5
            if (tempstring == " Classic Shades" or tempstring == " Classic Shades "):
                if (tempGender == " Female"):
                    tempEyes = 7
                if (tempGender == " Male"):
                    tempEyes = 8
            if (tempstring == " Clown Eyes Blue" or tempstring == " Clown Eyes Blue "):
                if (tempGender == " Female"):
                    tempEyes = 9
                if (tempGender == " Male"):
                    tempEyes = 10
            if (tempstring == " Clown Eyes Green" or tempstring == " Clown Eyes Green "):
                if (tempGender == " Female"):
                    tempEyes = 11
                if (tempGender == " Male"):
                    tempEyes = 12
            if (tempstring == " Eye Mask" or tempstring == " Eye Mask "):
                if (tempGender == " Female"):
                    tempEyes = 13
                if (tempGender == " Male"):
                    tempEyes = 14
            if (tempstring == " Eye Patch" or tempstring == " Eye Patch "):
                if (tempGender == " Female"):
                    tempEyes = 15
                if (tempGender == " Male"):
                    tempEyes = 16
            if (tempstring == " Horned Rim Glasses" or tempstring == " Horned Rim Glasses "):
                if (tempGender == " Female"):
                    tempEyes = 18
                if (tempGender == " Male"):
                    tempEyes = 19
            if (tempstring == " Nerd Glasses" or tempstring == " Nerd Glasses "):
                if (tempGender == " Female"):
                    tempEyes = 20
                if (tempGender == " Male"):
                    tempEyes = 21
            if (tempstring == " Regular Shades" or tempstring == " Regular Shades "):
                if (tempGender == " Female"):
                    tempEyes = 23
                if (tempGender == " Male"):
                    tempEyes = 24
            if (tempstring == " VR" or tempstring == " VR "):
                if (tempGender == " Female"):
                    tempEyes = 26
                if (tempGender == " Male"):
                    tempEyes = 27
            if (tempstring == " Big Beard" or tempstring == " Big Beard "):
                tempFacialHair = 2
            if (tempstring == " Chinstrap" or tempstring == " Chinstrap "):
                tempFacialHair = 3
            if (tempstring == " Front Beard" or tempstring == " Front Beard "):
                tempFacialHair = 4
            if (tempstring == " Front Beard Dark" or tempstring == " Front Beard Dark "):
                tempFacialHair = 5
            if (tempstring == " Goat" or tempstring == " Goat "):
                tempFacialHair = 6
            if (tempstring == " Handlebars" or tempstring == " Handlebars "):
                tempFacialHair = 7
            if (tempstring == " Luxurious Beard" or tempstring == " Luxurious Beard "):
                tempFacialHair = 8
            if (tempstring == " Mustache" or tempstring == " Mustache "):
                tempFacialHair = 9
            if (tempstring == " Muttonchops" or tempstring == " Muttonchops "):
                tempFacialHair = 10
            if (tempstring == " Normal Beard" or tempstring == " Normal Beard "):
                tempFacialHair = 11
            if (tempstring == " Normal Beard Black" or tempstring == " Normal Beard Black "):
                tempFacialHair = 12
            if (tempstring == " Shadow Beard" or tempstring == " Shadow Beard "):
                tempFacialHair = 13
            if (tempstring == " Choker" or tempstring == " Choker "):
                tempNeckAccessory = 2
            if (tempstring == " Gold Chain" or tempstring == " Gold Chain "):
                if (tempGender == " Female"):
                    tempNeckAccessory = 3
                if (tempGender == " Male"):
                    tempNeckAccessory = 4
            if (tempstring == " Silver Chain" or tempstring == " Silver Chain "):
                if (tempGender == " Female"):
                    tempNeckAccessory = 5
                if (tempGender == " Male"):
                    tempNeckAccessory = 6
            if (tempstring == " Cigarette" or tempstring == " Cigarette "):
                if (tempGender == " Female"):
                    tempMouthProp = 2
                if (tempGender == " Male"):
                    tempMouthProp = 3
            if (tempstring == " Medical Mask" or tempstring == " Medical Mask "):
                if (tempGender == " Female"):
                    tempMouthProp = 4
                if (tempGender == " Male"):
                    tempMouthProp = 5
            if (tempstring == " Pipe" or tempstring == " Pipe "):
                if (tempGender == " Female"):
                    tempMouthProp = 6
                if (tempGender == " Male"):
                    tempMouthProp = 7
            if (tempstring == " Vape" or tempstring == " Vape "):
                if (tempGender == " Female"):
                    tempMouthProp = 8
                if (tempGender == " Male"):
                    tempMouthProp = 9
            if (tempstring == " Black Lipstick" or tempstring == " Black Lipstick "):
                tempMouth = 2
            if (tempstring == " Buck Teeth" or tempstring == " Buck Teeth "):
                tempMouth = 3
            if (tempstring == " Frown" or tempstring == " Frown "):
                tempMouth = 4
            if (tempstring == " Hot Lipstick" or tempstring == " Hot Lipstick "):
                tempMouth = 5
            if (tempstring == " Purple Lipstick" or tempstring == " Purple Lipstick "):
                tempMouth = 6
            if (tempstring == " Smile" or tempstring == " Smile "):
                tempMouth = 7
            if (tempstring == " Mole" or tempstring == " Mole "):
                if (tempGender == " Female"):
                    tempBlemishes = 2
                if (tempGender == " Male"):
                    tempBlemishes = 3
            if (tempstring == " Rosy Cheeks" or tempstring == " Rosy Cheeks "):
                if (tempGender == " Female"):
                    tempBlemishes = 4
                if (tempGender == " Male"):
                    tempBlemishes = 5
            if (tempstring == " Spots" or tempstring == " Spots "):
                if (tempGender == " Female"):
                    tempBlemishes = 6
                if (tempGender == " Male"):
                    tempBlemishes = 7
            if (tempstring == " Earring" or tempstring == " Earring "):
                if (tempGender == " Female"):
                    tempEars = 2
                if (tempGender == " Male"):
                    tempEars = 3
            if (tempstring == " Clown Nose" or tempstring == " Clown Nose "):
                if (tempGender == " Female"):
                    tempNose = 2
                if (tempGender == " Male"):
                    tempNose = 3
            if (j == 11):
                print ("\"",tempBlemishes,"-",tempEars,"-",tempEyes,"-",tempFacialHair,"-",tempHair,"-",tempMouth,"-",tempMouthProp,"-",tempNeckAccessory,"-",tempNose,"-",tempType,"\",")

            if (4+intnumberoftraits >= j and tempstring != " Beanie" and tempstring != " Beanie " and tempstring != " Blonde Bob" and tempstring != " Blonde Bob " and tempstring != " Blonde Short" and tempstring != " Blonde Short " and tempstring != " Cap Forward" and tempstring != " Cap Forward " and tempstring != " Cowboy Hat" and tempstring != " Cowboy Hat " and tempstring != " Dark Hair" and tempstring != " Dark Hair " and tempstring != " Do-rag" and tempstring != " Do-rag " and tempstring != " Fedora" and tempstring != " Fedora " and tempstring != " Half Shaved" and tempstring != " Half Shaved " and tempstring != " Hoodie" and tempstring != " Hoodie " and tempstring != " Orange Side" and tempstring != " Orange Side " and tempstring != " Peak Spike" and tempstring != " Peak Spike " and tempstring != " Pigtails" and tempstring != " Pigtails " and tempstring != " Pilot Helmet" and tempstring != " Pilot Helmet " and tempstring != " Pink With Hat" and tempstring != " Pink With Hat " and tempstring != " Police Cap" and tempstring != " Police Cap " and tempstring != " Purple Hair" and tempstring != " Purple Hair " and tempstring != " Red Mohawk" and tempstring != " Red Mohawk " and tempstring != " Shaved Head" and tempstring != " Shaved Head " and tempstring != " Straight Hair" and tempstring != " Straight Hair " and tempstring != " Straight Hair Blonde" and tempstring != " Straight Hair Blonde " and tempstring != " Straight Hair Dark" and tempstring != " Straight Hair Dark " and tempstring != " Tassle Hat" and tempstring != " Tassle Hat " and tempstring != " Tiara" and tempstring != " Tiara " and tempstring != " Top Hat" and tempstring != " Top Hat " and tempstring != " Vampire Hair" and tempstring != " Vampire Hair " and tempstring != " Wild Blonde" and tempstring != " Wild Blonde " and tempstring != " Wild White Hair" and tempstring != " Wild White Hair " and tempstring != " Bandana" and tempstring != " Bandana " and tempstring != " Cap" and tempstring != " Cap " and tempstring != " Clown Hair Green" and tempstring != " Clown Hair Green " and tempstring != " Crazy Hair" and tempstring != " Crazy Hair " and tempstring != " Frumpy Hair" and tempstring != " Frumpy Hair " and tempstring != " Headband" and tempstring != " Headband " and tempstring != " Knitted Cap" and tempstring != " Knitted Cap " and tempstring != " Messy Hair" and tempstring != " Messy Hair " and tempstring != " Mohawk" and tempstring != " Mohawk " and tempstring != " Mohawk Dark" and tempstring != " Mohawk Dark " and tempstring != " Mohawk Thin" and tempstring != " Mohawk Thin " and tempstring != " Stringy Hair" and tempstring != " Stringy Hair " and tempstring != " Wild Hair" and tempstring != " Wild Hair " and tempstring != " Blue Eye Shadow" and tempstring != " Blue Eye Shadow " and tempstring != " Green Eye Shadow" and tempstring != " Green Eye Shadow " and tempstring != " Purple Eye Shadow" and tempstring != " Purple Eye Shadow " and tempstring != " Small Shades" and tempstring != " Small Shades " and tempstring != " Welding Goggles" and tempstring != " Welding Goggles " and tempstring != " 3D Glasses" and tempstring != " 3D Glasses " and tempstring != " Big Shades" and tempstring != " Big Shades " and tempstring != " Classic Shades" and tempstring != " Classic Shades " and tempstring != " Clown Eyes Blue" and tempstring != " Clown Eyes Blue " and tempstring != " Clown Eyes Green" and tempstring != " Clown Eyes Green " and tempstring != " Eye Mask" and tempstring != " Eye Mask " and tempstring != " Eye Patch" and tempstring != " Eye Patch " and tempstring != " Horned Rim Glasses" and tempstring != " Horned Rim Glasses " and tempstring != " Nerd Glasses" and tempstring != " Nerd Glasses " and tempstring != " Regular Shades" and tempstring != " Regular Shades " and tempstring != " VR" and tempstring != " VR " and tempstring != " Big Beard" and tempstring != " Big Beard " and tempstring != " Chinstrap" and tempstring != " Chinstrap " and tempstring != " Front Beard" and tempstring != " Front Beard " and tempstring != " Front Beard Dark" and tempstring != " Front Beard Dark " and tempstring != " Goat" and tempstring != " Goat " and tempstring != " Handlebars" and tempstring != " Handlebars " and tempstring != " Luxurious Beard" and tempstring != " Luxurious Beard " and tempstring != " Mustache" and tempstring != " Mustache " and tempstring != " Muttonchops" and tempstring != " Muttonchops " and tempstring != " Normal Beard" and tempstring != " Normal Beard " and tempstring != " Normal Beard Black" and tempstring != " Normal Beard Black " and tempstring != " Shadow Beard" and tempstring != " Shadow Beard " and tempstring != " Choker" and tempstring != " Choker " and tempstring != " Gold Chain" and tempstring != " Gold Chain " and tempstring != " Silver Chain" and tempstring != " Silver Chain " and tempstring != " Cigarette" and tempstring != " Cigarette " and tempstring != " Medical Mask" and tempstring != " Medical Mask " and tempstring != " Pipe" and tempstring != " Pipe " and tempstring != " Vape" and tempstring != " Vape " and tempstring != " Black Lipstick" and tempstring != " Black Lipstick " and tempstring != " Buck Teeth" and tempstring != " Buck Teeth " and tempstring != " Frown" and tempstring != " Frown " and tempstring != " Hot Lipstick" and tempstring != " Hot Lipstick " and tempstring != " Purple Lipstick" and tempstring != " Purple Lipstick " and tempstring != " Smile" and tempstring != " Smile " and tempstring != " Mole" and tempstring != " Mole " and tempstring != " Rosy Cheeks" and tempstring != " Rosy Cheeks " and tempstring != " Spots" and tempstring != " Spots " and tempstring != " Earring" and tempstring != " Earring " and tempstring != " Clown Nose" and tempstring != " Clown Nose "):
                 print ("THERE WAS AN ERROR. HEY NOTICE THIS TEXT AND FIND ERROR. TEMPSTRING IS",tempstring)
