#include<iostream>
using namespace std;

int main(){
    int n,A_won=0,D_won=0;
    cin>>n;
    char game;
    for(int i=0;i<n;i++){
        cin>>game;
        if(game=='A'){
            ++A_won;
        }else if (game == 'D'){
            ++D_won;
        }
    }
    if(A_won == D_won ){
        cout<<"Friendship";
    }else if(A_won > D_won){
        cout<<"Anton";
    }else{
        cout<<"Danik";
    }
    return 0;
}
