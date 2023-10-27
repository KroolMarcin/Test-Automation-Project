describe('Add/Remove Elements Test', () => {
    it('should add and remove elements', () => {
      cy.visit('https://the-internet.herokuapp.com/add_remove_elements/');
  
      // Adding two elements
      cy.get('[onclick="addElement()"]').click().click();
  
      // Checking if elements where added
      cy.get('.added-manually').should('have.length', 2);
  
      // Deleting one element
      cy.get('.added-manually').first().click();
  
      // Checking if elements were deleted
      cy.get('.added-manually').should('have.length', 1);
    });
  });
  