import React, { useEffect, useState } from 'react';

function LiveUpdateComponent() {
    const [sites, setSites] = useState([]);

    useEffect(() => {
        // Funkcja do pobierania listy monitorowanych stron
        const fetchSites = () => {
            fetch('/api/monitored-sites/')
                .then(response => response.json())
                .then(data => {
                    setSites(data);
                })
                .catch(error => console.error('Error fetching sites:', error));
        };

        // Wywołanie fetchSites co 5 sekund (5000 ms) dla aktualizacji na żywo
        const intervalId = setInterval(fetchSites, 5000);

        // Pobranie danych początkowych
        fetchSites();

        // Wyczyszczenie interwału po opuszczeniu komponentu
        return () => clearInterval(intervalId);
    }, []);

    return (
        <div>
            <h2>Monitored Sites</h2>
            <ul>
                {sites.map(site => (
                    <li key={site.id}>{site.url} (checked every {site.frequency} minutes)</li>
                ))}
            </ul>
        </div>
    );
}

export default LiveUpdateComponent;
