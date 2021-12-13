import React, {useEffect, useState} from 'react';
import Result from "./Result";
import {FetchResults, FetchTestResults} from "../../services/requests";
import {useLocalStorage} from "../../useLocalStorage";

const Results = () => {
    // const [proteinName, setProteinName] = useState([]);
    // const [results, setResults] = useState([]);
    // const [results, setResults] = useState([{'proteinName': 'protein 1', 'proteinLocation': 'protein 1 location'}, {'proteinName': 'protein 2', 'proteinLocation': 'protein 2 location'}]);

    // const [proteinName, setProteinName] = useState(() => {
    //     // getting stored value
    //     const saved = localStorage.getItem("proteinName");
    //     const initialValue = JSON.parse(saved);
    //     return initialValue || "";
    // });
    const [results, setResults] = useLocalStorage("results", []);

    // useEffect(() => {
    //     FetchTestResults()
    //         // .then(res => setResults(res));
    // }, []);
    // console.log(shoes)

    const resultsList = results.map(result =>
        <ul key={result.id}>
            <li key={result.name}>
                <Result {...result} />
            </li>
        </ul>
    );
    // const { results } = FetchTestResults();
    return (
        <>
            <h2>Results</h2>
            {/*<Result list={...results}/>*/}
            {resultsList}
        </>
    );
};
export default Results;