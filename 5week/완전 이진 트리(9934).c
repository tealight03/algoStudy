#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct Node {
    int key;
    struct Node *left, *right;
} Node;

Node *createNode(){
    Node* p = (Node*)malloc(sizeof(Node));
    p->key = 0;
    p->left = p->right = NULL;
    return p;
}

Node *insert(Node *p){
    if (p==NULL) return createNode();
    if (p->left == NULL) p->left = insert(p->left);
    else if (p->right == NULL) p->right = insert(p->right);
    return p;
}

Node* inorder_insert(Node *p){
    if (p == NULL){
        return 0;
    }
    inorder(p->left);
    scanf("%d", &(p->key));
    inorder(p->right);
}

void inorder(Node *p){
    if (p == NULL) return;
    inorder(p->left);
    printf("%d ", p->key);
    inorder(p->right);
}

int main(void){
    Node* root = NULL;
    int n;
    scanf("%d", &n);

    // 트리 생성
    for (int i = 0; i < sqrt(2, n); i++) root = insert(root);

    // 중위 순회를 이용해 트리에 데이터 삽입
    root = inorder_insert(root);

    inorder(root);

    return 0;
}