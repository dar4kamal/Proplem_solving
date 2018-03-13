#include<iostream>
using namespace std;

int main(){
    int n,h,a,w=0;
    cin>>n>>h;
    for(int i=0;i<n;i++){
        cin >> a;
        (a <= h) ? w+=1 : w+=2;
    }
    cout<<w;
    
    return 0;
}