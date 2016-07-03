'use strict';

describe('Filter: priceRange', function () {

  // load the filter's module
  beforeEach(module('clientApp'));

  // initialize a new instance of the filter before each test
  var priceRange;
  beforeEach(inject(function ($filter) {
    priceRange = $filter('priceRange');
  }));

  it('should return the input prefixed with "priceRange filter:"', function () {
    var text = 'angularjs';
    expect(priceRange(text)).toBe('priceRange filter: ' + text);
  });

});
