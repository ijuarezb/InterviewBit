#include <iostream>
#include <queue> 
using namespace std; 

void showq(queue <int> gq) { 
    queue <int> g = gq; 
    while (!g.empty()) { 
        cout << g.front() << ' '; 
        g.pop(); 
    } 
    cout << endl; 
} 

void showvp(vector< pair <int, char> > gv) { 
    vector< pair <int, char> > g = gv;
    pair <int, char> p;
    while (!g.empty()) {
	    p = g.back();
        cout << "(" << p.first << ", " << p.second << ") "; 
        g.pop_back(); 
    } 
    cout << endl; 
}

void showv(vector< int > gv) { 
    for (int x : gv)
    	cout << x << " ";
    cout << endl; 
}

string multiple(int A) {
    
    queue<int> q; q.push(1%A);
    vector<int> vis(A+1, -1); vis[1%A] = 1;
    vector< pair<int, char> > par(A+1, make_pair(-1, '1'));
    string s = "";
    int tp, p, a1, a2;

    while (!q.empty()) {
        tp = q.front();
        q.pop();
        
        if (tp == 0) {
            s = "";
            s += par[0].second;
            p = par[0].first;

            while(p != -1){
                s += par[p].second;
                p = par[p].first;
            }

            reverse(s.begin(), s.end());
            return s;
        }
        
        a1 = (tp * 10) % A;
        a2 = ((tp * 10) % A + 1) % A;

        if (vis[a1] == -1) {
        	q.push(a1);
        	vis[a1] = 1;
        	par[a1] = make_pair(tp, '0');
        }
          
        if (vis[a2] == -1) {
        	q.push(a2);
        	vis[a2] = 1;
        	par[a2] = make_pair(tp, '1');
        }        
    }
    return s;
}
  
int main() 
{ 
    cout << multiple(55) << endl;
    return 0; 
} 