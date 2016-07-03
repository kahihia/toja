'use strict';

/**
 * @ngdoc directive
 * @name clientApp.directive:callUber
 * @description
 * # callUber
 */
angular.module('clientApp')
  .directive('callUber', function ($mdDialog, $window, $rootScope, Uber) {
    return {
      templateUrl: 'views/directives/call-uber.html',
      restrict: 'E',
      replace: true,
      scope: {
        place: '='
      },
      link: function postLink(scope) {
        scope.callUber = function(event) {
          event.preventDefault();

          var params = {};
          params.dropoff = {
            name: scope.place.name,
            latitude: scope.place.latitude,
            longitude: scope.place.longitude
          };

          if ($rootScope.currentLocation) {
            params.pickup = {
              name: 'Current location',
              latitude: $rootScope.currentLocation.latitude,
              longitude: $rootScope.currentLocation.longitude
            };
          }

          var url = Uber.generateRideRequestUrl(params);
          $window.location.href = url;
        };
      }
    };
  });
