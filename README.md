# Python Memories

##Overview
The challenge is described below in the requirements below. Basic idea is to practice Python "pickling" (or serialization). This was my first exposure to the concept so combining it with the sys module was also a bit of a stretch, but I managed to get the data stored. The next step would be to figure out how to get the data to print out in a readable string fashion. Version 2.0. 

###Requirements
+ Create a mary.py module that contains a Mary class.
+ Create a margaret.py module that contains a Margaret class.
+ Each module must accept one command line argument that is a message to add to a list (see example below).
+ Each module must be able to serialize a dictionary to a file named messages.
+ Each module must be able to deserialize the dictionary stored in messages.
+ Each module, after the object is deserialized from the file, must add the message to the appropriate list in the dictionary.
+ Each module must handle exceptions properly. 
