'use strict';

/**
 * @ngdoc filter
 * @name clientApp.filter:priceRange
 * @function
 * @description
 * # priceRange
 * Filter in the clientApp.
 */
angular.module('clientApp')
.filter('priceRange', function () {
  return function (items, range) {
    var filtered = [];
    var min = parseInt(range.min);
    var max = parseInt(range.max);
    // If time is with the range
    angular.forEach(items, function(item) {
      if (item.budget >= min && item.budget <= max) {
        filtered.push(item);
      }
    });

    return filtered;
  };
});
