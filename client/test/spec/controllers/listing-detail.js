'use strict';

describe('Controller: ListingDetailCtrl', function () {

  // load the controller's module
  beforeEach(module('clientApp'));

  var ListingDetailCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    ListingDetailCtrl = $controller('ListingDetailCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(ListingDetailCtrl.awesomeThings.length).toBe(3);
  });
});
