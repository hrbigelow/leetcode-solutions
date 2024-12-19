class Solution {
public:
    bool isValid(string s) {
      stack<char> st;
      map<char, char> matching = { { '}', '{' }, { ')', '(' }, { ']', '[' } };
      for (auto ch : s) {
        switch (ch) {
          case '{':
          case '[':
          case '(':
          st.push(ch); break;
          case '}':
          case ']':
          case ')': {
            if (st.empty() || st.top() != matching[ch]) return false;
            st.pop();
          }
        }
      }
      return st.empty();
    }
};

/*

*/
