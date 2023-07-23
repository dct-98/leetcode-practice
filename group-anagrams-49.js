/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
  
    let strMap = {};

    for (let str of strs) {
        let chars = Array.from(str).sort().join();

        if(!strMap.hasOwnProperty(chars)) {
            strMap[chars] = [];
        }
        strMap[chars].push(str);
    }

    return Object.values(strMap);
};
