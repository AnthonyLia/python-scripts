for x in num:
	if os.path.exists("/Users/0007/Desktop/Actual 3D Punks/Master/Blend_My_NFTs Output .75 Roughness/Generated NFT Batches/Batch1/Images male_camera/Actual 3D Punk _%d.jpg" % (num[counter])):
		print ("yes, found it, number %d is here. Going to delete it now" % (num[counter]))
		os.remove("/Users/0007/Desktop/Actual 3D Punks/Master/Blend_My_NFTs Output .75 Roughness/Generated NFT Batches/Batch1/Images male_camera/Actual 3D Punk _%d.jpg" % (num[counter]))
	else:
		print ("nope, not here, can't find %d because you deleted it even though it's still on the list - or you messed up the list" % (num[counter]))

	counter = counter + 1


#NEEDS        import os
#and possibly import re