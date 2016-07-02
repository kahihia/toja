'use strict';

/**
 * @ngdoc function
 * @name clientApp.controller:PlaceDetailCtrl
 * @description
 * # PlaceDetailCtrl
 * Controller of the clientApp
 */
angular.module('clientApp')
.config(function($stateProvider) {

  $stateProvider
  .state('place-detail', {
    url: '/place/:id',
    templateUrl: 'views/place-detail.html',
    controller: 'PlaceDetailCtrl as ctrl'
  });

})
.controller('PlaceDetailCtrl', function () {
  this.map = { center: { latitude: 45, longitude: -73 }, zoom: 8 };
});
