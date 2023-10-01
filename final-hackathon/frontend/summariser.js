const pdfInput = document.getElementById('pdf-input');
const selectedFileName = document.getElementById('selected-file-name');
const generateButton = document.getElementById('generate-button');
const downloadLink = document.getElementById('download-link');

pdfInput.addEventListener('change', (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
        selectedFileName.textContent = `Selected File: ${selectedFile.name}`;
        generateButton.style.display = 'block';
        downloadLink.style.display = 'none';
    } else {
        selectedFileName.textContent = '';
        generateButton.style.display = 'none';
        downloadLink.style.display = 'none';
    }
});

generateButton.addEventListener('click', () => {
    const selectedFile = pdfInput.files[0];
    if (!selectedFile) {
        return;
    }

    const extractedText = 'This is the extracted text from the PDF.';
    const blob = new Blob([extractedText], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    downloadLink.href = url;
    downloadLink.style.display = 'block';
});