import React, {useEffect, useState} from 'react';
import {FetchResults, FetchTestResults} from "../../services/requests";
import {useLocalStorage} from "../../useLocalStorage";

const Form = () => {
    const [proteinName, setProteinName] = useState('');
    // const [proteinName, setProteinName] = useLocalStorage("proteinName", "");

    const handleChange = ({ target }) => setProteinName(target.value);

    const handleClick = () => {
        // FetchResults(proteinName);
        FetchTestResults();
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