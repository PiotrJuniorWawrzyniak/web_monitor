import React from 'react';
import './App.css';
import FormComponent from './FormComponent';
import Notification from './Notification'; // Importuj komponent

function App() {
  const [notification, setNotification] = useState({ message: '', type: '' });

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
      <Notification message={notification.message} type={notification.type} />
      <FormComponent setNotification={setNotification} /> {/* Przekaż funkcję do aktualizacji komunikatów */}
    </div>
  );
}

export default App;
