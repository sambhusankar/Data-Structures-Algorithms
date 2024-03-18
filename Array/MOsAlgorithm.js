function MOsAlgorithm(arr,query){
     for(let i = 0; i < query.length; i++){
         var sum = 0;
         for (let j = query[i][0]; j < query[i][1]+1; j++){
             sum += arr[j];
         }
         console.log(sum)
     }
 }
MOsAlgorithm([1, 1, 2, 1, 3, 4, 5, 2, 8], [[0, 4], [1, 3], [2, 4]])
// function MOsAlgorithm(arr, query) {
//     for (let i = 0; i < query.length; i++) {
//         var sum = 0;
//         for (let j = query[i][0]; j < query[i][1] + 1; j++) {
//             sum += arr[j];
//         }
//         console.log(sum);
//     }
// }

// MOsAlgorithm([1, 1, 2, 1, 3, 4, 5, 2, 8], [[0, 4], [1, 3], [2, 4]]);
