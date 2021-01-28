// RSA implementation
#include<iostream>
#include<cmath>
using namespace std;

const long prime_length = 1e9+7;

long long primes[10000];

int main()
{
   for(int i=3;i<=100;i++)
   {
       bool fl = 1;
       for(int j = 2;j<=sqrt(i);j++)
       {
           if(j%i==0)
           {
               fl = 0;
               break;
           }
       }
       if(fl==1)
       {
           cout<<i<<endl;
       }
   }
}