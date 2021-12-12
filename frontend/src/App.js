import logo from './logo.svg';
import './App.css';
import Form from "./Components/Form/Form";
import Results from "./Components/Results/Results";

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <Form/>
                <Results/>
            </header>
        </div>
    );
}

export default App;
