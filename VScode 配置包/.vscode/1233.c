// #include <stdio.h>
// int main() {
//     printf("Hello, World!\n");
//     return 0;
// }


// #include <stdio.h>  
// int main() {
//     char character;
//     printf("������һ����ĸ:",character);
//     if ('character'>='A' & 'character'<='Z')

// }

// #include <stdio.h>
// #include <ctype.h>  // ���� isupper �� tolower ����
// int main() {
//     char character;
//     printf("������һ����ĸ: ");
//     scanf("%c", &character);  // ��ȡ�û�������ַ�

//     if (character >= 'A' && character <= 'Z') {
//         // ����Ǵ�д��ĸ��ת��ΪСд��ĸ
//         character = tolower(character);
//     }

//     if  (character >= 'a' && character <= 'z') {
//         character = toupper(character);
//     }
//         // ���ת������ַ�
//     printf("ת�������ĸ��: %c\n", character);
//     return 0;
// }


#include <stdio.h>
#include <ctype.h>
int main() {
    char character;
    printf("������һ����ĸ: ");
    scanf("%c", &character);  
    if (isupper(character)) {
        character = tolower(character);
    } else if (islower(character)) {
        character = toupper(character);
    }
    printf("ת�������ĸ��: %c\n", character);
    return 0;
}





