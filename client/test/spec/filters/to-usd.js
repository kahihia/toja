'use strict';

describe('Filter: toUsd', function () {

  // load the filter's module
  beforeEach(module('clientApp'));

  // initialize a new instance of the filter before each test
  var toUsd;
  beforeEach(inject(function ($filter) {
    toUsd = $filter('toUsd');
  }));

  it('should return the input prefixed with "toUsd filter:"', function () {
    var text = 'angularjs';
    expect(toUsd(text)).toBe('toUsd filter: ' + text);
  });

});
