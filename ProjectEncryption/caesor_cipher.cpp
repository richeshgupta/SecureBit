#include<iostream>
#include<cstring>
using namespace std;
string alphabet = "abcdefghijklmnopqrstuvwxyz";

class caesor
{
    string text;
    int key;
    public:
    void input();
    string encrypt();
    string decrypt();
    caesor()
    {
        text = "abc";
        key = 1;
    }
};
void caesor::input()
{
    cout<<"Enter Text : \n";
    cin>>text;
    cout<<"\nEnter Key : \n";
    cin>>key;
}
string caesor::encrypt()
{
    string encrypted_text="";
    
    for(int i=0;i<(this->text).size();i++)
    {
        encrypted_text+=alphabet[(((int)caesor::text[i]-'a')+(key%26))];
    }
    return encrypted_text;
}

string caesor::decrypt()
{
    string decrypted_text = "";
    for(int i=0;i<(this->text).size();i++)
    {
        int x = (((int)caesor::text[i]-'a')-(key%26));
        
        decrypted_text+=alphabet[x];
    }
    return decrypted_text;
}   

int main(void)
{
    caesor c;
    cout<<" Encrypting ...\n";
    c.input();
    cout<<"Encrypted Text : "<<c.encrypt()<<endl;
    c.input();
    cout<<"\n Decrypted Text : "<<c.decrypt()<<endl;
    return 0;
}