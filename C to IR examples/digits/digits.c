#include <stdio.h>
int main(int argc, char *args[]){
	int num, digit, sum, reverse, num2;
	printf("Enter your input integer\n");
	scanf("%d",&num);
	num2 = num;
	sum = reverse = 0;
	while (num>0) {
		digit = num %10;
		sum += digit;
		reverse = reverse*10 + digit;
		num /= 10;
	}
	printf("Sum of digits of %d is %d\n",num2,sum);
	if (reverse == num2)
		printf("%d is Palindrom\n",num2);
	else
		printf("%d is not Palindrom\n",num2);
}
