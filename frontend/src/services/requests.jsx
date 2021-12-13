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

export const FetchTestResults = () => {
    // const [results, setResults] = useState([]);
    const [results, setResults] = useLocalStorage("results", []);
const json = [{'proteinName': 'protein 1', 'proteinLocation': 'protein 1 location'}, {'proteinName': 'protein 2', 'proteinLocation': 'protein 2 location'}];

    useEffect(() => {
        fetch('http://localhost:8000/api/sequence')
            .then(res => res.json())
            .then(json => {
                console.log(json)
                const results = json.data.map(protein => ({
                    // proteinId: protein.id,
                    proteinName: protein.proteinName,
                    proteinLocation: protein.proteinLocation
                }));
                setResults(results);
            });
    });
    setResults(json)
    return results;
};