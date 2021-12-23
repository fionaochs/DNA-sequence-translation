import React from 'react';
import {render, screen, fireEvent, waitFor, cleanup} from '@testing-library/react';
import Result from './Result';

describe('Result component', () => {
    afterEach(() => cleanup());
    it('renders Result', () => {
        let result = {};
        const {asFragment} = render(<Result result={result}/>);
        expect(asFragment()).toMatchSnapshot();
    });
    it('find result text in display', async () => {
        render(<Result result={'DNA sequence'}/>);
        const linkElement = screen.getByText(/DNA sequence/i);
        expect(linkElement).toBeInTheDocument();
    });
});