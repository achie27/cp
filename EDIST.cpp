/*#########################################
#
#	achie27
#	AC
#
#########################################*/

#include <iostream>
#include <algorithm>
using namespace std;

int ld[2001][2001];

int main(){
	int t;
	cin>>t;
	while(t--){
		string s1, s2;
		cin>>s1>>s2;
		
		int len1=s1.size(), len2=s2.size(), i=0, j=0;
		for(i=0; i<=len1 || i<=len2; i++){
			if(i<=len1)
				ld[0][i]=i;
			if(i<=len2)
				ld[i][0]=i;
		}
		
		for(i=1; i<=len1; i++){
			for(j=1; j<=len2; j++){
				int cost = s1[i-1] == s2[j-1] ? 0 : 1;
				int a=ld[i-1][j-1]+cost, b=ld[i-1][j]+1, c=ld[i][j-1]+1;
				ld[i][j] = a>b ? (b>c ? c:b) : (a>c ? c:a);
			}
		}

		cout<<ld[len1][len2]<<endl;
	}

	return 0;
}
