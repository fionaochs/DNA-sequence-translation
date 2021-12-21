import { render, screen } from '@testing-library/react';
import App from './App';

test('renders App header', () => {
  render(<App />);
  const linkElement = screen.getByText(/DNA Sequence Translator/i);
  expect(linkElement).toBeInTheDocument();
});
