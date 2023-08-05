/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    
    // Checks if equal length
    if (s.length != t.length) {
        return false;
    }

    // Initialize map
    let countMap = {};

    // Assign keys for all char inside s,t
    for (let i = 0; i < s.length; i++) {
        countMap [s[i]] = (countMap[s[i]] || 0) + 1;
        countMap [s[i]] = (countMap[s[i]] || 0) - 1;
    }

    // Checks if all key values are 0
    for (let key in countMap) {
        if (countMap[key] !== 0) {
            return false;
        }
    }

    return true;

};

console.log(isAnagram("anagram", "nagaram"));
console.log(isAnagram("rat","car"));
