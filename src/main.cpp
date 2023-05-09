#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {
  if (argc <= 1) {
    cerr << "Usage: ./SUM number1 [number2, [number3 ...]]" << endl;
    return -1;
  }

  double sum = 0;
  for (int i = 1; i < argc; i++) {
    const double value = stod(argv[i]);
    sum += value;
  }
  cout << sum << endl;

  return 0;
}
