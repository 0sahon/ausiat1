let arrayContainer = [];

function myTask3js(string) {
    for (let i = 1; i <= string; i++) {

        if (i % 2 == 0 && i % 3 == 0 && i % 5 == 0) {
            arrayContainer.push("yu-gi-oh");

        } else if (i % 3 == 0 && i % 5 == 0) {
            arrayContainer.push("gi-oh");

        } else if (i % 2 == 0 && i % 3 == 0) {
            arrayContainer.push("yu-gi");

        } else if (i % 2 == 0 && i % 5 == 0) {
            arrayContainer.push("yu-oh");

        } else if (i % 2 == 0) {
            arrayContainer.push("yu");

        } else if (i % 3 == 0) {
            arrayContainer.push("gi");

        } else if (i % 5 == 0) {
            strArr.push("oh");

        } else {
            strArr.push(i);
        }
    }
    return strArr;
}
console.log(myTask3js(30));