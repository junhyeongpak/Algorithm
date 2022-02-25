#include <iostream>
#include <vector>
#include <queue>
using namespace std;


// 문제에서 요구하는 요소의 개수를 잘 확인하자.
vector<int> V[100001];
int parent[100001];
bool visited[100001];
queue<int> q;

// 트리도 결국은 그래프의 일종이다.
// 방문하지 않은 지점은 root에서부터 출발하므로 자식노드가 된다.
// vector를 활용하여 연결리스트를 활용한 그래프 문제가 된다.
// 여기서는 dfs를 활용하여 문제를 해결하였다. bfs로도 해결해볼까?
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


// bfs로 탐색하는 방법
// bfs가 메모리를 약 2/3정도만 활용하면서 시간도 더 빠르게 수행하였다.
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

// bfs와 dfs를 활용하는 문제
// dfs는 회귀를 이용하였지만
// bfs는 단순 while반복을 수행하였다.