#include <iostream>
#include <queue>
#include <ctime>

using namespace std;

// priority_queue<int, vector<int>, greater<int>> q; // min heap

/*  // �켱����ť �޼���
* q.push(value) : value�� ť�� �ִ´�
* q.top() : max heap������ ���� ū �� min heap������ ���� ���� ����
* q.size() : ť�� ��� ��Ұ� �ִ��� �����Ѵ�.
* q.empty() : ť�� ��������� false�� �����Ѵ�.
* q.pop() : min������ ���� ���� ��, max heap������ ���� ū ���� ����
*/

int main(void) {
	/*
	time_t start, finish;
	double duration;
	*/

	priority_queue< int, vector<int>, less<int> > q; // max heap�� ���� ��
	int num;  // ������ ���� ���� ����
	scanf("%d", &num); // ������ ���� �Է� �ޱ�
	//start = time(NULL);  //����
	for (int i = 0; i < num; i++) {
		int x; // �Է¹��� ����
		scanf("%d", &x);
		
		// x�� 0�� ���
		if (x == 0) {
			// ť�� ����ִ� ���
			if (q.empty() == true) {
				printf("%d\n", 0);  // endl�� �ſ� ������.
			}
			else {
				printf("%d\n", q.top());
				q.pop();
			}
		} 
		// x�� �ڿ����� ���
		else{
			q.push(x);
		}
	}
	/*
	finish = time(NULL); // ��

	duration = (double)(finish - start);
	cout << duration << "��" << '\n';
	*/
	return 0;
}


// ����� cout�� cin�� endl�� �ſ�ſ� ������
// �ǵ����̸� printf, scanf, \n�� �������!!