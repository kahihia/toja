'use strict';

/**
 * @ngdoc directive
 * @name clientApp.directive:listingItem
 * @description
 * # listingItem
 */
angular.module('clientApp')
  .directive('listingItem', function () {
    return {
      templateUrl: 'views/directives/listing-item.html',
      restrict: 'E',
      link: function postLink() {
      }
    };
  });
