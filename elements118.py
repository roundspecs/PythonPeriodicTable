from vars import elems, sym, mass_no


def prompt(sentence, opt):
	print(sentence)
	size = len(opt)

	for i in range(size):
		print(f'{i+1}. {opt[i]}')

	num = int(input("Enter the corresponding number: "))

	# if user inputs a number out of list
	while num not in range(1, size + 1):
		print("Please enter a number between 1 and", size)
		num = int(input("Enter the corresponding number: "))

	return num


def e_con(atm):
	i = 0
	conf = ['1s0', '2s0', '2p0', '3s0', '3p0', '4s0', '3d0', '4p0', '5s0', '4d0', '5p0', '6s0', '4f0', '5d0', '6p0', '7s0', '5f0', '6d0', '7p0', '8s0']

	while atm > 0:
		if conf[i][1:] in ['s2', 'p6', 'd10', 'f14']:
			i += 1
		else:
			conf[i] = conf[i][:2] + str(int(conf[i][2:]) + 1)
			atm -= 1
	# print(' '.join(conf))
	for _ in range (2):
		for i, j in enumerate(conf):
			if j[1:] == 'd9':
				conf[i] = conf[i][:2] + '10'
				conf[i - 1] = conf[i - 1][:2] + str(int(conf[i - 1][2:]) - 1)
			elif j[1:] == 'd4':
				conf[i] = conf[i][:2] + '5'
				conf[i - 1] = conf[i - 1][:2] + str(int(conf[i - 1][2:]) - 1)
			elif j[1:] == 'f6':
				conf[i] = conf[i][:2] + '7'
				conf[i - 1] = conf[i - 1][:2] + str(int(conf[i - 1][2:]) - 1)
			elif j[1:] == 'f13':
				conf[i] = conf[i][:2] + '14'
				conf[i - 1] = conf[i - 1][:2] + str(int(conf[i - 1][2:]) - 1)


	while conf[-1][2] == '0':
		conf.pop()
	return conf


def grp_no(atm, conf):
	if sym[atm-1] == 'He':
		return 18
	elif 56 < atm < 72 or 88 < atm < 104:
		return 3
	elif conf[-1][1] == 's':
		return int(conf[-1][2])
	elif conf[-1][1] == 'p':
		return int(conf[-1][2]) + 12
	elif conf[-1][1] == 'd':
		if conf[-2][1] == 's':
			return int(conf[-2][2:]) + int(conf[-1][2:])
		else:
			return int(conf[-3][2:]) + int(conf[-1][2:])


def p_no(conf):
	last_shell = max(conf)
	return last_shell[0]


def by_atm_num(atm_num):
	econ = e_con(atm_num)
	print(f'''
		Element: {elems[atm_num-1]}
		Symbol: {sym[atm_num-1]}
		Atomic number: {atm_num}
		Electronic configuration: {' '.join(econ)}
		Group number: {grp_no(atm_num, econ)}
		Period number: {p_no(econ)}
''')

choices = {
	1: lambda: by_atm_num(int(input("Enter the atomic number: "))),
	2: lambda: by_atm_num(sym.index(input("Enter the symbol of the element: ").title()) + 1),
	3: lambda: by_atm_num(elems.index(input("Enter the name of the element: ").title()) + 1)
}

while True:
	choices.get(
		prompt("Find element by,", ["Atomic number", "Symbol", "Name of element"]),
		lambda: print("Out of option")
	)()
