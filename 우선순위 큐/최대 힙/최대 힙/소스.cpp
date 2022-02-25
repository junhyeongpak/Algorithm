#include <iostream>
#include <queue>
#include <ctime>

using namespace std;

// priority_queue<int, vector<int>, greater<int>> q; // min heap

/*  // 우선순위큐 메서드
* q.push(value) : value를 큐에 넣는다
* q.top() : max heap에서는 가장 큰 값 min heap에서는 작은 값을 리턴
* q.size() : 큐에 몇개의 요소가 있는지 리턴한다.
* q.empty() : 큐가 비어있으면 false를 리턴한다.
* q.pop() : min에서는 가장 작은 값, max heap에서는 가장 큰 값을 제거
*/

int main(void) {
	/*
	time_t start, finish;
	double duration;
	*/

	priority_queue< int, vector<int>, less<int> > q; // max heap에 대한 것
	int num;  // 연산의 개수 변수 선언
	scanf("%d", &num); // 연산의 개수 입력 받기
	//start = time(NULL);  //시작
	for (int i = 0; i < num; i++) {
		int x; // 입력받을 정수
		scanf("%d", &x);
		
		// x가 0일 경우
		if (x == 0) {
			// 큐가 비어있는 경우
			if (q.empty() == true) {
				printf("%d\n", 0);  // endl은 매우 느리다.
			}
			else {
				printf("%d\n", q.top());
				q.pop();
			}
		} 
		// x가 자연수인 경우
		else{
			q.push(x);
		}
	}
	/*
	finish = time(NULL); // 끝

	duration = (double)(finish - start);
	cout << duration << "초" << '\n';
	*/
	return 0;
}


// 배운점 cout과 cin과 endl은 매우매우 느리다
// 되도록이면 printf, scanf, \n을 사용하자!!