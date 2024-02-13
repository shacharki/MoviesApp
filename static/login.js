$(document).ready(function() {
    $('#login-form').submit(function(event) {
        event.preventDefault();
        
        var username = $('#username').val();
        var password = $('#password').val();
        
        // Perform validation checks
        if (!username || !password) {
            showError("Please fill in all fields.");
            return;
        }
        
        // Submit the form
        $(this)[0].submit();
    });

    // Function to display error message
    function showError(message) {
        alert(message);
    }
});
