
//import { exec } from 'child_process';

document.getElementById('fileInput').addEventListener('change', function(event) {
    const file = event.target.files[0];

    
    const validTypes = ['image/jpeg', 'image/jpg', 'image/png'];
    if (file && validTypes.includes(file.type)) {
        const reader = new FileReader();
        reader.onload = function(e) {
            console.log(e.target.result);
            const arrayBuffer = e.target.result;
            const byteArray = new Uint8Array(arrayBuffer);
            console.log(byteArray);
            runPython();
            const preview = document.getElementById('preview');
            preview.innerHTML = `<img src="${e.target.result}" alt="Image Preview">`;

            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = e.target.result;
            downloadLink.download = file.name;
            downloadLink.style.display = 'inline-block';
            downloadLink.textContent = 'Download Image';
        }
        reader.readAsDataURL(file);
    } else {
        alert('Please upload a valid image file (JPEG, JPG, PNG).');
    }
    
});


function runPython() {
    // runPython.js

exec('python backend.py', (error, stdout, stderr) => {
    if (error) {
        console.error(`Error executing Python script: ${error}`);
        return;
    }
    if (stderr) {
        console.error(`Error output: ${stderr}`);
        return;
    }
    console.log(`Python output: ${stdout}`);
});

}