import { useEffect, useState } from 'react';
import {useLocalStorage} from "../useLocalStorage";

export const FetchResults = (proteinName) => {
    // const [results, setResults] = useState([]);
    const [results, setResults] = useLocalStorage("results", []);

    useEffect(() => {
        fetch(`http://localhost:8000/api/${proteinName}`)
            .then(res => res.json())
            .then(json => {
                const proteins = json.results.map(protein => ({
                    proteinId: protein.id,
                    proteinName: protein.name,
                    proteinLocation: protein.location
                }));
                setResults(proteins);
            });
    }, [proteinName]);
    return results;
};
