import React, { useState } from 'react';

function FormComponent() {
    const [formData, setFormData] = useState({
        url: '',
        frequency: '',
        phrase: ''
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        fetch('/api/submit-form/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify(formData)
        }).then(response => {
            if (response.ok) {
                console.log("Form submitted successfully!");
            } else {
                console.error("Error submitting form.");
            }
        });
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>Website URL:</label>
                <input
                    type="url"
                    name="url"
                    value={formData.url}
                    onChange={handleChange}
                    required
                />
            </div>
            <div>
                <label>Monitoring Frequency (min):</label>
                <input
                    type="number"
                    name="frequency"
                    value={formData.frequency}
                    onChange={handleChange}
                    min="1"
                    required
                />
            </div>
            <div>
                <label>Search Phrase:</label>
                <input
                    type="text"
                    name="phrase"
                    value={formData.phrase}
                    onChange={handleChange}
                    required
                />
            </div>
            <button type="submit">Submit</button>
        </form>
    );
}

export default FormComponent;
