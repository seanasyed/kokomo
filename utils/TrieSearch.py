from TrieNode import TrieNode

"""
Implements a text corpus search as a trie
"""
class TrieSearch: 

	def __init__(self):
		self.root = TrieNode.TrieNode("")

	"""
	Searches for a particular song based on an input list of words

	Returns a duple where the first element is a bool indicating whether or 
	not a single song was identified or if a candidate list of songs was 
	returned. The second element is the list of songs that were identified by
	the search contents. 
	"""
	def search(self, words): 
		pass

	"""
	Inserts a particular phrase into the trie based on the given list of words
	"""
	def insertPhrase(self, words, song): 
		pass

	



