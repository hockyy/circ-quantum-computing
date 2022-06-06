import math
from termcolor import colored

def get_period(a, n):
	ret = 1
	cur = a
	print(colored(f"2**1 == {cur}", "green"))
	while(cur != 1):
		cur = (cur * a) % n
		ret += 1
		print(colored(f"2**{ret} == {cur}", "green"))
	return ret

def main():
	n = int(input())
	factors = set()
	for a in range(1, n):
		print(colored(f"\nComputing {a}:", "blue"))
		gcd = math.gcd(a, n)
		print(colored(f"Got gcd {gcd}", "yellow"))
		if(gcd != 1):
			print(f"GCD is equal to {gcd}, which is factor of {n}")
			factors.add(gcd)
			factors.add(n//gcd)
			continue
		r = get_period(a, n)
		print(colored(f"Got period {r}", "yellow"))
		if(r % 2 == 1):
			print(f"r is {r}, which is odd")
			continue
		p = (int)(math.pow(a, r // 2))
		if(p % n == n - 1):
			print(f"a**(r / 2) === (n - 1) % n is satisfied")
			print(f"{a}**({r} / 2) == ({n} - 1) % {n} is satisfied")
			continue
		print("Got the factor is gcd(a**(r/2) + 1, n) and gcd(a**(r/2) - 1, n)")
		fac1 = (math.gcd(p + 1, n))
		fac2 = (math.gcd(p - 1, n))
		print(f"{fac1} and {fac2} is factors of {n}")
		factors.add(fac1)
		factors.add(fac2)

	print(factors)

if __name__ == '__main__':
	main()
