y=int(input('Y='))
x=int(input('X='))
if x>0 and y>0:
	print('в первой четверти')
elif x<0 and y>0:
	print('во второй четверти')
elif x<0 and y<0:
	print('в третьей четверти')
else:
	print('в четвертой четверти')
