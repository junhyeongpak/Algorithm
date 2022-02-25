#include <iostream>
#include <cmath>
using namespace std;

void hanoi(int n, char from, char temp, char to) {

	if (n == 1) {
		printf("%c %c\n", from, to);
		return;
	}
	else {
		hanoi(n - 1, from, to, temp);
		printf("%c %c\n", from, to);
		hanoi(n - 1, temp, from, to);
	}
}
int main(){
	cout.tie(0);
	cin.tie(0);
	cin.sync_with_stdio(0);

	int num;
	cin >> num;
	printf("%d\n", (int)pow(2, num) - 1);
	hanoi(num, '1', '2', '3');
	return 0;
}