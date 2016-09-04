/******************************

achie27
AC, jugaad

******************************/

#include <iostream>
#include <stack>
using namespace std;

#define ll long long int
bool issorted(int* arr, int len);

int main(){
    int t;
    cin>>t;
    while(t>0){
        int a[t];
        stack<int> st;
        int res[t], x=0, i=0;
        for(i=0; i<t; i++)
            cin>>a[i];
        
        for(i=0; i<t; i++){
       		if(x==0){
       			if(a[i]==1)
       				res[x++]=a[i];
       			else
       				st.push(a[i]);
       			continue;
       		}
            if(res[x-1]==a[i]-1){
                res[x++]=a[i];
            }
            else{
                int tp;                
                while(!st.empty() && (tp=st.top())==res[x-1]+1){
                    res[x++]=tp;
                    st.pop();
                }
                if(a[i]-1==res[x-1])
                	res[x++]=a[i];
                else
                	st.push(a[i]);
            }
        }
      
        while(!st.empty()){
            res[x++]=st.top();
            st.pop();
        }
        
        if(issorted(res, t))
        	cout<<"yes";
        else
        	cout<<"no";

        cout<<endl;
        cin>>t;
    }
}

bool issorted(int* arr, int len){
    int i=0;
    for(i=1; i<len; i++){
        if(arr[i]<arr[i-1])
            return false;
    }
    return true;
}