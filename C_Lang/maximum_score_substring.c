#include <stdio.h>
#include <string.h>

// Function prototype
int MaxScore(char str[]);

int main() {

    // Correctly call the MaxScore function with a string
    MaxScore("010");

    return 0;
}

// Function definition
int MaxScore(char str[]) {
    int c = 0;
    int len = strlen(str);
    char left[ len+1 ];
    char right[ len+1 ];
    for(int i = 0; i < len; i++){
        for(int j = 0; j < len; j++){
            if(j+i <= len){
                strncpy(left, str + j, i);
                left[i] = '\0';
                int rightIndex = 0;
                if(j > 0 && strlen(left) > 0){
                    strncpy(right, str, j);
                    rightIndex = j;
                }
                if(j + i < len && strlen(left) > 0){
                    strcpy(right + rightIndex, str + j + i);
                }
                else{
                    right[rightIndex] = '\0';
                }
            }

                int l_c = 0;
                int r_c = 0;
                if(strlen(left) > 0){
                    for(int k = 0; k < strlen(left); k++){
                        if(left[k] == '0'){
                            l_c += 1;
                        }
                }
                }
                if(strlen(right) > 0){
                    for(int k = 0; k < strlen(right); k++){
                        if(right[k] == '1'){
                            r_c += 1;
                        }
                }
                }

                if(c < l_c + r_c){
                    printf("%s \n", "greater than");
                    c = l_c + r_c;
                }
                
                
                 
        }
    }
    return c;
}
