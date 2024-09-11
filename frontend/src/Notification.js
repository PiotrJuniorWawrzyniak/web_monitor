import React from 'react';
import './Notification.css'; // Dodaj stylizację, jeśli chcesz

function Notification({ message, type }) {
    if (!message) return null;

    return (
        <div className={`notification ${type}`}>
            {message}
        </div>
    );
}

export default Notification;
