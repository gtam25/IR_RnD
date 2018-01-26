
int main(int argc, char *args[]){
	scanf("%d",&num);
	num2 = num;
	sum = reverse = 0;
	do{
		digit = num %10;
		sum += digit;
		reverse = reverse*10 + digit;
		num /= 10;
	}while (num>0);
	printf("Sum of digits of %d is %d\n",num2,sum);
	if (reverse == num2){
		printf("%d is Palindrom\n",num2);
		printf("hi");
	}
	else if (x>0) 
	{
		printf("go");
		printf("go");
		printf("go");
	}
	else{
		printf("%d is not Palindrom\n",num2*2, n, max(3, 5));
	}
}
