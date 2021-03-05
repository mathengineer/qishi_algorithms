int rangeBitwiseAnd(int m, int n){
    if (n>m) {
        return rangeBitwiseAnd(m>>1, n>>1)<<1;
    } 
    else {
        return m;
    }
}