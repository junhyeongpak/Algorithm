#include <iostream>
#include <vector>
#include <queue>
using namespace std;


// �������� �䱸�ϴ� ����� ������ �� Ȯ������.
vector<int> V[100001];
int parent[100001];
bool visited[100001];
queue<int> q;

// Ʈ���� �ᱹ�� �׷����� �����̴�.
// �湮���� ���� ������ root�������� ����ϹǷ� �ڽĳ�尡 �ȴ�.
// vector�� Ȱ���Ͽ� ���Ḯ��Ʈ�� Ȱ���� �׷��� ������ �ȴ�.
// ���⼭�� dfs�� Ȱ���Ͽ� ������ �ذ��Ͽ���. bfs�ε� �ذ��غ���?
/*
void dfs(int x) {
	visited[x] = true;
	for (int j = 0; j < V[x].size(); j++) {
		int next = V[x][j];
		if (visited[next] == false) {
			parent[next] = x;
			dfs(next);
		}
	}
}*/


// bfs�� Ž���ϴ� ���
// bfs�� �޸𸮸� �� 2/3������ Ȱ���ϸ鼭 �ð��� �� ������ �����Ͽ���.
void bfs(int x) {
	visited[x] = true;
	q.push(x);

	while (q.empty() == false) {
		int a = q.front();
		q.pop();
		for (int j = 0; j < V[a].size(); j++) {
			int next = V[a][j];
			if (visited[next] == false) {
				visited[next] = true;
				parent[next] = a;
				q.push(next);
			}
		}
	}
}

int main() {
	cin.tie(0);
	cin.sync_with_stdio(0);

	int a, b;
	int num;
	cin >> num;
	for (int i = 1; i < num; i++) {
		cin >> a >> b;
		V[a].push_back(b);
		V[b].push_back(a);
	}

	bfs(1);

	for (int j = 2; j < num + 1; j++) {
		cout << parent[j] << '\n';
	}

	return 0;
}

// bfs�� dfs�� Ȱ���ϴ� ����
// dfs�� ȸ�͸� �̿��Ͽ�����
// bfs�� �ܼ� while�ݺ��� �����Ͽ���.