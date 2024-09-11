import React, { useState, useEffect } from 'react';

function SitesList() {
    const [sites, setSites] = useState([]);
    const [error, setError] = useState(null);

    // Funkcja do pobierania danych z API
    const fetchSites = async () => {
        try {
            const response = await fetch('/api/sites-list/');
            if (response.ok) {
                const data = await response.json();
                setSites(data.sites);
            } else {
                setError('Błąd podczas pobierania listy stron.');
            }
        } catch (err) {
            setError('Błąd połączenia z serwerem.');
        }
    };

    // Hook useEffect do pobierania danych przy załadowaniu komponentu
    useEffect(() => {
        fetchSites();
    }, []);

    return (
        <div>
            <h2>Monitorowane Strony</h2>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <ul>
                {sites.length > 0 ? (
                    sites.map((site) => (
                        <li key={site.id}>
                            {site.url} - Częstotliwość: {site.frequency} min
                        </li>
                    ))
                ) : (
                    <p>Brak monitorowanych stron.</p>
                )}
            </ul>
        </div>
    );
}

export default SitesList;
