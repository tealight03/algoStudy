#include <stdio.h>

long long arr[1000000];
long long tree[4000000];

long long MakeSegmentTree(int start, int end, int node) { 
	if (start == end)
		return tree[node]=arr[start];

	int mid = (start + end) / 2;
	tree[node] =  MakeSegmentTree(start, mid, node * 2) + MakeSegmentTree(mid + 1, end, node * 2 + 1); 
	
	return tree[node];
}

long long sum(int start, int end, int node, int left, int right) {
	if (start > right || end < left)
		return 0;
	if (left <= start && end <= right)
		return tree[node];

	int mid = (start + end) / 2;
	
	return sum(start, mid, node * 2, left, right) + sum(mid + 1, end, node * 2 + 1, left, right);
}

long long UpdateSegmentTree(int start, int end, int node, int index, long long diff) {
	if (index < start || index > end)
		return 0;

	tree[node] += diff; 
	
	if (start == end)
		return 0;

	int mid = (start + end) / 2;
	UpdateSegmentTree(start, mid, node * 2, index, diff);
	UpdateSegmentTree(mid + 1, end, node * 2 + 1, index, diff);
}

int main() {
	int n, x, y;
	scanf("%d %d %d", &n,&x,&y);

	for (int i = 0; i < n; i++) {
		scanf("%lld", &arr[i]);
	}

	MakeSegmentTree(0, n - 1, 1);
	int cnt = x + y;
	for (int i = 0; i < cnt; i++) {
		long long a, b, c;
		scanf("%lld %lld %lld", &a, &b, &c);
		if (a == 1) {
			UpdateSegmentTree(0, n - 1, 1, b - 1, c - arr[b - 1]);
			arr[b - 1] = c;
		}
		else {
			printf("%lld\n", sum(0, n - 1, 1, b - 1, c - 1));
		}
	}

	return 0;
}