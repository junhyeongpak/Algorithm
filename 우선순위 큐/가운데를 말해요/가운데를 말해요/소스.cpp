#include <iostream>
#include <queue>
#include<functional> 

using namespace std;

struct cmp {
	bool operator()(int a, int b, int c) {
		return a > b && b < c;
	}
};

int main() {
	cin.tie(0);
	cin.sync_with_stdio(0);

	priority_queue<int, vector<int>, cmp> q;
	int num;
	for (int i = 0; i < num; i++) {
		int x;
		cin >> x;
		q.push(x);
		cout << q.top() << '\n';
	}
	return 0;
}