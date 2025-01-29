from main import *



def test_linear_search():
	""" done. """
	assert linear_search([1,2,3,4,5], 5) == 4
	assert linear_search([1,2,3,4,5], 1) == 0
	assert linear_search([1,2,3,4,5], 6) == -1



def test_binary_search():
	""" done. """
	assert binary_search([1,2,3,4,5], 5) == 4
	assert binary_search([1,2,3,4,5], 1) == 0
	assert binary_search([1,2,3,4,5], 6) == -1



def test_time_search():
	""" done. """
	assert time_search(linear_search, [1,2,3,4,5], 5) < 1
	assert time_search(linear_search, [1,2,3,4,5], 1) < 1
	assert time_search(linear_search, [1,2,3,4,5], 6) < 1


def test_binary_search():
	assert binary_search([1,2,3,4,5], 5) == 4
	assert binary_search([1,2,3,4,5], 1) == 0
	assert binary_search([1,2,3,4,5], 6) == -1
	### TODO: add two more tests here.
	assert binary_search([], 1) == -1
	assert binary_search([2,4,6,8,10,12,14,16,18,20], 20) == 9




def test_compare_search():
	res = compare_search(sizes=[10, 100])
	print(res)
	assert res[0][0] == 10
	assert res[1][0] == 100
	assert res[0][1] < 1
	assert res[1][1] < 1
