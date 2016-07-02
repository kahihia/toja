'use strict';

describe('Service: uber', function () {

  // load the service's module
  beforeEach(module('clientApp'));

  // instantiate service
  var uber;
  beforeEach(inject(function (_uber_) {
    uber = _uber_;
  }));

  it('should do something', function () {
    expect(!!uber).toBe(true);
  });

});
