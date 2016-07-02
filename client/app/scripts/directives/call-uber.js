'use strict';

/**
 * @ngdoc directive
 * @name clientApp.directive:callUber
 * @description
 * # callUber
 */
angular.module('clientApp')
  .directive('callUber', function ($mdDialog, $window, Uber) {
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

          var url = Uber.generateRideRequestUrl({
            dropoff: {
              name: scope.place.name,
              latitude: scope.place.latitude,
              longitude: scope.place.longitude
            }
          });
          $window.location.href = url;
        };
      }
    };
  });
