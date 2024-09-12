import EgoForm from '@egodesign/form'
export const contactForm = () => {
    const contactForm = document.getElementById('contactForm')
    if (!contactForm) return

    const myForm = new EgoForm({
        element: contactForm,
        submitType: 'get',
        debug: true,
        submitDataFormat: 'formData',
        requestHeaders: {},
        fieldGroups: {
            phone_numbers: ['phone', 'mobile'],
        },
        serializerIgnoreList: ['ignore'],
        classes: {
            requiredField: '--required',
            requiredIfFilledField: '--required-if-filled',
            fieldHasError: '--has-error',
            controlHasError: 'is-danger',
            hiddenErrorMessage: 'is-hidden',
            formSubmittingState: '--submitting',
            buttonSubmittingState: 'is-loading',
        },
        customValidations: {
            test: [
                {
                    name: 'isValid',
                    condition: (value) => value === 'testing',
                    message: 'This field value should be "testing".',
                },
            ],
        },
        customValidationsMessages: {
            fieldName: {
                empty: 'message',
                invalid: 'message',
            },
        },
        onStepChange: (previous, next) => console.log(current, next),
        onBeforeSubmit: () => console.log('Before submit'),
        onValidationError: (fields) => console.log({ fields }),
        onSubmitStart: () => console.log('Submit start'),
        onSubmitEnd: () => console.log('Submit end'),
        onSuccess: (res) => {
            console.log('Success')

            res.json().then(({ data }) => {
                console.log(data)
            })
        },
        onError: (err) => console.log('Error', { err }),
        preventSubmit: false,
    })
}
