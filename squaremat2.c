#include <stdio.h>
int main() 
{
  int i,j,a[100][100],n,mul=1,v=1,k=0,dia;
  scanf("%d",&n);
  for(i=0;i<n;i++)
  {
    for(j=0;j<n;j++)
    {
      scanf("%d",&a[i][j]);
    }
     printf("\n");
  }
  for(i=0;i<n;i++)
  {
    for(j=0;j<n;j++)
    {
      if(i==j)
      {
        mul=mul*a[i][j];
      }
      if(i==0+k&j==n-k-1)
      {
        k++;
        v=v*a[i][j];
      }
    }
  }
  
  dia=mul+v;
  printf("%d",dia);
  
  return 0;
}
