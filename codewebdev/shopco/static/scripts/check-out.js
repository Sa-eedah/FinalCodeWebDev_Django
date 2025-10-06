
$(document).ready(function () {

    $('#billingForm').validate({

        rules: {
            Cardholder: "required",
            CreditCardNumber: {
                required: true,
                digits: true,
                minlength: 16,
                maxlength: 16

            },
            CVV: {
                required: true,
                digits: true,
                minlength: 3,
                maxlength:3
                
            },

            ExpirationDate:{

                required: true,
            }

        },

        messages: {
            Cardholder: "Please enter full name",
            CreditCardNumber: {
                required: "Please enter a Credit Card Number",
                digits: "Credit Card Number code must be a number",
                minlength: "Credit Card Number code must be minimum of 16 digits",
                maxlength: "Credit Card Number code must be maximum of 16 digits"

            },
            CVV: {
                required: "Provide CVV number",
                minlength: "CVV number must be a minimum of 3 characters",
                digits: "CVV must be a number",
                maxlength: "CVV number must be maximum of 4 digits"
            },
            ExpirationDate: {
                required: "Please enter Expiration Date",                
            },



        },

        highlight: function (element) {
            $(element).addClass('error-input')
            $(element).removeClass('valid-input')

        },

        unhighlight: function (element) {
            $(element).removeClass('error-input')
            $(element).addClass('valid-input')

        }

    });




});