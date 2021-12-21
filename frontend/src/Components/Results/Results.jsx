import React, {useEffect, useState} from 'react';
import Result from "./Result";
import {useLocalStorage} from "../../useLocalStorage";
import styles from './Results.css';

const Results = () => {
    const [results, setResults] = useLocalStorage("results", []);

    if(results) {
        const resultsList = results.map(result =>
            <ul key={result.id}>
                <li key={result.id}>
                    <Result {...result} />
                </li>
            </ul>
        );
        return (
            <div className={styles.results}>
                <h2>Results</h2>
                {resultsList}
            </div>
        );
    } else {
        return (
            <div>
                <h3>Sequence '{DNASequence}'</h3>
                <h3>did not match any organisms on file</h3>
            </div>

        )
    }
};
export default Results;
