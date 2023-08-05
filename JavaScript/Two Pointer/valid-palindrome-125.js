/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {


    // Create new extracting only alphanumeric and lowering the case
    const testString = s.replace(/[^a-z0-9]/ig, '').toLowerCase();

    // Left pointer
    let left = 0;

    // Right pointer
    let right = testString.length - 1;


    // Loop to run while left pointer is less than right pointer
    while (left < right) {

        // If statement to return false if the two characters are not equal to eachother
        if (testString[left] != testString[right]) {
            return false;
        }
        left++;
        right--;
    }

    return true;
};