#include <iostream>
#include <algorithm>
using namespace std;
int N, B, i, j;
struct Tthing
{
    int nr;
    int price;
    int weight;
};
bool best (Tthing a, Tthing b)
{
    return a.price*b.weight>b.price*a.weight;
}
void backpack_best(Tthing tab[], int N, int B)
{
    j=0;
    int occupied=0;
    sort(tab+1, tab+N, best);
    while (occupied<B || j<=N)
    {
        if (tab[j].weight+occupied<=B)
        {
            cout<<tab[j].nr<<" ";
            occupied=occupied+tab[j].weight;
        }
        j++;
    }
}
int main()
{
    cout<<"Podaj pojemnosc plecaka"<<endl;
    cin>>B;
    cout<<"Podaj ilosc rzeczy"<<endl;
    cin>>N;
    Tthing* tab;
    tab=new Tthing[N+1];
    cout<<"W "<<N<<" linijkach podaj wartosc i wage przedmiotow w podanej kolejnosci"<<endl;
    for (i=1; i<=N; i++)
    {
        int tmp, tmp2;
        cin>>tmp;
        cin>>tmp2;
        tab[i].nr=i;
        tab[i].price=tmp;
        tab[i].weight=tmp2;
    }
    cout<<"Stosunek cena/waga jako kryterium"<<endl;
    backpack_best(tab, N, B);
return 0;
}
