'use strict';

describe('Filter: listingSearch', function () {

  // load the filter's module
  beforeEach(module('clientApp'));

  // initialize a new instance of the filter before each test
  var listingSearch;
  beforeEach(inject(function ($filter) {
    listingSearch = $filter('listingSearch');
  }));

  it('should return the input prefixed with "listingSearch filter:"', function () {
    var text = 'angularjs';
    expect(listingSearch(text)).toBe('listingSearch filter: ' + text);
  });

});
