'''
Heap Sort (max Heap)

by Chandan Agrawal

'''


def heap(seq, n, i):
	g = i
	l = 2 * i + 1
	r = 2 * i + 2

	if l < n and seq[i] < seq[l]:
		g = l

	if r < n and seq[g] < seq[r]:
		g = r

	if g != i:
		seq[i],seq[g] = seq[g],seq[i]
		heap(seq, n, g)

def sort(seq):
	n = len(seq)

	for i in range(n // 2 - 1, -1, -1):
		heap(seq, n, i)

	for i in range(n-1, 0, -1):
		seq[i], seq[0] = seq[0], seq[i]
		heap(seq, i, 0)

def main() :
	seq = []
	n = int(input("How many numbers to be sorted : "))
	print("Enter the numbers to be sorted : ")
	i = 0
	for i in range (n) :
		a = int(input())
		seq.append(a)
	sort(seq)
	n = len(seq)
	print("Sorted array is :")
	for i in range(n):
		print("%d" %seq[i])

if __name__ == '__main__':
    main()
