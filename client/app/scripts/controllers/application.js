'use strict';

/**
 * @ngdoc function
 * @name clientApp.controller:ApplicationCtrl
 * @description
 * # ApplicationCtrl
 * Controller of the clientApp
 */
angular.module('clientApp')
.controller('ApplicationCtrl', function ($rootScope, $state, geolocation) {
  this.$state = $state;

  geolocation.getLocation().then(function(data) {
    $rootScope.currentLocation = {
      latitude: data.coords.latitude,
      longitude: data.coords.longitude
    };
    console.debug('Current location:', $rootScope.currentLocation);
  }).catch(function(error) {
    console.debug('Cannot get current location');
  });
});
