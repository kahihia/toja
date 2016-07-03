'use strict';

describe('Service: venue', function () {

  // load the service's module
  beforeEach(module('clientApp'));

  // instantiate service
  var venue;
  beforeEach(inject(function (_venue_) {
    venue = _venue_;
  }));

  it('should do something', function () {
    expect(!!venue).toBe(true);
  });

});
