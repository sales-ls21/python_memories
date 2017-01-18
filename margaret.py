import pickle
import sys

class Margaret(object):

	def __init__(self):
		self.margaret_notes = dict()

		try:
	  		self.margaret_notes = self.deserialize()

		except FileNotFoundError:
			self.serialize()

	def add_note(self, note):
		self.margaret_notes.update({"Maggie": note})
		self.serialize()

	def serialize(self):
		with open('messages.txt', 'wb+') as f:
			pickle.dump(self.margaret_notes, f)

		with open('messages.txt', 'rb') as f:
			binary = f.read()

		return binary

	def deserialize(self):
		try:
			with open('messages.txt', 'rb+') as f:
				self.margaret_notes = pickle.load(f)
		except EOFError:
			print("Error")

		return self.margaret_notes

if __name__ == '__main__':
	new_margaret = Margaret()
	new_margaret.add_note(sys.argv[1])
	if sys.argv[1] == "ls":
		new_margaret.list_notes()
		