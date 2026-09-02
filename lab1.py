def fib_iterative(n):
	seq = []
	a, b = 0, 1
	for _ in range(n):
		seq.append(a)
		a, b = b, a + b
	return seq


def main():
	with open("output/fibonacci.txt", "w") as f:
		for value in fib_iterative(25):
			f.write(f"{value}\n")

if __name__ == "__main__":
	main()

