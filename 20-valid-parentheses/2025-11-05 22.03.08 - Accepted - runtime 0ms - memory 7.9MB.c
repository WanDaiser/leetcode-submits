#include <stdio.h>
#include <stdbool.h>
#define MAX 100000

char stack[MAX];
int top = -1;

void push(char c) {
    if (top == MAX - 1) return;
    stack[++top] = c;
}

char pop() {
    if (top == -1) return '\0';
    return stack[top--];
}

bool isEmpty() {
    return top == -1;
}

bool isMatch(char open, char close) {
    return (open == '(' && close == ')') ||
           (open == '[' && close == ']') ||
           (open == '{' && close == '}');
}

bool isValid(char *s) {
    top=-1;
    for (int i = 0; s[i] != '\0'; i++) {
        char c = s[i];
        if (c == '(' || c == '[' || c == '{') {
            push(c);
        } 
        else if (c == ')' || c == ']' || c == '}') {
            char last = pop();
            if (!isMatch(last, c)) {
                return false;
            }
        }
    }
    return isEmpty();
}