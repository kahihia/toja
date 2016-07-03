'use strict';

/**
 * @ngdoc filter
 * @name clientApp.filter:stripTags
 * @function
 * @description
 * # stripTags
 * Filter in the clientApp.
 */
angular.module('clientApp')
  .filter('stripTags', function () {
    return function (input) {
      return String(input).replace(/<[^>]+>/gm, '');
    };
  });
