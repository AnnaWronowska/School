#include <iostream>
using namespace std;
struct Tthing
{
    int nr;
    int price;
    int weight;
};
int main()
{
    int N, B, i, j, pom;
    cout<<"Podaj wielkosc plecaka"<<endl;
    cin>>B;
    cout<<"Podaj ilosc rzeczy"<<endl;
    cin>>N;
    int ptab[N+1][B+1];
    int qtab[N+1][B+1];
    for (i=0; i<=N; i++)
    {
        for (j=0; j<=B; j++)
        {
            ptab[i][j]=0;
            qtab[i][j]=0;
        }
    }
    Tthing* tab;
    tab=new Tthing[N];
    cout<<"W "<<N<<" linijkach podaj ceny i wagi rzeczy (cena waga)"<<endl;
    for (i=1; i<=N; i++)
    {
        cin>>tab[i].price;
        cin>>tab[i].weight;
        tab[i].nr=i;
    }
    for (i=1; i<=N; i++)
    {
        for (j=1; j<=B; j++)
        {
            if ((ptab[i][j-tab[i].weight]+tab[i].price)>ptab[i-1][j] && tab[i].weight<=j)
            {
                ptab[i][j]=ptab[i][j-tab[i].weight]+tab[i].price;
                qtab[i][j]=1;
            }
            else
            {
                ptab[i][j]=ptab[i-1][j];
                qtab[i][j]=0;
            }
        }
     }
     cout<<"Wartosc plecaka "<<ptab[N][B]<<endl;
     cout<<"Wzieto nastepujace rzeczy ";
     int y=B;
     int x=N;
     while (y>0)
     {
         if (qtab[x][y]==1)
         {
             cout<<x<<" ";
             y=y-tab[x].weight;
         }
         x--;
     }
return 0;
}
