import React, {useEffect, useState} from 'react';
import {FetchResults, FetchTestResults} from "../../services/requests";
import {useLocalStorage} from "../../useLocalStorage";

const Form = () => {
    const [proteinName, setProteinName] = useState('');
    const [results, setResults] = useLocalStorage("results", []);

    // useEffect(() => {
    //     const res = FetchTestResults()
    //     setResults(res)
    // }, []);
    const handleChange = ({target}) => setProteinName(target.value);

    const handleClick = () => {
        // FetchResults(proteinName);
        // FetchTestResults()
        const res = FetchTestResults()
        setResults(res)
    };

    return (
        <form>
            {/*<input type="text" value={proteinName} onChange={({ target }) => handleClick(target)}*/}
            <input type="text" value={proteinName} onChange={handleChange}
                   placeholder="Protein sequence"/>
            <button onClick={handleClick}>Find protein</button>
        </form>
    );
};

export default Form;