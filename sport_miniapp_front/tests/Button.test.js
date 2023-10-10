import React from 'react'; 
import { render } from '@testing-library/react'; 
// your component that you want to test 
import Button from '../src/components/Button/Button';
describe('Button', () => { 
  // test case 
  it('Button is in the button component', () => { 
    const { getByRole } = render(<Button />);
    const buttonElement = getByRole("button");
    expect(buttonElement).toBeInTheDocument();
  }); 
});