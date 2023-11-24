describe('Checkbox tests', () => {
    it('Select and unselect checkbox', () => {
      cy.visit('https://the-internet.herokuapp.com/checkboxes');
      cy.get('input[type="checkbox"]').first().check().should('be.checked');
      cy.get('input[type="checkbox"]').first().uncheck().should('not.be.checked');
    });
  });