#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n); // 정수 n 입력

    int a[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]); // 배열 a 입력
    }

    // 배열 뒤집기
    int reversed[n];
    for (int i = 0; i < n; i++) {
        reversed[i] = a[n - 1 - i];
    }

    int result_array[n];
    int size = 0; // result_array 크기

    for (int index = 0; index < n; index++) {
        int value = reversed[index];

        if (size >= 1) {
            if (value == 1) {
                // 배열 맨 앞에 삽입
                for (int i = size; i > 0; i--) {
                    result_array[i] = result_array[i - 1];
                }
                result_array[0] = index + 1;
            } else if (value == 2) {
                // 배열 두 번째에 삽입
                for (int i = size; i > 1; i--) {
                    result_array[i] = result_array[i - 1];
                }
                result_array[1] = index + 1;
            } else if (value == 3) {
                // 배열 맨 끝에 삽입
                result_array[size] = index + 1;
            }
        } else {
            result_array[0] = index + 1;
        }
        size++;
    }

    // 결과 출력
    for (int i = 0; i < size; i++) {
        printf("%d ", result_array[i]);
    }

    return 0;
}
