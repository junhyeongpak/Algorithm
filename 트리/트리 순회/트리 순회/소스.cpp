#include <iostream>
#include <vector>

using namespace std;

// ����Ʈ���� �����ϱ� ���� Node����ü�� ���� ���ʰ� ������ ����
struct Node {
	char left; 
	char right;
};

// �迭 ũ�� ����
struct Node arr[27];


// ������ȸ
void preoreder(char root) {
	if (root == '.') return;
	else {
		cout << root;
		preoreder(arr[root].left);
		preoreder(arr[root].right);
	}
}

// ������ȸ
void inorder(char root) {
	if (root == '.') return;
	else {
		inorder(arr[root].left);
		cout << root;
		inorder(arr[root].right);
	}
}

// ������ȸ
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