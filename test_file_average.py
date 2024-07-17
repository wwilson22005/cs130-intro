from averaging import average

def avg_2():
	assert average(1,2) == 1.5
	assert average(-1, 1) == 0

def avg_3():
	assert average(0,1,2) == 1
	assert average(-1, 0, 1) == 0
	assert average(10,20,30) == 20