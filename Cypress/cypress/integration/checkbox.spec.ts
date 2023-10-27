describe('Checkbox Test', () => {
    it('should check and uncheck checkboxes', () => {
      cy.visit('https://the-internet.herokuapp.com/checkboxes');
  
      // Checking first checkbox
      cy.get('input[type="checkbox"]').first().as('firstCheckbox');
      cy.get('@firstCheckbox').not('[checked]').click().should('be.checked');
  
      // Unchecking last checkbox
      cy.get('input[type="checkbox"]').last().as('secondCheckbox');
      cy.get('@secondCheckbox').click().should('not.be.checked');
    });
  });
  