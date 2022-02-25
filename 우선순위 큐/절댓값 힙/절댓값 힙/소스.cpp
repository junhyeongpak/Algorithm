#include <iostream>
#include <queue>
//#include <ctime>
#include <cmath>

using namespace std;


int main(void) {
    /*
    time_t start, finish;
    double duration;
    */

    priority_queue<int, vector<int>, greater<int> > q1;  //min��
    priority_queue<int, vector<int>, less<int> > q2; // max��

    deque<int> q;

    int num;  // ������ ���� ���� ����
    scanf("%d", &num); // ������ ���� �Է� �ޱ�

    //start = time(NULL); //����

    for (int i = 0; i < num; i++) {
        int x;
        scanf("%d", &x);
        if (x == 0) {
            if (q1.empty() == true && q2.empty() == false) {
                printf("%d\n", q2.top());
                q2.pop();
            }
            else if (q1.empty() == false && q2.empty() == true) {
                printf("%d\n", q1.top());
                q1.pop();
            }
            else if (q1.empty() == true && q2.empty() == true) {
                printf("%d\n", 0);
            }
            else if (abs(q1.top()) == abs(q2.top())) {
                printf("%d\n", q2.top());
                q2.pop();
            }
            else if (abs(q1.top()) > abs(q2.top())) {
                printf("%d\n", q2.top());
                q2.pop();
            }
            else {
                printf("%d\n", q1.top());
                q1.pop();
            }
        }
        else {
            if (x > 0) { q1.push(x); }
            else { q2.push(x); }
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