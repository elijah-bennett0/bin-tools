from subprocess import getoutput as go
from pwn import *
from colorama import init, Fore, Back, Style

# Color BS
y, r = Fore.YELLOW, Style.RESET_ALL
init()

# Just gonna prettify readelf output for this shitty script
o = go('readelf --relocs compilation_example.o')
lines = o.split('\n')
entries = []

# My trashy wine cleanup
for line in lines:
	if line.startswith("0"):
		entries.append(line)

# Probably the ugliest print statement ever
print('\n'+'=-'*7+'='+' SYMBOL DUMP '+'='+'-='*7+'\n')
for entry in entries:
	'''
	1: offset
	2: info
	3: type
	4: symbol value
	5: symbol name
	6: addend ([-3:])
	'''
	raw = entry.split(' ')
	parsed = [el for el in raw if el.strip()]
	offset,info,type,symval,symname,addend = \
		parsed[0], parsed[1], parsed[2], parsed[3], parsed[4], ' '.join(parsed[-2:])
	f = lambda x: "%s%s%s" % (y,x,r) # nice
	success("Symbol Name: {:<50}\n\tType: {:<50}\n\tOffset: {:<50}\n\tAddend: {:<5}\n\n" .format(f(symname), \
										f(type), f(offset), f(addend)))
