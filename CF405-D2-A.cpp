#include<iostream>
#include<algorithm>
#include<bits/stdc++.h>

bool desc (int i,int j){return i<j;}

using namespace std;

int main(){
    int n;
    cin>>n;
    int cubes[n];
    for(int i=0;i<n;i++){
        cin>>cubes[i];
    }
    sort(cubes,cubes+n,desc);
    for(int i=0;i<n;i++) cout<<cubes[i]<<" ";
    
    return 0;
}