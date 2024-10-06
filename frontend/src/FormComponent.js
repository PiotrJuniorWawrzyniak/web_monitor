//import React, { useState } from 'react';
//import Notification from './Notification';
//
//function FormComponent({ setNotification }) {
//    const [formData, setFormData] = useState({
//        url: '',
//        frequency: '',
//        keyword: ''
//    });
//    const [isDuplicate, setIsDuplicate] = useState(false);
//    const [isValidUrl, setIsValidUrl] = useState(true);
//
//    const handleChange = (e) => {
//        const { name, value } = e.target;
//        setFormData({
//            ...formData,
//            [name]: value
//        });
//
//        if (name === 'url') {
//            validateUrl(value);
//        }
//    };
//
//    const validateUrl = (url) => {
//        const urlPattern = /^(ftp|http|https):\/\/[^ "]+$/;
//        setIsValidUrl(urlPattern.test(url));
//    };
//
//    const handleSubmit = (e) => {
//        e.preventDefault();
//
//        // Sprawdzenie duplikacji
//        fetch(`/api/check-duplicate/`, {
//            method: 'POST',
//            headers: {
//                'Content-Type': 'application/json',
//            },
//            body: JSON.stringify({ url: formData.url })
//        })
//        .then(response => response.json())
//        .then(data => {
//            if (data.duplicate) {
//                setNotification({ message: 'Podana strona jest już monitorowana.', type: 'error' });
//                setIsDuplicate(true);
//            } else {
//                submitForm();
//            }
//        })
//        .catch(() => {
//            setNotification({ message: 'Błąd sieci. Spróbuj ponownie.', type: 'error' });
//        });
//    };
//
//    const submitForm = () => {
//        console.log("Wysyłane dane:", formData);
//
//        fetch('/api/submit-form/', {
//            method: 'POST',
//            headers: {
//                'Content-Type': 'application/json',
//            },
//            body: JSON.stringify(formData)
//        }).then(response => {
//            if (response.ok) {
//                setNotification({ message: 'Form submitted successfully!', type: 'success' });
//                setFormData({ url: '', frequency: '', keyword: '' });
//            } else {
//                return response.json().then(data => {
//                    setNotification({ message: data.error || 'Error submitting form.', type: 'error' });
//                });
//            }
//        }).catch(() => {
//            setNotification({ message: 'Network error. Please try again.', type: 'error' });
//        });
//    };
//
//    return (
//        <div>
//            <form onSubmit={handleSubmit}>
//                <div>
//                    <label>Website URL:</label>
//                    <input
//                        type="url"
//                        name="url"
//                        value={formData.url}
//                        onChange={handleChange}
//                        required
//                    />
//                    {!isValidUrl && <p style={{ color: 'red' }}>Podaj poprawny URL.</p>}
//                    {isDuplicate && <p style={{ color: 'red' }}>Podana strona jest już monitorowana.</p>}
//                </div>
//                <div>
//                    <label>Monitoring Frequency (min):</label>
//                    <input
//                        type="number"
//                        name="frequency"
//                        value={formData.frequency}
//                        onChange={handleChange}
//                        min="1"
//                        required
//                    />
//                </div>
//                <div>
//                    <label>Search Phrase:</label>
//                    <input
//                        type="text"
//                        name="keyword"
//                        value={formData.keyword}
//                        onChange={handleChange}
//                        required
//                    />
//                </div>
//                <button type="submit" disabled={!isValidUrl || isDuplicate}>Submit</button>
//            </form>
//        </div>
//    );
//}
//
//export default FormComponent;

import React, { useState } from 'react';

function FormComponent({ setNotification, refreshSiteList }) { // Dodano refreshSiteList jako props
    const [formData, setFormData] = useState({
        url: '',
        check_interval: '', // Zmieniono 'frequency' na 'check_interval'
        keyword: ''
    });
    const [isDuplicate, setIsDuplicate] = useState(false);
    const [isValidUrl, setIsValidUrl] = useState(true);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value
        });

        if (name === 'url') {
            validateUrl(value);
        }
    };

    const validateUrl = (url) => {
        const urlPattern = /^(ftp|http|https):\/\/[^ "]+$/;
        setIsValidUrl(urlPattern.test(url));
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        // Sprawdzenie duplikacji
        fetch(`/api/check-duplicate/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url: formData.url })
        })
        .then(response => response.json())
        .then(data => {
            if (data.duplicate) {
                setNotification({ message: 'Podana strona jest już monitorowana.', type: 'error' });
                setIsDuplicate(true);
            } else {
                submitForm();
            }
        })
        .catch(() => {
            setNotification({ message: 'Błąd sieci. Spróbuj ponownie.', type: 'error' });
        });
    };

    const submitForm = () => {
        console.log("Wysyłane dane:", formData);

        fetch('/api/submit-form/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        }).then(response => {
            if (response.ok) {
                setNotification({ message: 'Form submitted successfully!', type: 'success' });
                setFormData({ url: '', check_interval: '', keyword: '' }); // Resetowanie formularza

                if (refreshSiteList) { // Sprawdzanie i odświeżanie listy
                    refreshSiteList();
                }
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
                    {!isValidUrl && <p style={{ color: 'red' }}>Podaj poprawny URL.</p>}
                    {isDuplicate && <p style={{ color: 'red' }}>Podana strona jest już monitorowana.</p>}
                </div>
                <div>
                    <label>Monitoring Frequency (min):</label> {/* Zmieniono label */}
                    <input
                        type="number"
                        name="check_interval" // Zmieniono 'frequency' na 'check_interval'
                        value={formData.check_interval}
                        onChange={handleChange}
                        min="1"
                        required
                    />
                </div>
                <div>
                    <label>Search Phrase:</label>
                    <input
                        type="text"
                        name="keyword"
                        value={formData.keyword}
                        onChange={handleChange}
                        required
                    />
                </div>
                <button type="submit" disabled={!isValidUrl || isDuplicate}>Submit</button>
            </form>
        </div>
    );
}

export default FormComponent;
