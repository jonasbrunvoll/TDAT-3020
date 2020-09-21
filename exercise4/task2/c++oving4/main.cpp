#include <iostream>
using namespace std;

string input;

string transform(string input){

    for (int i = 0; i < input.length(); ++i) {
        if (input[i] == '&') {
            input.replace(i, 1, "&amp");
        } else if (input[i] == '<'){
            input.replace(i, 1, "&lt");
        } else if (input[i] == '>') {
            input.replace(i, 1, "&gt");
        }

    }
    return "This is the output: " + input;
}

int main() {
    cout << "Write a sentence: " << endl;
    getline(cin, input);
    string output = transform(input);
    cout << output << endl;
    return 0;
}
