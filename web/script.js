const fileInput = document.getElementById("fileInput");
const fileInfo = document.getElementById("fileInfo");
const sendButton = document.getElementById("sendButton");
const status = document.getElementById("status");

let selectedFile = null;


// When the user chooses a file
fileInput.addEventListener("change", () => {

    selectedFile = fileInput.files[0];

    if (!selectedFile) {
        fileInfo.textContent = "No file selected";
        return;
    }

    const sizeMB = (selectedFile.size / (1024 * 1024)).toFixed(2);

    fileInfo.textContent = `${selectedFile.name} • ${sizeMB} MB`;

    status.textContent = "File ready to send";
});


// When SEND FILE is clicked
sendButton.addEventListener("click", async () => {

    if (!selectedFile) {
        status.textContent = "Please choose a file first";
        return;
    }

    status.textContent = "Sending...";

    const formData = new FormData();

    formData.append("file", selectedFile);

    try {

        const response = await fetch("/upload", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error("Upload failed");
        }

        const result = await response.json();

        status.textContent = `✓ ${result.message}`;

    } catch (error) {

        console.error(error);

        status.textContent = "❌ Transfer failed";

    }

});