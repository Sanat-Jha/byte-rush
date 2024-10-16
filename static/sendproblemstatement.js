document.getElementById('imageUpload').addEventListener('change', function(event) {
    const previewImage = document.getElementById('previewImage');
    const sendButton = document.getElementById('sendButton');
    
    const file = event.target.files[0];
    
    if (file) {
        const reader = new FileReader();
        
        reader.onload = function(e) {
            previewImage.src = e.target.result;
            previewImage.style.display = 'block';
        };
        
        reader.readAsDataURL(file);
        sendButton.disabled = false;
    }
});

document.getElementById('sendButton').addEventListener('click', function() {
    alert('Image sent successfully!');
});

document.getElementById('imageUpload').addEventListener('change', function(event) {
    const previewImage = document.getElementById('previewImage');
    const sendButton = document.getElementById('sendButton');
    
    const file = event.target.files[0];
    
    if (file) {
        const reader = new FileReader();
        
        reader.onload = function(e) {
            previewImage.src = e.target.result;
            previewImage.style.display = 'block';
        };
        
        reader.readAsDataURL(file);
        sendButton.disabled = false;
    }
});

document.getElementById('sendButton').addEventListener('click', function() {
    const fileInput = document.getElementById('imageUpload');
    const file = fileInput.files[0];

    if (file) {
        const formData = new FormData();
        formData.append('image', file);

        fetch(window.location.href, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken') // Add CSRF token to ensure secure requests
            },
            body: formData
        })
        .then(response => {
            if (response.ok) {
                return response.text();
            } else {
                throw new Error('Error in sending the image.');
            }
        })
        .then(data => {
            alert(data);  // Show the response message, e.g., "Email sent successfully!"
        })
        .catch(error => {
            alert('Failed to send image: ' + error.message);
        });
    } else {
        alert('Please upload an image before sending.');
    }
});

// Function to get the CSRF token from the cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Check if this cookie string begins with the name we want
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
