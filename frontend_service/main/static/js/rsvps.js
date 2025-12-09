// rsvps.js

document.addEventListener('DOMContentLoaded', function () {
  // Submit RSVP
  const rsvpForm = document.getElementById('rsvp-form');
  if (rsvpForm) {
    rsvpForm.addEventListener('submit', async function (e) {
      e.preventDefault();

      const event_id = document.getElementById('event_id').value;
      const name = document.getElementById('name').value;
      const email = document.getElementById('email').value;

      const response = await fetch('http://localhost:8003/api/rsvps/create/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ event_id, name, email, response: "Yes" })
      });

      if (response.ok) {
        alert('RSVP submitted!');
        window.location.reload();
      } else {
        alert('Error submitting RSVP');
      }
    });
  }

  // Fetch events to display on RSVP page
  const rsvpList = document.getElementById('rsvp-list');
  if (rsvpList) {
    fetch('http://localhost:8002/api/events/')
      .then(response => response.json())
      .then(events => {
        rsvpList.innerHTML = '';
        events.forEach(event => {
          const li = document.createElement('li');
          li.innerHTML = `
            <strong>${event.title}</strong><br>
            ${event.description}<br>
            ${event.location}<br>
            ${new Date(event.start_time).toLocaleString()} - ${new Date(event.end_time).toLocaleString()}
          `;
          rsvpList.appendChild(li);
        });
      })
      .catch(err => {
        console.error('Error loading events on RSVP page:', err);
      });
  }
});


// document.addEventListener('DOMContentLoaded', function () {
//   const rsvpForm = document.getElementById('rsvp-form');
//   if (rsvpForm) {
//     rsvpForm.addEventListener('submit', async function (e) {
//       e.preventDefault();

//       const event_id = document.getElementById('event_id').value;
//       const name = document.getElementById('name').value;
//       const email = document.getElementById('email').value;

//       const response = await fetch('http://localhost:8003/api/rsvps/', {
//         method: 'POST',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify({ event: event_id, name, email })
//       });

//       if (response.ok) {
//         alert('RSVP submitted!');
//         window.location.reload();
//       } else {
//         alert('Error submitting RSVP');
//       }
//     });
//   }
// });
