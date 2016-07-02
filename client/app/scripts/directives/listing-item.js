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
        item: '=?'
      },
      link: function postLink(scope) {
        scope.$localStorage = $localStorage;

        scope.fave = function(event) {
          event.preventDefault();
          event.stopPropagation();

          console.debug('Faved', scope.item.id);
          if (!$localStorage.faves) {
            $localStorage.faves = {
              venues: {}
            };
          } else if (!$localStorage.faves.venues) {
            $localStorage.faves.venues = {};
          }

          $localStorage.faves.venues[scope.item.id] = !$localStorage.faves.venues[scope.item.id];
          // TODO: sync to server
        };
      }
    };
  });
