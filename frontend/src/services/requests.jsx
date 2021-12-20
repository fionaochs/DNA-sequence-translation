import { useEffect, useState } from 'react';
import {useLocalStorage} from "../useLocalStorage";

export const FetchResults = (proteinName) => {
    const [results, setResults] = useLocalStorage("results", []);

    useEffect(() => {
        fetch(`http://localhost:8000/api/sequence/${proteinName}`,{
            'methods':'GET',
            headers : {
                'Content-Type':'application/json'
            }
        })
            .then(res => res.json())
            .then(json => {
                const results = json.map(protein => ({
                    proteinId: protein.id,
                    DNASequence: protein.sequence,
                    proteinName: protein.proteinName,
                    proteinLocation: protein.proteinLocation,
                    organism: protein.organism
                }));
                setResults(results);
            });
    }, [proteinName]);
    return results;
};

export const FetchDBResults = () => {
    const [results, setResults] = useLocalStorage("results", []);

    useEffect(() => {
        fetch('http://localhost:8000/api/protein',{
            'methods':'GET',
            headers : {
                'Content-Type':'application/json'
            }
        })
            .then(res => res.json())
            .then(json => {
                const newResults = json.map(protein => ({
                    proteinId: protein.id,
                    DNASequence: protein.sequence,
                    proteinName: protein.proteinName,
                    proteinLocation: protein.proteinLocation,
                    organism: protein.organism
                }));
                setResults(results.concat(newResults));
            });
    }, [results]);
    return results;
};

export const FetchTestResults = (proteinName) => {
    // const [results, setResults] = useState([]);
    const [results, setResults] = useLocalStorage("results", []);
// const json = [{'proteinName': 'protein 1', 'proteinLocation': 'protein 1 location'},
//     {'proteinName': 'protein 2', 'proteinLocation': 'protein 2 location'},
//     {'proteinName': 'protein 3', 'proteinLocation': 'protein 3 location'}
// ];
// return json
    useEffect(() => {
        fetch('http://localhost:8000/api',{
            'methods':'GET',
            headers : {
                'Content-Type':'application/json'
            }
        })
            .then(res => res.json())
            .then(json => {
                console.log(json)
                const results = json.map(protein => ({
                    proteinId: protein.id,
                    proteinName: protein.title,
                    proteinLocation: protein.description
                }));
                setResults(results);
            });
    }, [proteinName]);
    // setResults(json)
    return results;
};