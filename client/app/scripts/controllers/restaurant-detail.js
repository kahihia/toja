'use strict';

/**
 * @ngdoc function
 * @name clientApp.controller:RestaurantDetailCtrl
 * @description
 * # RestaurantDetailCtrl
 * Controller of the clientApp
 */
angular.module('clientApp')
.config(function($stateProvider) {

  $stateProvider
  .state('restaurant-detail', {
    url: '/restaurant/:id',
    templateUrl: 'views/restaurant-detail.html',
    controller: 'RestaurantDetailCtrl as ctrl'
  });

})
.controller('RestaurantDetailCtrl', function () {
  this.map = { center: { latitude: 45, longitude: -73 }, zoom: 8 };
});
