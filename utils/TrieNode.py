"""
A rudimentary implementation of a Trie data structure that will suit our needs
for this project. 
"""
class TrieNode: 

	def __init__(self, word, endOfLine=False):
		self.word = word
		self.endOfLine = endOfLine
		self.children = set()

	"""
	Insert a node into the trie by adding it to its parent's list of children
	"""
	def addChild(self, word): 
		for node in self.children: 
			if node.word == word: 
				return
		self.children.add(word)

	"""
	Search for a particular phrase. If we reach the end of the phrase, then we
	should return all of the children of the node at the end since they 
	will all be candidate songs. 

	Returns a duple where the first element contains the list of songs (if any)
	and the second element is the list of words that need to be searched from
	the root node if no candidate songs were found. 
	"""
	def searchAtNode(self, words=[], currNode=self): 
		
		# Iterate through the list of words in order
		for word in words: 
			for child in currNode.children: 

				# A child node has been found for the current word
				if child.word = word:
					foundNode = child

					# If this word is the end of the phrase, return the songs
					if foundNode.endOfLine: 
						return (foundNode.children, words[words.index(word):])
					break

			# A match for the word was not found, so the phrase does not exist
			if currNode == foundNode: 
				return ([], words[words.index(word):])

	

		



