// Given two non-empty arrays of intergers, write a function that determines whether the second array is a subsequence of the firt one
// A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they apper in the array
// For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and so do the number [2, 4].
// Note that a single number in an array and the array itself are both valid subsequences of the array

// Solution is Big O(n) where n = array.length
// Even though we have a for > while here, since the while block will run at most n times becaus

function isValidSubsequence(array, sequence) {
    let arrIndex = 0;
    for (let seqIndex = 0; seqIndex < sequence.length; seqIndex++) {
        const seqElement = sequence[seqIndex]; 

        while (seqElement !== array[arrIndex]) {
            arrIndex++;
            if (arrIndex >= array.length) {
                return false;
            }
        }
        
        arrIndex++;
    }

    return true;
}

const result = isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10])

console.log(result);