# Coinmarketcap.com logos

Coinmarketcap.com has recently changed the filenames of the cryptocurrency logos.

For example:
Instead of ethereum.png, it's now 1027.png.

So, I created this python script. The script parses https://coinmarketcap.com/coins/views/all/ and maps the coin ids to the new logo ids. Then it downloads all logos and saves them with their old coin id.

You can set the image size of the files it will download by changing the IMG_SIZE variable.
