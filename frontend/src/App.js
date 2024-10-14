import React, { useState, useEffect } from 'react';
import './App.css';
import FormComponent from './FormComponent';
import Notification from './Notification';
import SiteList from './SiteList';
import EditDeleteModal from './EditDeleteModal';

function App() {
    const [notification, setNotification] = useState({ message: '', type: '' });
    const [modalIsOpen, setModalIsOpen] = useState(false);
    const [selectedSite, setSelectedSite] = useState(null);
    const [sites, setSites] = useState([]);

    // Funkcja do pobierania listy stron
    const fetchSites = () => {
        fetch('/api/monitored-sites/')
            .then(response => response.json())
            .then(data => setSites(data))
            .catch(error => console.error('Error fetching sites:', error));
    };

    // Automatyczne odświeżanie listy stron po renderowaniu komponentu
    useEffect(() => {
        fetchSites();  // Pobranie stron po załadowaniu komponentu

        // Dodano automatyczne odświeżanie co 5 sekund
        const intervalId = setInterval(fetchSites, 5000);
        return () => clearInterval(intervalId);
    }, []);

    // Funkcja do otwierania modala
    const openModal = (site) => {
        setSelectedSite(site);
        setModalIsOpen(true);
    };

    // Funkcja do zamykania modala
    const closeModal = () => {
        setModalIsOpen(false);
        setSelectedSite(null);
    };

    // Funkcja do zapisywania zmian w formularzu edycji
    const handleSaveChanges = (updatedSite) => {
        const siteId = selectedSite.id;
        fetch(`/api/monitored-sites/${siteId}/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(updatedSite),
        })
        .then(response => {
            if (response.ok) {
                setNotification({ message: 'Zmiany zostały zapisane pomyślnie!', type: 'success' });
                fetchSites();  // Odśwież listę po zapisaniu zmian
            } else {
                setNotification({ message: 'Błąd podczas zapisywania zmian.', type: 'error' });
            }
            closeModal();
        })
        .catch(error => {
            console.error('Error saving changes:', error);
            setNotification({ message: 'Błąd sieci. Spróbuj ponownie.', type: 'error' });
            closeModal();
        });
    };

    // Funkcja do usuwania strony
    const handleDeleteSite = () => {
        const siteId = selectedSite.id;
        fetch(`/api/monitored-sites/${siteId}/`, {
            method: 'DELETE',
        })
        .then(response => {
            if (response.ok) {
                setNotification({ message: 'Strona została usunięta pomyślnie!', type: 'success' });
                fetchSites();  // Odśwież listę po usunięciu strony
            } else {
                setNotification({ message: 'Błąd podczas usuwania strony.', type: 'error' });
            }
            closeModal();
        })
        .catch(error => {
            console.error('Error deleting site:', error);
            setNotification({ message: 'Błąd sieci. Spróbuj ponownie.', type: 'error' });
            closeModal();
        });
    };

    return (
        <div className="App">
            <h1>WEB MONITOR</h1>

            <Notification message={notification.message} type={notification.type} />
            <FormComponent setNotification={setNotification} refreshSiteList={fetchSites} />  {/* Poprawiono nazwę prop */}
            <SiteList openModal={openModal} sites={sites} />  {/* Przekazanie listy stron do SiteList */}

            {/* Modal do edycji/usuwania */}
            <EditDeleteModal
                site={selectedSite}
                isOpen={modalIsOpen}
                onClose={closeModal}
                onSave={handleSaveChanges}
                onDelete={handleDeleteSite}
            />
        </div>
    );
}

export default App;
