import React, { useState } from 'react';
import Notification from './Notification'; // Importuj komponent

function FormComponent() {
    const [formData, setFormData] = useState({
        url: '',
        frequency: '',
        phrase: ''
    });
    const [notification, setNotification] = useState({ message: '', type: '' });

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
                setNotification({ message: 'Form submitted successfully!', type: 'success' });
            } else {
                return response.json().then(data => {
                    setNotification({ message: data.error || 'Error submitting form.', type: 'error' });
                });
            }
        }).catch(() => {
            setNotification({ message: 'Network error. Please try again.', type: 'error' });
        });
    };

    return (
        <div>
            <Notification message={notification.message} type={notification.type} />
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
        </div>
    );
}

export default FormComponent;
