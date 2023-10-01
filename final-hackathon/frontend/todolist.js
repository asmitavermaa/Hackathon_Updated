function addTask() {

    var taskText = document.getElementById("new-task").value.trim();

    
    if (taskText !== "") {
    
        var taskItem = document.createElement("li");

    
        var checkbox = document.createElement("input");
        checkbox.type = "checkbox";

    
        var label = document.createElement("label");
        label.textContent = taskText;

    
        taskItem.appendChild(checkbox);
        taskItem.appendChild(label);

        
    

    
        checkbox.addEventListener("change", function () {
            if (checkbox.checked) {
                taskItem.classList.add("completed");
            } else {
                taskItem.classList.remove("completed");
            }
        });

    
        var taskList = document.getElementById("task-list");

    
        taskList.appendChild(taskItem);

    
        document.getElementById("new-task").value = "";
    }
}
