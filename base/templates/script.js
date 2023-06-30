const dateInput = document.getElementById('dateInput');
    const dateForm = document.getElementById('dateForm');

    dateInput.addEventListener('change', () => {
        dateForm.submit();
    });