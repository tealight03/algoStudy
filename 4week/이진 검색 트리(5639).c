#include<stdio.h>
#include<stdlib.h>

typedef struct node {
	int key;
	struct node* left;
	struct node* right;
} Node;

Node *createNode(int key){
	Node *p = (Node*)malloc(sizeof(Node));
	p->key = key;
	p->left = p->right=NULL;
	return p;
}

Node *insert(Node *p, int key){
	if (p == NULL) return createNode(key);
	if (key < p->key) p->left = insert(p->left,key);
	else if (key > p->key) p->right = insert(p->right,key);
	return p;
}

Node* postorder(Node* head){
	if (head == NULL) return 0;
	postorder(head->left);
	postorder(head->right);
	printf("%d\n", head->key);
}

int main(void){
	Node* head = NULL;
	int key = 0;
	
	while (scanf("%d", &key) != EOF){
		head = insert(head, key);
	}
	
	postorder(head);
	
	return 0;
}