#include <stdio.h>
#include <stdlib.h>

int main()
{
	int a, b, s, n, tmp;
	do
	{
		printf("donner un intervale [a,b] :\n");
		printf("donner a: ");
		scanf("%d", &a);
		printf("donner b: ");
		scanf("%d", &b);
	} while (5 > a || a >= b || b > 200);
	for (n = a; n <= b; n++)
	{
		s = 0;
		tmp = n;
		while (tmp != 0)
		{
			s = s + tmp % 10;
			tmp = tmp / 10;
		}
		if (n % s == 0)
			printf("%d est un nombre Harshad \n", n);
	}
	return 0;
}