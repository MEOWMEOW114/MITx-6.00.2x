import random, pylab


# You are given this function
def getMeanAndStd(X):
	mean = sum(X) / float(len(X))
	tot = 0.0
	for x in X:
		tot += (x - mean) ** 2
	std = (tot / len(X)) ** 0.5
	return mean, std


# You are given this class
class Die(object):
	def __init__(self, valList):
		""" valList is not empty """
		self.possibleVals = valList[:]

	def roll(self):
		return random.choice(self.possibleVals)


# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
	"""
	  - values, a list of numbers
	  - numBins, a positive int
	  - xLabel, yLabel, title, are strings
	  - Produces a histogram of values with numBins bins and the indicated labels
		for the x and y axes
	  - If title is provided by caller, puts that title on the figure and otherwise
		does not title the figure
	"""
	pylab.hist(values, bins=numBins)
	pylab.xlabel(xLabel)
	pylab.ylabel(yLabel)
	if title is not None:
		pylab.title(title)

	pylab.show()


# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
	"""
	  - die, a Die
	  - numRolls, numTrials, are positive ints
	  - Calculates the expected mean value of the longest run of a number
		over numTrials runs of numRolls rolls.
	  - Calls makeHistogram to produce a histogram of the longest runs for all
		the trials. There should be 10 bins in the histogram
	  - Choose appropriate labels for the x and y axes.
	  - Returns the mean calculated
	"""
	longest_run = []

	numTrue = 0

	for trial in range(numTrials):
		run=[]
		for roll in range(numRolls):
			die = Die(die.possibleVals)
			run.append(die.roll())

		import itertools
		result = max(sum(1 for _ in l) for n, l in itertools.groupby(run))
		# result = max(set(run), key=run.count)
		# print result
		longest_run.append(result)

	# print reduce(lambda x, y: x + y, longest_run)
	# print numTrials
	mean = float(reduce(lambda x, y: x + y, longest_run)) / float(len(longest_run))
	# print mean
	# return mean
	makeHistogram(longest_run, 10, "Aaaaa", "Bbbbb", "Ccccc")
	return mean

fff = getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000)
print fff

#
# # One test case
# print getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000) 5.312
# Write a function called makeHistogram(values, numBins, xLabel, yLabel, title=None), with the following specification:


