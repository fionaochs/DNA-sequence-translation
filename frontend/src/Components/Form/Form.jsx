import React, {useState} from 'react';
import {FetchResults} from "../../services/requests";
import {useLocalStorage} from "../../useLocalStorage";
import styles from './Form.css';

const Form = () => {
        const [proteinName, setProteinName] = useState('');
        const [results, setResults] = useLocalStorage("results", []);

        const handleChange = ({target}) => setProteinName(target.value);

        const HandleClick = () => {
            FetchResults(proteinName)
                .then(res => {
                    if (res === undefined) {
                        setResults([...results, {'id': -1, 'DNASequence': proteinName}])
                    } else {
                        setResults(results.concat(res))
                    }
                })
        };

        return (
            <form onSubmit={HandleClick}>
                <input type="text" value={proteinName} onChange={handleChange}
                       placeholder="Sequence"/>
                <button onClick={HandleClick}>Find protein</button>
            </form>
        );
    }
;

export default Form;