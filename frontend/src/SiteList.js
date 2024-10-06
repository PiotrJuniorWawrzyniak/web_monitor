//import React, { useEffect, useState } from 'react';
//
//function SiteList({ openModal }) {
//    const [sites, setSites] = useState([]);
//    const [error, setError] = useState(null);
//
//    const fetchSites = async () => {
//        try {
//            const response = await fetch('/api/monitored-sites/');
//            if (response.ok) {
//                const data = await response.json();
//                setSites(data);
//            } else {
//                setError('Błąd podczas pobierania listy stron.');
//            }
//        } catch (err) {
//            setError('Błąd połączenia z serwerem.');
//        }
//    };
//
//    useEffect(() => {
//        fetchSites();
//    }, []);
//
//    return (
//        <div>
//            <h2>Monitorowane Strony</h2>
//            {error && <p style={{ color: 'red' }}>{error}</p>}
//            <ul>
//                {sites.length > 0 ? (
//                    sites.map((site) => (
//                        <li key={site.id} onClick={() => openModal(site)} style={{ cursor: 'pointer' }}>
//                            {site.url} - Częstotliwość: {site.check_interval} min - Fraza: {site.keyword} - Status: {site.last_phrase_status ? 'Znaleziono' : 'Nie znaleziono'}
//                        </li>
//                    ))
//                ) : (
//                    <p>Brak monitorowanych stron.</p>
//                )}
//            </ul>
//        </div>
//    );
//}
//
//export default SiteList;

import React, { useEffect, useState } from 'react';

function SiteList({ openModal }) {
    const [sites, setSites] = useState([]);
    const [error, setError] = useState(null);

    const fetchSites = async () => {
        try {
            const response = await fetch('/api/monitored-sites/');
            if (response.ok) {
                const data = await response.json();
                setSites(data);
            } else {
                setError('Błąd podczas pobierania listy stron.');
            }
        } catch (err) {
            setError('Błąd połączenia z serwerem.');
        }
    };

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
                        <li key={site.id} onClick={() => openModal(site)} style={{ cursor: 'pointer' }}>
                            {site.url} - Częstotliwość: {site.check_interval} min - Fraza: {site.keyword} - Status: {site.last_phrase_status ? 'Znaleziono' : 'Nie znaleziono'}
                        </li>
                    ))
                ) : (
                    <p>Brak monitorowanych stron.</p>
                )}
            </ul>
        </div>
    );
}

export default SiteList;
