// Independent exhaustive audit for Gamma_9, k=6, 2026-11-12.
// Different code representation from the source: 7-ary distance histograms.
// A sum of powers of seven is unique for <=6 landmarks (no digit carry).
#include <array>
#include <atomic>
#include <bit>
#include <chrono>
#include <cstdint>
#include <cstdio>
#include <vector>
#include <omp.h>
using std::array;using std::vector;
static constexpr int n=9,k=6;
struct Search {
  vector<int> vertices;
  array<array<uint32_t,89>,89> add{};
  uint32_t signatures[89]{};
  uint32_t slot_key[512]{};
  uint32_t slot_epoch[512]{};
  uint32_t epoch=0;
  bool selected[89]{};
  unsigned long long tested=0;
  bool collision_free() {
    ++tested;
    ++epoch;
    for (int x=0;x<89;++x) if (!selected[x]) {
      uint32_t value=signatures[x];
      unsigned h=(value*2654435761U) >> 23;
      while(slot_epoch[h]==epoch && slot_key[h]!=value)
        h=(h+1)&511;
      if(slot_epoch[h]==epoch) return false;
      slot_epoch[h]=epoch;
      slot_key[h]=value;
    }
    return true;
  }
  bool search(int next,int depth) {
    if(depth==k) return collision_free();
    int remain=k-depth;
    for(int j=next;j<=89-remain;j++) {
      selected[j]=true;
      for(int x=0;x<89;x++) signatures[x]+=add[x][j];
      bool found=search(j+1,depth+1);
      for(int x=0;x<89;x++) signatures[x]-=add[x][j];
      selected[j]=false;
      if(found) return true;
    }
    return false;
  }
};
int main(){
  vector<int> words;
  for(int mask=0;mask<512;mask++)if((mask&(mask<<1))==0) words.push_back(mask);
  if(words.size()!=89) return 10;
  array<uint32_t,10> power{};power[0]=1;
  for(int d=1;d<10;d++)power[d]=power[d-1]*7;
  array<array<uint32_t,89>,89> contribution{};
  for(int i=0;i<89;i++)for(int j=0;j<89;j++){
    int diff=words[i]^words[j];
    unsigned count=0;
    for(;diff;diff&=diff-1) count++;
    contribution[i][j]=power[count];
  }
  unsigned long long total=0;
  int success=0;
  auto start=std::chrono::steady_clock::now();
  #pragma omp parallel for schedule(dynamic,1) reduction(+:total) reduction(|:success) num_threads(5)
  for(int first=0;first<=89-k;first++) {
    Search s;
    s.add=contribution;
    s.selected[first]=true;
    for(int v=0;v<89;v++)s.signatures[v]=contribution[v][first];
    if(s.search(first+1,1))success=1;
    total+=s.tested;
  }
  double elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
  printf("INDEPENDENT_BASE7 n=9 N=89 k=6 found=%d tested=%llu elapsed=%.3f sec\n",success,total,elapsed);
  if (total!=581106988ULL) return 11;
  return success?12:0;
}
