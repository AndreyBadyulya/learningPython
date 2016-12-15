class JustCounter:
	_secretCount = 0

	def count(self):
		self._secretCount += 1
		print self._secretCount
		