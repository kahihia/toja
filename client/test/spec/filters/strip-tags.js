'use strict';

describe('Filter: stripTags', function () {

  // load the filter's module
  beforeEach(module('clientApp'));

  // initialize a new instance of the filter before each test
  var stripTags;
  beforeEach(inject(function ($filter) {
    stripTags = $filter('stripTags');
  }));

  it('should return the input prefixed with "stripTags filter:"', function () {
    var text = 'angularjs';
    expect(stripTags(text)).toBe('stripTags filter: ' + text);
  });

});
