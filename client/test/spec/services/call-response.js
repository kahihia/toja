'use strict';

describe('Service: callResponse', function () {

  // load the service's module
  beforeEach(module('clientApp'));

  // instantiate service
  var callResponse;
  beforeEach(inject(function (_callResponse_) {
    callResponse = _callResponse_;
  }));

  it('should do something', function () {
    expect(!!callResponse).toBe(true);
  });

});
