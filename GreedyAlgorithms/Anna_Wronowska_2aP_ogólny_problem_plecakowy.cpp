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
bool by_price(Tthing a, Tthing b)
{
    return a.price>b.price;
}
bool by_weight (Tthing a, Tthing b)
{
    return a.weight<b.weight;
}
bool best (Tthing a, Tthing b)
{
    return a.price*b.weight>b.price*a.weight;
}
void backpack_by_price(Tthing tab[], int N)
{
    j=0;
    int occupied=0;
    sort(tab, tab+N, by_price);
    while (occupied<B || j<N)
    {
        if (tab[j].weight+occupied<=B)
        {
            cout<<tab[j].nr<<" ";
            occupied=occupied+tab[j].weight;
        }
        else
        {
            j++;
        }
    }
    cout<<endl;
}
void backpack_by_weight(Tthing tab[], int N)
{
    j=0;
    int occupied=0;
    sort(tab, tab+N, by_weight);
    while (occupied<B || j<N)
    {
        if (tab[j].weight+occupied<=B)
        {
            cout<<tab[j].nr<<" ";
            occupied=occupied+tab[j].weight;
        }
        else
        {
            j++;
        }
    }
    cout<<endl;
}
void backpack_best(Tthing tab[], int N)
{
    j=0;
    int occupied=0;
    sort(tab, tab+N, best);
    while (occupied<B || j<N)
    {
        if (tab[j].weight+occupied<=B)
        {
            cout<<tab[j].nr<<" ";
            occupied=occupied+tab[j].weight;
        }
        else
        {
            j++;
        }
    }
    cout<<endl;
}
int main()
{
    cout<<"Podaj pojemnosc plecaka"<<endl;
    cin>>B;
    cout<<"Podaj ilosc rzeczy"<<endl;
    cin>>N;
    Tthing* tab;
    tab=new Tthing[N];
    cout<<"W "<<N<<" linijkach podaj wartosc i wage przedmiotow w podanej kolejnosci"<<endl;
    for (i=0; i<N; i++)
    {
        int tmp, tmp2;
        cin>>tmp;
        cin>>tmp2;
        tab[i].nr=i+1;
        tab[i].price=tmp;
        tab[i].weight=tmp2;
    }
    cout<<"Cena jako kryterium"<<endl;
    backpack_by_price(tab, N);
    cout<<"Waga jako kryterium"<<endl;
    backpack_by_weight(tab, N);
    cout<<"Stosunek cena/waga jako kryterium"<<endl;
    backpack_best(tab, N);
return 0;
}
