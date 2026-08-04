#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        vector<int> eval_stack;

        for (std::string& token : tokens) {
                if (token.size() == 1 && !isdigit(token[0])) {
                    int num2 = eval_stack.back(); eval_stack.pop_back();
                    int num1 = eval_stack.back(); eval_stack.pop_back();
                    int output = eval(num1, num2, token[0]);
                    eval_stack.push_back(output);
                } else {
                    eval_stack.push_back(stoi(token));
                }
        }

        return eval_stack.back();
    }

private:
    static int eval(int num1, int num2, char opr) {
        switch(opr) {
            case '+': return num1 + num2;
            case '-': return num1 - num2;
            case '*': return num1 * num2;
            default: return num1 / num2;
        }
    }
};

int main() {
    Solution sol;
    vector<string> tokens = {"2", "1", "+", "3", "*"};
    cout << sol.evalRPN(tokens) << endl; // 9

    tokens = {"4", "13", "5", "/", "+"};
    cout << sol.evalRPN(tokens) << endl; // 6

    tokens = {"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"};
    cout << sol.evalRPN(tokens) << endl; // 22

    return 0;
}
