import React, {useState} from 'react';
import Result from "./Result";
import {fetchResults} from "../../services/requests";

const Results = () => {
    const [proteinName, setProteinName] = useState('');

    const { results } = fetchResults(proteinName);
    return (
        <>
            <Result list={results} />
        </>
    );
};
export default Results;