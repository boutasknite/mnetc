document.getElementById('cv').onchange = function () {
    this.previousElementSibling.innerHTML = this.files[0].name;
};

document.getElementById('image').onchange = function () {
    this.previousElementSibling.innerHTML = this.files[0].name;
};

document.getElementById('myButton').addEventListener('click', function(event) {
    event.preventDefault();
    var allValid = is_all_valid();
    if(allValid){
     send_information();
    }

});

function getCookie(name) {
const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
return cookieValue ? cookieValue.pop() : '';
}


document.getElementById('CloseBtn').addEventListener('click', function(event) {
    window.dialog.close();
    location.reload();
});


function send_information(){
    first_name = document.getElementById('first name').value;
    last_name = document.getElementById('last name').value;
    email = document.getElementById('email').value;
    phone_number = document.getElementById('phone number').value;
    affiliation = document.getElementById('affiliation').value;
    research_area = document.getElementById('research area').value;
    position = document.getElementById('position').value;
    cv = document.getElementById('cv').files[0];
    image = document.getElementById('image').files[0];
    biography = document.getElementById('biography').value;
    motivation = document.getElementById('motivation').value;
    contribution = document.getElementById('contribution').value;
    references = document.getElementById('references').value;

    const formData = new FormData();
    formData.append('first_name', first_name);
    formData.append('last_name', last_name);
    formData.append('email', email);
    formData.append('phone_number', phone_number);
    formData.append('affiliation', affiliation);
    formData.append('research_area', research_area);
    formData.append('position', position);
    formData.append('image', image);
    formData.append('biography', biography);
    formData.append('motivation', motivation);
    formData.append('contribution', contribution);
    formData.append('references', references);
    formData.append('cv', cv);

    fetch('/save_application/', {
      method: 'POST',
      body: formData,
      headers: {
        'X-CSRFToken': getCookie('csrftoken'),
      },
    })

    .then(response => {
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return response.json();
    })

    .then(data  => {
        if (data && data.msg !== "Success") {
            document.getElementById('errorMessages').innerHTML = data.msg;
            document.getElementById('errorMessages').style.display = "block";
        }
        else{
            window.dialog.showModal();
        }
    })
    .catch(error => {

    });

}




function is_all_valid(){
    first_name = document.getElementById('first name');
    last_name = document.getElementById('last name');
    email = document.getElementById('email');
    phone_number = document.getElementById('phone number');
    affiliation = document.getElementById('affiliation');
    research_area = document.getElementById('research area');
    position = document.getElementById('position');
    cv = document.getElementById('cv');
    image = document.getElementById('image');
    biography = document.getElementById('biography');
    motivation = document.getElementById('motivation');
    contribution = document.getElementById('contribution');
    references = document.getElementById('references');
    let allValid = true;
    let errorMessages = '';
    const fields = [
        first_name, last_name, email, phone_number, affiliation,
        research_area, position, cv, image, biography,
        motivation, contribution, references
    ];
    fields.forEach(field => {
        if (!field.value) {
            allValid = false;
            field.classList.add('error-border');
        } else {
            field.classList.remove('error-border');
        }
    });

     if (!allValid) {
        errorMessages = 'Please fill all fields.';
        document.getElementById('errorMessages').innerHTML = errorMessages;
        document.getElementById('errorMessages').style.display = "block";
    }

    const text = biography.value.trim();
    const nb_words = text.split(/\s+/).filter(word => word !== '').length;
    if(nb_words < 100){
        errorMessages = "The biography should contains at least 100 words";
        document.getElementById('errorMessages').innerHTML = errorMessages;
        document.getElementById('errorMessages').style.display = "block";
        allValid = false;
    }

    if(nb_words > 120){
        errorMessages = "The biography should contains maximum 120 words";
        document.getElementById('errorMessages').innerHTML = errorMessages;
        document.getElementById('errorMessages').style.display = "block";
        allValid = false;
    }


    return allValid;
}


 document.querySelectorAll('.faq-item h3, .faq-item .faq-toggle').forEach((faqItem) => {
    faqItem.addEventListener('click', () => {
      faqItem.parentNode.classList.toggle('faq-active');
    });
  });


const textInput = document.getElementById('biography');
const wordCount = document.getElementById('wordCount');

textInput.addEventListener('input', function() {
  const text = this.value.trim();
  const words = text.split(/\s+/).filter(word => word !== '');
  wordCount.textContent = `${words.length}/120`;
});