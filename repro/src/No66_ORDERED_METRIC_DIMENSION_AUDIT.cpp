// Independent ordered resolving-set comparison, Gamma_9.
// For metric dimension (ordered vectors), supersets of resolving sets also resolve.
#include <array>
#include <cstdio>
#include <vector>
#include <cstdint>
using namespace std;
int main(){
 constexpr int n=9;vector<int> vs;
 for(int v=0;v<(1<<n);v++)if((v&(v<<1))==0)vs.push_back(v);
 if(vs.size()!=89)return 9;
 uint8_t D[89][89];for(int a=0;a<89;a++)for(int b=0;b<89;b++){
   int x=vs[a]^vs[b],d=0;while(x){x&=x-1;d++;}D[a][b]=d;
 }
 static uint32_t stamp[10000]={};uint32_t current=0;long long tested=0;
 // First independently exclude every ordered resolving set of size three.
 for(int a=0;a<87;a++)for(int b=a+1;b<88;b++)for(int c=b+1;c<89;c++){
   ++tested; ++current; bool good=true;
   for(int v=0;v<89;v++){
     unsigned code=100*D[a][v]+10*D[b][v]+D[c][v];
     if(stamp[code]==current){good=false;break;}stamp[code]=current;
   }
   if(good){printf("METRIC3_FOUND %d %d %d\n",vs[a],vs[b],vs[c]);return 10;}
 }
 printf("ORDERED_METRIC_DIM n=9 k=3 result=NONE tested=%lld\n",tested);
 if(tested!=113564) return 11;
 tested=0;
 for(int a=0;a<86;a++)for(int b=a+1;b<87;b++)for(int c=b+1;c<88;c++)for(int d=c+1;d<89;d++){
   ++tested; ++current;bool good=true;
   for(int v=0;v<89;v++){
     unsigned code=1000*D[a][v]+100*D[b][v]+10*D[c][v]+D[d][v];
     if(stamp[code]==current){good=false;break;}stamp[code]=current;
   }
   if(good){printf("METRIC4_FOUND %d %d %d %d\n",vs[a],vs[b],vs[c],vs[d]);return 0;}
 }
 printf("ORDERED_METRIC_DIM n=9 k=4 result=NONE tested=%lld\n", tested);
 return tested==2441626?0:11;
}
