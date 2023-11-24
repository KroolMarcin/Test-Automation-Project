describe('Drag and drop tests', () => {
    it('Makes action with drag and drop', () => {
      cy.visit('https://the-internet.herokuapp.com/drag_and_drop');
      cy.get('#column-a').drag('#column-b');
    });
  });