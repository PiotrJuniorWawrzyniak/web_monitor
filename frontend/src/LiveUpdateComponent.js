import React, { useEffect, useState } from 'react';

function LiveUpdateComponent() {
    const [sites, setSites] = useState([]);

    useEffect(() => {
        const fetchSites = () => {
            fetch('/api/monitored-sites/')
                .then(response => response.json())
                .then(data => {
                    setSites(data);
                })
                .catch(error => console.error('Error fetching sites:', error));
        };

        const intervalId = setInterval(fetchSites, 5000);  // Aktualizacja co 5 sekund
        fetchSites();

        return () => clearInterval(intervalId);
    }, []);

    return (
        <div>
            <h2>Monitored Sites</h2>
            <ul>
                {sites.map(site => (
                    <li key={site.id}>
                        {site.url} (checked every {site.check_interval} minutes)
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default LiveUpdateComponent;
