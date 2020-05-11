import re
def transform(value):
	print(value)
	match_char=value.group()
	if match_char=='a':
		return 'm'
	return 'h'

print(re.sub('\w',transform,'a23a13aasdfjklajkajklaa',count=0))

