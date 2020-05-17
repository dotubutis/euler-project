# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

py_triples = []
def find_pytriple_1000(range_min, range_max):
	for x in range(range_min, range_max):
		for y in range(x+1,range_max):
			z = y + 1
			while z**2 < x**2 + y**2:
				z += 1
			if (x**2 + y**2 == z**2) and (x < y < z):
				py_triples.append((x,y,z))
				if (x + y + z) == 1000:
					result = (x, y, z)
					return result

py_triple = find_pytriple_1000(0, 1000)
result = py_triple[0] * py_triple[1] * py_triple[2]
print(result)