function FindMostOccurance(arr,k){
 const mp = {}
 for(let i=0;i<arr.length;i++){
    if(arr[i] in mp){
        mp[arr[i]]+=1
    }
    else{
        mp[arr[i]] = 1
    }
 }
 const entries  = Object.entries(mp)
 entries.sort((a,b)=>b[1]-a[1])
 const occur = entries.slice(0,k)
 occur.map((item)=> console.log(item[0]))
}
FindMostOccurance([7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9],4)