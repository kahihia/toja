'use strict';

describe('Controller: RestaurantDetailCtrl', function () {

  // load the controller's module
  beforeEach(module('clientApp'));

  var RestaurantDetailCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    RestaurantDetailCtrl = $controller('RestaurantDetailCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(RestaurantDetailCtrl.awesomeThings.length).toBe(3);
  });
});
