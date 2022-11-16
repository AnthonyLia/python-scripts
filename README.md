Hello all,

This is a collection of python scripts I have ran as of November 2022.
They all correlate to a project I created called Actual 3D Punks, based off of the authentic project CryptoPunks.
I'm fairly certain I'm still considered "beginner" or "junior" coder/programmer/software engineer. Therefore, I 
feel I have permission to publish "amateur" code, in that it uses very brute-force/specific programming and isn't
organized as best as it can be. I'll do a mini summary in chronological order:

1. Produce NFT Record Array.py
The Blender plugin I used to create the project, called BlendMyNFTs, makes a random NFT Record Array, but since
I was modeling Actual 3D Punks off of CryptoPunks, I needed the array to be non-random, and the plugin didn't have
that option. With a community obtained "cryptopunks attribute data.csv" of data of all of the traits of CryptoPunks,
I needed to transfer the names of the attributes to numbers, as BlendMyNFTs uses numbers to run and generate 3D 
NFTs. wholestring has all of the .csv file in a huge string, and sifts through the whole string reading for traits
and storing them in temporary variables to print the "DNA" for each NFT on each line. 
The last if statement is a redundancy in that it checks to make sure the script didn't check for more traits than
it had (in case the 10,000 row community data had an error in number of traits not corresponding to actual number
of traits).

2. Finish ERC721 Metadata
Before putting all of the finished NFTs on IPFS, I wanted to test 10,000 files uploaded mimicking 10,000 .glb 3D 
files and 10,000 JSON files renamed without the .json; these were all pinned to IPFS, while a smart contract on 
a testnet referenced them as NFTs. 

3. Convert BMNFT Data to ERC721
The plugin BlendMyNFTs didn't actually work perfectly for my application. After generating a collection of 3D files
from the NFT Record "DNA", it generated JSON files for each 3D file. However, these JSON files weren't notated 
exactly for the Ethereum ERC721 blockchain standard; it did that after finalizing the collection (in case I 
wanted to generate 10,000 image files to go along with the 3D files, and in this case I did that as well). However,
when it finalized the metadata, it scrambled the JSON files again, but not mislabeling JSON traits to wrong 3D files,
it simply changed ID numbers for JSON/3D/image file pairs/triplets. This was not going to work for my project as the 
ID numbers needed to be specific for specific NFTs, to correspond to the original NFT collection. 
The script goes file by file and sifts through the text in the file. It changed the JSON notation to be correct ERC721
notation, and add in the description of the project that I wanted to be in every NFT. I put lots of redundancy console
error messages, if occurred, because I needed the JSON files to be perfect as they are literally the NFT. All NFTs 
are published to the ethereum blockchain and live.

4. Delete JPGs In Batch
I ran into another problem with using BlendMyNFTs. The images I wanted to use as previews to the 3D NFTs were from 
different angles for different genders of the NFTs. BlendMyNFTs could only use 1 camera angle per batch of images,
as it was mainly developed for 3D generation. I therefore had to generate the whole collection of images twice, each
time with different camera angles. Then, I needed to delete the male-camera-angle pictures of the female NFTs, and 
the female-camera-angle pictures of the male NFTs, then put them together in the final image folder. This was amazing
to me at the time as I had began mass-selecting the to-be-deleted files to try to do it manually, but it took so long,
and then I saw the script delete the exact files I needed to delete a few hundred pictures per second.

5. Web Scraper
Again, the Actual 3D Punks project is based off of the CryptoPunks project, and to launch it I planned to giveaway
every Actual 3D Punk to the owner of the corresponding CryptoPunk. The blockchain is public. So while I may not know
the personal identity of who owns a given CryptoPunk, I can always find what wallet address does on the blockchain. 
The creator of CryptoPunks, Larva Labs, has the information on their website, as well as Etherscan, and Ethereum block
explorer. There was no API that had the ID numbers that each wallet address held. Only the number of IDs/NFTs each 
wallet address held. I tried to run the web scraper with beautifulsoup4, but it had a plethora of content for that 
module that wasn't relevant to what I was doing, and therefore made it harder for me to use. I decided to brute-force
it and import the text of every web page of wallet address that own CryptoPunks. Then used very embedded finds and 
indexes to locate the ID numbers in the HTML, and loop through a number of times that's equal to how many that wallet
has. I was amazed how fast the interface "get"s the HTML response from the website, but after about 20 seconds and 
a few lines created in my output, it stopped. I was confused and thought Python was lagging, but I quickly realized
their server blocked me. I had requested web pages too quickly and they wrote an algorithm to block IP addresses that
do that. I decided to let it run while I slept, and put a pause of 7 seconds after every wallet address scrape, and 
it worked.

6. Make 1 ID Listings
After having the data of how many IDs per wallet address and what ID numbers for each wallet address, I needed to 
list the Actual 3D Punks for free on OpenSea to those wallet addresses. OpenSea apparently doesn't give out API 
keys to interface with their marketplace easily anymore. Therefore, I had to manually list all 10,000 NFTs. I did
the math and realized I had to program it, and even that would take a while if each listing takes 20-40 seconds to
do. Alas, it was done that way. This script has a lot of specific locations, and they corresponded to different 
buttons on the website to click to make a free private listing to a specific wallet. After testing it for a few 
hours while being monitored, I realized the internet isn't fast enough for the commands sometimes when it lags 
momentarily. Therefore, I had to put very healthy time margins to make sure it doesn't miss clicking confirm on
the blockchain "transaction" to list the NFT. This script ran for a total of around 52 hours.

7. Make Multiple ID Bundle Listings
Some CryptoPunk owners only have 1 punk and some have multiple. OpenSea lets sellers bundle NFTs, so I figured it's 
most efficient to bundle the items for wallet addresses that own multiple CryptoPunks. This script does the same
as the previous, but makes one bundle when the wallet address owns less than 30 CryptoPunks (OpenSea only lets the
bundle be a maximum of 30 NFTs for sale) and calls it "0x<address> Bundle". For wallet addresses that own more than 
30 punks, it lists Actual 3D Punks for free (0.000001 ETH is less than $0.01) in multiple bundles and calls them 
"0x<address> Bundle 1" and "0x<address> Bundle 2" and so on.


Again, this a collection of Python scripts I wrote this year, so I can look back on later and appreciate how much 
I've progressed in my coding abilities. Thanks for reading!