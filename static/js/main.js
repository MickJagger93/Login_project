document.addEventListener("DOMContentLoaded", function() {
    
    const passwordInput = document.getElementById("password-input");
    const toggleBtn = document.getElementById("toggle-password");
    if (passwordInput && toggleBtn) {
        let visible = false;
        toggleBtn.addEventListener("click", function() {
            visible = !visible;
            passwordInput.type = visible ? "text" : "password";
            toggleBtn.textContent = visible ? "🙈" : "👁️";
        });
    }

    const newPasswordInput = document.getElementById("new-password-input");
    const toggleNewPassword = document.getElementById("toggle-new-password");
    if (newPasswordInput && toggleNewPassword) {
        let newVisible = false;
        toggleNewPassword.addEventListener("click", function() {
            newVisible = !newVisible;
            newPasswordInput.type = newVisible ? "text" : "password";
            toggleNewPassword.textContent = newVisible ? "🙈" : "👁️";
        });
    }

    const confirmPasswordInput = document.getElementById("confirm-password-input");
    const toggleConfirmPassword = document.getElementById("toggle-confirm-password");
    if (confirmPasswordInput && toggleConfirmPassword) {
        let confirmVisible = false;
        toggleConfirmPassword.addEventListener("click", function() {
            confirmVisible = !confirmVisible;
            confirmPasswordInput.type = confirmVisible ? "text" : "password";
            toggleConfirmPassword.textContent = confirmVisible ? "🙈" : "👁️";
        });
    }

    const confirmNewPasswordInput = document.getElementById("confirm-new-password-input");
    const toggleConfirmNewPassword = document.getElementById("toggle-confirm-new-password");
    if (confirmNewPasswordInput && toggleConfirmNewPassword) {
        let confirmNewVisible = false;
        toggleConfirmNewPassword.addEventListener("click", function() {
            confirmNewVisible = !confirmNewVisible;
            confirmNewPasswordInput.type = confirmNewVisible ? "text" : "password";
            toggleConfirmNewPassword.textContent = confirmNewVisible ? "🙈" : "👁️";
        });
    
    }

    const forms = document.querySelectorAll("form.form-style");
    forms.forEach(form => {
        form.addEventListener("submit", function() {
            const spinner = form.querySelector("#spinner");
            if (spinner) {
                spinner.style.display = "block";
            }
            const btn = form.querySelector("button[type='submit']");
            if (btn) {
                btn.disabled = true;
            }
        });
    });

});