# Import OrderedDict from collections
from collections import OrderedDict

# Create a dictonary called glossary
glossary = OrderedDict()

# Have the glossary include a list of five (5) programing words you have learned in chapters 4-6.
# Use these words as keys to your dictionary.
# Find the definition of these words and use them as the values to the keys.
glossary['variable'] = 'A reserved memory location to store values.'
glossary['list'] = 'A list of comma-separated values (items) between square brackets.'
glossary['tuple'] = 'A datatype that can\'t be overwritten.'
glossary['loop'] = 'A way for programmers to iterate over items in a dataset.'
glossary['slice'] = 'Used to specify a specific items in a list.'

# Using a loop, print each word and its meaning as neatly formatted output.
for word, definition in glossary.items():
	print(word.title() + " - " + definition)