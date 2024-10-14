import React from 'react';

function SiteList({ openModal, sites }) {
    return (
        <div>
            <h2>Monitorowane Strony</h2>
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
