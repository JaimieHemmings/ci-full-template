document.addEventListener('DOMContentLoaded', function() {

// Get all instances of the delete class
const deleteButtons = document.querySelectorAll('.delete');

  // for each instance of the delete class, add an event listener
  deleteButtons.forEach(button => {
      button.addEventListener('click', () => {
        
        // toggle hidden class on this instance of the button
        button.classList.toggle('hidden');
        
        //toggle hidden class on sister element
        button.nextElementSibling.classList.toggle('hidden');
        
      });
  });

  // Get all instances of the cancel class
  const cancelButtons = document.querySelectorAll('.btn-no');

  // for each instance of the cancel class, add an event listener
  cancelButtons.forEach(button => {
      button.addEventListener('click', () => {
        
        // find parent element with class "confirm"
        const parent = button.closest('.confirm');
        parent.classList.toggle('hidden');

        // Show the delete button
        const deleteButton = parent.previousElementSibling;
        deleteButton.classList.toggle('hidden');
        
      });
  });

});