from averaging import average_2, average_3

def test_avg_2():
	assert average_2(1,2) == 1.5
	assert average_2(-1, 1) == 0

def test_avg_3():
	assert average_3(0,1,2) == 1
	assert average_3(-1, 0, 1) == 0
	assert average_3(10,20,30) == 20
