// Independent finite cross-check (new for v0.4): BFS metrics and base-7 histograms.
// Enumeration covers ALL k smaller than the first successful multiset size.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <queue>
#include <unordered_set>
#include <vector>
using namespace std;
static bool nextset(vector<int>& a, int n) {
  const int k=(int)a.size();
  for (int i=k-1;i>=0;--i) {
    if (a[i]<n-k+i){++a[i];for(int j=i+1;j<k;j++)a[j]=a[j-1]+1;return true;}
  }
  return false;
}
static string binary(int x,int n){string s(n,'0');for(int i=0;i<n;i++)if(x&(1<<(n-1-i)))s[i]='1';return s;}
struct Cube{
 int n,N;
 vector<int> words;
 vector<vector<unsigned char>> d;
 Cube(int m):n(m){
   for(int x=0;x<(1<<n);x++) if(!(x&(x>>1)))words.push_back(x);
   N=words.size();d.assign(N,vector<unsigned char>(N,255));
   vector<int> ind(1<<n,-1);
   for(int i=0;i<N;i++)ind[words[i]]=i;
   for(int i=0;i<N;i++){
     queue<int>q;q.push(i);d[i][i]=0;
     while(!q.empty()){
       int v=q.front();q.pop();
       for(int b=0;b<n;b++){
         int y=words[v]^(1<<b),j=ind[y];
         if(j>=0&&d[i][j]==255){d[i][j]=d[i][v]+1;q.push(j);}
       }
     }
   }
   for(int i=0;i<N;i++)for(int j=0;j<N;j++){
     if(d[i][j]!=__builtin_popcount((unsigned)(words[i]^words[j]))){cerr<<"ISOMETRY FAIL";exit(2);}
   }
 }
 bool works(const vector<int>& s,bool unordered){
   unordered_set<uint64_t> seen;seen.reserve(N*2);
   for(int v=0;v<N;v++){
     uint64_t key=0;
     if(unordered){
       static const uint64_t p7[]={1,7,49,343,2401,16807,117649,823543,5764801};
       for(int z:s) key += p7[d[v][z]];
     }else{for(int z:s)key=16*key + 1+d[v][z];}
     if(!seen.insert(key).second)return false;
   }
   return true;
 }
 struct Search{int k;uint64_t count,success;vector<int>first;};
 Search search(int k,bool unordered,bool all_success){
   vector<int>s(k);for(int i=0;i<k;i++)s[i]=i;
   Search r{k,0,0,{}};
   do{
     r.count++;
     if(works(s,unordered)){
       r.success++;if(r.first.empty())r.first=s;
       if(!all_success)break;
     }
   }while(nextset(s,N));
   return r;
 }
};
int main(){
 for(int n=1;n<=8;n++){
   Cube c(n);cout<<"ISOMETRY_PASS n="<<n<<" vertices="<<c.N<<" ordered_pairs="<<c.N*c.N<<"\n";
   for(bool unordered : {true,false}){
     for(int k=0;k<=6;k++){
       if(k>c.N)break;
       bool all_success=(n==8&&unordered&&k==5);
       auto r=c.search(k,unordered,all_success);
       cout<<(unordered?"MD":"DIM")<<" n="<<n<<" k="<<k<<" tested="<<r.count<<" successes="<<r.success;
       if(r.success){cout<<" witness=";for(int z:r.first)cout<<binary(c.words[z],n)<<",";}
       cout<<"\n";
       if(r.success)break;
     }
   }
 }
 cout<<"INDEPENDENT_BFS_FINITE_REPLAY_PASS\n";
}
