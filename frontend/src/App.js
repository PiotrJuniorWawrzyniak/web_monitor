import React, { useState } from 'react';
import './App.css';
import FormComponent from './FormComponent';
import Notification from './Notification';
import SiteList from './SiteList'; // Importuj komponent listy stron
import EditDeleteModal from './EditDeleteModal'; // Importuj komponent modala

function App() {
  const [notification, setNotification] = useState({ message: '', type: '' });
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const [selectedSite, setSelectedSite] = useState(null); // Przechowuje wybraną stronę

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
    closeModal();
  };

  // Funkcja do usuwania strony
  const handleDeleteSite = () => {
    console.log('Strona została usunięta:', selectedSite);
    setNotification({ message: 'Site deleted successfully!', type: 'success' });
    closeModal();
  };

  return (
    <div className="App">
      <h1>WEB MONITOR</h1> {/* Dodaj własny nagłówek */}

      <Notification message={notification.message} type={notification.type} />
      <FormComponent setNotification={setNotification} /> {/* Przekaż funkcję do aktualizacji komunikatów */}

      <SiteList openModal={openModal} /> {/* Przekaż funkcję otwierania modala do listy stron */}

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
