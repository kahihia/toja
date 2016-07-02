'use strict';

/**
 * @ngdoc filter
 * @name clientApp.filter:toUsd
 * @function
 * @description
 * # toUsd
 * Filter in the clientApp.
 */
angular.module('clientApp')
  .filter('toUsd', function () {
    return function (input) {
      // TODO: use real data JPY <-> USD
      var JPY_USD_RATE = 0.01;

      if (typeof input !== 'number') {
        return 0;
      }

      return parseFloat((input*JPY_USD_RATE).toFixed(2));
    };
  });
