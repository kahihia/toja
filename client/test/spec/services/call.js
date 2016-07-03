'use strict';

describe('Service: call', function () {

  // load the service's module
  beforeEach(module('clientApp'));

  // instantiate service
  var call;
  beforeEach(inject(function (_call_) {
    call = _call_;
  }));

  it('should do something', function () {
    expect(!!call).toBe(true);
  });

});
