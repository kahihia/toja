'use strict';

/**
 * @ngdoc filter
 * @name clientApp.filter:listingSearch
 * @function
 * @description
 * # listingSearch
 * Filter in the clientApp.
 */
angular.module('clientApp')
  .filter('listingSearch', function () {
    /**
     * Filter items by search term
     * @param  {Array} items - list of items
     * @return {Array}
     */
    return function (items, searchText) {
      if (!searchText) {
        return items;
      }

      if (!angular.isArray(items)) {
        return [];
      }

      var nameMatched, descriptionMatched;

      return items.filter(function(item) {
        nameMatched = false;
        descriptionMatched = false;

        if (item.name && item.name.indexOf(searchText) > -1) {
          nameMatched = true;
        }

        if (item.description && item.description.indexOf(searchText) > -1) {
          descriptionMatched = true;
        }
        return nameMatched || descriptionMatched;
      });
    };
  });
