import React, { useState } from 'react';

function FormComponent({ setNotification, refreshSiteList }) {
    const [formData, setFormData] = useState({
        url: '',
        check_interval: '',
        keyword: ''
    });
    const [isDuplicate, setIsDuplicate] = useState(false);
    const [isValidUrl, setIsValidUrl] = useState(true);

    // Pobieramy token CSRF z ciasteczka
    const getCookie = (name) => {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    };

    const csrftoken = getCookie('csrftoken'); // Pobieramy CSRF token

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
                'X-CSRFToken': csrftoken  // Dodanie tokenu CSRF
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
        const dataToSend = {
            ...formData,
            check_interval: parseInt(formData.check_interval, 10)
        };

        fetch('/api/submit-form/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken  // Dodanie tokenu CSRF
            },
            body: JSON.stringify(dataToSend)
        }).then(response => {
            if (response.ok) {
                setNotification({ message: 'Formularz został pomyślnie wysłany!', type: 'success' });
                setFormData({ url: '', check_interval: '', keyword: '' }); // Resetowanie formularza

                if (refreshSiteList) {
                    refreshSiteList();
                }
            } else {
                return response.json().then(data => {
                    setNotification({ message: data.error || 'Błąd podczas wysyłania formularza.', type: 'error' });
                });
            }
        }).catch(() => {
            setNotification({ message: 'Błąd sieci. Spróbuj ponownie.', type: 'error' });
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
                    <label>Monitoring Frequency (min):</label>
                    <input
                        type="number"
                        name="check_interval"
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
