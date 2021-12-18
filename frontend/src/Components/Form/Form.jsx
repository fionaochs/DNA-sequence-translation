import React, {useEffect, useState} from 'react';
import {FetchDBResults, FetchResults, FetchTestResults} from "../../services/requests";
import {useLocalStorage} from "../../useLocalStorage";

const Form = () => {
    const [proteinName, setProteinName] = useState('');
    const [results, setResults] = useLocalStorage("results", []);

    useEffect(() => {
    fetch('http://localhost:8000/api',{
        'methods':'GET',
        headers : {
            'Content-Type':'application/json'
        }
    })
        .then(res => res.json())
        .then(json => {
            // const results = json.map(protein => ({
            //     proteinId: protein.id,
            //     DNASequence: protein.sequence,
            //     proteinName: protein.proteinName,
            //     proteinLocation: protein.proteinLocation,
            //     organism: protein.organism
            // }));
                const results = json.map(protein => ({
                proteinId: protein.id,
                proteinName: protein.title,
                proteinLocation: protein.description
            }));
            setResults(results);
        });
}, [proteinName]);
    // useEffect(() => {
    //     fetch(`http://localhost:8000/api/protein`, {
    //     'methods':'GET',
    //         headers: {
    //             'Content-Type': 'application/json'
    //         }
    //     })
    //         .then(res => res.json())
    //         .then(json => {
    //             const proteins = json.map(protein => ({
    //                 proteinId: protein.id,
    //                 proteinName: protein.proteinName,
    //                 proteinLocation: protein.proteinLocation
    //             }));
    //             setResults(proteins);
    //         });
    // }, [proteinName]);

const handleChange = ({target}) => setProteinName(target.value);

const HandleClick = () => {
    // FetchResults(proteinName);
    // FetchTestResults(proteinName)
    // const res = FetchDBResults()
    // const res = FetchTestResults()
    // setResults(res)
    // useEffect(() => {
    //     fetch('http://localhost:8000/api',{
    //         'methods':'GET',
    //         headers : {
    //             'Content-Type':'application/json'
    //         }
    //     })
    //         .then(res => res.json())
    //         .then(json => {
    //             console.log(json)
    //             const results = json.map(protein => ({
    //                 proteinId: protein.id,
    //                 proteinName: protein.title,
    //                 proteinLocation: protein.description
    //             }));
    //             setResults(results);
    //         });
    // }, [proteinName]);
};

return (
    <form>
        {/*<input type="text" value={proteinName} onChange={({ target }) => handleClick(target)}*/}
        <input type="text" value={proteinName} onChange={handleChange}
               placeholder="Protein sequence"/>
        <button onClick={HandleClick}>Find protein</button>
    </form>
);
}
;

export default Form;