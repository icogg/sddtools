
import json
import base64

def printsdd(dict, seperator='\t', offset=0):
  """This is a module that parses the json file type used for the SDD tool and 
  outputs it to the screen with appropriate indenting.
  """
		for k, v in dict.items():
			if isinstance(v, type(dict)):
				print (seperator * offset, k)
				offset += 1
				printsdd(v, seperator, offset)
				offset -= 1
			elif isinstance(v, list):
				print (seperator * offset, k)
				offset += 1
				for i in v:
					printsdd(i, seperator, offset)
				offset -= 1
			elif k == 'Data':
				print(seperator * offset, k,': \n', base64.b64decode(v),'\n')
			else:
				print(seperator * offset, k,':', v)
		offset -= 1
