#include <stdio.h>

int main()
{
	int n, k;
	int a1, a2, a3, a4;
	for (n = 1100; n <= 9988; n++)
	{
		a1 = n % 10;
		a2 = (n / 10) % 10;
		a3 = (n / 100) % 10;
		a4 = (n / 1000) % 10;
		if (a1 == a2 && a3 == a4 && a1 != a3)
		{
			for (k = 1; k <= n / 2; k++)
			{
				if (k*k == n)
					printf("%d est un carre parfait puisqu'il est egale  %d^2 \n", n, k);
			}
		}
	}
	return 0;
}