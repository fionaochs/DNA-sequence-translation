import React, {useState} from 'react';
import {FetchResults, PostProtein} from "../../services/requests";
import {useLocalStorage} from "../../useLocalStorage";
import styles from './Form.css';
import Modal from 'react-modal';
import SearchModal from './Modal';

const Form = () => {
        const [proteinName, setProteinName] = useState('');
        const [results, setResults] = useLocalStorage("results", []);
        const [modalIsOpen, setModalIsOpen] = useState(false);

        const handleChange = ({target}) => setProteinName(target.value);

        const setModalIsOpenToTrue = () => {
            setModalIsOpen(true)
        }
        const setModalIsOpenToFalse = () => {
            setModalIsOpen(false)
        }
        const HandleClick = (e) => {
            e.preventDefault();

            setModalIsOpenToTrue();

            PostProtein(proteinName)
                .then(res => {
                    // window.location.reload(false);
                })
        };
        const getResults = (e) => {
            e.preventDefault();

            FetchResults()
                .then(res => {
                    if (res === undefined) {
                        setResults([...results, {'id': -1, 'DNASequence': proteinName}])
                    } else {
                        setResults(res)
                    }
                    window.location.reload(false);
                })
        };
        const customStyles = {
            content: {
                top: '50%',
                left: '50%',
                right: 'auto',
                bottom: 'auto',
                marginRight: '-50%',
                transform: 'translate(-50%, -50%)',
                backgroundColor: '#1A8CA9',
                width: '30rem'
            },
            overlay: {
                background: "#1c49a4"
            }
        };
        return (
            <form onSubmit={HandleClick}>
                <input type="text" value={proteinName} onChange={handleChange}
                       label="Sequence" placeholder="Sequence"/>
                <button onClick={HandleClick}>Find protein</button>
                <button onClick={getResults}>Get results</button>

                <Modal isOpen={modalIsOpen} style={customStyles} onRequestClose={setModalIsOpenToFalse}>
                    <button onClick={setModalIsOpenToFalse}>x</button>
                    <SearchModal DNASequence={proteinName}/>
                </Modal>
            </form>
        );
    }
;

export default Form;