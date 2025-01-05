#include<stdio.h>
#include<string.h>

int add(int a, int b);
int div(int a, int b);
int main(){
    int a, b, sum, divison;
    char opr[10];
    printf("Enter num1: \n");
    scanf("%d", &a);
    printf("Enter num2: \n");
    scanf("%d", &b);
    sum = add(a, b);
    divison = div(a, b);
    printf("Enter the operation you want to perform:  ");
    scanf("%s", &opr);
    if(strcmp(opr, "Sum") == 0){   
        printf("Sum of %d and %d is %d \n", a, b, sum);
        return 0;
    }
    
    printf("Divison of %d and %d is %d \n", a, b, divison);
    return  0;
}

int add(int a, int b){
    return  a + b;
}
int div(int a, int b){
    return a - b;
}