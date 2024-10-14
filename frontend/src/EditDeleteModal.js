import React, { useState, useEffect } from 'react';
import './Modal.css';

function EditDeleteModal({ site, isOpen, onClose, onSave, onDelete }) {
    const [formData, setFormData] = useState({
        url: '',
        check_interval: '',
        keyword: '',
    });

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
        onSave(formData);
    };

    const handleDelete = () => {
        onDelete();
    };

    if (!isOpen || !site) {
        return null;
    }

    return (
        <div className="modal">
            <div className="modal-content">
                <span className="close" onClick={onClose}>&times;</span>
                <h2>Edytuj lub Usuń Monitorowaną Stronę</h2>

                <form>
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
                </form>

                <button onClick={handleSave}>Zapisz Zmiany</button>
                <button onClick={handleDelete} style={{ color: 'red' }}>Usuń Stronę</button>
            </div>
        </div>
    );
}

export default EditDeleteModal;
