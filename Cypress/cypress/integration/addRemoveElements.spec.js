describe('Advanced Tests for Adding Elements', () => {
    // Defines a test for dynamic addition of elements
    it('Dynamically adds multiple elements and checks their state asynchronously', () => {
      cy.visit('https://the-internet.herokuapp.com/add_remove_elements/');

      const addAndCheckElementAsync = (index) => {
        return new Cypress.Promise((resolve, reject) => {
          cy.get('[onclick="addElement()"]').click().then(() => {
            cy.get('.added-manually').eq(index).should('exist');
            resolve();
          });
        });
      };

      const promises = [];
      for (let i = 0; i < 5; i++) {
        promises.push(addAndCheckElementAsync(i));
      }
      Promise.all(promises).then(() => {
        cy.get('.added-manually').should('have.length', 5);
      });
    });
  });

  describe('Advanced Tests for Removing Elements', () => {
    // Defines a test for removing selected elements
    it('Removes selected elements from the list', () => {
      cy.visit('https://the-internet.herokuapp.com/add_remove_elements/');
  
      for (let i = 0; i < 5; i++) {
        cy.get('[onclick="addElement()"]').click();
      }
  
      const removeSpecificElement = (index) => {
        return new Cypress.Promise((resolve, reject) => {
          cy.get('.added-manually').eq(index).click().then(() => {
            cy.get('.added-manually').eq(index).should('not.exist');
            resolve();
          });
        });
      };
  
      removeSpecificElement(2).then(() => {
        removeSpecificElement(3).then(() => {
          cy.get('.added-manually').should('have.length', 3);
        });
      });
    });
  });

  describe('Testing Element Order', () => {
  // Defines a test to check the order of elements during addition and removal
  it('Adds and removes elements, checking their order', () => {
    cy.visit('https://the-internet.herokuapp.com/add_remove_elements/');

    // Adds several elements and checks their order
    for (let i = 0; i < 5; i++) {
      cy.get('[onclick="addElement()"]').click();
      cy.get('.added-manually').eq(i).should('exist');
    }

    const removeAndCheckOrder = (index) => {
      return new Cypress.Promise((resolve, reject) => {
        cy.get('.added-manually').eq(index).click().then(() => {
          cy.get('.added-manually').each(($el, idx, $list) => {
            if (idx >= index) {
              expect($el).to.not.exist;
            }
          });
          resolve();
        });
      });
    };

    removeAndCheckOrder(3).then(() => {
      removeAndCheckOrder(1);
    });
  });
});
