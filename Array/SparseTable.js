class SparseTable {
    constructor(arr){
        this.arr = arr
        this.n = this.arr.length
        this.table = new Array(this.n)
        this.Build_SparseTable()
    }
    Build_SparseTable(){
        for(let i= 0; i < this.n; i++){
            this.table[i]= new Array(this.n)
        }
        
        for(let j = 1; (1 << j) <= this.n; j++){
            for(let i = 0; i + (1 << j) - 1 < this.n; i++){
                if (this.arr[this.table[i][j - 1]] < this.arr[this.table[i + (1 << (j - 1))][j - 1]]) {
                    this.table[i][j] = this.table[i][j - 1];
                } else {
                    this.table[i][j] = this.table[i + (1 << (j - 1))][j - 1];
                }
            }
        }
        
    }
    
    queryMin(left, right) {
        const k = Math.floor(Math.log2(right - left + 1));
        if (this.arr[this.table[left][k]] <= this.arr[this.table[right - (1 << k) + 1][k]]) {
            return this.arr[this.table[left][k]];
        } else {
            return this.arr[this.table[right - (1 << k) + 1][k]];
        }
    }

}

const a = new SparseTable([7, 2, 3, 0, 5, 10, 3, 12, 18])

console.log(a.queryMin(3,8))