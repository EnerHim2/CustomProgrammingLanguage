import enerscript

while True:
	text = input('basic > ')
	result, error = enerscript.run('<stdin>', text)
	if error: print(error.as_string())
	elif result: print(result)