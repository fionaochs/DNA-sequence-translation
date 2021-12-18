import React, {useEffect, useState} from 'react';
import Result from "./Result";
import {useLocalStorage} from "../../useLocalStorage";

const Results = () => {
    const [results, setResults] = useLocalStorage("results", []);

    const resultsList = results.map(result =>
        <ul key={result.id}>
            <li key={result.proteinName}>
                <Result {...result} />
            </li>
        </ul>
    );
    return (
        <>
            <h2>Results</h2>
            {resultsList}
        </>
    );
};
export default Results;
