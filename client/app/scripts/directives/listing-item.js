'use strict';

/**
 * @ngdoc directive
 * @name clientApp.directive:listingItem
 * @description
 * # listingItem
 */
angular.module('clientApp')
  .directive('listingItem', function ($localStorage) {
    return {
      templateUrl: 'views/directives/listing-item.html',
      restrict: 'E',
      scope: {
        item: '=?',
        /**
         * Type of listing item
         * @type {String} ['venue'|'attraction']
         */
        type: '=?'
      },
      link: function postLink(scope) {
        scope.$localStorage = $localStorage;

        scope.fave = function(event) {
          event.preventDefault();
          event.stopPropagation();

          console.debug('Faved', scope.item.id);

          if (scope.type === 'venue') {
            if (!$localStorage.faves) {
              $localStorage.faves = {
                venues: {}
              };
            } else if (!$localStorage.faves.venues) {
              $localStorage.faves.venues = {};
            }

            $localStorage.faves.venues[scope.item.id] = !$localStorage.faves.venues[scope.item.id];
          } else if (scope.type === 'attraction') {
            if (!$localStorage.faves) {
              $localStorage.faves = {
                attractions: {}
              };
            } else if (!$localStorage.faves.attractions) {
              $localStorage.faves.attractions = {};
            }

            $localStorage.faves.attractions[scope.item.id] = !$localStorage.faves.attractions[scope.item.id];
          }

          // TODO: sync to server
        };
      }
    };
  });
