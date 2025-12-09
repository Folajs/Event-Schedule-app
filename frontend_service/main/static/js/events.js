// events.js

document.addEventListener('DOMContentLoaded', function () {
  const eventForm = document.getElementById('event-form');
  if (eventForm) {
    eventForm.addEventListener('submit', async function (e) {
      e.preventDefault();

      const title = document.getElementById('title').value;
      const description = document.getElementById('description').value;
      const location = document.getElementById('location').value;
      const start_time = document.getElementById('start_time').value;
      const end_time = document.getElementById('end_time').value;

      const response = await fetch("http://localhost:8002/api/events/create/", {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, description, location, start_time, end_time })
      });

      if (response.ok) {
        alert('Event created!');
        window.location.reload();
      } else {
        alert('Error creating event');
      }
    });
  }
});

// function openEventModal() {
//   const modal = document.getElementById("event-modal");
//   if (modal) {
//     modal.classList.remove("hidden");
//   }
// }

// function closeEventModal() {
//   const modal = document.getElementById("event-modal");
//   if (modal) {
//     modal.classList.add("hidden");
//   }
// }

// window.addEventListener("click", function (event) {
//   const modal = document.getElementById("event-modal");
//   if (event.target === modal) {
//     modal.classList.add("hidden");
//   }
// });

// document.addEventListener('DOMContentLoaded', function () {
//   const eventForm = document.getElementById('event-form');
//   if (eventForm) {
//     eventForm.addEventListener('submit', async function (e) {
//       e.preventDefault();

//       const title = document.getElementById('title').value;
//       const description = document.getElementById('description').value;
//       const location = document.getElementById('location').value;
//       const start_time = document.getElementById('start_time').value;
//       const end_time = document.getElementById('end_time').value;

//       const response = await fetch('http://localhost:8002/api/events/', {
//         method: 'POST',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify({ title, description, location, start_time, end_time })
//       });

//       if (response.ok) {
//         alert('Event created!');
//         window.location.reload();
//       } else {
//         alert('Error creating event');
//       }
//     });
//   }
// });

