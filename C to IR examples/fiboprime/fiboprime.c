#include <stdio.h>
int IsPrime(int b)	{
	int i;
	for (i=2 ; i<=b/2;i++){
		if (b%i == 0)
			break;
	}
	if (b<=1 || i <=b/2)
		printf("Not Prime");
	else
		printf("Prime");
}

void main()	{
	int i, n, a, b, t;
	printf("Input value of n");	
	scanf("%d",&n);
	a = 0;
	if (n ==1)
		printf("Fibo Term is %d ",a);
	else	{
		b = 1;
		for (i = 3; i <=n ; i++){
			t = a + b;
			a = b;
			b = t;
		}
		printf("Fibo Term is %d ",b);
	}
	IsPrime(b);
}
