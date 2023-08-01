def stutter(word):
	return (word[0:2]+"... ")*2+word+"?"


actual_param = [
    "increasing", "adventures", "enticing", "unacceptable", "accountable", "incredible", "exquisite",
    "am", "enduring", "outstanding", "astonishing", "astounding", "impressive", "revolutionize",
    "recurring", "recollection", "so", "gorgeous", "captivating"
]
for p in actual_param:
	print(stutter(p))