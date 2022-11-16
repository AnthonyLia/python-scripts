
#Take random GLB and make 10,000 copies in *_n format: ______________________________________________________

#NEEDS import os
#and   import shutil

for i in random:
	shutil.copy2("/users/0007/Desktop/Actual 3D Punks/Master/Blend_My_NFTs Output 1stIPFStest/Blend_My_NFTs Output/Complete_Collection/Models/Actual 3D Punk _0.glb", "/users/0007/Desktop/Actual 3D Punks/Master/Blend_My_NFTs Output 1stIPFStest/Blend_My_NFTs Output/Complete_Collection/Models/Actual 3D Punk _%d.glb" % (i))

#______________________________________________________________________________________________________________



for i in range(0,10000):
	os.rename("/Users/0007/Desktop/Actual 3D Punks/Master/Blend_My_NFTs Output .825 Roughness - Smaller Scale/Generated NFT Batches/Batch1/BMNFT_metaData/Data_Actual 3D Punk _%d.json" % (i), "/Users/0007/Desktop/Actual 3D Punks/Master/Blend_My_NFTs Output .825 Roughness - Smaller Scale/Generated NFT Batches/Batch1/BMNFT_metaData/%d" % (i))