describe('Dropdown list test', () => {
    it('Choose option from list', () => {
      cy.visit('/dropdown');
      // Wybiera opcję z listy rozwijanej i sprawdza, czy ta opcja została wybrana.
      cy.get('select').select('Opcja 1').should('have.value', 'opcja1');
    });
  });