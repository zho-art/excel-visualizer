// #include <stdio.h>
// int main() {
//     printf("Hello, World!\n");
//     return 0;
// }


// #include <stdio.h>  
// int main() {
//     char character;
//     printf("请输入一个字母:",character);
//     if ('character'>='A' & 'character'<='Z')

// }

// #include <stdio.h>
// #include <ctype.h>  // 包含 isupper 和 tolower 函数
// int main() {
//     char character;
//     printf("请输入一个字母: ");
//     scanf("%c", &character);  // 读取用户输入的字符

//     if (character >= 'A' && character <= 'Z') {
//         // 如果是大写字母，转换为小写字母
//         character = tolower(character);
//     }

//     if  (character >= 'a' && character <= 'z') {
//         character = toupper(character);
//     }
//         // 输出转换后的字符
//     printf("转换后的字母是: %c\n", character);
//     return 0;
// }


#include <stdio.h>
#include <ctype.h>
int main() {
    char character;
    printf("请输入一个字母: ");
    scanf("%c", &character);  
    if (isupper(character)) {
        character = tolower(character);
    } else if (islower(character)) {
        character = toupper(character);
    }
    printf("转换后的字母是: %c\n", character);
    return 0;
}





