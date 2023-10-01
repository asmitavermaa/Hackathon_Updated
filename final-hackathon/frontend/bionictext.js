const fileInput = document.getElementById('file-input');
const fileNameDisplay = document.getElementById('file-name');
const generateButton = document.getElementById('generate-button');
const successMessage = document.getElementById('success-message');
const downloadButton = document.getElementById('download-button');

fileInput.addEventListener('change', () => {
    const selectedFile = fileInput.files[0];
    if (selectedFile) {
        fileNameDisplay.textContent = `Selected file: ${selectedFile.name}`;
    } else {
        fileNameDisplay.textContent = '';
    }
});

generateButton.addEventListener('click', () => {
    successMessage.style.display = 'block';
    downloadButton.style.display = 'block';
});