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
.controller('RestaurantDetailCtrl', function ($scope, $rootScope, Venue, venue) {
  var unwatchLocation;

  var self = this;

  this.map = { zoom: 15 };

  this.venue = venue;

  this.venue.$promise.then(function() {
    $rootScope.navTitle = venue.name;
  });

  this.nearByVenues = [];

  if ($rootScope.currentLocation) {
    this.nearByVenues = Venue.byLocation($rootScope.currentLocation);
  } else {
    unwatchLocation = $rootScope.$watch('currentLocation', function(value) {
      if (value) {
        self.nearByVenues = Venue.byLocation($rootScope.currentLocation);
      }
    });
  }

  $scope.$on('$destroy', function() {
    if (unwatchLocation) {
      unwatchLocation();
    }
  });

});
