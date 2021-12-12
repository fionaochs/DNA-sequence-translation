import { useEffect, useState } from 'react';

export const fetchResults = (proteinName) => {
    const [results, setResults] = useState([]);

    useEffect(() => {
        fetch(`http://localhost:8000/api/${proteinName}`)
            .then(res => res.json())
            .then(json => {
                const proteins = json.proteins.map(protein => ({
                    proteinId: protein.id,
                    proteinName: protein.name,
                    proteinLocation: protein.location
                }));
                setResults(proteins);
            });
    }, [name]);
    return results;
};
