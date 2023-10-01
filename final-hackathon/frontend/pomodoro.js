document.addEventListener("DOMContentLoaded", function () {
    const timerDisplay = document.getElementById("timer");
    const startButton = document.getElementById("start");
    const stopButton = document.getElementById("stop");
    const resetButton = document.getElementById("reset");
    const workDurationInput = document.getElementById("work-duration");
    const breakDurationInput = document.getElementById("break-duration");

    let timer;
    let minutes = parseInt(workDurationInput.value);
    let seconds = 0;
    let isRunning = false;

    const timerSound = new Audio('achievement-bell.mp3');

    function updateDisplay() {
        timerDisplay.textContent = `${minutes.toString().padStart(2, "0")}:${seconds.toString().padStart(2, "0")}`;
    }

    function completeSession() {
        clearInterval(timer);
        isRunning = false;
        
        // Play the sound
        timerSound.play();
    }

    function startTimer() {
        if (!isRunning) {
            isRunning = true;
            timer = setInterval(function () {
                if (seconds === 0) {
                    if (minutes === 0) {
                        completeSession(); 
                        resetTimer(); 
                        return; 
                    } else {
                        minutes--;
                        seconds = 59;
                    }
                } else {
                    seconds--;
                }
                updateDisplay();
            }, 1000);
        }
    }

    function stopTimer() {
        if (isRunning) {
            clearInterval(timer);
            isRunning = false;
        }
    }

    function resetTimer() {
        stopTimer();
        minutes = parseInt(workDurationInput.value); 
        seconds = 0;
        updateDisplay();
    }

    startButton.addEventListener("click", startTimer);
    stopButton.addEventListener("click", stopTimer);
    resetButton.addEventListener("click", resetTimer);

    workDurationInput.addEventListener("change", function () {
        minutes = parseInt(workDurationInput.value);
        resetTimer(); 
    });

    breakDurationInput.addEventListener("change", function () {
        
    });

    updateDisplay();
});
