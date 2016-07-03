'use strict';

describe('Service: callStatus', function () {

  // load the service's module
  beforeEach(module('clientApp'));

  // instantiate service
  var callStatus;
  beforeEach(inject(function (_callStatus_) {
    callStatus = _callStatus_;
  }));

  it('should do something', function () {
    expect(!!callStatus).toBe(true);
  });

});
