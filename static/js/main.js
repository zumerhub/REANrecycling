// main.js
// document.addEventListener('DOMContentLoaded', function() {
//     // Contact Form Submission
//     const contactForm = document.getElementById('contactForm');
//     if (contactForm) {
//         contactForm.addEventListener('submit', function(e) {
//             e.preventDefault();
            
//             const formData = {
//                 name: document.getElementById('name').value,
//                 email: document.getElementById('email').value,
//                 message: document.getElementById('message').value
//             };

//             fetch('/contact/', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json',
//                     'X-CSRFToken': getCsrfToken()
//                 },
//                 body: JSON.stringify(formData)
//             })
//             .then(response => response.json())
//             .then(data => {
//                 if (data.status === 'success') {
//                     showNotification('Message sent successfully!', 'success');
//                     contactForm.reset();
//                 } else {
//                     showNotification('Error sending message. Please try again.', 'error');
//                 }
//             })
//             .catch(error => {
//                 console.error('Error:', error);
//                 showNotification('An error occurred. Please try again.', 'error');
//             });
//         });
//     }




// document.addEventListener("DOMContentLoaded", function () {
//   const contactForm = document.getElementById("contactForm");
//   if (contactForm) {
//       contactForm.addEventListener("submit", function (e) {
//           e.preventDefault();

//           const formData = {
//               name: document.getElementById("name").value,
//               email: document.getElementById("email").value,
//               message: document.getElementById("message").value,
//           };

//           fetch("/api/general/", {
//               method: "POST",
//               headers: {
//                   "Content-Type": "application/json",
//                   "X-CSRFToken": getCsrfToken(),
//               },
//               body: JSON.stringify(formData),
//           })
//           .then(response => response.json().catch(() => ({ success: false, error: "Invalid JSON response" })))
//           .then((data) => {
//               if (data.success) {  // Ensure backend returns "success: true"
//                   showNotification("✅ Message sent successfully!", "success");
//                   contactForm.reset();
//               } else {
//                   showNotification("❌ Error: " + (data.error || "Unknown error"), "error");
//               }
//           })
//           .catch((error) => {
//               console.error("Error:", error);
//               showNotification("❌ An error occurred. Please try again.", "error");
//           });
//       });
//   }

//   function getCsrfToken() {
//       const csrfInput = document.querySelector("input[name='csrfmiddlewaretoken']");
//       return csrfInput ? csrfInput.value : "";
//   }

//   function showNotification(message, type = "info") {
//       alert(message);
//   }






// function showNotification(message, type) {
//   let notification = document.createElement("div");
//   notification.innerText = message;
//   notification.className = `alert alert-${type === "success" ? "success" : "danger"} text-center`;
  
//   // Style the notification
//   notification.style.padding = "15px";
//   notification.style.margin = "10px";
//   notification.style.zIndex = "1050";
//   notification.style.position = "fixed";
//   notification.style.top = "70px"; // Adjust this value based on your navbar height
//   notification.style.left = "50%";
//   notification.style.transform = "translateX(-50%)";
//   notification.style.width = "fit-content";
//   notification.style.maxWidth = "90%"; // Ensure it doesn't get too wide
//   notification.style.borderRadius = "5px";
//   notification.style.boxShadow = "0px 4px 6px rgba(0, 0, 0, 0.1)";
//   notification.style.backgroundColor = type === "success" ? "#28a745" : "#dc3545";
//   notification.style.color = "white";

//   document.body.appendChild(notification);

//   setTimeout(() => {
//       notification.remove();
//   }, 3000); // Hide after 3 seconds
// }





// document.getElementById("contactForm").addEventListener("submit", function(event) {
//   event.preventDefault();

//   let formData = new FormData(this);
//   let csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;

