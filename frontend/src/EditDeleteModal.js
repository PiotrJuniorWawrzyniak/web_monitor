import React, { useState, useEffect } from 'react';
import './Modal.css';

function EditDeleteModal({ site, isOpen, onClose, onSave, onDelete }) {
    const [formData, setFormData] = useState({
        url: '',
        check_interval: '',
        keyword: '',
    });

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

    useEffect(() => {
        if (site) {
            setFormData({
                url: site.url || '',
                check_interval: site.check_interval || '',
                keyword: site.keyword || '',
            });
        }
    }, [site]);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value
        });
    };

    const handleSave = () => {
        // Zaktualizowany kod, przekazujemy token CSRF przy zapisywaniu zmian
        onSave(formData, csrftoken);
    };

    const handleDelete = () => {
        // Zaktualizowany kod, przekazujemy token CSRF przy usuwaniu
        onDelete(csrftoken);
    };

    if (!isOpen || !site) {
        return null;
    }

    return (
        <div className="modal">
            <div className="modal-content">
                <span className="close" onClick={onClose}>&times;</span>
                <h2>Edytuj lub usuń monitorowaną stronę</h2>

                <form>
                    <div>
                        <label>Adres strony:</label>
                        <input
                            type="url"
                            name="url"
                            value={formData.url}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <div>
                        <label>Częstotliwość monitorowania (min):</label>
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
                        <label>Wyszukiwana fraza:</label>
                        <input
                            type="text"
                            name="keyword"
                            value={formData.keyword}
                            onChange={handleChange}
                            required
                        />
                    </div>
                </form>

                <button onClick={handleSave}>Zapisz zmiany</button>
                <button onClick={handleDelete} style={{ color: 'red' }}>Usuń stronę</button>
            </div>
        </div>
    );
}

export default EditDeleteModal;
