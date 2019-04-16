import base64


def base64decoder():
	decoded = base64.b64decode(encoded_string)
	print (decoded.decode("UTF-8"))

def base64encoder():
	string = base64.b64encode(encoded_string)
	print (string.decode("UTF-8"))

def base16decoder():
	decoded = base64.b16decode(encoded_string)
	print (decoded.decode("UTF-8"))

def base16encoder():
	string = base64.b16encode(encoded_string)
	print (string.decode("UTF-8"))

def base32decoder():
	decoded = base64.b32decode(encoded_string)
	print (decoded.decode("UTF-8"))
	
def base32encoder():
	encoded = base64.b32encode(encoded_string)
	print (encoded.decode("UTF-8"))
	
def base85decoder():
	decoded = base64.a85decode(encoded_string)
	print (decoded.decode("UTF-8"))
	
def base85encoder():
	encoded = base64.a85encode(encoded_string)
	print (encoded.decode("UTF-8"))


x = int(input("Press\n1) Base16\n2) Base32\n3) Base64\n4) Base85\n\n0)For fast Base64 decode option\n"))
if x == 0:
	encoded_string = input ("Paste the encoded and press Enter\n").encode('ascii')
	base64decoder()
else:
	y = int(input("Press\n1) Decode\n2) Encode\n"))

encoded_string = input ("Paste the encoded and press Enter\n").encode('ascii')



if x == 1 and y == 1:
	base16decoder()
elif x == 1 and y == 2:
	base16encoder()
elif x == 2 and y == 1:
	base32decoder()
elif x == 2 and y == 2:
	base32encoder()
elif x == 3 and y == 1:
	base64decoder()
elif x == 3 and y == 2:
	base64encoder()
elif x == 4 and y == 1:
	base85decoder()
elif x == 4 and y == 2:
	base85encoder()
else:
	print("Error")



