'use strict';

/**
 * @ngdoc function
 * @name clientApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the clientApp
 */
angular.module('clientApp')
.config(function($stateProvider) {

  $stateProvider
  .state('main', {
    url: '/',
    templateUrl: 'views/main.html',
    controller: 'MainCtrl as ctrl',
    resolve: {
      venues: function(Venue) {
        return Venue.query();
      },
      attractions: function(Attraction) {
        return Attraction.query();
      }
    }
  });

})
.controller('MainCtrl', function ($scope, $rootScope, Venue, venues, attractions) {
  var self = this;

  var foodPriceRangeOptions = [
    {
      min: 0,
      max: 9999999,
      label: 'Any price'
    },
    {
      min: 0,
      max: 2000,
      label: 'Less than $20'
    },
    {
      min: 2001,
      max: 5000,
      label: 'From $21 to $50'
    },
    {
      min: 5001,
      max: 9999999,
      label: 'More than $51'
    }
  ];

  this.foodTab = {
    priceRangeOptions: foodPriceRangeOptions,
    priceRange: foodPriceRangeOptions[0],
    show: 'all'
  };

  this.venues = venues;
  this.attractions = attractions;

  this.venueLimit = 5;
  this.attractionLimit = 5;

  this.loadMore = function(type) {
    console.debug('Loading more %s ...', type);
    if (type === 'attraction') {
      this.attractionLimit += 5;
    } else if (type === 'venue') {
      this.venueLimit += 5;
    }
  };

  $scope.$watch('ctrl.foodTab.show', function(newValue, oldValue) {
    if (newValue && oldValue && newValue !== oldValue) {
      if (newValue === 'all') {
        console.debug('Showing all locations');
        self.venues = Venue.query();
      } else if (newValue === 'nearby') {
        console.debug('Showing nearby locations');
        if (!$rootScope.currentLocation) {
          self.venues = [];
        } else {
          self.venues = Venue.byLocation($rootScope.currentLocation);
        }
      }
    }
  });
});
