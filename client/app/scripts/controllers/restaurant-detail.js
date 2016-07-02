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
    controller: 'RestaurantDetailCtrl as ctrl',
    resolve: {
      venue: function($stateParams, Venue) {
        return Venue.get({id: $stateParams.id});
      }
    }
  });

})
.controller('RestaurantDetailCtrl', function (venue) {
  this.map = { zoom: 15 };

  this.venue = venue;
});
