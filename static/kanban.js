var toDoList = document.getElementById("to-do-list");
var inProgressList = document.getElementById("in-progress-list");
var doneList = document.getElementById("done-list");
var historyList = document.getElementById("history-list");

function allowDrop(ev) {
ev.preventDefault();
}

function drag(ev) {
ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev, target) {
ev.preventDefault();
var data = ev.dataTransfer.getData("text");
var taskItem = document.getElementById(data);
var taskList = document.getElementById(target + "-list");
taskList.appendChild(taskItem);
}

function removeTask(taskId) {
    var url = 'remove_task/' + taskId + '/';
    window.location.href = url;
}

function toggleHistory() {
var historyList = document.getElementById("history-list");
if (historyList.style.display === "none") {
historyList.style.display = "block";
} else {
historyList.style.display = "none";
}
}

var historyHeader = document.querySelector("#history-column h2");
historyHeader.addEventListener("click", toggleHistory);