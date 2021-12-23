import React from 'react';
import {render, cleanup} from '@testing-library/react';
import Form from './Form';

describe('Form component', () => {
    afterEach(() => cleanup());
    it('renders Form', () => {
        const {asFragment} = render(<Form/>);
        expect(asFragment()).toMatchSnapshot();
    });
    it('renders form text', () => {
        const {getByText} = render(<Form/>);
        const linkElement = getByText(/Find protein/i);
        expect(linkElement).toBeInTheDocument();
    });
});