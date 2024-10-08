import React, { useState, useEffect } from 'react';
import './App.css';
import FormComponent from './FormComponent';
import Notification from './Notification';
import SiteList from './SiteList';
import EditDeleteModal from './EditDeleteModal';
import LiveUpdateComponent from './LiveUpdateComponent';

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
        console.log('Zapisano zmiany:', updatedSite);
        setNotification({ message: 'Changes saved successfully!', type: 'success' });
        fetchSites();  // Odśwież listę po zapisaniu zmian
        closeModal();
    };

    // Funkcja do usuwania strony
    const handleDeleteSite = () => {
        console.log('Strona została usunięta:', selectedSite);
        setNotification({ message: 'Site deleted successfully!', type: 'success' });
        fetchSites();  // Odśwież listę po usunięciu strony
        closeModal();
    };

    return (
        <div className="App">
            <h1>WEB MONITOR</h1>

            <Notification message={notification.message} type={notification.type} />
            <FormComponent setNotification={setNotification} fetchSites={fetchSites} />  {/* Przekazanie fetchSites */}
            <SiteList openModal={openModal} sites={sites} />  {/* Przekazanie listy stron do SiteList */}

            {/* Modal do edycji/usuwania */}
            <EditDeleteModal
                site={selectedSite}
                isOpen={modalIsOpen}
                onClose={closeModal}
                onSave={handleSaveChanges}
                onDelete={handleDeleteSite}
            />

            <LiveUpdateComponent />
        </div>
    );
}

export default App;
