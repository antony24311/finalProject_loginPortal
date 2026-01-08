// External script to avoid inline scripts
// Put any DOM-manipulating code here. Example: log and add helpers.
document.addEventListener('DOMContentLoaded', () => {
  console.log('External script loaded');
});

// Example helper exposed to window
window.__authHelpers = {
  getToken() {
    return localStorage.getItem('access_token');
  }
};
