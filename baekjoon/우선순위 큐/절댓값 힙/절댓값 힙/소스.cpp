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

    priority_queue<int, vector<int>, greater<int> > q1;  //min힙
    priority_queue<int, vector<int>, less<int> > q2; // max힙

    deque<int> q;

    int num;  // 연산의 개수 변수 선언
    scanf("%d", &num); // 연산의 개수 입력 받기

    //start = time(NULL); //시작

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
    finish = time(NULL); // 끝

    duration = (double)(finish - start);
    cout << duration << "초" << '\n';
    */
    return 0;
}


// 배운점 cout과 cin과 endl은 매우매우 느리다
// 되도록이면 printf, scanf, \n을 사용하자!!