/*
https://www.acmicpc.net/problem/1920
*/
#include <stdio.h>
#include <stdlib.h>
int arr[100001], parr[100001], tmp[100001];
/*
void insertion_sort(int list[], int n) {
	int i, j, key;
	for (i = 1; i < n; i++) {
		key = list[i];

		for (j = i - 1; j >= 0 && list[j] > key; j--) {
			list[j + 1] = list[j];
		}
		list[j + 1] = key;
	}
}
*/

void merge(int arr[], int left, int right) {

	int L, R, k, a;
	int mid = (left + right) / 2;
	L = left;
	R = mid + 1;
	k = left;

	while (L <= mid && R <= right)
		tmp[k++] = arr[L] <= arr[R] ? arr[L++] : arr[R++];

	if (L > mid)
		for (a = R; a <= right; a++)
			tmp[k++] = arr[a];
	else
		for (a = L; a <= mid; a++)
			tmp[k++] = arr[a];

	for (a = left; a <= right; a++)
		arr[a] = tmp[a];

}


void mergeSort(int arr[], int left, int right) {

	if (left == right) return;
	int mid;
	mid = (left + right) / 2;
	mergeSort(arr, left, mid);
	mergeSort(arr, mid + 1, right);
	merge(arr, left, right);

}



int sol(int k,int left,int right) {
	int mid;
	//left = 0, right = n-1;
	while (left <= right) {
		mid = (left + right) / 2;
		if (arr[mid] == k) return 1;
		else {
			if (arr[mid] < k) left = mid + 1;
			else right = mid - 1;
		}
	}
	return -1;
}
int main() {
	int n,m,k;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	} 
	scanf("%d", &m);
	for (int i = 0; i < m; i++) {
		scanf("%d", &parr[i]);
	}
	mergeSort(arr, 0, n - 1);

	for (int i = 0; i < m; i++) {
		k = sol(parr[i],0,n-1);
		if (k == 1) printf("1\n");
		else printf("0\n");
	}


	return 0;
}