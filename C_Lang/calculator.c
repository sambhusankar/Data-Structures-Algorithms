#include <stdio.h>
#include <string.h>
int main()
{
    char a[20];
    printf("Enter an operation: ");
    scanf("%s", &a);  
    int len = sizeof(a);
    printf("%d", len);
    return 0;
}