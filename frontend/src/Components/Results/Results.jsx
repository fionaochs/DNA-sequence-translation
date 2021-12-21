import React, {useEffect, useState} from 'react';
import Result from "./Result";
import {useLocalStorage} from "../../useLocalStorage";
import styles from './Results.css';

const Results = () => {
    const [results, setResults] = useLocalStorage("results", []);

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
};
export default Results;
