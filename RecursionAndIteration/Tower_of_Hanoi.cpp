#include <iostream>
using namespace std;
void przeloz_krazek (char skad, char dokad)
{
    cout<<"przeloz z "<<skad<<" na "<<dokad<<endl;
}
void hanoi (int ile, char a, char b, char c)
{
    if (ile==1)
    {
        przeloz_krazek(a, c);
    }
    else
    {
        hanoi (ile-1, a, c, b);
        przeloz_krazek (a, c);
        hanoi (ile-1, b, a, c);
    }
}
int main()
{
    int ilosc;
    cout<<"Podaj ilosc krazkow: ";
    cin>>ilosc;
    hanoi(ilosc, 'a', 'b', 'c');
return  0;
}
