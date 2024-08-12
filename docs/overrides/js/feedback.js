document.addEventListener('DOMContentLoaded', function() {
  const feedbackContainer = document.getElementById('feedback-form-container');
  if (feedbackContainer) {
    const chapters = [
      "1 - Capabilities",
      "2 - Risks Landscape",
      "3 - Solutions Landscape",
      "4 - Evaluations",
      "5 - Governance",
      "6 - Reward Misspecification",
      "7 - Goal Misgeneralization",
      "8 - Scalable Oversight",
      "9 - Intepretability",
      "10 - Agent Foundations"
    ];

    const formHTML = `
      <form id="feedback-form" class="feedback-form">
        <div>
          <label for="feedback-type">Feedback Type:</label>
          <select id="feedback-type" name="feedback-type">
            <option value="book">Book Level</option>
            <option value="chapter">Chapter Level</option>
          </select>
        </div>
        <div id="chapter-select" style="display: none;">
          <label for="chapter">Select Chapter:</label>
          <select id="chapter" name="chapter">
            <option value="">Select a chapter</option>
            ${chapters.map(chap => `<option value="${chap}">${chap}</option>`).join('')}
          </select>
        </div>
        <div>
          <label for="feedback">Your Feedback:</label>
          <textarea id="feedback" name="feedback" rows="4" required></textarea>
        </div>
        <button type="submit">Submit Feedback</button>
      </form>
      <div id="feedback-success" class="feedback-success" style="display: none;">
        Your feedback has been submitted. Thank you!
      </div>
    `;

    feedbackContainer.innerHTML = formHTML;

    const form = document.getElementById('feedback-form');
    const feedbackType = document.getElementById('feedback-type');
    const chapterSelect = document.getElementById('chapter-select');
    const successMessage = document.getElementById('feedback-success');

    feedbackType.addEventListener('change', function() {
      chapterSelect.style.display = this.value === 'chapter' ? 'block' : 'none';
    });

    form.addEventListener('submit', function(e) {
      e.preventDefault();
      const formData = new FormData(form);
      const feedbackData = Object.fromEntries(formData.entries());
      
      // Here you would typically send the feedback to your backend
      console.log(feedbackData);

      // Show success message
      successMessage.style.display = 'block';
      form.reset();
      chapterSelect.style.display = 'none';

      // Hide success message after 3 seconds
      setTimeout(() => {
        successMessage.style.display = 'none';
      }, 3000);
    });
  }
});