//   fetch("http://127.0.0.1:8000/api/general/", {
//       method: "POST",
//       headers: {
//           "X-CSRFToken": csrfToken
//       },
//       body: formData
//   })
//   .then(response => response.json())
//   .then(data => {
//       if (data.success) {
//           showNotification("✅ Success: Your message has been sent!", "success");
//           document.getElementById("contactForm").reset();
//       } else {
//           showNotification("❌ Error: " + (data.error || "Failed to send message. Please try again."), "error");
//       }
//   })
//   .catch(error => {
//       console.error("Fetch Error:", error);
//       showNotification("⚠️ Error: A network error occurred. Please try again later.", "error");
//   });
// });


      

  document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');
    const formResponse = document.getElementById('formResponse');
    
    contactForm.addEventListener('submit', function(e) {
      e.preventDefault();
      
      const formData = new FormData(contactForm);
      
      fetch('http://localhost:8000/api/general/', {
        method: 'POST',
        body: formData,
        headers: {
          'X-Requested-With': 'XMLHttpRequest',
        }
      })
      .then(response => response.json())
      .then(data => {
        if (data.status === 'success') {
          formResponse.innerHTML = '<div class="alert alert-success">Your message has been sent successfully!</div>';
          contactForm.reset();
        } else {
          let errorMessage = '<div class="alert alert-danger"><ul>';
          for (const [field, errors] of Object.entries(data.errors)) {
            errors.forEach(error => {
              errorMessage += `<li>${field}: ${error}</li>`;
            });
          }
          errorMessage += '</ul></div>';
          formResponse.innerHTML = errorMessage;
        }
      })
      .catch(error => {
        formResponse.innerHTML = '<div class="alert alert-danger">Something went wrong. Please try again later.</div>';
        console.error('Error:', error);
      });
    });
  });



  

    // Paystack Payment Initialization
    // const paymentModal = document.getElementById('paymentModal');
    // if (paymentModal) {
    //     const paymentForm = paymentModal.querySelector('form');
    //     paymentForm.addEventListener('submit', function(e) {
    //         e.preventDefault();
            
    //         const amount = document.getElementById('paymentAmount').value;
    //         const email = document.getElementById('paymentEmail').value;

    //         // Validate inputs
    //         if (!amount || !email) {
    //             showNotification('Please fill in all payment details.', 'error');
    //             return;
    //         }

    //         // Disable submit button to prevent multiple submissions
    //         const submitBtn = paymentForm.querySelector('button[type="submit"]');
    //         submitBtn.disabled = true;
    //         submitBtn.innerHTML = 'Processing...';

    //         // Initiate Paystack payment
    //         fetch('/initiate-payment/', {
    //             method: 'POST',
    //             headers: {
    //                 'Content-Type': 'application/json',
    //                 'X-CSRFToken': getCsrfToken()
    //             },
    //             body: JSON.stringify({ 
    //                 amount: parseFloat(amount), 
    //                 email: email 
    //             })
    //         })
    //         .then(response => response.json())
    //         .then(data => {
    //             if (data.status === 'success') {
    //                 // Redirect to Paystack payment page
    //                 window.location.href = data.authorization_url;
    //             } else {
    //                 showNotification(data.message || 'Payment initialization failed.', 'error');
    //                 submitBtn.disabled = false;
    //                 submitBtn.innerHTML = 'Pay Now';
    //             }
    //         })
    //         .catch(error => {
    //             console.error('Payment Error:', error);
    //             showNotification('Network error. Please try again.', 'error');
    //             submitBtn.disabled = false;
    //             submitBtn.innerHTML = 'Pay Now';
    //         });
    //     });
    // }

    // // Utility Functions
    // function getCsrfToken() {
    //     const csrfTokenElement = document.querySelector('[name=csrfmiddlewaretoken]');
    //     return csrfTokenElement ? csrfTokenElement.value : '';
    // }

    // function showNotification(message, type = 'info') {
    //     // Create notification element
    //     const notification = document.createElement('div');
    //     notification.className = `alert alert-${type === 'success' ? 'success' : 'danger'} fixed-top text-center`;
    //     notification.textContent = message;
        
    //     // Add to body
    //     document.body.appendChild(notification);

    //     // Remove after 3 seconds
    //     setTimeout(() => {
    //         notification.remove();
    //     }, 3000);
    // }
// });


  // FAQ Toggle Functionality
//   document.querySelectorAll('.faq-question').forEach(question => {
//     question.addEventListener('click', () => {
//         const answer = question.nextElementSibling;
//         const isActive = question.classList.contains('active');
        
//         // Close all FAQs
//         document.querySelectorAll('.faq-question').forEach(q => {
//             q.classList.remove('active');
//             q.nextElementSibling.classList.remove('active');
//         });
        
//         // If the clicked FAQ wasn't active, open it
//         if (!isActive) {
//             question.classList.add('active');
//             answer.classList.add('active');
//         }
//     });
// });




  // About Contact Form 
//   // Wait for the DOM to be fully loaded
// document.addEventListener('DOMContentLoaded', function() {
//     // Select the form inside the contact modal
//     const contactForm = document.querySelector('#contact-us form');
    
//     // Add submit event listener to the form
//     contactForm.addEventListener('submit', function(event) {
//       // Prevent the default form submission
//       event.preventDefault();
      
//       // Collect form data
//       const formData = {
//         name: document.getElementById('name').value,
//         email: document.getElementById('email').value,
//         phone: document.getElementById('phone').value,
//         property: document.getElementById('property').value,
//         message: document.getElementById('message').value
//       };
      
