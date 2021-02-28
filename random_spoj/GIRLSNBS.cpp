#include <iostream>
using namespace std;

int main(int argc, char const *argv[]){
	int g, b;
	cin>>g>>b;
	//talk about bad style
	while(g!=-1 && b!=-1){
		if(g>b){
			if(g%(b+1)!=0)
				cout<<(g/(b+1))+1<<endl;
			else
				cout<<(g/(b+1))<<endl;
		}
		else if(g<b){
			if(b%(g+1)!=0)
				cout<<(b/(g+1))+1<<endl;
			else
				cout<<(b/(g+1))<<endl;
		}
		else{
			if(g==0 && b==0)
				cout<<0<<endl;
			else
				cout<<1<<endl;
		}

		cin>>g>>b;
	}

	return 0;
}