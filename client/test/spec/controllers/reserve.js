'use strict';

describe('Controller: ReserveCtrl', function () {

  // load the controller's module
  beforeEach(module('clientApp'));

  var ReserveCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    ReserveCtrl = $controller('ReserveCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(ReserveCtrl.awesomeThings.length).toBe(3);
  });
});
