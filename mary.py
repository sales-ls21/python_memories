import pickle
import sys

class Mary(object):

	def __init__(self):
		self.mary_notes = dict()

		try:
	  		self.mary_notes = self.deserialize()

		except FileNotFoundError:
			self.serialize()


	def add_note(self, note):
		self.mary_notes.update({"Mary": note})
		self.serialize()


	def serialize(self):
		with open('messages.txt', 'wb+') as f:
			pickle.dump(self.mary_notes, f)

		with open('messages.txt', 'rb') as f:
			binary = f.read()

		return binary

	def deserialize(self):
		try:
			with open('messages.txt', 'rb+') as f:
				self.mary_notes = pickle.load(f)
		except EOFError:
			print("Error")

		return self.mary_notes

if __name__ == '__main__':
	new_mary = Mary()
	new_mary.add_note(sys.argv[1])
	if sys.argv[1] == "ls":
		new_mary.list_notes()
	# elif sys.argv[1] == "add":
	# 	new_mary.add_note(sys.argv[2])
	# elif sys.argv[1] == "delete":
	# 	new_mary.delete_note(sys.argv[2])