//       // Send data to backend using fetch API
//       fetch('http://127.0.0.1:8000/api/business/contact/', {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json',
//           'X-CSRFToken': getCSRFToken(),
//         },
//         body: JSON.stringify(formData)
//       })
//       .then(response => {
//         if (!response.ok) {
//           throw new Error('Network response was not ok');
//         }
//         return response.json();
//       })
//       .then(data => {
//         // Display success message
//         const modalBody = document.querySelector('#contact-us .modal-body');
//         const originalContent = modalBody.innerHTML;
        
//         modalBody.innerHTML = `
//           <div class="alert alert-success">
//             <h4>Thank you for contacting us!</h4>
//             <p>We've received your message and will get back to you shortly.</p>
//           </div>
//         `;
        
//         // Reset form after 3 seconds and hide modal
//         setTimeout(() => {
//           contactForm.reset();
//           modalBody.innerHTML = originalContent;
//           // Close the modal (using Bootstrap's modal method)
//           const modalInstance = bootstrap.Modal.getInstance(document.getElementById('contact-us'));
//           modalInstance.hide();
//         }, 3000);
//       })
//       .catch(error => {
//         // Handle errors
//         console.error('Error submitting form:', error);
        
//         // Display error message in the form
//         const errorMessage = document.createElement('div');
//         errorMessage.className = 'alert alert-danger mt-3';
//         errorMessage.textContent = 'There was an error submitting your message. Please try again later.';
        
//         contactForm.appendChild(errorMessage);
        
//         // Remove error message after 4 seconds
//         setTimeout(() => {
//           errorMessage.remove();
//         }, 4000);
//       });

  
//     });
//   });


// document.addEventListener('DOMContentLoaded', function () {
//   const contactForm = document.querySelector('#contact-us form');

//   contactForm.addEventListener('submit', function (event) {
//       event.preventDefault();

//       // Collect form data
//       const formData = {
//           name: document.getElementById('name').value.trim(),
//           email: document.getElementById('email').value.trim(),
//           phone: document.getElementById('phone').value.trim(),
//           property: document.getElementById('property').value.trim(),
//           message: document.getElementById('message').value.trim()
//       };

//       console.log("Sending data:", formData);  // Debugging output
//           console.log("CSRFToken:", getCSRFToken());
//       fetch('http://127.0.0.1:8000/api/business/contact/', {
//           method: 'POST',
//           headers: {
            
//               'Content-Type': 'application/json',
//               'X-CSRFToken': getCSRFToken(), // Ensure you include CSRF token

//             },

//           body: JSON.stringify(formData)

//       })

//       .then(response => {
//           console.log("Response status:", response.status);
//           return response.json();
//       })
//       .then(data => {
//           console.log("Response data:", data);

//           if (data.success) {
//               alert("Message sent successfully!");
//               contactForm.reset();
//           } else {
//               alert("Error: " + data.error);
//           }
//       })
//       .catch(error => {
//           console.error("Error:", error);
//           alert("An error occurred. Please try again.");
//       });
      
//   });
// });



document.addEventListener("DOMContentLoaded", function () {
  const contactForm = document.querySelector("#contact-form");

  contactForm.addEventListener("submit", function (event) {
      event.preventDefault();

      // Collect form data
      const formData = {
          name: document.getElementById("name").value.trim(),
          email: document.getElementById("email").value.trim(),
          phone: document.getElementById("phone").value.trim(),
          property: document.getElementById("property").value.trim(),
          message: document.getElementById("message").value.trim(),
      };

      // Get CSRF Token from cookies
      function getCSRFToken() {
          let cookieValue = null;
          const cookies = document.cookie.split(";");
          for (let i = 0; i < cookies.length; i++) {
              const cookie = cookies[i].trim();
              if (cookie.startsWith("csrftoken=")) {
                  cookieValue = cookie.substring("csrftoken=".length, cookie.length);
                  break;
              }
          }
          return cookieValue;
      }

      fetch("http://127.0.0.1:8000/api/business/contact/", {
          method: "POST",
          headers: {
              "Content-Type": "application/json",
              "X-CSRFToken": getCSRFToken(),  // ✅ Include CSRF token
          },
          body: JSON.stringify(formData),
      })
          .then((response) => response.json())
          .then((data) => {
              console.log("Response:", data);
              if (data.success) {
                  alert("Message sent successfully!");
                  contactForm.reset();
              } else {
                  alert("Error: " + data.error);
              }
          })
          .catch((error) => {
              console.error("Error:", error);
              alert("An error occurred. Please try again.");
          });
  });
});
