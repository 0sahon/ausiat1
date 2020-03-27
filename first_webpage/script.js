var my_name = "Airhienbuwa Osahon";
var courses;
courses = ["HTML", "CSS", "JAVASCRIPT", "NODE.JS", "PYTHON", "DESIGN"];
var numOfCourses = courses.length;
var numDisplay = "";
for (var i = 1; i <= 200; i++) {
    if (numOfCourses % 2 == 1) {
        if (i % 2 == 1) {
            if (i == 200 - 1) {
                break;
            }
            numDisplay += i + 2 + " ";
        }
    }
}

console.log(numDisplay);