// auth.js

// Validate login form
const loginForm = document.getElementById('login-form');
if (loginForm) {
  loginForm.addEventListener('submit', function (e) {
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value;
    if (!username || !password) {
      alert('Please fill out all fields.');
      e.preventDefault();
    }
  });
}

// Validate register form
const registerForm = document.getElementById('register-form');
if (registerForm) {
  registerForm.addEventListener('submit', function (e) {
    const username = document.getElementById('username').value.trim();
    const email = document.getElementById('email').value.trim();
    const password1 = document.getElementById('password1').value;
    const password2 = document.getElementById('password2').value;

    if (!username || !email || !password1 || !password2) {
      alert('Please fill out all fields.');
      e.preventDefault();
    } else if (password1 !== password2) {
      alert('Passwords do not match.');
      e.preventDefault();
    }
  });
}
