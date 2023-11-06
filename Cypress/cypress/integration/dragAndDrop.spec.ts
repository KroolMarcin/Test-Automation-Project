describe('Drag and Drop Test', () => {
    it('should drag and drop', () => {
      cy.visit('https://the-internet.herokuapp.com/drag_and_drop');
      
      // Użyjemy `trigger` do symulacji przeciągania
      cy.get('#column-a').trigger('mousedown', { which: 1 });
      cy.get('#column-b').trigger('mousemove').trigger('mouseup');
      
      // Weryfikacja, czy elementy zostały zamienione miejscami
      // (zależne od implementacji, tutaj przykładowy test)
      cy.get('#column-a').should('contain', 'B');
      cy.get('#column-b').should('contain', 'A');
    });
  });
  