# Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.

def centered_average(list):
	sum = 0
	div = 0 #init sum and div to 0
	list = sorted(list) #init the list in sorted order
	for i in range(1, len(list) - 1): #loop through the list, but ignore first and last
		if list[i] != list[i + 1]: #check to see if it's a dupe
			div += 1 #it's not a dupe, so update the divider by 1
			sum += list[i] #update the sum by the ith index
	print sum/div #or return

centered_average([1, 2, 3, 4, 100])
centered_average([1, 1, 5, 5, 10, 8, 7])
centered_average([-10, -4, -2, -4, -2, 0])


def mean(numbers):
	sorted_list = sorted(numbers) #make sure the list is in order
	low = min(sorted_list) #get the minimum val in the now sorted list of "numbers"
	high = max(sorted_list) #get max val from same list
	sorted_list.remove(low) #remove first
	sorted_list.remove(high) #remove last
	print sum(sorted_list)/len(sorted_list)

mean([1, 2, 3, 4, 100])
mean([1, 1, 5, 5, 10, 8, 8, 7])
mean([-10, -4, -2, -4, -2, 0])

def shorty(list):
	list = sorted(list) #init the list in sorted order
	list.pop(0)
	list.pop(len(list)-1)
	print sum(list)/len(list)

shorty([1, 2, 3, 4, 100])
shorty([1, 1, 5, 5, 10, 8, 8, 7])
shorty([-10, -4, -2, -4, -2, 0])

def shorty(list):
	list = sorted(list) #init the list in sorted order
	centerd_list = list[1:-1] #splice that array, son! (or daugther)
	print sum(list)/len(list)