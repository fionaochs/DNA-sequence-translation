import React, {useState} from 'react';
import Result from "./Result";
import {FetchResults} from "../../services/requests";
import {useLocalStorage} from "../../useLocalStorage";

const Results = () => {
    // const [proteinName, setProteinName] = useState('');
    // const [results, setResults] = useState([]);

    // const [proteinName, setProteinName] = useState(() => {
    //     // getting stored value
    //     const saved = localStorage.getItem("proteinName");
    //     const initialValue = JSON.parse(saved);
    //     return initialValue || "";
    // });
    const [results, setResults] = useLocalStorage("results", []);

    // const { results } = FetchResults(proteinName);
    return (
        <>
            <Result list={results} />
        </>
    );
};
export default Results;