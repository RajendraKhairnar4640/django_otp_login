var input = document.querySelector('#zipcode');
        var indicator = document.querySelector('.ri');
        var info = document.querySelector('.info');
        var info2 = document.querySelector('.info2');

        var codelength = /^\d{6}$/
    
        input.addEventListener('keyup', () => {
            if (input.value.match(codelength)) {
                $.ajax({
                    type: "GET",
                    url: "https://api.postalpincode.in/pincode/" + input.value,
    
                    success: (response) => {
                        info.innerHTML = (response[0].PostOffice[0].Name);
                        info2.innerHTML = (response[0].PostOffice[0].State);

                    }
                });
    
                indicator.classList.add('ri-checkbox-circle-fill');
                indicator.classList.remove('ri-close-circle-fill');
            }
    
            else {
                indicator.classList.add('ri-close-circle-fill');
                indicator.classList.remove('ri-checkbox-circle-fill');
                info.innerHTML = "Type valid zipcode";
            }
    
        });