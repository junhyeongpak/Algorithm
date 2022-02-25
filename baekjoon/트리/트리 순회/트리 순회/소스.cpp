#include <iostream>
#include <vector>

using namespace std;

// 이진트리를 구성하기 위해 Node구조체를 만들어서 왼쪽과 오른쪽 만듦
struct Node {
	char left; 
	char right;
};

// 배열 크기 선언
struct Node arr[27];


// 전위순회
void preoreder(char root) {
	if (root == '.') return;
	else {
		cout << root;
		preoreder(arr[root].left);
		preoreder(arr[root].right);
	}
}

// 중위순회
void inorder(char root) {
	if (root == '.') return;
	else {
		inorder(arr[root].left);
		cout << root;
		inorder(arr[root].right);
	}
}

// 후위순회
void postorder(char root) {
	if (root == '.') return;
	else {
		postorder(arr[root].left);
		postorder(arr[root].right);
		cout << root;
	}
}
int main() {

	std::ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int num;
	cin >> num;
	for (int i = 0; i < num; i++) {
		char a, b, c;
		cin >> a >> b >> c;
		arr[a].left = b;
		arr[a].right = c;
	}

	preoreder('A');
	cout << '\n';
	inorder('A');
	cout << '\n';
	postorder('A');
	cout << '\n';

	return 0;
}