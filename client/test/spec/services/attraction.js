'use strict';

describe('Service: attraction', function () {

  // load the service's module
  beforeEach(module('clientApp'));

  // instantiate service
  var attraction;
  beforeEach(inject(function (_attraction_) {
    attraction = _attraction_;
  }));

  it('should do something', function () {
    expect(!!attraction).toBe(true);
  });

});
